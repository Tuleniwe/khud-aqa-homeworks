class User:

    def __init__(self, firtsName, lastName):
        self.firstName = firtsName
        self.lastName = lastName
    
    def sayFirstName(self):
        print("Мое имя:", self.firstName)

    def sayLastName(self):
        print("Моя фамилия:", self.lastName)

    def sayFullName(self):
        print("Меня зовут:", self.firstName, self.lastName)

        
