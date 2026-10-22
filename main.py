import os
import threading
import tkinter as tk
from tkinter import ttk, scrolledtext
from dotenv import load_dotenv

from neela.voice import speak, listen
from neela.ai_router import get_ai_response
from neela.pc_control import open_app
from neela.vision import capture_image

load_dotenv()

class NeelaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ShakilAI - Neela Assistant")
        self.root.geometry("550x650")
        self.root.configure(bg="#1e1e2e")

        # শিরোনাম
        title_label = tk.Label(
            root, text="🤖 নীলা এআই অ্যাসিস্ট্যান্ট", 
            font=("Arial", 18, "bold"), bg="#1e1e2e", fg="#cba6f7"
        )
        title_label.pack(pady=15)

        # চ্যাট প্রদর্শন স্ক্রিন
        self.chat_area = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, width=58, height=18, 
            font=("Arial", 10), bg="#181825", fg="#cdd6f4", insertbackground="white"
        )
        self.chat_area.pack(padx=15, pady=5)
        self.chat_area.config(state=tk.DISABLED)

        # ইনপুট ফ্রেম
        input_frame = tk.Frame(root, bg="#1e1e2e")
        input_frame.pack(fill=tk.X, padx=15, pady=10)

        self.entry_box = tk.Entry(
            input_frame, font=("Arial", 11), bg="#313244", fg="#cdd6f4", insertbackground="white"
        )
        self.entry_box.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=6, padx=(0, 5))
        self.entry_box.bind("<Return>", lambda event: self.process_text_input())

        send_btn = tk.Button(
            input_frame, text="পাঠান", font=("Arial", 10, "bold"), 
            bg="#89b4fa", fg="#11111b", command=self.process_text_input
        )
        send_btn.pack(side=tk.RIGHT, ipadx=10, ipady=3)

        # বাটন ফ্রেম (ভয়েস ও ক্যামেরা)
        btn_frame = tk.Frame(root, bg="#1e1e2e")
        btn_frame.pack(pady=10)

        mic_btn = tk.Button(
            btn_frame, text="🎤 মুখে বলুন", font=("Arial", 11, "bold"), 
            bg="#a6e3a1", fg="#11111b", command=self.start_voice_input
        )
        mic_btn.pack(side=tk.LEFT, padx=10, ipady=5)

        cam_btn = tk.Button(
            btn_frame, text="📷 ছবি তুলুন", font=("Arial", 11, "bold"), 
            bg="#f9e2af", fg="#11111b", command=self.take_photo
        )
        cam_btn.pack(side=tk.RIGHT, padx=10, ipady=5)

        # প্রারম্ভিক বার্তা
        self.display_message("নীলা", "শাকিল স্যার, আমি নীলা। আপনাকে কীভাবে সাহায্য করতে পারি?")
        threading.Thread(target=speak, args=("শাকিল স্যার, আমি নীলা। আপনাকে কীভাবে সাহায্য করতে পারি?",), daemon=True).start()

    def display_message(self, sender, message):
        """চ্যাট স্ক্রিনে মেসেজ দেখানোর ফাংশন"""
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_area.see(tk.END)
        self.chat_area.config(state=tk.DISABLED)

    def handle_command(self, user_input):
        """কমান্ড প্রসেস করার লজিক"""
        if not user_input.strip():
            return

        self.display_message("আপনি", user_input)

        if "open" in user_input.lower() or "খুলো" in user_input or "চালু করো" in user_input:
            response = open_app(user_input)
            if not response:
                response = get_ai_response(user_input)
        elif "ছবি তোলো" in user_input or "ক্যামেরা" in user_input:
            response = capture_image()
        else:
            response = get_ai_response(user_input)

        self.display_message("নীলা", response)
        speak(response)

    def process_text_input(self):
        text = self.entry_box.get()
        self.entry_box.delete(0, tk.END)
        threading.Thread(target=self.handle_command, args=(text,), daemon=True).start()

    def start_voice_input(self):
        def voice_thread():
            user_speech = listen()
            if user_speech:
                self.handle_command(user_speech)
        threading.Thread(target=voice_thread, daemon=True).start()

    def take_photo(self):
        def photo_thread():
            res = capture_image()
            self.display_message("নীলা", res)
            speak(res)
        threading.Thread(target=photo_thread, daemon=True).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = NeelaGUI(root)
    root.mainloop()