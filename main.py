import telebot
from telebot import *
from dbase import *
from telebot.types import *
import requests

bot = telebot.TeleBot("bot-token-here")
path = 'US.db'
conn = sqlite3.connect(path, check_same_thread=False)
c = conn.cursor()

token = "yourtokenfrom5sim.net"
bot_name = "yourbotname"
bot_username = "yourbotusername"
channel = "yourchannel"
poof_id = "yourapitokenfrompoof.io"


@bot.message_handler(commands=['start'])
def start(message):
    userid = message.from_user.id
    name = message.from_user.first_name
    if not check_user(userid):
        create_user_two(userid)
        print(f"created user - {userid}")
    balance = int(fetch_balance(userid))
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(InlineKeyboardButton("💰 Top Up", callback_data="top_up"))
    markup.add(InlineKeyboardButton("📞 Buy Number", callback_data="buy_number"))
    markup.add(InlineKeyboardButton("📑 Purchase History", callback_data="history"))
    markup.add(InlineKeyboardButton("📩 Channel", url=f"t.me/{channel_name}"))
    if check_admin(userid):
        markup.add(InlineKeyboardButton("🤖 ADMIN PANEL", callback_data="admin_panel"))
        bot.send_message(message.chat.id, "You are an admin", reply_markup=markup)
    bot.send_message(message.chat.id, f"*📮 Welcome to {bot_name} Bot, {name}.\n\n📧 Your ID: {userid}\n💳 Your Balance: ${balance}\n\n💡 Purchase Virtual Numbers for Receiving SMS Codes on Any Platform\n\nPlease choose an option:*", reply_markup=markup, parse_mode="MARKDOWN")


@bot.callback_query_handler(lambda call: call.data == 'home')
def home(call):
    userid = call.from_user.id
    name = call.from_user.first_name
    chat_id = call.message.chat.id
    balance = int(fetch_balance(userid))
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(InlineKeyboardButton("💰 Top Up", callback_data="top_up"))
    markup.add(InlineKeyboardButton("📞 Buy Number", callback_data="buy_number"))
    markup.add(InlineKeyboardButton("📑 Purchase History", callback_data="history"))
    markup.add(InlineKeyboardButton("📩 Channel", url=f"t.me/{channel}"))
    if check_admin(userid):
        markup.add(InlineKeyboardButton("🤖 ADMIN PANEL", callback_data="admin_panel"))
        bot.send_message(chat_id, "You are an admin", reply_markup=markup)
    bot.send_message(chat_id, f"*📮 Welcome to {bot_name}, {name}.\n\n📧 Your ID: {userid}\n💳 Your Balance: ${balance}\n\n💡 Purchase Virtual Numbers for Receiving SMS Codes on Any Platform\n\nPlease choose an option:*", reply_markup=markup, parse_mode="MARKDOWN")


@bot.callback_query_handler(lambda call: call.data == 'admin_panel')
def admin_panel(call):
    userid = call.from_user.id
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(InlineKeyboardButton("Add Balance", callback_data="give_balance"))
    markup.add(InlineKeyboardButton("Subtract Balance", callback_data="subtract_balance"))
    markup.add(InlineKeyboardButton("Add Admin", callback_data="add_admin"))
    markup.add(InlineKeyboardButton("Remove Admin", callback_data="remove_admin"))
    markup.add(InlineKeyboardButton("Home", callback_data="home"))
    bot.send_message(call.message.chat.id, "*🛠 Admin Panel:*", parse_mode="MARKDOWN", reply_markup=markup)


@bot.callback_query_handler(lambda call: call.data == 'give_balance')
def give_balance(call):
    msg = bot.send_message(call.message.chat.id, "Enter the User ID and the amount to add (Format: user_id amount):")
    bot.register_next_step_handler(msg, process_give_balance)

