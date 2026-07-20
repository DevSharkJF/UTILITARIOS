from instascrape import Reel
import time

SESSIONID = "id de sessão"

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43",
"cookie":f'sessionid={SESSIONID};'
}

google_reel=Reel('Link do Reel')
google_reel.scrape(headers=headers)
google_reel.download(fp=f".//Desktop//reel{int(time.time())}.mp4")
print('Download Completo.')
