#Импорт модулей
from vk_api.utils import get_random_id
from rich import print
import rich
import vk_api
import time
import os

#баннер
info = '''
	[red]██╗░░░██╗██╗░░██╗[/red][green]░█████╗░██████╗░██╗[/green]
	[red]██║░░░██║██║░██╔╝[/red][green]██╔══██╗██╔══██╗██║[/green]
	[red]╚██╗░██╔╝█████═╝[/red][green]░███████║██████╔╝██║[/green]
	[red]░╚████╔╝░██╔═██╗[/red][green]░██╔══██║██╔═══╝░██║[/green]
	[red]░░╚██╔╝░░██║░╚██╗[/red][green]██║░░██║██║░░░░░██║[/green]
	[red]░░░╚═╝░░░╚═╝░░╚═╝[/red][green]╚═╝░░╚═╝╚═╝░░░░░╚═╝[/green]
       [white]Made by:[/white] [bold white]@karuseel_noname[/bold white], [white]Version:[/white] 1.0\n\n'''

#Очистка консоли
def cls():
	os.system('cls' if os.name == 'nt' else 'clear')

#Пост на стене
def post():
	try:
		print(info)
		tokk = input("Введите токен: ") 
		token = vk_api.VkApi(token=tokk) 
		vk = token.get_api()
		nm = int(input('Сколько постов создать: '))
		mess = input('Текст поста/постов: ')
		onlf = int(input('Кому будет виден пост? 1-друзьям, 0-всем: '))
		for i in range(nm):
			time.sleep(4)
			vk.wall.post(message=mess, friends_only=onlf)
			print('[bold white]Пост/Посты успешно созданы[/bold white]')
			input('Что-бы попасть на главное меню нажмите enter: ')
			main()
	except Exception as er:
		print('[bold red]Неверный токен или проблемы с сетью[/bold red]')
		print(er)

#Информация о прифиле		
def profile():
	try:
		print(info)
		tokk = input("Введите токен: ")
		token = vk_api.VkApi(token=tokk)
		vk = token.get_api()
		res = vk.users.get()
		st = vk.status.get()
		print(f'[bold white]ФИО:[/bold white] [bold red]{res[0]["first_name"]} {res[0]["last_name"]}[/bold red] | [bold white]ID:[/bold white] {res[0]["id"]} | [bold white]Ваш статус:[/bold white] [bold yellow]{st["text"]}[/bold yellow]')
		input('Что-бы попасть на главное меню нажмите enter: ')
		main()
	except Exception as er:
		print('[bold red]Неверный токен или проблемы с сетью[/bold red]')
		print(er)

#Изменить статус
def sets():
	try:
		print(info)
		tokk = input("Введите токен: ")
		token = vk_api.VkApi(token=tokk)
		vk = token.get_api()
		mess = input('Введите текст нового статуса: ')
		vk.status.set(text=mess)
		print('[bold white]Статус успешно установлен![/bold white]')
		input('Что-бы попасть на главное меню нажмите enter: ')
		main()
	except Exception as er:
		print('[bold red]Неверный токен или проблемы с сетью[/bold red]')
		print(er)

#Информация о онлайн друзьях		
def onlf():
	try:
		print(info)
		tokk = input('Введите токен: ')
		token = vk_api.VkApi(token=tokk)
		vk = token.get_api()
		fr = vk.friends.getOnline()
		for f in fr:
			inf = vk.users.get(user_ids=f)
			print(f'[bold white]ФИО:[/bold white] [bold red]{inf[0]["first_name"]} {inf[0]["last_name"]}[/bold red] | ID: {inf[0]["id"]}')
	except Exception as er:
		print('[bold red]Неверный токен или проблемы с сетью[/bold red]')
		print(er)		

#Отправка сообщение по ID
def send():
	try:
		print(info)
		tokk = input('Введите токен: ')
		token = vk_api.VkApi(token=tokk)
		vk = token.get_api()
		id = int(input('Введите id пользователя: '))
		mess = input('Введите сообщение для отправки: ')
		vk.messages.send(user_id=id, message=mess, random_id=get_random_id())
		print('[bold white]Сообщение успешно отправлено![/bold white]')
		input('Что-бы попасть на главное меню нажмите enter: ')
		main()
	except Exception as er:
		print('[bold red]Неверный токен или проблемы с сетью[/bold red]')
		print(er)

#Инфоомация о всех друзьях	
def fget():
	try:
		print(info)
		tokk = input('Введите токен: ')
		token = vk_api.VkApi(token=tokk)
		vk = token.get_api()
		fr = vk.friends.get()
		print(f'Количество друзей: {fr["count"]}')
		frr = fr['items']
		for f in frr:
			inf = vk.users.get(user_ids=f)
			print(f'[bold white]ФИО:[/bold white] [bold red]{inf[0]["first_name"]} {inf[0]["last_name"]}[/bold red] | ID: {inf[0]["id"]}')
	except Exception as er:
		print('[bold red]Неверный токен или проблемы с сетью[/bold red]')
		print(er)

#Типо handler		
def main():
	cls()
	print(info)
	print('''[1][bold magenta]Мой профиль[/bold magenta]
[2][bold magenta]Список моих друзей[/bold magenta]
[3][bold magenta]Список моих онлайн друзей[/bold magenta]
[4][bold magenta]Сделать пост на стене[/bold magenta]
[5][bold magenta]Установить новый статус[/bold magenta]
[6][bold magenta]Отправить сообщение по ID[/bold magenta]
[7][bold magenta]Выход из скрипта[/bold magenta]

''')
	func = input('Выберите функцию: ')
	if func == '1':
		cls()
		profile()
	elif func == '2':
		cls()
		fget()
	elif func == '3':
		cls()
		onlf()
	elif func == '4':
		cls()
		post()
	elif func == '5':
		cls()
		sets()
	elif func == '6':
		cls()
		send()
	elif func == '7':
		os.system(exit())
	else:
		cls()
		print('[bold red]Такого варианта нету![/bold red]')
	
main()			