def process_give_balance(message):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(InlineKeyboardButton("Home", callback_data="home"))
    markup.add(InlineKeyboardButton("🤖 ADMIN PANEL", callback_data="admin_panel"))
    try:
        user_id, amount = map(int, message.text.split())
        current_balance = int(fetch_balance(user_id))
        new_balance = current_balance + amount
        save_balance(new_balance, user_id)
        bot.send_message(message.chat.id, f"✅ Successfully added {amount} to user {user_id}. New balance: {new_balance}", reply_markup=markup)
    except:
        bot.send_message(message.chat.id, "❌ Invalid input. Please use the format: user_id amount.", reply_markup=markup)


@bot.callback_query_handler(lambda call: call.data == 'subtract_balance')
def subtract_balance(call):
    msg = bot.send_message(call.message.chat.id, "Enter the User ID and the amount to subtract (Format: user_id amount):")
    bot.register_next_step_handler(msg, process_subtract_balance)

def process_subtract_balance(message):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(InlineKeyboardButton("Home", callback_data="home"))
    markup.add(InlineKeyboardButton("🤖 ADMIN PANEL", callback_data="admin_panel"))
    try:
        user_id, amount = map(int, message.text.split())
        current_balance = int(fetch_balance(user_id))
        new_balance = current_balance - amount
        if new_balance < 0:
            new_balance = 0
        save_balance(new_balance, user_id)
        bot.send_message(message.chat.id, f"✅ Successfully subtracted {amount} from user {user_id}. New balance: {new_balance}", reply_markup=markup)
    except:
        bot.send_message(message.chat.id, "❌ Invalid input. Please use the format: user_id amount.", reply_markup=markup)


@bot.callback_query_handler(lambda call: call.data == 'add_admin')
def add_admin(call):
    msg = bot.send_message(call.message.chat.id, "Enter the User ID to make admin:")
    bot.register_next_step_handler(msg, process_add_admin)

def process_add_admin(message):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(InlineKeyboardButton("Home", callback_data="home"))
    markup.add(InlineKeyboardButton("🤖 ADMIN PANEL", callback_data="admin_panel"))
    try:
        user_id = int(message.text)
        create_admin(user_id)
        bot.send_message(message.chat.id, f"✅ User {user_id} is now an admin.", reply_markup=markup)
    except:
        bot.send_message(message.chat.id, "❌ Failed to add admin. Please enter a valid user ID.", reply_markup=markup)


@bot.callback_query_handler(lambda call: call.data == 'remove_admin')
def remove_admin(call):
    msg = bot.send_message(call.message.chat.id, "Enter the Admin ID to remove:")
    bot.register_next_step_handler(msg, process_remove_admin)

def process_remove_admin(message):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(InlineKeyboardButton("Home", callback_data="home"))
    markup.add(InlineKeyboardButton("🤖 ADMIN PANEL", callback_data="admin_panel"))
    try:
        admin_id = int(message.text)
        delete_specific_AdminData(admin_id)
        bot.send_message(message.chat.id, f"✅ Admin {admin_id} has been removed.", reply_markup=markup)
    except:
        bot.send_message(message.chat.id, "❌ Failed to remove admin. Please enter a valid admin ID.", reply_markup=markup)


@bot.callback_query_handler(lambda call: call.data == 'top_up')
def top_up(call):
    chat_id = call.message.chat.id
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(InlineKeyboardButton("BTC", callback_data="btc"))
    markup.add(InlineKeyboardButton("LTC", callback_data="ltc"))
    markup.add(InlineKeyboardButton("ETH", callback_data="eth"))
    markup.add(InlineKeyboardButton("SOL", callback_data="sol"))
    markup.add(InlineKeyboardButton("Home", callback_data="home"))
    bot.send_message(chat_id, "*📞 Choose your payment method:*", parse_mode="MARKDOWN", reply_markup=markup)


@bot.callback_query_handler(lambda call: call.data == 'btc')
def btc(call):
    chat_id = call.message.chat.id
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(InlineKeyboardButton("$10", callback_data="b1"))
    markup.add(InlineKeyboardButton("$20", callback_data="b2"))
    markup.add(InlineKeyboardButton("$50", callback_data="b5"))
    markup.add(InlineKeyboardButton("$100", callback_data="b100"))
    markup.add(InlineKeyboardButton("Home", callback_data="home"))
    bot.send_message(chat_id, "*📞 Choose your amount to top up:*", parse_mode="MARKDOWN", reply_markup=markup)


