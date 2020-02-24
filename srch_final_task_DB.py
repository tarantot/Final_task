import re

def srch_final_task_DB():
    input_filename = '../final_task_DB.db'
    results_filename = '../results.txt'

    inputfile = (input_filename, mode='r', encoding='UTF-8')
    resultfile = (results_filename, mode='w', encoding='UTF-8')
    mytext = inputfile.read()

    results = [srch]
    
    for result in results:
        regex = re.compile(result)
        match = re.search(regex, inputfile)
        if match:
            print('Found "{}" in "{}"'.format(string, text))
            text_pos = match.span()
            print(text[match.start():match.end()])
            resultfile.write(results)
        else:
            print('Did not find "{}"'.format(string))
