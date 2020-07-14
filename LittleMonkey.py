import random

LetterList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

buff = ''



with open('Shakespeare.txt','a+')as file:

    while True:

        if len(buff) != 4096:
            i = random.randint(0,25)
            buff = buff + LetterList[i]
        else:
            file.write(buff)
            buff = ''