@bot.callback_query_handler(lambda call: call.data == 'ltc')
def ltc(call):
    chat_id = call.message.chat.id
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(InlineKeyboardButton("$10", callback_data="l1"))
    markup.add(InlineKeyboardButton("$20", callback_data="l2"))
    markup.add(InlineKeyboardButton("$50", callback_data="l5"))
    markup.add(InlineKeyboardButton("$100", callback_data="l100"))
    markup.add(InlineKeyboardButton("Home", callback_data="home"))
    bot.send_message(chat_id, "*📞 Choose your amount to top up:*", parse_mode="MARKDOWN", reply_markup=markup)


@bot.callback_query_handler(lambda call: call.data == 'eth')
def eth(call):
    chat_id = call.message.chat.id
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(InlineKeyboardButton("$10", callback_data="e1"))
    markup.add(InlineKeyboardButton("$20", callback_data="e2"))
    markup.add(InlineKeyboardButton("$50", callback_data="e5"))
    markup.add(InlineKeyboardButton("$100", callback_data="e100"))
    markup.add(InlineKeyboardButton("Home", callback_data="home"))
    bot.send_message(chat_id, "*📞 Choose your amount to top up:*", parse_mode="MARKDOWN", reply_markup=markup)


@bot.callback_query_handler(lambda call: call.data == 'sol')
def sol(call):
    chat_id = call.message.chat.id
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(InlineKeyboardButton("$10", callback_data="s1"))
    markup.add(InlineKeyboardButton("$20", callback_data="s2"))
    markup.add(InlineKeyboardButton("$50", callback_data="s5"))
    markup.add(InlineKeyboardButton("$100", callback_data="s100"))
    markup.add(InlineKeyboardButton("Home", callback_data="home"))
    bot.send_message(chat_id, "*📞 Choose your amount to top up:*", parse_mode="MARKDOWN", reply_markup=markup)


def handle_payment(call, amount, crypto):
    chat_id = call.message.chat.id
    try:
        bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)
    except telebot.apihelper.ApiTelegramException:
        pass
    except requests.exceptions.ConnectionError:
        bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)
    userid = call.from_user.id
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("✅ CHECK PAYMENT", callback_data="check_payment"))
    markup.add(InlineKeyboardButton("SUPPORT", url=f"t.me/{bot_username}"))
    json_data = {
        "amount": amount,
        "crypto": crypto,
        "currency": "USD",
        "redirect": f"https://t.me/{bot_username}/{userid}"
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"{poof_id}"
    }
    r = requests.post("https://www.poof.io/api/v2/create_invoice", json=json_data, headers=headers)
    jsonResponse = r.json()
    print(jsonResponse)
    payment_link = jsonResponse["payment_link"]
    charge = jsonResponse["charge"]
    address = jsonResponse["address"]
    rate = jsonResponse["rate"]
    var2 = payment_link.split('/')[-1]
    save_option2(userid, var2)
    for key, value in jsonResponse.items():
        print(key, ":", value)
    try:
        invoice = (
            f"📦 *REBEL CODES BOT*\n\n📂 Invoice ID - {userid}\n\n"
            f"💎 TX ID: {var2}\n\n🔑 Address:\n\n`{address}`\n\n"
            f"💵 Amount: `{amount} USD worth of {crypto}`\n"
            f"💸 Charge: `{charge}`\n🔗 Payment Link: [Click Here]({payment_link})\n"
            f"💱 Rate: `{rate} USD`"
        )
        url1 = f"https://www.bitcoinqrcodemaker.com/api/?style={crypto}&amount={charge}&color=1&border=1&address={address}"
        response1 = requests.get(url1)
        if response1.status_code == 200:
            with open("bitcoin_qr_code.png", "wb") as f:
                f.write(response1.content)
            with open('bitcoin_qr_code.png', 'rb') as f:
                bot.send_photo(call.message.chat.id, photo=f, caption=invoice, parse_mode="markdown",
                               reply_markup=markup)
    except telebot.apihelper.ApiTelegramException:
        pass


