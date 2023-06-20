from address import Address
from mailing import Mailing

toAddress = Address(344000, "Ростов-на-Дону", "Соколова", 66, 108)
fromAddress = Address(119160, "Москва", "Знаменка", 19, 358)
mailing = Mailing(toAddress, fromAddress, 219, 5298632)

print(f"Отправление {mailing.track} из {fromAddress.index}, {fromAddress.town}, {fromAddress.street}, {fromAddress.house}  - {fromAddress.apartment} в {toAddress.index}, {toAddress.town}, {toAddress.street}, {toAddress.house} - {toAddress.apartment}. Стоимость {mailing.cost} рублей")