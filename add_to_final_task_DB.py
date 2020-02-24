import sqlite3
import datetime

def add_to_final_task_DB():
    for personal_ID = 0:
        personal_ID+=1
    emp_age = datetime.emp_bdate - datetime.date.today()
    emp_sex = emp_sex.upper()
    if emp_sex is not 'М' is not 'Ж':
        print('Пожалуйста выберите корректное значение!')
    for emp_phonenumber != 0:
        data = json.load(open('countries&codes.json'))
        for name in data['countries&codes'].items():
            if emp_phonenumber==dial_code:
                reply = input('Are you from {0}? Y / N'.format(name))
                if reply=='Y':
                    emp_phonenumber = input('Please type your phone number with the country code +XXX : ')
                else:
                    emp_phonenumber = input('Please type your valid phone number! ')
    
    conn = sqlite3.connect("final_task_DB.db") 
    cursor = conn.cursor()
    cursor.execute("""INSERT into employees VALUES (personal_ID, emp_full_name, emp_sex, emp_age, emp_phonenumber)""" )    
    
    conn.commit()
    cursor.close()
    conn.close()
    
final_task_DB()
