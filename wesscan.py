from discord_webhook import DiscordWebhook
import time
import subprocess
from colorama import Fore, Style, Back, init

init(autoreset=True)

print(Back.BLACK + Fore.MAGENTA + '''
__  _  __ ____   ______ ______ ____ _____    ____  
\ \/ \/ // __ \ /  ___//  ___// ___\\__  \  /    \ 
 \     /\  ___/ \___ \ \___ \\  \___ / __ \|   |  \
  \/\_/  \___  >____  >____  >\___  >____  /___|  /
             \/     \/     \/     \/     \/     \/
''')

print(Back.BLACK + Fore.YELLOW + 'max 255')
Range_input = int(input(Back.BLACK + Fore.WHITE + 'Check de 1 à :'))

results = []
for ping in range(1, Range_input + 1): 
    address = "192.168.133." + str(ping)
    res = subprocess.call(['ping', '-c', '1', address], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if res == 0: 
        result = f"ping à {address} OK"
        print(Back.BLACK + Fore.GREEN + result)
    elif res == 2: 
        result = f"Non active : {address}"
        print(Back.BLACK + Fore.YELLOW + result)
    else: 
        result = f"Ping à {address} n'as pas marchée !"
        print(Back.BLACK + Fore.RED + result)
    results.append(result)

webhook_url = 'https://discord.com/api/webhooks/1249380402074882180/-RhSdBmlcnMQoo2E1XJfRwRfShWKQnWXQqmTt9dk0tFLbwWtpVko9CH8O4P8S6WIr9qj'
webhook = DiscordWebhook(url=webhook_url, content="\n".join(results))
webhook.execute()

time.sleep(10)
