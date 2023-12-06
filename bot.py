from flask import Flask, request
import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import urllib3
import pandas as pd
import re
import time
import base64
from io import BytesIO

# Setup
proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(
        proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30
    ),
}
telepot.api._onetime_pool_spec = (
    urllib3.ProxyManager,
    dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30)
)

secret = "123"
bot_token = '6862571743:AAF49GijrkW6hy0w3ktX6kaA5LNGgqUD4Lg'
bot = telepot.Bot(bot_token)
bot.setWebhook("https://badeelbot.pythonanywhere.com/{}".format(secret), max_connections=1)

csv_file = '/home/badeelbot/badeelbot_sheet2211.csv'
df = pd.read_csv(csv_file)

app = Flask(__name__)

# Main menu's categories
food_button = "طعام"
clean_button = "منطفات و عناية منزلية"
baby_button = "مستلزمات الأطفال"
personal_button = "العناية الشخصية"
makeup_button = "العناية بالبشرة"
drug_button = "أدوية"

# Food menu's categories
buttonf1 = "مواد تموينية و معلبات"
buttonf2 = "الأرز و المعكرونة"
buttonf3 = "الزيوت و السمنة"
buttonf4 = "سلطات"
buttonf5 = "الألبان و الأجبان"
buttonf6 = "مجمدات"
buttonf7 = "البوظة و المثلجات"
buttonf8 = "الشكولاتة و السكاكر"
buttonf9 = "المشروبات الباردة"
buttonf10 = "القهوة و الشاي"
buttonf11 = "صحي و حبوب إفطار"

# Cleaning menu's categories
buttonc1 = "مسحوق غسيل"
buttonc2 = "معطر غسيل"
buttonc3 = "سائل جلي"
buttonc4 = "صابون سائل"
buttonc5 = "ملمع زجاج"
buttonc6 = "سائل تنظيف الأرض"
buttonc7 = "أقراص جلاية"
buttonc8 = "كلور"
buttonc9 = "فاتح مجاري"
buttonc10 = "ليف جلي"
buttonc11 = "ملح الجلاية"

#Baby menu's categories
buttonb1 = "حليب أطفال"
buttonb2 = "حفاضات أطفال"

#Personal menu's categories
buttonp1 = "العناية بالأسنان"
buttonp2 = "العناية بالجسم و الشعر"
buttonp3 = "فوط نسائية"

#Dental care menu's categories
dental_care1 = "معجون أسنان"
dental_care2 = "فرشاة أسنان"

#Body care menu's categories
body_care1 = "شامبو شعر"
body_care2 = "بلسم شعر"
body_care3 = "مزبلات عرق"

#Feminine pads meuns' categories
feminine_pads1 = "فوط نسائية"
feminine_pads2 = "فوط نسائية يومية"

#Makup menu's categories
buttonm1 = "غسول بشرة"
buttonm2 = "تونر"
buttonm3 = "واقي شمس"
buttonm4 = "كريم عيون"
buttonm5 = "مرطب وجه"
buttonm6 = "كريمات التصبغات"
buttonm7 = "مستحضرات التجميل"

def main_menu(chat_id):
    """
    Send main menu to user.
    """
    main_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=food_button, callback_data="food_menu")],
        [InlineKeyboardButton(text=clean_button,callback_data="clean_menu")],
        [InlineKeyboardButton(text=baby_button, callback_data="baby_menu")],
        [InlineKeyboardButton(text=personal_button, callback_data="personal_menu")],
        [InlineKeyboardButton(text=makeup_button, callback_data="makeup_menu")],
        [InlineKeyboardButton(text=drug_button, callback_data="drug_button")]
    ])
    bot.sendMessage(chat_id, "يرجى أختيار الصنف", reply_markup=main_menu_keyboard)

def food_menu(chat_id):
    """
    Send food menu to user.
    """
    food_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=buttonf1, callback_data="press")],
        [InlineKeyboardButton(text=buttonf2, callback_data="press")],
        [InlineKeyboardButton(text=buttonf3, callback_data="press")],
        [InlineKeyboardButton(text=buttonf4, callback_data="press")],
        [InlineKeyboardButton(text=buttonf5, callback_data="press")],
        [InlineKeyboardButton(text=buttonf6, callback_data="press")],
        [InlineKeyboardButton(text=buttonf7, callback_data="press")],
        [InlineKeyboardButton(text=buttonf8, callback_data="press")],
        [InlineKeyboardButton(text=buttonf9, callback_data="press")],
        [InlineKeyboardButton(text=buttonf10, callback_data="press")],
        [InlineKeyboardButton(text=buttonf11, callback_data="press")]
    ])
    bot.sendMessage(chat_id, "يرجى اختيار الصنف من قائمة الطعام", reply_markup=food_menu_keyboard)

def clean_menu(chat_id):
    """
    send clean menu to user
    """
    clean_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=buttonc1,callback_data="press")],
        [InlineKeyboardButton(text=buttonc2,callback_data="press")],
        [InlineKeyboardButton(text=buttonc3,callback_data="press")],
        [InlineKeyboardButton(text=buttonc4,callback_data="press")],
        [InlineKeyboardButton(text=buttonc5,callback_data="press")],
        [InlineKeyboardButton(text=buttonc6,callback_data="press")],
        [InlineKeyboardButton(text=buttonc7,callback_data="press")],
        [InlineKeyboardButton(text=buttonc8,callback_data="press")],
        [InlineKeyboardButton(text=buttonc9,callback_data="press")],
        [InlineKeyboardButton(text=buttonc10,callback_data="press")],
        [InlineKeyboardButton(text=buttonc11,callback_data="press")]
    ])
    bot.sendMessage(chat_id, "يرجى اختيار الصنف من قائمة المنظفات و العناية المنزلية", reply_markup=clean_menu_keyboard)

