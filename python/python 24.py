class Person:
    def say(self):
        print('吃')
class Chinese(Person):
    def say(self):
       print('你好')
class English(Person):
    def say(self):
        print('hello')
def eat(m):
    if isinstance(m,Person):
        m.say()
    else:
        print('not')
eat(Chinese())
eat(English())