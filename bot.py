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
#تكدر اتسوي صوره بس حط رابط تلكراف

@moa_yad.on(events.NewMessage(pattern="/start"))
async def start(event):
  await event.reply("رساله الستارت",
                    link_preview=False
                   )

#هنا الردود انته ومخك
#النجمه هيه الرد
#تكدر تنسخ الصطر 49-50-51-52--53
#وتلسقه وتئكد منه ايكون مطابق % بدون اي نقص او زياده
#تكدر اتكرر هاي العمليه مليون مره ومليون رد 
#(كلمه)يعني الشي الي راح ادزه ويرد عليك
#ومهم تعرف تكدر اتسوي الرد صوره 
#شلون
#امسح النجمه وحط رابط تلكراف للصوره
#ويكون مضبوط يعني لا ناقص ولا زايد

@moa_yad.on(events.NewMessage(pattern="كلمه"))
async def start(event):
  await event.reply("🌟",
                    link_preview=False
                   )

#هنا راح اسويلك مثال شلون اتسوي رد ويا زر
#بكل بصاطه
#تسوي رد مثل ما علمتك فوك
#بس اتحط امر الزر.
#شلون اتسوي.
#سوي راس صطر انتبه وين مكانه.
#مكانه الكلمه الي راح ترد بيها الي هيا النجمه انتبه النجمه بعدها علامه (") وبعدها علامة (,) ـمـ.
#(,)تسوي راس صطر بعد علامة الـ
#تلسق الامر الي تحت ودير بالك احذف الهاشتاك علمود يشتغل
#buttons=(
#                      [
#                        Button.url('مطور البوت', 'https://t.me/MOA_YAD'),   
#                      ]
#                   ),

#مثال لرد + زر
@moa_yad.on(events.NewMessage(pattern="المطور"))
async def start(event):
  await event.reply("🌟",
                    buttons=(
                      [
                        Button.url('مطور البوت', 'https://t.me/MOA_YAD'),   
                      ]
                   ),
                    link_preview=False
                   )

#هنا الكلمات الي راح تطلع بعد ما تنصب بهيروكو
print("تم تنصيب بوتك بنجاح")
print("لو محتاج مساعده @MOA_YAF")
moa_yad.run_until_disconnected()
