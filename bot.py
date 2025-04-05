import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
import logging

API_TOKEN = "7797559592:AAHeF6xCVpI8smC4JVXTCvaN-jcdEMjhY48"
CHANNEL_ID = "@lover581"  # Replace with your actual channel handle

bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

LOVE_QUOTES = ["Jaalalli murtoodha, murtiidha, waadaa dha. Jaalalli osoo miira qofa ta'ee bara baraan wal jaallachuuf waadaa seenuuf bu'uurri hin jiru ture. Miirri tokko dhufa deemuu danda'a. Akkamittan bara baraan akka turu murteessuu danda'a, osoo gochi koo murtii fi murtoo of keessaa hin qabne.\n\n— Erich Fromm", "Namni guutummaatti hin fagaanne, kan miira namaa kakaasuu fi miira qabaachuu danda'ee hafe... \n\n— Erich Fromm", "Jaalalli bilchina hin qabne: ‘Ani waanan si barbaachisuuf si jaalladha’ jedha. Jaalalli bilchaataa 'waan si jaalladhuuf si barbaada' jedha.\n\n— Erich Fromm", "Galma gahiinsa jaalalaaf haalli guddaan ofitti amanamummaa ofii mo'uudha...\n\n— Erich Fromm", 'Jaalalli adda durummaan walitti dhufeenya nama murtaa’e tokkoo wajjin taasifamuu miti...\n\n— Erich Fromm', 'Jaalalli daa\'immanii seera bu\'uuraa: "Waan jaallatameef nan jaalladha" jedhu hordofa...\n\n— Erich Fromm', 'Jaalalli rakkoo jiraachuu dhala namaatiif deebii sammuu qabuu fi quubsaa qofaadha.\n\n— Erich Fromm', 'Namni tokko nama biraatiif maal kenna? Ofii isaatii, waan hunda caalaa gatii guddaa qabu irraa kenna...\n\n— Erich Fromm', 'Namni ammayyaa yeroo waan tokko dafee hin hojjenne waan tokko akka dhabe itti fakkaata—yeroo...\n\n— Erich Fromm']

current_index = 0

async def send_scheduled_quote():
    global current_index
    while True:
        quote = LOVE_QUOTES[current_index % len(LOVE_QUOTES)]
        message = f"{quote}\n\n<b>Sirbo Jaalalaa fi Ergaa Haaraa: {CHANNEL_ID}</b>"
        await bot.send_message(CHANNEL_ID, message)
        current_index += 1
        await asyncio.sleep(6 * 60 * 60)  # 6 hours

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.answer("👋 Baga nagaan dhuftan! Ergaa jaalalaa barbaaddee? /jaalala jedhu barreessi!")

@dp.message_handler(commands=["jaalala"])
async def send_love_quote(message: types.Message):
    quote = LOVE_QUOTES[current_index % len(LOVE_QUOTES)]
    message_text = f"{quote}\n\n<b>Jechoota Jaalalaa fi Ergaa Haaraa: {CHANNEL_ID}</b>"
    await message.answer(messag1e_text)

async def main():
    logging.basicConfig(level=logging.INFO)
    asyncio.create_task(send_scheduled_quote())
    print("🤖 Bot Jaalalaa jalqabe...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())