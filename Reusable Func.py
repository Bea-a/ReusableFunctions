#writing reusable Functions

# box a string

def boxString(content):
    n = len(content)
    if n ==0:
        return
    print('-'*(n+2))
    print('-'+content+'-')
    print('-'* (n+2))
boxString('Hello')

#in case of hello it is 5 length
# okay so content is Hello- the length is 5, but as we want to wrap around it and make a box,
# we need extra two spaces...
#the middle part where the word is will print - then the word and again + '-'
#Makes sense now!

# okay i want to make my own function

def cashmoney(word):
    n = len(word)
    if n ==0:
        return
    print('$'*(n+4))
    print('$$'+word+'$$')
    print('$'*(n+4))
cashmoney('MoneyHoney')


