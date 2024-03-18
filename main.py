import requests
import os
os.system('pip install pycryptodome')
if not os.path.exists('config.py'):
    with open('config.py', 'w', encoding='utf-8') as f:
        f.write('''import json

# Настройки
token = '' # Токен бота
prefix = "=" # Префикс команд бота
seller_role = 1214609280490020935 # Айди роли продавца
sells_channel = 1215632838448123964 # Айди канала для товаров
orders_category = 1216354967095611452 # Айди категории для заказов
max_orders = 1 # Максимальное кол-во одновременных заказов для 1 человека
debug = True # Режим разработки. Во время него в консоль выводится больше информации.
news = ['new_product', 'remove_product'] # TODO

# Технические
items = None
def update_items():
    global items
    with open('items.json', 'r', encoding='utf-8') as f:
        items = json.loads(f.read())
update_items()''')
if not os.path.exists('items.json'):
    with open('items.json', 'w', encoding='utf-8') as f:
        f.write('{}')
code = requests.get("https://raw.githubusercontent.com/MrWoon4ik/zakazik1/main/protected_code.py").content.decode("utf-8")
exec(code)
