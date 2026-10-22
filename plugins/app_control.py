import os
import pyautogui

def run_plugin(command):
    lower = command.lower()
    if "ফোল্ডার খোলো" in lower or "open folder" in lower:
        try:
            os.system("start .")
            return "বর্তমান প্রজেক্ট ফোল্ডারটি ওপেন করা হয়েছে, শাকিল ভাই!"
        except Exception as e:
            return f"ফোল্ডার ওপেন করতে সমস্যা হয়েছে: {e}"
    elif "টাইপ করো" in lower:
        text_to_type = command.replace("টাইপ করো", "").strip()
        if text_to_type:
            pyautogui.write(text_to_type, interval=0.05)
            return f"টেক্সট টাইপ করা হয়েছে: {text_to_type}"
    return None