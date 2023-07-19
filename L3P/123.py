from userl import User
from cardl import Card

alex = User("Alex")

alex.sayName()
alex.setAge(33)
alex.sayAge()

card = Card("4356 6528 9658 7456", "11/28", "Alex F")

alex.addCard(card)
alex.getCard().pay(1000)

