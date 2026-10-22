import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None

def get_ai_response(prompt):
    if not client:
        return "শাকিল স্যার, .env ফাইলে Gemini API Key বসানো হয়নি।"
    
    # ট্রাই করার জন্য উপযুক্ত মডেলের তালিকা
    models_to_try = ['gemini-2.5-flash', 'gemini-1.5-flash', 'gemini-3.8-flash']
    
    system_instruction = f"তোমার নাম নীলা। তুমি শাকিল স্যারের ব্যক্তিগত AI অ্যাসিস্ট্যান্ট। সংক্ষিপ্ত ও মিষ্টি করে বাংলা ভাষায় উত্তর দাও। প্রশ্ন: {prompt}"

    for model_name in models_to_try:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=system_instruction
            )
            return response.text.strip()
        except Exception as e:
            # যদি এই মডেলে সমস্যা হয়, পরের মডেল চেষ্টা করবে
            continue

    return "শাকিল স্যার, এআই সার্ভারে এই মুহূর্তে সংযোগ করতে সমস্যা হচ্ছে। কিছুক্ষণ পর আবার চেষ্টা করুন।"