class ATM:

    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name

    def withdraw(self, request):
        print(self.bank_name, 'Current Balance =' , self.balance)
        result = self.balance

        if request > self.balance:
            print("Can't give you all this money !!")

        elif request < 0:
            print("More than zero plz!")

        else:
            self.balance -= request
            notes = [100, 50, 10, 5]
            
            for note in notes :
                while request >= note :
                    request -= note
                    print('give ' + str(note))
                if request < 5 and request > 0 :
                    print('give ' + str(request))
            result = self.balance

        return result
balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Saba Bank")
atm2 = ATM(balance2, "Jeen Bank")

atm1.withdraw(700)
atm1.withdraw(421)
atm1.withdraw(82)

atm2.withdraw(500)
atm2.withdraw(450)
atm2.withdraw(51)