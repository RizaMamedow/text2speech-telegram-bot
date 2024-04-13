from gtts import gTTS
import telebot

from src.additions import match_lang
from config import TOKEN


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id, 
        """TextToSpeech (by krugleshock) \nНапиши сообщение получишь звук"""
        )


@bot.message_handler(content_types=['text'])
def send_voices(message):
    voice_path = 'voices/voice.mp3'

    bot.send_message(message.chat.id, "Подождите секунду пока обработается запрос")

    tts = gTTS(
        message.text, 
        lang=("en" if match_lang(message.text) else "ru")
    )

    tts.save(voice_path)

    with open(voice_path, 'rb') as audio:
        bot.send_audio(message.from_user.id, audio)