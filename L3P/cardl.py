class Card:
    number = "0000 1111 2222 3333"
    validDate = "12/24"
    holder = "unknown"

    def __init__(self, number, date, holder):
        self.holder = holder
        self.number = number
        self.validDate = date

    def pay(self, amount):
        print("С карты ", self.number, "списали", amount)
    