@bot.callback_query_handler(lambda call: call.data == 'b1')
def b1(call):
    handle_payment(call, amount='10', crypto='bitcoin')


@bot.callback_query_handler(lambda call: call.data == 'b2')
def b2(call):
    handle_payment(call, amount='20', crypto='bitcoin')


@bot.callback_query_handler(lambda call: call.data == 'b5')
def b3(call):
    handle_payment(call, amount='50', crypto='bitcoin')


@bot.callback_query_handler(lambda call: call.data == 'b100')
def b3(call):
    handle_payment(call, amount='100', crypto='bitcoin')


@bot.callback_query_handler(lambda call: call.data == 'l1')
def l1(call):
    handle_payment(call, amount='10', crypto='litecoin')


@bot.callback_query_handler(lambda call: call.data == 'l2')
def l2(call):
    handle_payment(call, amount='20', crypto='litecoin')


@bot.callback_query_handler(lambda call: call.data == 'l5')
def l3(call):
    handle_payment(call, amount='50', crypto='litecoin')


@bot.callback_query_handler(lambda call: call.data == 'l100')
def l3(call):
    handle_payment(call, amount='100', crypto='litecoin')


@bot.callback_query_handler(lambda call: call.data == 'e1')
def e1(call):
    handle_payment(call, amount='10', crypto='ethereum')


@bot.callback_query_handler(lambda call: call.data == 'e2')
def e2(call):
    handle_payment(call, amount='20', crypto='ethereum')


@bot.callback_query_handler(lambda call: call.data == 'e5')
def e3(call):
    handle_payment(call, amount='50', crypto='ethereum')


@bot.callback_query_handler(lambda call: call.data == 'e100')
def e3(call):
    handle_payment(call, amount='100', crypto='ethereum')


@bot.callback_query_handler(lambda call: call.data == 's1')
def s1(call):
    handle_payment(call, amount='10', crypto='solana')


@bot.callback_query_handler(lambda call: call.data == 's2')
def s2(call):
    handle_payment(call, amount='20', crypto='solana')


@bot.callback_query_handler(lambda call: call.data == 's5')
def s3(call):
    handle_payment(call, amount='50', crypto='solana')


@bot.callback_query_handler(lambda call: call.data == 's100')
def s3(call):
    handle_payment(call, amount='100', crypto='solana')


@bot.callback_query_handler(lambda call: call.data == 'check_payment')
def check_pay(call):
    user = call.from_user.username
    userid = str(call.from_user.id)
    balance = fetch_balance(userid)
    transid = fetch_option2(userid)
    url = "https://www.poof.io/api/v1/transaction"
    payload = {'transaction': transid}
    headers = {
        "Authorization": f"{poof_id}",
        "content-type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    json_data = response.json()
    paid = json_data.get('paid', '')
    amount = json_data.get('amount', '')
    if paid == 'yes':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=f"* \n\n👤 @{user} - {userid}\n\n📇 Transaction ID: {transid}"
                                   f"\n\n💸 Paid: {paid}\n\n💸 Amount: {amount}"
                                   f"\n\n✅ INVOICE PAID SUCCESSFULLY.\n\nPress /start*",
                              parse_mode="MARKDOWN")
        new_balance = balance + amount
        save_balance(new_balance, userid)
        bot.send_message(call.message.chat.id, f"${amount} in balance added. Press /start to refresh.", parse_mode="MARKDOWN")
    elif paid == 'processing' or paid == 'no':
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("✅ CHECK PAYMENT", callback_data="check_payment"))
        text = f"💰 Payment Details\n\n"
        text += f"👤 User: @{user} - {userid}\n"
        text += f"📇 Transaction ID: {transid}\n"
        text += f"💸 Paid: *{paid}*\n"
        text += f"💸 Amount: *{amount}*\n\n"
        if paid == 'processing':
            text += "✅ Payment Detected 🎉\n\n"
            text += "Please wait until all confirmations have been reached.\n\n"
            text += "If you have paid and this message pops up, use /ipaid"
        else:
            text += "🛑 Payment Error ❌\n\n"
            text += "❌ Invoice has not been paid. " \
                    "Please make payment or wait until confirmations have been reached.\n\n"
            text += "If you have paid and this message pops up, use /ipaid"
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text,
                                  parse_mode="MARKDOWN", reply_markup=markup)
        except telebot.apihelper.ApiTelegramException:
            bot.send_message(call.message.chat.id, text=text, parse_mode="MARKDOWN", reply_markup=markup)


