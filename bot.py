import telebot
token='05ec9bae4b077815fda7e0f5c4e2a47629e192b73ee5a2d85dad477d464d48638e75da98644febb666fcb'
vk = vk_api.VkApi(token=token) 
longpoll = VkLongPoll(vk)
from vk_api.longpoll import VkLongPoll, VkEventType
for event in longpoll.listen():
	if event.type == VkEventType.wall_post_new:
		response = requests.post(url='https://api.telegram.org/bot707930160:AAFgY1cC4r4g_qpyKoEYKBhMhzpQuyASVpc/SendMessage',data={'chat_id': @Bwahahaher, 'text': event.text}).json()