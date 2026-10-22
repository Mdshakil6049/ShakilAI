import requests

def run_plugin(command):
    lower = command.lower()
    if "আবহাওয়া" in lower or "weather" in lower:
        try:
            url = "https://wttr.in/Dhaka?format=j1"
            res = requests.get(url, timeout=3)
            if res.status_code == 200:
                data = res.json()
                current = data['current_condition'][0]
                temp = current['temp_C']
                desc = current['weatherDesc'][0]['value']
                return f"বর্তমান আবহাওয়া: {desc}, তাপমাত্রা {temp} ডিগ্রি সেলসিয়াস।"
        except Exception:
            return "দুঃখিত, লাইভ আবহাওয়া তথ্য এই মুহূর্তে সংগ্রহ করা যায়নি।"
    return None