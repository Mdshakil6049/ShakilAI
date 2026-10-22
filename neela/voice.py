import asyncio
import edge_tts
import os
import threading
import speech_recognition as sr
import sounddevice as sd
import scipy.io.wavfile as wav

# অডিও কথা বলা (Text-to-Speech)
async def _speak_async(text):
    voice = "bn-BD-NabanitaNeural"
    output_file = "neela_speech.mp3"
    
    if os.path.exists(output_file):
        try:
            os.remove(output_file)
        except Exception:
            pass

    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)
    
    # ব্যাকগ্রাউন্ড থ্রেডে অডিও প্লে করা
    os.system(f'start /min "" "{output_file}"')

def speak(text):
    print(f"[নীলা কথা বলছে]: {text}")
    try:
        # নন-ব্লকিং অডিও এক্সিকিউশন
        threading.Thread(target=lambda: asyncio.run(_speak_async(text)), daemon=True).start()
    except Exception as e:
        print(f"ভয়েস আউটপুটে সমস্যা: {e}")

# কথা শোনা (Speech-to-Text)
def listen():
    recognizer = sr.Recognizer()
    duration = 4  # ৪ সেকেন্ড অপেক্ষা করবে
    sample_rate = 44100
    temp_wav = "temp_voice.wav"
    
    try:
        print("\n🎤 নীলা শুনছে... (বলুন)")
        audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
        sd.wait()
        
        wav.write(temp_wav, sample_rate, audio_data)
        
        with sr.AudioFile(temp_wav) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio, language='bn-BD')
            print(f"🗣️ আপনি বলেছেন: {text}")
            
            if os.path.exists(temp_wav):
                os.remove(temp_wav)
            return text
            
    except sr.UnknownValueError:
        print("নীলা: দুঃখিত স্যার, আপনার কথা বুঝতে পারিনি।")
    except Exception as e:
        print(f"মাইক্রোফোনে সমস্যা: {e}")
        
    if os.path.exists(temp_wav):
        os.remove(temp_wav)
    return ""