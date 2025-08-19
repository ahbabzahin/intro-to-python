class computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))
    def set_max_price(self, price):
        self.__maxprice = price
c=computer()
c.sell()
c.set_max_price(1000)
c.sell()
c.set_max_price(1000)