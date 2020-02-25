import re

def srch_final_task_DB():
    input_filename = '../final_task_DB.db'
    results_filename = '../results.txt'

    inputfile = (input_filename, mode='r', encoding='UTF-8')
    resultfile = (results_filename, mode='w', encoding='UTF-8')
    mytext = inputfile.read()

    srch_parameter = srch_parameter.casefold()
    if srch_parameter is not 'full name' is not 'phone number':
        print('Please choose a correct option!')
    srch = srch.casefold()
    results = re.findall(srch, mytext)
    
    if srch_parameter=='full name':
        for title, in cursor.execute('SELECT "full name" FROM employees WHERE "full name" LIKE ?', [srch]):
        print(title)
        resultfile.write(results)
    else:
        for title, in cursor.execute('SELECT "phone number" FROM employees WHERE "phone number" LIKE ?', [srch]):
        print(title)
        resultfile.write(results)
