import os
import shutil
import time

class SecurityManager:
    def __init__(self, project_dir="."):
        self.project_dir = project_dir
        self.backup_dir = os.path.join(project_dir, "backups")
        os.makedirs(self.backup_dir, exist_ok=True)

    def create_backup(self):
        """আপডেটের আগে প্রজেক্টের ব্যাকআপ তৈরি করা"""
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        target_backup = os.path.join(self.backup_dir, f"backup_{timestamp}")
        
        # neela ফোল্ডার এবং main.py ব্যাকআপ করা
        os.makedirs(target_backup, exist_ok=True)
        if os.path.exists("neela"):
            shutil.copytree("neela", os.path.join(target_backup, "neela"), dirs_exist_ok=True)
        if os.path.exists("main.py"):
            shutil.copy("main.py", target_backup)
            
        print(f"[Security]: ব্যাকআপ তৈরি হয়েছে -> {target_backup}")
        return target_backup

    def rollback(self, backup_path):
        """কোনো সমস্যা হলে আগের অবস্থায় ফিরিয়ে আনা"""
        print("[Security]: আপডেট ব্যর্থ হয়েছে! আগের অবস্থায় রোলব্যাক করা হচ্ছে...")
        try:
            if os.path.exists(os.path.join(backup_path, "neela")):
                if os.path.exists("neela"):
                    shutil.rmtree("neela")
                shutil.copytree(os.path.join(backup_path, "neela"), "neela")
                
            if os.path.exists(os.path.join(backup_path, "main.py")):
                shutil.copy(os.path.join(backup_path, "main.py"), "main.py")
                
            print("[Security]: সফলভাবে আগের ব্যাকআপে রিস্টোর করা হয়েছে।")
            return True
        except Exception as e:
            print(f"[Security Rollback Error]: {e}")
            return False