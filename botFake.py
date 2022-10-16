import telebot
from telebot import types
from faker import Faker
Token = "5523757035:AAEB83pwPkYwZ-4fobFY2kz3gIu2Ir4sUvA"
bot = telebot.TeleBot(Token)
key = types.InlineKeyboardMarkup()
A = types.InlineKeyboardButton(text="Developer",url="t.me/BEEEB8")
B = types.InlineKeyboardButton(text="Channel",url="t.me/php06")
key.add(A,B)
@bot.message_handler(commands=['start'])
def start(message):
	x = """
*- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*
*- Welcome to fake information .*

*- Send command* /fake *.*
*- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*
"""
	bot.send_message(message.chat.id,x,parse_mode="Markdown",reply_markup=key)
	
@bot.message_handler(commands=["fake"])
def fake(message):
	F=Faker()
	email=F.free_email() ;ip=F.ipv4()
	date=F.date() ;last=F.last_name_male() 
	first=F.first_name_male() ;job=F.job()
	con=F.country() ;city=F.city()
	str=F.street_name() ;zip=F.zipcode()
	card=F.credit_card_full() ;zone=F.timezone()
	num=F.phone_number()
	tele = f"""
*First Name:* `{first}`
*Last Name:* `{last}`
*Job:* `{job}`
*Time Zone:* `{zone}`
*Country:* `{con}`
*City:* `{city}`
*Street:* `{str}`
*Zip Code:* `{zip}`
*Email:* `{email}`
*Phone:* `{num}`
*IP:* `{ip}`
*Credit Card:* `{card}`
"""
	bot.send_message(message.chat.id,tele,parse_mode="Markdown",reply_markup=key)
	
bot.polling(True)