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

import requests

def post_serpapi(question: str):
    url = "https://fastapi-render-danigpt.onrender.com/serpapi"
    parametros = {
        "question": question
    }
    respuesta = requests.post(url, json=parametros)
    if respuesta.status_code == 200:
        print("Solicitud POST exitosa")
        print(respuesta.json())
    else:
        print("Error en la solicitud POST")


@bot.message_handler(commands=['danigpt'])
def danigpt(message):
    clean_text = message.text.replace("/danigpt", "")
    url = 'https://api.codegpt.co/api/v1/chat/completions'
    headers = {"Content-Type": "application/json; charset=utf-8", "Authorization": "Bearer "+api_key}
    {
      "agentId": agent_id,
      "stream":true,
      "format":"json"
      "messages":
      [{
        "content": "What is the meaning of life?",
        "role": "user"
      }]
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
