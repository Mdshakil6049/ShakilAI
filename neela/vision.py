import cv2

def capture_image():
    """ওয়েবক্যাম থেকে ছবি তুলে সেভ করার ফাংশন"""
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return "ক্যামেরা চালু করা সম্ভব হয়নি, স্যার।"
    
    ret, frame = cap.read()
    cap.release()
    cv2.destroyAllWindows()
    
    if ret:
        file_name = "neela_vision_snap.jpg"
        cv2.imwrite(file_name, frame)
        return f"শাকিল স্যার, ছবি তুলে '{file_name}' নামে সেভ করা হয়েছে।"
    else:
        return "ছবি তুলতে সমস্যা হয়েছে, স্যার।"