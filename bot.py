import os, logging, asyncio

from telegraph import upload_file

from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
xavierbot = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

moment_worker = []


#start
@xavierbot.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("رساله الستارت",
                    buttons=(
                      [
                        Button.url('مكان زر', 'مكان رابط'),   
                      ]
                   ), 
                    link_preview=False
                   )

#help
@xavierbot.on(events.NewMessage(pattern="^مكان كلمه مردود عليها$"))
async def help(event):
  helptext = "الرد"
  await event.reply(helptext,
                    buttons=(
                      [
                        Button.url('مطور البوت', 'https://t.me/MOA_YAD'),   
                      ]
                   ), 
                    link_preview=False
                   )


print("تم تنصيب بوت التاك بنجاح 💕🍂")
print("لو محتاج مساعده @MOA_YAF")
xavierbot.run_until_disconnected()
