import os
import streamlit as st
import telebot
import requests
import json
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('TELEGRAM_KEY')
api_key= os.getenv("CODEGPT_API_KEY")
agent_id= os.getenv("CODEGPT_AGENT_ID")

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['danigpt'])
def danigpt(message):
    clean_text = message.text.replace("/danigpt", "")
    url = 'https://plus.codegpt.co/api/v1/agent/'+agent_id
    headers = {"Content-Type": "application/json; charset=utf-8", "Authorization": "Bearer "+api_key}
    data = {
        "messages": [
            {
                "role": "user",
                "content": clean_text
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data, stream=True)
    raw_data = ''
    full_response = ""
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            raw_data = chunk.decode('utf-8').replace("data: ", '')
            if raw_data != "":
                lines = raw_data.strip().splitlines()
                for line in lines:
                    line = line.strip()
                    if line and line != "[DONE]":
                        try:
                            json_object = json.loads(line) 
                            result = json_object['data']
                            full_response += result
                        except json.JSONDecodeError:
                            print(f'Error al decodificar el objeto JSON en la línea: {line}')
    bot.reply_to(message, full_response)

st.success("Bot is running...")
bot.polling()