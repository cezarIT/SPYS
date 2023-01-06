from datetime import datetime
def add(word, number):
    now = datetime.now()
    text = str(str(now.strftime('%H:%M:%S')) + ' .N ' + str(number) + '. ' + str(word) + '\n')
    #str(text)
    fale = open('log.txt', 'a')
    fale.write(text)
    fale.close()
def clear():
    fale = open('log.txt', 'w')
    fale.write('')
    fale.close()
