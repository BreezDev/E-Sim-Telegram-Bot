import sqlite3
from datetime import *
from threading import Lock

lock = Lock()

path = 'US001989.db'
conn = sqlite3.connect(path, check_same_thread=False)

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS UserData (
        id int AUTO_INCREMENT,
        balance int,
        user_id int,
        phone_no text,
        user_number text,
        expiry_date int,
        option1 text,
        option2 text,
        option3 text,
        option4 text,
        option_number text,
        script text,
        script1 text,
        script2 text,
        script3 text,
        script4 text,
        script5 text,
        script6 text,
        script7 text,
        script8 text,
        script9 text,
        script10 int,
        name1 text,
        name2 text,
        name3 text,
        name4 text,
        name5 text,
        name6 text,
        name7 text,
        name8 text,
        name9 text,
        name10 int,
        end1 text,
        end2 text,
        end3 text,
        is_premium text
    )""")

c.execute("""CREATE TABLE IF NOT EXISTS Admindata (
        id int AUTO_INCREMENT,
        admin_id int
   )""")


c.execute("""CREATE TABLE IF NOT EXISTS transactions (
        id int AUTO_INCREMENT,
        user_id int,
        transaction_id text
    )""")


def save_trans(transaction_id, userid):
    c.execute("INSERT INTO transactions (transaction_id, user_id) VALUES (?, ?)", (transaction_id, userid))
    conn.commit()
    print("Transaction saved successfully.")


def fetch_trans(transaction_id):
    c.execute("SELECT user_id FROM transactions WHERE transaction_id = ?", (transaction_id,))
    result = c.fetchone()
    if result:
        return result[0]
    else:
        return None


def create_user_two(userid):
    today = date.today()
    exp_day_test = today + timedelta(days=100)
    sql = f"Insert into UserData (user_id, balance, bank_name, banned, is_reseller, username, ip_address, language_name, voice_name, spoof_no, phone_no, user_number, otp_code, Recording_url, card_number, card_cvv, card_expiry, account_number, atm_pin, expiry_date, option1, option2, option3, option4, option_number, numbers_collected1, numbers_collected2, voice, dl_number, ssn_number, app_number, isrefer, referred, script, script1, script2, script3, script4, script5, script6, script7, script8, script9, script10, name1, name2, name3, name4, name5, name6, name7, name8, name9, name10, end1, end2, end3, is_premium) values ('{userid}', 0, 'Notavailable', 0, 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 0, 'Notavailable', 0, 0, 0, 0, 0, '{exp_day_test}', 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 'NO', 0, 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 'Notavailable', 0, 'Notavailable', 'Notavailable', 'Notavailable', 'NO')"
    c.execute(sql)
    conn.commit()


def save_balance(balance, user_id):
    c.execute("UPDATE UserData SET balance = ? WHERE user_id = ?",
              (balance, user_id))
    conn.commit()


def fetch_balance(user_id):
    c.execute(f"SELECT balance FROM UserData WHERE user_id = '{user_id}'")
    balance = str(c.fetchone()[0])
    conn.commit()
    return balance


def save_expire(expire, userid):
    c.execute("UPDATE UserData SET expiry_date = ? WHERE user_id = ?", (expire, userid))
    conn.commit()


def save_phonenumber(phone_no2, userid):
    c.execute("UPDATE UserData SET phone_no = ? WHERE user_id = ?", (phone_no2, userid))
    # c.execute("INSERT INTO UserData VALUES (?)", (phone_no,))
    conn.commit()



def save_username(usern, userid):
    c.execute("UPDATE UserData SET username = ? WHERE user_id = ?", (str(usern), userid))
    conn.commit()



def save_option1(option1option, userid):
    c.execute("UPDATE UserData SET option1 = ? WHERE user_id = ?", (option1option, userid))
    conn.commit()


def save_option2(option2option, userid):
    c.execute("UPDATE UserData SET option2 = ? WHERE user_id = ?", (option2option, userid))
    conn.commit()


def save_option3(option3option, userid):
    c.execute("UPDATE UserData SET option3 = ? WHERE user_id = ?", (option3option, userid))
    conn.commit()


def save_option4(option4option, userid):
    c.execute("UPDATE UserData SET option4 = ? WHERE user_id = ?", (option4option, userid))
    conn.commit()


def save_script(script, userid):
    c.execute("UPDATE UserData SET script = ? WHERE user_id = ?", (script, userid))
    conn.commit()


def save_script1(script1, userid):
    c.execute("UPDATE UserData SET script1 = ? WHERE user_id = ?", (script1, userid))
    conn.commit()


def save_script2(script2, userid):
    c.execute("UPDATE UserData SET script2 = ? WHERE user_id = ?", (script2, userid))
    conn.commit()


def save_script3(script3, userid):
    c.execute("UPDATE UserData SET script3 = ? WHERE user_id = ?", (script3, userid))
    conn.commit()


def save_script4(script4, userid):
    c.execute("UPDATE UserData SET script4 = ? WHERE user_id = ?", (script4, userid))
    conn.commit()


def save_script5(script5, userid):
    c.execute("UPDATE UserData SET script5 = ? WHERE user_id = ?", (script5, userid))
    conn.commit()


def save_script6(script6, userid):
    c.execute("UPDATE UserData SET script6 = ? WHERE user_id = ?", (script6, userid))
    conn.commit()


def save_script7(script7, userid):
    c.execute("UPDATE UserData SET script7 = ? WHERE user_id = ?", (script7, userid))
    conn.commit()


def save_script8(script8, userid):
    c.execute("UPDATE UserData SET script8 = ? WHERE user_id = ?", (script8, userid))
    conn.commit()


def save_script9(script9, userid):
    c.execute("UPDATE UserData SET script9 = ? WHERE user_id = ?", (script9, userid))
    conn.commit()


def save_script10(script10, userid):
    c.execute("UPDATE UserData SET script10 = ? WHERE user_id = ?", (script10, userid))
    conn.commit()


def save_name1(name1, userid):
    c.execute("UPDATE UserData SET name1 = ? WHERE user_id = ?", (name1, userid))
    conn.commit()


def save_name2(name2, userid):
    c.execute("UPDATE UserData SET name2 = ? WHERE user_id = ?", (name2, userid))
    conn.commit()


def save_name3(name3, userid):
    c.execute("UPDATE UserData SET name3 = ? WHERE user_id = ?", (name3, userid))
    conn.commit()


def save_name4(name4, userid):
    c.execute("UPDATE UserData SET name4 = ? WHERE user_id = ?", (name4, userid))
    conn.commit()


def save_name5(name5, userid):
    c.execute("UPDATE UserData SET name5 = ? WHERE user_id = ?", (name5, userid))
    conn.commit()


def save_name6(name6, userid):
    c.execute("UPDATE UserData SET name6 = ? WHERE user_id = ?", (name6, userid))
    conn.commit()


def save_name7(name7, userid):
    c.execute("UPDATE UserData SET name7 = ? WHERE user_id = ?", (name7, userid))
    conn.commit()


def save_name8(name8, userid):
    c.execute("UPDATE UserData SET name8 = ? WHERE user_id = ?", (name8, userid))
    conn.commit()


def save_name9(name9, userid):
    c.execute("UPDATE UserData SET name9 = ? WHERE user_id = ?", (name9, userid))
    conn.commit()


def save_name10(name10, userid):
    c.execute("UPDATE UserData SET name10 = ? WHERE user_id = ?", (name10, userid))
    conn.commit()


def save_end1(end1, userid):
    c.execute("UPDATE UserData SET end1 = ? WHERE user_id = ?", (end1, userid))
    conn.commit()


def save_end2(end2, userid):
    c.execute("UPDATE UserData SET end2 = ? WHERE user_id = ?", (end2, userid))
    conn.commit()


def save_end3(end3, userid):
    c.execute("UPDATE UserData SET end3 = ? WHERE user_id = ?", (end3, userid))
    conn.commit()


def save_is_premium(is_premium, userid):
    c.execute("UPDATE UserData SET is_premium = ? WHERE user_id = ?", (is_premium, userid))
    conn.commit()


def save_option_number(option_number, userid):
    c.execute("UPDATE UserData SET option_number = ? WHERE user_id = ?", (option_number, userid))
    conn.commit()




def fetch_phonenumber(userid):
    c.execute(f"SELECT phone_no FROM UserData WHERE user_id = '{userid}'")
    result = c.fetchone()
    if result is not None:
        phonenumber = str(result[0])
    else:
        phonenumber = None
    conn.commit()
    return phonenumber


def fetch_username(userid):
    c.execute(f"SELECT username FROM UserData WHERE user_id = '{userid}'")
    username = str(c.fetchone()[0])
    conn.commit()
    return username


def fetch_expiry_date(userid):
    try:
        c.execute(f"SELECT expiry_date FROM UserData WHERE user_id = '{userid}'")
        expiry_str = str(c.fetchone()[0])
        expiry_datetime = datetime.strptime(expiry_str, '%Y-%m-%d')
        expiry_date = expiry_datetime.date()
        conn.commit()
        return expiry_date
    except:
        return ''



def fetch_option1(userid):
    c.execute(f"SELECT option1 FROM UserData WHERE user_id = '{userid}'")
    try:
        option1 = str(c.fetchone()[0])
        conn.commit()
    except:
        return ''
    else:
        return option1


def fetch_option3(userid):
    c.execute(f"SELECT option3 FROM UserData WHERE user_id = '{userid}'")
    try:
        option3 = str(c.fetchone()[0])
        conn.commit()
    except:
        return ''
    else:
        return option3


def fetch_option2(userid):
    c.execute(f"SELECT option2 FROM UserData WHERE user_id = '{userid}'")
    try:
        option2 = str(c.fetchone()[0])
        conn.commit()
    except:
        return ''
    else:
        return option2


def fetch_option4(userid):
    c.execute(f"SELECT option4 FROM UserData WHERE user_id = '{userid}'")
    try:
        option4 = str(c.fetchone()[0])
        conn.commit()
    except:
        return ''
    else:
        return option4


def fetch_script(userid):
    c.execute(f"SELECT script FROM UserData WHERE user_id = '{userid}'")
    try:
        script = str(c.fetchone()[0])
        conn.commit()
    except:
        return 'Error fetching script'
    else:
        return script


def fetch_script1(userid):
    c.execute(f"SELECT script1 FROM UserData WHERE user_id = '{userid}'")
    try:
        script1 = str(c.fetchone()[0])
        conn.commit()
    except:
        return ''
    else:
        return script1


def fetch_script2(userid):
    c.execute(f"SELECT script2 FROM UserData WHERE user_id = '{userid}'")
    try:
        script2 = str(c.fetchone()[0])
        conn.commit()
    except:
        return ''
    else:
        return script2


def fetch_script3(userid):
    c.execute(f"SELECT script3 FROM UserData WHERE user_id = '{userid}'")
    try:
        script3 = str(c.fetchone()[0])
        conn.commit()
    except:
        return ''
    else:
        return script3


def fetch_script4(userid):
    c.execute(f"SELECT script4 FROM UserData WHERE user_id = ?", (userid,))
    try:
        script4 = str(c.fetchone()[0])
        conn.commit()
    except:
        return ''
    else:
        return script4


def fetch_script5(userid):
    c.execute(f"SELECT script5 FROM UserData WHERE user_id = '{userid}'")
    try:
        script5 = str(c.fetchone()[0])
        conn.commit()
    except:
        return ''
    else:
        return script5


def fetch_script6(userid):
    c.execute(f"SELECT script6 FROM UserData WHERE user_id = '{userid}'")
    try:
        script6 = str(c.fetchone()[0])
        conn.commit()
    except:
        return ''
    else:
        return script6


def fetch_script7(userid):
    c.execute(f"SELECT script7 FROM UserData WHERE user_id = '{userid}'")
    try:
        script7 = str(c.fetchone()[0])
        conn.commit()
    except:
        return ''
    else:
        return script7


def fetch_script8(userid):
    c.execute(f"SELECT script8 FROM UserData WHERE user_id = '{userid}'")
    try:
        script8 = str(c.fetchone()[0])
        conn.commit()
    except:
        return ''
    else:
        return script8


def fetch_script9(userid):
    c.execute(f"SELECT script9 FROM UserData WHERE user_id = '{userid}'")
    try:
        script9 = str(c.fetchone()[0])
        conn.commit()
    except:
        return ''
    else:
        return script9


def fetch_script10(userid):
    c.execute(f"SELECT script10 FROM UserData WHERE user_id = '{userid}'")
    try:
        script10 = str(c.fetchone()[0])
        conn.commit()
    except:
        return ''
    else:
        return script10


def fetch_name1(userid):
    c.execute(f"SELECT name1 FROM UserData WHERE user_id = '{userid}'")
    try:
        name1 = str(c.fetchone()[0])
        conn.commit()
    except:
        return ''
    else:
        return name1


def fetch_name2(userid):
    c.execute(f"SELECT name2 FROM UserData WHERE user_id = '{userid}'")
    try:
        name2 = str(c.fetchone()[0])
        conn.commit()
    except:
        return ''
    else:
        return name2


def fetch_name3(userid):
    c.execute(f"SELECT name3 FROM UserData WHERE user_id = '{userid}'")
    try:
        name3 = str(c.fetchone()[0])
        conn.commit()
    except:
        return ''
    else:
        return name3


def fetch_name4(userid):
    c.execute(f"SELECT name4 FROM UserData WHERE user_id = '{userid}'")
    try:
        name4 = str(c.fetchone()[0])
        conn.commit()
    except:
        return ''
    else:
        return name4


def fetch_name5(userid):
    c.execute(f"SELECT name5 FROM UserData WHERE user_id = '{userid}'")
    try:
        name5 = str(c.fetchone()[0])
        conn.commit()
    except:
        return ''
    else:
        return name5


def fetch_name6(userid):
    c.execute(f"SELECT name6 FROM UserData WHERE user_id = '{userid}'")
    try:
        name6 = str(c.fetchone()[0])
        conn.commit()
    except:
        return ''
    else:
        return name6


def fetch_name7(userid):
    c.execute(f"SELECT name7 FROM UserData WHERE user_id = '{userid}'")
    try:
        name7 = str(c.fetchone()[0])
        conn.commit()
    except:
        return ''
    else:
        return name7


def fetch_name8(userid):
    c.execute(f"SELECT name8 FROM UserData WHERE user_id = '{userid}'")
    try:
        name8 = str(c.fetchone()[0])
        conn.commit()
    except:
        return ''
    else:
        return name8


def fetch_name9(userid):
    c.execute(f"SELECT name9 FROM UserData WHERE user_id = '{userid}'")
    try:
        name9 = str(c.fetchone()[0])
        conn.commit()
    except:
        return ''
    else:
        return name9


def fetch_name10(userid):
    c.execute(f"SELECT name10 FROM UserData WHERE user_id = '{userid}'")
    try:
        name10 = str(c.fetchone()[0])
        conn.commit()
    except:
        return ''
    else:
        return name10


def fetch_end1(userid):
    c.execute(f"SELECT end1 FROM UserData WHERE user_id = '{userid}'")
    try:
        end1 = str(c.fetchone()[0])
        conn.commit()
    except:
        return ''
    else:
        return end1


def fetch_end2(userid):
    c.execute(f"SELECT end2 FROM UserData WHERE user_id = '{userid}'")
    try:
        end2 = str(c.fetchone()[0])
        conn.commit()
    except:
        return ''
    else:
        return end2


def fetch_end3(userid):
    c.execute(f"SELECT end3 FROM UserData WHERE user_id = ?", (userid,))
    try:
        end3 = str(c.fetchone()[0])
        conn.commit()
    except:
        return ''
    else:
        return end3


def fetch_is_premium(userid):
    c.execute(f"SELECT is_premium FROM UserData WHERE user_id = ?", (userid,))
    is_premium = str(c.fetchone()[0])
    conn.commit()
    return is_premium



def fetch_option_number(userid):
    c.execute(f"SELECT option_number FROM UserData WHERE user_id = '{userid}'")
    option_number = str(c.fetchone()[0])
    conn.commit()
    return option_number




def userid_fetcher():
    c.execute("SELECT user_id FROM UserData")
    listuserid = c.fetchall()
    conn.commit()
    return listuserid




def create_admin(admin_id):
    sql = f"Insert into Admindata (admin_id) values({admin_id})"
    c.execute(sql)
    conn.commit()


def adminid_fetcher():
    c.execute("SELECT admin_id FROM Admindata")
    listadminid = c.fetchall()
    conn.commit()
    return listadminid



def fetch_specific_user(userid):
    c.execute(f"SELECT * From UserData WHERE user_id = '{userid}'")
    useridshit = str(c.fetchall())
    conn.commit()

    return useridshit


def fetch_UserData_table():
    c.execute("SELECT * FROM UserData")
    table = c.fetchall()
    conn.commit()

    return table


def fetch_all_users():
    c.execute("SELECT user_id FROM UserData")
    table = c.fetchall()
    conn.commit()
    return table


def fetch_Admindata_table():
    c.execute("SELECT * FROM AdminData")
    table = c.fetchall()
    conn.commit()

    return table


def delete_alldata_UserData():
    c.execute("DELETE FROM UserData")
    conn.commit()


def delete_alldata_AdminData():
    c.execute("DELETE FROM Admindata")
    conn.commit()


def delete_specific_UserData(userid):
    c.execute("DELETE FROM UserData WHERE user_id = ?", (userid,))
    conn.commit()


def delete_specific_AdminData(admin_id):
    c.execute("DELETE FROM Admindata WHERE admin_id = ?", (admin_id,))
    conn.commit()



def check_admin(userid):
    admin_list = adminid_fetcher()
    for x in admin_list:
        if userid in x:
            return True
        else:
            continue
    else:
        return False


def check_user(userid):
    cursor1 = conn.cursor()
    cursor2 = conn.cursor()
    cursor1.execute("SELECT user_id FROM UserData")
    user_list = cursor1.fetchall()
    for x in user_list:
        if userid in x:
            cursor1.close()
            cursor2.close()
            return True
    cursor1.close()
    cursor2.close()
    return False


def check_name(userid):
    user_list = userid_fetcher()
    for x in user_list:
        if userid in x:
            return True
        else:
            continue
    else:
        return False


def check_expiry_days(userid):
    exp = fetch_expiry_date(userid)
    today = date.today()
    days_left = (exp - today).days
    return days_left


