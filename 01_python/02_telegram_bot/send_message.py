import requests
from decouple import config


base = "https://api.telegram.org"

token = config{'TELEGRAM_BOT_TOKEN'} #토큰 값     --> 숨긴다. 

chat_id = config{'CHAT_ID'}##보낸 사람의 id : 1054943909

#.env에서 token값과 chat_id 숨겨준다. 


text = "hello"## 보낼 메시지 

url = f'{base}/bot{token}/sendMessage?chat_id={chat_id}&text={text}' #f stream

send_message = requests.get(url)

print(send_message)