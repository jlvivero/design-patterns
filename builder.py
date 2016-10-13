class Reservation(object):
    def __init__(self, hotel, meals, days, car):
        self.hotel = hotel
        self.meals = meals
        self.days = days
        self.car = car

    def report(self):
        print("Hotel: ", self.hotel)
        print("Meals: ", self.meals)
        print("Days: ", self.days)
        print("Car: ", self.car)

class Reservation_builder(object):
    def __init__(self):
        self.reservation = None
        self.hotel = None
        self.meals = None
        self.days = None
        self.car = None
    def add_hotel(self,value):
        self.hotel = value
    def number_of_meals(self, value):
        self.meals = value
    def days_of_stay(self, value):
        self.days = value
    def car_name(self, value):
        self.car = value
    def build(self):
        reservation = Reservation(self.hotel,self.meals,self.days,self.car)
        return reservation
#main
builder = Reservation_builder()
builder.add_hotel("Fiesta Inn")
builder.number_of_meals(3)
builder.days_of_stay(2)
builder.car_name("ferrari")
reservation = builder.build()
reservation.report()
