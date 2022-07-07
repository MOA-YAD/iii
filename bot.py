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
moa_yad = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

moment_worker = []



#هنا رسالة الستارت
#تكدر اتغير الرد مالتها 
#تشوف النجمه 
#امسح بس 🌟
#""وحط الرد بدون ما تمسح الـ


@moa_yad.on(events.NewMessage(pattern="/start"))
async def start(event):
  await event.reply("رساله الستارت",
                    link_preview=False
                   )

#هنا الردود انته ومخك
#النجمه هيه الرد


@moa_yad.on(events.NewMessage(pattern="كلمه"))
async def start(event):
  await event.reply("🌟",
                    link_preview=False
                   )


print("تم تنصيب بوت التاك بنجاح")
print("لو محتاج مساعده @MOA_YAF")
moa_yad.run_until_disconnected()
