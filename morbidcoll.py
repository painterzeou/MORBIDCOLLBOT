from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon import TelegramClient, sync
from telethon import events
from telethon.tl.custom import Button
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
from bs4 import BeautifulSoup
import time
import re, threading
from time import sleep
c = requests.session()
def css():
	api_id = '24439789'
	api_hash = 'db157eec30c0274f7b3ca5ccabffa836'
	client = TelegramClient('session', api_id, api_hash)
	client.start()
	channel_username = '@@MORBIDCOLLBOT'
	channel_entity = client.get_entity(channel_username)
	client.send_message('@MORBIDCOLLBOT' ,'/start')
	sleep(1)
	mssag = client.get_messages('@MORBIDCOLLBOT', limit=1)
	mssag[0].click(2)
	sleep(3)
	mssag1 = client.get_messages('@MORBIDCOLLBOT', limit=1)
	mssag1[0].click(0)
	sleep(1)
	for ffguf  in range(10000):
	    sleep(4)
	    l = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
	    j = l.messages[0]
	    if j.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
	        client.send_message('احا ')
	        break
	    url = j.reply_markup.rows[0].buttons[0].url
	    try :
	        try :
	           client(JoinChannelRequest(url))
	        except :
	            bott = url.split('/')[-1]
	            client(ImportChatInviteRequest(bott))
	
	        mssag2 = client.get_messages('@MORBIDCOLLBOT', limit=1)
	        mssag2[0].click(text='تحقق')
	    except :
	        client.send_message('me','حظروك ياريس ')
	        break
	client.disconnect()



css()