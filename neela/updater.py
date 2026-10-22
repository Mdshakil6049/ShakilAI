import sys
import subprocess
from neela.security import SecurityManager

security = SecurityManager()

def apply_new_feature(file_path, new_code):
    """নতুন কোড সেভ করা এবং টেস্ট করে ব্যর্থ হলে ব্যাকআপে ফিরে যাওয়া"""
    backup_path = security.create_backup()
    
    try:
        # নতুন কোড ফাইলে লেখা
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_code)
            
        # টেস্ট রান: পাইথন কোডে কোনো সিনট্যাক্স এরর আছে কি না পরীক্ষা
        result = subprocess.run(
            [sys.executable, "-m", "py_compile", file_path],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print(f"[Updater Error]: কোডে ভুল রয়েছে:\n{result.stderr}")
            security.rollback(backup_path)
            return "শাকিল স্যার, কোডে সমস্যা থাকায় স্বয়ংক্রিয়ভাবে আগের নিরাপদ অবস্থায় ফিরে যাওয়া হয়েছে।"
        
        print("[Updater]: নতুন ফিচার সফলভাবে যুক্ত করা হয়েছে!")
        return "শাকিল স্যার, নতুন ফিচার সফলভাবে যুক্ত হয়েছে এবং টেস্টে পাস করেছে!"
        
    except Exception as e:
        print(f"[Updater Exception]: {e}")
        security.rollback(backup_path)
        return "শাকিল স্যার, আপডেট করতে সমস্যা হওয়ায় রোলব্যাক করা হয়েছে।"