@bot.callback_query_handler(lambda call: call.data == 'buy_number')
def buy_number(call):
    userid = call.from_user.id
    print(call.data)
    balance = int(fetch_balance(userid))
    if balance <= 1:
        markup = InlineKeyboardMarkup(row_width=2)
        markup.add(InlineKeyboardButton("💰 Top Up", callback_data="top_up"))
        markup.add(InlineKeyboardButton("Home", callback_data="home"))
        bot.send_message(userid, "*You must have at least $1 to start purchasing. Please make a deposit.*", parse_mode="MARKDOWN", reply_markup=markup)
    else:
        markup = InlineKeyboardMarkup(row_width=2)
        markup.add(InlineKeyboardButton("AirBNB", callback_data="airbnb"), InlineKeyboardButton("AliExpress", callback_data="aliexpress"))
        markup.add(InlineKeyboardButton("Amazon", callback_data="amazon"), InlineKeyboardButton("Discord", callback_data="discord"))
        markup.add(InlineKeyboardButton("eBay", callback_data="ebay"), InlineKeyboardButton("FaceBook", callback_data="facebook"))
        markup.add(InlineKeyboardButton("FeetFinder", callback_data="feetfinder"), InlineKeyboardButton("Fiverr", callback_data="fiverr"))
        markup.add(InlineKeyboardButton("Flip", callback_data="flip"), InlineKeyboardButton("Google Voice", callback_data="googlevoice"))
        markup.add(InlineKeyboardButton("Grindr", callback_data="grindr"), InlineKeyboardButton("Instagram", callback_data="instagram"))
        markup.add(InlineKeyboardButton("Lyft", callback_data="lyft"), InlineKeyboardButton("Netflix", callback_data="netflix"))
        markup.add(InlineKeyboardButton("PayPal", callback_data="paypal"), InlineKeyboardButton("Snapchat", callback_data="snapchat"))
        markup.add(InlineKeyboardButton("Telegram", callback_data="telegram"), InlineKeyboardButton("Temu", callback_data="temu"))
        markup.add(InlineKeyboardButton("TikTok", callback_data="tiktok"), InlineKeyboardButton("Uber", callback_data="uber"))
        markup.add(InlineKeyboardButton("Venmo", callback_data="venmo"), InlineKeyboardButton("Whatsapp", callback_data="whatsapp"))
        bot.send_message(userid, "*📺 Each SMS code is $1.\n\n👉 Please choose an option:*", parse_mode="MARKDOWN", reply_markup=markup)


@bot.callback_query_handler(lambda call: call.data == 'airbnb' or call.data == 'amazon' or call.data == 'ebay' or call.data == 'feetfinder' or call.data == 'flip' or call.data == 'grindr' or call.data == 'lyft' or call.data == 'paypal')
def purchase_fr(call):
    userid = call.from_user.id
    print(call.data)
    option = call.data
    save_option4(option, userid)
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(InlineKeyboardButton("✅ YES", callback_data="complete"),
               InlineKeyboardButton("❌ NO", callback_data="home"))
    bot.send_message(userid, f"*📺 Are you sure you want to purchase {option} SMS code for $1?*", parse_mode="MARKDOWN",
                     reply_markup=markup)


