
class Human:
    def __init__(self, name):
        self.n=name
        self.mood = 'Great!'
        self.has_money = False
        self.alpha = 10
    def my_mood(self):
        print(self.alpha)
        if self.has_money:
            self.mood = 'Great!'
        else:
            self.mood = 'Horrible T.T'

class Chinese(Human):
    def is_commuist_party(self):
        if self.mood == 'Great!':
            return True
        else:
            return False

class American(Human):
    def is_Trump_supporter(self):
        if self.mood == 'Great!':
            return True
        else:
            return False

John = American('John SMith')
print(John.n)
print(John.is_Trump_supporter())
#print(John.is_communist_party())
result = John.my_mood()
print('result:', result)
exit()

adam = Human('ADAM')
print(adam.mood)
adam.my_mood()
print(adam.n, adam.mood)
print("exit here")
eve = Human('eeee')
print(eve.n, eve.mood)
exit()
def my_mood(mood):

    if mood:
        print('yay')
    else:
        print('oh no')

m_week = [True, False, False, True, True]

for s in m_week:
    my_mood(s)

print('\n')
print(m_week)