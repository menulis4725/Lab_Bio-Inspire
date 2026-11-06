import unittest
from read_only_bus import ReadOnlyBus, read_packet, record_blockers


class FakePort:
    def __init__(self):self.data=bytearray(); self.sent=[]
    def reset_input_buffer(self):self.data.clear()
    @property
    def in_waiting(self):return len(self.data)
    def write(self,packet):
        self.sent.append(packet)
        assert packet[4]==2
        address,count=packet[5:7]
        values={33:bytes([0]),40:bytes([0]),56:bytes([0,8,0,0,0,0,72,31]),65:bytes([0,0])}
        body=bytes([packet[2],count+2,0])+values[address]
        self.data.extend(b'\xff\xff'+body+bytes([(~sum(body))&255]))
    def flush(self):pass
    def read(self,n):
        result=bytes(self.data[:n]); del self.data[:n]; return result


class ReadOnlyTests(unittest.TestCase):
    def test_only_allowed_unicast_reads(self):
        for sid in (0,6,254,255):
            with self.assertRaises(ValueError):read_packet(sid,40,1)
        for address,count in ((42,2),(55,1),(40,2),(56,80)):
            with self.assertRaises(ValueError):read_packet(1,address,count)
        packet=read_packet(1,56,8)
        self.assertEqual(packet[4],2)
        self.assertEqual(sum(packet[2:])&255,255)

    def test_full_snapshot_uses_read_only_packets(self):
        bus=ReadOnlyBus.__new__(ReadOnlyBus); bus.port=FakePort()
        rows=bus.snapshot()
        self.assertEqual(len(rows),5)
        self.assertEqual(rows[0]['position_raw'],2048)
        self.assertEqual(rows[0]['voltage_V'],7.2)
        self.assertEqual(record_blockers(rows),[])
        self.assertEqual(len(bus.port.sent),20)
        self.assertTrue(all(p[4]==2 and p[2] in (1,2,3,4,5) for p in bus.port.sent))

    def test_bad_state_prevents_recording(self):
        bus=ReadOnlyBus.__new__(ReadOnlyBus); bus.port=FakePort()
        rows=bus.snapshot()
        for field,value in [('torque_raw',1),('status_raw',4),('mode',1),('position_raw',65535)]:
            changed=[dict(r) for r in rows]; changed[0][field]=value
            self.assertTrue(record_blockers(changed))
        self.assertTrue(record_blockers(rows[:-1]))
        prior={r['id']:r['position_raw'] for r in rows}; prior[1]=4090
        rows[0]['position_raw']=5
        self.assertTrue(any('wrap/' in r for r in record_blockers(rows,prior)))


if __name__=='__main__':unittest.main()
