import asyncio
import requests
import json
from telethon import TelegramClient, events
import logging
import asyncpraw
import shutil
import os, sys
import subprocess
from redvid import Downloader


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
print('Loading env variables.')
api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')
bot_token = os.getenv('bot_token')
print('Env vars loaded correctly.')

channel = os.getenv('channel')
log = os.getenv('log')

CLIENT_ID = os.getenv('CLIENT_ID')
SECRET = os.getenv('SECRET')
# subreddit = 'RWBY'
username = os.getenv('username')
password = os.getenv('password')

reddit = asyncpraw.Reddit(
    client_id=CLIENT_ID,
    client_secret=SECRET,
    user_agent=os.getenv('user_agent'),
    username=username,
    password=password
)

bot = TelegramClient(os.getenv('SESSION'), api_id, api_hash).start(bot_token=bot_token)
@bot.on(events.NewMessage)
async def my_event_handler(event):
    if event.raw_text.startswith("/gib"):
        if event.chat_id != channel:
            await bot.send_message(event.chat_id,
                                   os.getenv('YOUR_MESSAGE'))
        else:
            i = 0
            z = 0
            lista = []
            gallist = []
            subreddit = await reddit.subreddit(os.getenv('SUBREDDITS'))
            async for submission in subreddit.stream.submissions():
                my_list = submission.url.split("/")
                if not submission.stickied:
                    if submission.url.endswith(".jpg") or submission.url.endswith(
                            ".png") or submission.url.endswith("gif"):
                        lista.append(submission.url)
                        while i < len(lista):
                            taitle = submission.url
                            textoc = submission.title
                            try:
                                await bot.send_file(channel, lista[i], caption=f"[{textoc}]({taitle})", link_preview=False)
                                await asyncio.sleep(1)
                            except:
                                await bot.send_message(channel, f"[{textoc}]({taitle})", link_preview=True)
                                await asyncio.sleep(1)
                            lista.pop(i)
                            i += 1
                    if my_list[3] == "gallery":
                        try:
                            o = 0
                            p = subprocess.Popen("mkdir extractions", shell=True)
                            await asyncio.sleep(3)
                            os.chdir("extractions")
                            post = await reddit.submission(id=submission.id)
                            print(post)
                            gallery = []
                            ids = [j['media_id'] for j in post.gallery_data['items']]
                            for id in ids:
                                # print(i)
                                url = post.media_metadata[id]['p'][0]['u']
                                url = url.split("?")[0].replace("preview", "i")
                                gallery.append(url)
                            for img in gallery:
                                name = (str(o) + "." + img.split(".")[3])
                                req = requests.get(img)
                                with open(name, 'wb') as f:
                                    f.write(req.content)
                                    o += 1
                            pops = 0
                            arr = os.listdir()
                            elar = len(arr) - 1
                            if arr[elar].endswith(".jpg"):
                                mmo = len(arr)
                            else:
                                mmo = len(arr) - 1
                            while pops < mmo:
                                subir = (str(pops) + "." + img.split(".")[3])
                                await bot.send_file(channel, subir)
                                await asyncio.sleep(1)
                                pops += 1
                                try:
                                    os.remove(os.getenv('SESSION')+'.session')
                                except:
                                    pass
                            for img in gallery:
                                xd = 0
                                arr = os.listdir()
                                ror = len(arr)
                                while ror > xd:
                                    borrar = (str(xd) + "." + img.split(".")[3])
                                    os.remove(borrar)
                                    await asyncio.sleep(1)
                                    xd += 1
                            os.chdir("..")

                        except:
                            await bot.send_message(log, submission.url)



loop = asyncio.get_event_loop()
loop.run_forever()
