# การส่ง GitHub และวิดีโอ

ไฟล์ข้อความ/CSV/JSONL/source snapshots เก็บไบต์เดิมด้วย .gitattributes (* -text) เพื่อให้hashตรงกับข้อมูลต้นฉบับ ไม่เปลี่ยนข้อมูลทดลองหรือแก้historical source hashesให้ตามการแปลงบรรทัดของGit

วิดีโอ10นาทีอยู่ที่ 07_Evidence/CSV_คลิปเล่นกับคน_10นาที_C1_20261106/คลิปเล่นกับคน_10นาที_C1.MOV ขนาด616,429,505bytes ใช้Git LFS ต้องติดตั้งGit LFS และgit lfs pullหลังcloneหากวิดีโอยังเป็นpointer อย่าอัปไฟล์MOVขนาดนี้เป็นGit blobปกติ

คลิปเก่า167.05sอยู่ใน07_Evidence/CSV ของ วิดีโอทดลองเล่น/คลิปทดลองเล่น.mp4 เป็นคนละรอบกับคลิป10นาที ไม่แทนหรือรวมCSVข้ามรอบ

MANIFEST_SHA256.jsonตรวจไฟล์ที่แนบจริง ไม่รวมcache .pyc/__pycache__ ซึ่งGitละไว้ หลังcloneพร้อมLFSให้รันpython verify_package.pyจากโฟลเดอร์Week_07_Lab_07 ตัวตรวจนี้ตรวจความครบและhash/evidence contract บางส่วน ไม่ใช่การรับรองscientific validity และfield final_research_complete:falseเดิมไม่ได้หมายถึงไฟล์ขาด

GitHubหน้าเว็บจะแสดงGit LFS pointer/ปุ่มดาวน์โหลดแทนเนื้อวิดีโอ บางกรณีDownload ZIPของGitHubมีแต่pointer จึงควรcloneแล้วgit lfs pull หรือนำคลิปจริงแนบชุดส่งโดยตรง
