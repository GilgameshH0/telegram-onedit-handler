from telethon import TelegramClient, events, sync
import telebot

#берем из BotFather
bot = telebot.TeleBot('')

# брать с сайта телеграмма https://my.telegram.org/auth
api_id = ''
api_hash = ''
client = TelegramClient('mirror', api_id, api_hash)

client.start()

#Id чата откуда перехватывать сообщения при редактировании
@client.on(events.MessageEdited(-1111111111111))
async def sendMyMessage(event):
    #Id чата куда отправлять сообщения
    bot.send_message(-1111111111111, event.message.text)

@client.on(events.MessageEdited(-1111111111111))
async def sendMyMessage(event):
    bot.send_message(-1111111111111, event.message.text)    

client.run_until_disconnected()