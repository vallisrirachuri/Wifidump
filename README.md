# WiFiDump

WiFiDump is a Python script that extracts saved Wi-Fi SSIDs and their passwords on **Windows** systems.  
It uses the built-in `netsh wlan` commands to retrieve details of stored Wi-Fi profiles.

⚠️ **Disclaimer:** This tool is for educational and personal recovery purposes only.  
Do **not** use it on machines you don’t own or without explicit permission. Misuse can be illegal.

---

## 📌 Features
- Lists all saved Wi-Fi SSIDs on your Windows machine.  
- Retrieves corresponding passwords (if stored).  
- Skips networks without saved keys.  
- Error handling for missing or restricted profiles.  

---

## ✅ Pros
- Simple and lightweight script (no external libraries needed).  
- Works directly with built-in Windows commands.  
- Useful for recovering forgotten Wi-Fi passwords.  
- Easy to understand and modify.  

---

## ❌ Cons
- Works **only on Windows** (Linux/Mac not supported).  
- Requires appropriate permissions (sometimes *Administrator*).  
- Passwords are shown in plain text (security concern if misused).  
- Relies on `netsh`, so formatting changes in Windows may break regex.  

---

## 🚀 Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/wifidump.git
   cd wifidump
