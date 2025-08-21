import subprocess
import re
import platform
import sys

if platform.system() != "Windows":
    print("This script only works on Windows!")
    sys.exit()

wifi_list = []

try:
    command_output = subprocess.run("netsh wlan show profiles", shell=True, capture_output = True).stdout.decode()
    profile_names = (re.findall("All User Profile     : (.*)\r", command_output))

    if len(profile_names) != 0:
        for name in profile_names:
            try:
                wifi_profile = {}
                profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
                if re.search("Security key           : Absent", profile_info):
                    continue
                else:
                    wifi_profile["ssid"] = name
                    profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
                    password = re.search("Key Content            : (.*)\r", profile_info_pass)
                    if password == None:
                        wifi_profile["password"] = None
                    else:
                        wifi_profile["password"] = password[1]
                    wifi_list.append(wifi_profile)
            except subprocess.CalledProcessError:
                print(f"[!] Failed to get details for SSID: {name}")
            except Exception as e:
                print(f"[!] Unexpected error for SSID '{name}': {str(e)}")
except subprocess.CalledProcessError:
    print("[!] Failed to run netsh command. Are you running this as Administrator?")
except Exception as e:
    print(f"[!] Unexpected error: {str(e)}")
    
    
for wifi in wifi_list:
    result = f"\nWifi: {wifi['ssid']}\nPassword: {wifi['password']}\n"
    print(result)