@bot.callback_query_handler(lambda call: call.data == 'aliexpress' or call.data == 'discord' or call.data == 'discord' or call.data == 'fiverr' or call.data == 'telegram' or call.data == 'tiktok' or call.data == 'venmo')
def purchase_fr(call):
    userid = call.from_user.id
    print(call.data)
    option = call.data
    save_option4(option, userid)
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(InlineKeyboardButton("✅ YES", callback_data="complete"),
               InlineKeyboardButton("❌ NO", callback_data="home"))
    bot.send_message(userid, f"*📺 Are you sure you want to purchase {option} SMS code for $1?*", parse_mode="MARKDOWN",
                     reply_markup=markup)


@bot.callback_query_handler(lambda call: call.data == 'googlevoice' or call.data == 'instagram' or call.data == 'netflix' or call.data == 'snapchat' or call.data == 'temu' or call.data == 'uber' or call.data == 'whatsapp')
def purchase_fr(call):
    userid = call.from_user.id
    print(call.data)
    option = call.data
    save_option4(option, userid)
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(InlineKeyboardButton("✅ YES", callback_data="complete"),
               InlineKeyboardButton("❌ NO", callback_data="home"))
    bot.send_message(userid, f"*📺 Are you sure you want to purchase {option} SMS code for $1?*", parse_mode="MARKDOWN",
                     reply_markup=markup)


@bot.callback_query_handler(lambda call: call.data == 'complete')
def complete_purchase(call):
    userid = call.from_user.id
    print(call.data)
    option = fetch_option4(userid)
    balance = int(fetch_balance(userid))
    new_balance = balance - 1
    save_balance(new_balance, userid)
    country = 'usa'
    operator = 'any'
    product = option
    headers = {
        'Authorization': 'Bearer ' + token,
        'Accept': 'application/json',
    }
    response = requests.get('https://5sim.net/v1/user/buy/activation/' + country + '/' + operator + '/' + product, headers=headers)

    print(json.dumps(response.json(), indent=4, sort_keys=True))
    json_data = response.json()
    transid = json_data.get('id', '')
    phone = json_data.get('phone', '')
    save_option3(transid, userid)
    save_phonenumber(phone, userid)
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(InlineKeyboardButton("✅ Get Code", callback_data="getcode"))
    bot.send_message(userid, f"*📣 Your phone number is: {phone}.\n\n🔔 Please click 'Get Code' below, after you have sent the SMS code.\n\n⛔ This number will only be valid for 15 minutes.*", parse_mode="MARKDOWN", reply_markup=markup)


@bot.callback_query_handler(lambda call: call.data == 'getcode')
def getcode(call):
    userid = call.from_user.id
    print(call.data)
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(InlineKeyboardButton("✅ Get Code", callback_data="getcode"))
    transid = fetch_option3(userid)
    headers = {
        'Authorization': 'Bearer ' + token,
        'Accept': 'application/json',
    }
    response = requests.get('https://5sim.net/v1/user/check/' + transid, headers=headers)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    if response.status_code == 200:
        json_data = response.json()
        print(json.dumps(json_data, indent=4, sort_keys=True))
        sms_list = json_data.get('sms', [])
        phone = json_data.get('phone', '')
        if sms_list:
            code = sms_list[0].get('code', '')
            text = sms_list[4].get('text', '')
            print(f"Code: {code}")
            bot.send_message(call.message.chat.id, f"*Phone: {phone}\nCode: {code}\nText: {text}*", reply_markup=markup,
                             parse_mode="MARKDOWN")
        else:
            code = ''
            print("No SMS code found.")
            bot.send_message(call.message.chat.id, "*Failed to retrieve the code, because the code may not have been received. Please retry.*", reply_markup=markup, parse_mode="MARKDOWN")
    else:
        print(f"Failed to get data")
        bot.send_message(call.message.chat.id, "*Failed to retrieve the code, because the code may not have been received. Please retry.*", reply_markup=markup, parse_mode="MARKDOWN")


bot.polling()
