rate_as_str = input("Оцените работу оператора от 1 до 5:")
rate = int(rate_as_str)
if(rate < 1):
    rate = 1
if(rate > 5):
    rate = 5

print(rate)

feedback = ""

if rate == 1:
    feedback = input("Что нам улучшить?:")
elif rate == 2:
    feedback = input("Что вам не понравилось?:")
elif rate == 3:
    feedback = input("Чем остались недовольны?:")
elif rate == 4:
    feedback = input("А че не пять?")
else:
    feedback = input("Рахмет, рахмет, от души братишка, за что оператора похвалить?:")

print(feedback)