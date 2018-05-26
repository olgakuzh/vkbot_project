Python 3.7.0b4 (v3.7.0b4:eb96c37699, May  2 2018, 19:02:22) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import vk
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import vk
ModuleNotFoundError: No module named 'vk'
>>> import vk
>>> from flask import Flask
>>> bot = Flask(__bot__)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    bot = Flask(__bot__)
NameError: name '__bot__' is not defined
>>> bot = Flask(__name__)
>>> #created app object
>>> @bot.route('/', methods=['POST'])
def processing():
	data = json.loads(request.data)
	if data['type']=='confirmation' and data['group_id']==77276649:
		return 'ddba1e57'

	
>>> token = 9eaf8db387202be2153ccc9cbdeed9807ecaf064ac34ad04fea14591cbe4586562b513c6121771d1b32e3
SyntaxError: invalid syntax
>>> token = '9eaf8db387202be2153ccc9cbdeed9807ecaf064ac34ad04fea14591cbe4586562b513c6121771d1b32e3'
>>> @bot.route('/', methods=['POST'])
def welcome():
	if data['type']=='group_join':
		session=vk.session()
		api=vk.API(session)
		data['type']=='group_join':
		session=vk.session()
		api=vk.API(session, v=5.50)
		user_id = data['object']['user_id']
		api.message.send(access_token=token, user_id=str(user_id), message='Добро пожаловать в группу Волонтерского Центра ППОС ИГУ!')
		return 'ok'
	
SyntaxError: invalid syntax
>>> @bot.route('/',methods=['POST'])
def welcome():
	if data['type']=='group_join':
		session=vk.session()
		api=vk.API(session, v=5.50)
		user_id = data['object']['user_id']
		api.message.send(access_token=token, user_id=str(user_id), message='Добро пожаловать в группу Волонтерского Центра ППОС ИГУ!')
		return 'ok'

	
>>> 
