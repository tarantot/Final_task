import sqlite3
 
def final_task_DB():
    
    conn = sqlite3.connect("final_task_DB.db") 
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE employees ('personal ID' integer PRIMARY KEY, 
                                              'full name' text NOT NULL, 
                                              'sex' text NOT NULL, 
                                              'age' text NOT NULL,
                                              'phone number' integer NOT NULL)""")
    conn.commit()
    cursor.close()
    conn.close()
    
final_task_DB()