#this is the subject
class stock():
    def __init__(self):
        self.observers = []
        self.price = None
        self.symbol = None

    def attatch(self):
        raise NotImplementedError

    def detach(self):
        raise NotImplementedError

    def notify(self):
        raise NotImplementedError


class ibm(stock):
    def __init__(self, symbol, price):
        self.observers = []
        self.symbol = symbol
        self.price = price #state

    def attatch(self, observer):
        if observer in self.observers:
            print observer, 'already subscribed observer'
        else:
            self.observers.append(observer)

    def detach(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
        else:
            print 'observer not found'

    def set_price(self, p):
        self.price = p
        self.notify()

    def get_price(self):
        return self.price

    def set_symbol(self, s):
        self.symbol = s

    def get_symbol(self):
        return self.symbol

    def notify(self):
        for obs in self.observers:
            obs.update(self)

class observer(object):
    def __init__(self):
        self.name = None
        self.stock = None
    def update(self):
        raise NotImplementedError

class investor(observer):
    def __init__(self, name):
        self.name = name
        self.stock = None

    def update(self, subject):
        print 'notified ', self.name, 'of ', subject.get_symbol(), 'change to ', subject.get_price()
        stock = subject

    def set_stock(self, stock):
        self.stock = stock

    def get_stock(self):
        return stock

#main
stock1 = ibm('ibm', 120)
invest1 = investor("zorros")
invest2 = investor("berkshire")
stock1.attatch(invest1)
stock1.attatch(invest2)
stock1.set_price(20)
stock1.set_price(30)
stock1.set_price(10)
