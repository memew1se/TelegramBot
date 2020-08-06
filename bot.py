import requests
import aiogram
from config import API_link

updates = requests.get(API_link + "/getUpdates?offset=-1").json()

message = updates["result"][0]["message"]
chat_id = message["from"]["id"]
text = message["text"]

sent_message = requests.get(API_link + f'/sendMessage?text=Привiт, ты напи'
                                       f'сал - {text}&chat_id={chat_id}')
