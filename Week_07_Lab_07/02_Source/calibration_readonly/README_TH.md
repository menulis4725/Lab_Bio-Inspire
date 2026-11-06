# Read-only servo transport dependency

read_only_bus.py คัดลอกตรงต้นฉบับ calibration_readonly/read_only_bus.py ของโปรเจกต์ ใช้โดย shared/runtime/motor_baseline.py และ normal_gaze_motor.py เป็น transportฐานสำหรับservo ไม่ใช่ไฟล์CSVหรือข้อมูลรอบทดลอง

โฟลเดอร์02_Sourceคือrootของsourceที่แนบ ดังนั้นพาธ calibration_readonly/read_only_bus.py ในโค้ดจึงอยู่ที่02_Source/calibration_readonly/read_only_bus.py ในชุดส่ง ไม่ใช่ข้างนอกZIP

การimportโมดูลไม่เปิดUART การสร้างReadOnlyBusจริงจึงจะใช้pyserialและ /dev/ttyAMA0 บนPi ไม่สั่งเชื่อมมอเตอร์จากการตรวจแพ็กเกจนี้ test_readonly.pyใช้FakePortโดยไม่เปิดฮาร์ดแวร์