def baby_menu(chat_id):
    """
    send baby menu to user
    """
    baby_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=buttonb1,callback_data="press")],
        [InlineKeyboardButton(text=buttonb2,callback_data="press")]
    ])
    bot.sendMessage(chat_id,"يرجى اختيار الصنف من قائمة مستلزمات الأطفال",reply_markup=baby_menu_keyboard)

def personal_menu(chat_id):
    """
    send personal menu to user
    """
    personal_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=buttonp1,callback_data="dental_care_menu")],
        [InlineKeyboardButton(text=buttonp2,callback_data="body_care_menu")],
        [InlineKeyboardButton(text=buttonp3,callback_data="feminine_pads_menu")]
    ])
    bot.sendMessage(chat_id,"يرجى اختيار الصنف من قائمة العناية الشخصية",reply_markup=personal_menu_keyboard)

def dental_care_menu(chat_id):
    """
    send dental care menu to user
    """
    dental_care_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=dental_care1,callback_data="press")],
        [InlineKeyboardButton(text=dental_care2,callback_data="press")]
    ])
    bot.sendMessage(chat_id,"يرجى اختيار الصنف من قائمة العناية بالأسنان",reply_markup=dental_care_menu_keyboard)

def body_care_menu(chat_id):
    """
    send body care menu to user
    """
    body_care_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=body_care1,callback_data="press")],
        [InlineKeyboardButton(text=body_care2,callback_data="press")],
        [InlineKeyboardButton(text=body_care3,callback_data="press")]
    ])
    bot.sendMessage(chat_id,"يرجى اختيار الصنف من قائمة العناية بالجسم و الشعر",reply_markup=body_care_menu_keyboard)

def feminine_pads_menu(chat_id):
    """
    send feminine pads menu to user
    """
    feminine_pads_menu_keyboard = InlineKeyboardMarkup(inline_keyboard = [
        [InlineKeyboardButton(text=feminine_pads1,callback_data="press")],
        [InlineKeyboardButton(text=feminine_pads2,callback_data="press")]
    ])
    bot.sendMessage(chat_id,"يرجى اختيار الصنف من قائمة الفوط الصحية ",reply_markup=feminine_pads_menu_keyboard)

def makeup_menu(chat_id):
    """
    send makup mneu to user
    """
    makeup_menu_keyboard = InlineKeyboardMarkup(inline_keyboard = [
        [InlineKeyboardButton(text=buttonm1,callback_data="press")],
        [InlineKeyboardButton(text=buttonm2,callback_data="press")],
        [InlineKeyboardButton(text=buttonm3,callback_data="press")],
        [InlineKeyboardButton(text=buttonm4,callback_data="press")],
        [InlineKeyboardButton(text=buttonm5,callback_data="press")],
        [InlineKeyboardButton(text=buttonm6,callback_data="press")],
        [InlineKeyboardButton(text=buttonm7,callback_data="press")]
    ])
    bot.sendMessage(chat_id,"يرجى اختيار الصنف من قائمة العناية بالبسرة",reply_markup=makeup_menu_keyboard)

def safe_send_message(chat_id, message):
    """
    Send message safely with error handling.
    """
    try:
        bot.sendMessage(chat_id, message)
    except telepot.exception.TooManyRequestsError as e:
        retry_after = e.json['parameters']['retry_after']
        time.sleep(retry_after)
        bot.sendMessage(chat_id, message)

def safe_send_photo(chat_id, photo_url):
    """
    Send photo safely with error handling.
    """
    try:
        bot.sendPhoto(chat_id, photo_url)
    except telepot.exception.TooManyRequestsError as e:
        retry_after = e.json['parameters']['retry_after']
        time.sleep(retry_after)
        bot.sendPhoto(chat_id, photo_url)

@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    """
    Handle incoming updates from Telegram.
    """
    update = request.get_json()

    if 'callback_query' in update:
        query_id = update['callback_query']['id']
        chat_id = update['callback_query']['message']['chat']['id']
        query_data = update['callback_query']['data']

        if query_data == 'food_menu':
            food_menu(chat_id)
            bot.answerCallbackQuery(query_id)
            return "OK"
        if query_data == 'clean_menu':
            clean_menu(chat_id)
            bot.answerCallbackQuery(query_id)
            return "OK"
        if query_data == 'baby_menu':
            baby_menu(chat_id)
            bot.answerCallbackQuery(query_id)
            return "OK"
        if query_data == 'personal_menu':
            personal_menu(chat_id)
            bot.answerCallbackQuery(query_id)
            return "OK"
        if query_data == 'dental_care_menu':
            dental_care_menu(chat_id)
            bot.answerCallbackQuery(query_id)
            return"OK"
        if query_data == 'body_care_menu':
            body_care_menu(chat_id)
            bot.answerCallbackQuery(query_id)
            return"OK"
        if query_data == 'feminine_pads_menu':
            feminine_pads_menu(chat_id)
            bot.answerCallbackQuery(query_id)
            return"OK"
        if query_data == 'makeup_menu':
            makeup_menu(chat_id)
            bot.answerCallbackQuery(query_id)
            return"OK"

    elif 'message' in update and 'text' in update['message']:
        chat_id = update["message"]["chat"]["id"]
        text = update['message']['text']
        if text == '/start':
            main_menu(chat_id)
            return "OK"

    # Handle other types of messages and callback queries
    # ...

    return "OK"

if __name__ == "__main__":
    app.run(debug=True)
