import threading
import requests,os,random


def tg(username,discriminator,token):
    global worked,failed
    r = requests.Session()
    
    url = "https://discord.com/api/v9/users/@me/relationships"
    headers = {"accept": "/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en-CH;q=0.9,en-GB;q=0.8",
    "authorization": token,
    "content-length": "0",
    "origin": "https://discord.com",
    "referer": "https://discord.com/channels/@me",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.669 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36",
    "x-debug-options": "bugReporterEnabled",
    "x-discord-locale": "hu",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42NjkiLCJvc192ZXJzaW9uIjoiMTAuMC4xOTA0MyIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMzMwOTgsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }
    body = {"username": username, "discriminator": discriminator}
    

    proxyb = random.choice(workproxy)
    proxies = {'http': f'http://{proxyb}','https':f'http://{proxyb}'}
    try:  
      res = r.post(url, headers=headers, json=body,proxies=proxies)
    except:
      pass
    
    if res.status_code == 204:
        worked +=1
    else:
      if res.status_code == 401:
        failed += 1
      else:
        failed += 1

    os.system(f"title discord.gg/catcha ^| Worked: {worked} ^| Failed: {failed}")


os.system("cls")
worked = 0
failed = 0

readproxy = open('proxies.txt','r')
readproxy2 = readproxy.readlines()
workproxy = []
for proxy3 in readproxy2:
    proxystrip = proxy3.strip('\n')
    workproxy.append(proxystrip)

user = input("Enter the tag (catcha80#0001): ")
th = input("Thread Amount ->")

for x in range(int(th)):
    filefile = open('tokens.txt')
    token = random.choice(open("tokens.txt", "r" ).read().splitlines())
    filefile.close()
    username = user.split("#")[0]
    discriminator = user.split("#")[1]
    token = token.replace("\n", "")

    threading.Thread(target=tg,args=(username,discriminator,token,)).start()


input("Press enter to close")

