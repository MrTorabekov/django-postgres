import requests
from datetime import datetime



def send_msg(**kwargs):
    token = "6862275470:AAFXJGsaji2GO6Uc9K-IpX8DF7R3Ij7OEfQ"  # bot token

    user_id = "1747966069"  # user id
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + user_id + "&text=" + f"{datetime.now().strftime(f'<b>%d/%m/%y  %H : %M : %S \n\nism: {kwargs['first_name']}\nfamiliya: {kwargs['last_name']}\nusername: {kwargs['username']}\nemail: {kwargs['email']}</b>')}&parse_mode=HTML"
    response = requests.get(url_req)
    print(response.json())
