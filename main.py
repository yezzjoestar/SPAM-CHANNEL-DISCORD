import requests, time

def main():
    channelId = str(input("Identifiant du salon ou envoyer le spam -> "))
    auth = str(input("ton token -> "))
    
    headers = {
      "authorization": f"{auth}",
    }
    
    payload = {
      "content": "TON MESSAGE"
    }
    
    while True:
      r = requests.post(f"https://canary.discord.com/api/v9/channels/{channelId}/messages", headers=headers, data=payload)
      if r.ok:
        print("raidsent")
      else:
        print("Status code : ", r.status_code)
        break
      time.sleep(0)
main()
