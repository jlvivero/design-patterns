class Player(object):
    class __Player(object):
        def __init__(self):
            self.life = 100
        def was_hit(self, damage):
            print("player suffered ", damage, " damage")
            self.life = self.life - damage
        def get_life(self):
            return self.life
    instance = None
    def __new__(cls): #new is always a classmethod
        if not Player.instance:
            Player.instance = Player.__Player()
        return Player.instance

def enemy1():
    player = Player()
    player.was_hit(25)
    currentlife1 = player.get_life()
    print(currentlife1)
def enemy2():
    player2 = Player()
    player2.was_hit(10)
    currentlife2 = player2.get_life()
    print(currentlife2)
    

#main
enemy1()
enemy2()


#the constructor of the class is private
#class OnlyOne(object):
#    class __OnlyOne:
#        def __init__(self):
#            self.val = None
#        def __str__(self):
#            return `self` + self.val
#    instance = None
#    def __new__(cls): # __new__ always a classmethod
#        if not OnlyOne.instance:
#            OnlyOne.instance = OnlyOne.__OnlyOne()
#        return OnlyOne.instance
#    def __getattr__(self, name):
#        return getattr(self.instance, name)
#    def __setattr__(self, name):
#        return setattr(self.instance, name)
#x = OnlyOne()
#x.val = 'sausage'
#print(x)
#y = OnlyOne()
#y.val = 'eggs'
#print(y)
#z = OnlyOne()
#z.val = 'spam'
#print(z)
#print(x)
#print(y)
