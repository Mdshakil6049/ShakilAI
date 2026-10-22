import cv2
import pyautogui
from pathlib import Path

def run_plugin(command):
    lower = command.lower()
    if "স্ক্রিনশট" in lower or "screenshot" in lower:
        try:
            img_path = Path("screenshot.png")
            pyautogui.screenshot(str(img_path))
            return "একটি স্ক্রিনশট সফলভাবে সেভ করা হয়েছে, শাকিল ভাই!"
        except Exception as e:
            return f"স্ক্রিনশট নিতে সমস্যা হয়েছে: {e}"
    elif "ক্যামেরা" in lower or "webcam" in lower or "ছবি তোলো" in lower:
        try:
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            if ret:
                img_path = Path("webcam_shot.png")
                cv2.imwrite(str(img_path), frame)
                cap.release()
                return "ওয়েবক্যাম থেকে একটি ছবি সফলভাবে তোলা হয়েছে!"
            cap.release()
            return "ওয়েবক্যাম চালু করা যায়নি।"
        except Exception as e:
            return f"ক্যামেরা এরর: {e}"
    return None