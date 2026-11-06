"""Mocked PC checks only. Does not start camera/GPIO/UART/ROS."""
from pathlib import Path
import os,sys,unittest,subprocess
root=Path(__file__).resolve().parent/'02_Source';os.chdir(root)
sys.path[:0]=[str(root),str(root/'bio_inspire/runtime'),str(root/'shared/runtime')]
# Fresh interpreter catches dependencies that mocked tests may conceal.
check_code=("import sys,unittest;sys.path[:0]="+repr([str(root/'shared/runtime'),str(root/'calibration_readonly')])+";import motor_baseline,read_only_bus;print('Isolated source dependency import: PASS',flush=True);r=unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromName('test_readonly'));sys.exit(not r.wasSuccessful())")
subprocess.run([sys.executable,'-I','-B','-c',check_code],cwd=root,check=True)
names=['bio_inspire.experiments.test_automatic_component','bio_inspire.experiments.test_all_state_compare',
       'bio_inspire.experiments.test_ahm_cpg_compare','test_interested_player_reference',
       'test_button_look','test_three_state_behavior','test_interested_head','test_native_posture',
       'test_lab07_start_gate','test_session_recording','test_led_ring','bio_inspire.experiments.test_ros13']
result=unittest.TextTestRunner(verbosity=1).run(unittest.defaultTestLoader.loadTestsFromNames(names))
raise SystemExit(not result.wasSuccessful())
