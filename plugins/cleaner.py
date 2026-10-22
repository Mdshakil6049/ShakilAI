import os
from pathlib import Path

def run_plugin(command):
    lower = command.lower()
    if "ক্লিন" in lower or "clean" in lower or "টেম্পোরারি" in lower or "পরিষ্কার" in lower:
        try:
            temp_dir = Path(os.environ.get('TEMP', 'C:\\Windows\\Temp'))
            deleted_files = 0
            for item in temp_dir.iterdir():
                try:
                    if item.is_file():
                        item.unlink()
                        deleted_files += 1
                except Exception:
                    pass
            return f"সফলভাবে {deleted_files}টি টেম্পোরারি ফাইল পরিষ্কার করা হয়েছে, শাকিল ভাই!"
        except Exception as e:
            return f"ক্লিন করতে সমস্যা হয়েছে: {e}"
    return None