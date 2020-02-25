import re

def srch_final_task_DB():
    input_filename = '../final_task_DB.db'
    results_filename = '../results.txt'

    inputfile = (input_filename, mode='r', encoding='UTF-8')
    resultfile = (results_filename, mode='w', encoding='UTF-8')
    mytext = inputfile.read()

    srch = srch.casefold()
    results = re.findall(srch, mytext)
    
    for srch in results:
        regex = re.compile(srch)
        match = re.finditer(regex, inputfile)
        if match:
            print('Found "{srch}" at {begin}:{end}'.format(srch, begin=match.start(), end=match.end())
            resultfile.write(results)
        else:
            print('Can not find "{}" in "{}"!'.format(srch, input_filename))
