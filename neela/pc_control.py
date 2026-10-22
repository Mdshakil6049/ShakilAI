import os
import subprocess
import webbrowser

def open_app(command):
    command = command.lower()
    
    # ব্রাউজার ও ওয়েবসাইট খোলা
    if "youtube" in command or "ইউটিউব" in command:
        webbrowser.open("https://www.youtube.com")
        return "শাকিল স্যার, ইউটিউব চালু করা হয়েছে।"
        
    elif "google" in command or "গুগল" in command:
        webbrowser.open("https://www.google.com")
        return "শাকিল স্যার, গুগল খুলে দেওয়া হয়েছে।"
        
    elif "facebook" in command or "ফেসবুক" in command:
        webbrowser.open("https://www.facebook.com")
        return "শাকিল স্যার, ফেসবুক ওপেন করা হয়েছে।"

    # পিসির বিভিন্ন অ্যাপস খোলা
    elif "notepad" in command or "নোটপ্যাড" in command:
        os.system("start notepad")
        return "শাকিল স্যার, নোটপ্যাড চালু করা হয়েছে।"
        
    elif "calculator" in command or "ক্যালকুলেটর" in command:
        os.system("start calc")
        return "শাকিল স্যার, ক্যালকুলেটর খোলা হয়েছে।"
        
    elif "cmd" in command or "টার্মিনাল" in command:
        os.system("start cmd")
        return "command prompt চালু করা হয়েছে, স্যার।"
        
    elif "chrome" in command or "ক্রোম" in command:
        try:
            os.system("start chrome")
            return "শাকিল স্যার, ক্রোম ব্রাউজার চালু করা হয়েছে।"
        except Exception:
            webbrowser.open("https://www.google.com")
            return "গুগল ক্রোম খোলা হয়েছে, স্যার।"

    return None