import subprocess

def run_plugin(command):
    lower = command.lower()
    if "ব্যাটারি" in lower or "battery" in lower:
        try:
            cmd = "powershell (Get-WmiObject Win32_Battery).EstimatedChargeRemaining"
            res = subprocess.run(cmd, capture_output=True, text=True, shell=True)
            pct = res.stdout.strip()
            if pct:
                return f"আপনার পিসির ব্যাটারি চার্জ আছে: {pct} শতাংশ!"
            return "পিসিতে কোনো ব্যাটারি পাওয়া যায়নি (হতে পারে এটি ডেক্সটপ পিসি)।"
        except Exception as e:
            return f"ব্যাটারি চেক করতে সমস্যা হয়েছে: {e}"
    return None