import json

DEBUG = False
with open('settings.json', 'r', encoding='utf-8') as file:
    settings = json.load(file)