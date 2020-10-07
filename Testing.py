class ATM:
    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name

    

    def withdraw(self, request):
         def print_nameBanke():
          print(bank_name) 

          result = self.balance

          if request > self.balance:
              print("No sufficient funds available ")

          elif request < 0:
              print("Please enter more than zero! ")

          else:
              result = self.balance - request

              while request > 0:

                  if request >= 100:
                      request -=100
                      print("give 100")

                  elif request >= 50:
                      request -= 50
                      print("give 50")

                  elif request >= 10:
                      request -= 10
                      print("give 10")

                  elif request >= 5:
                      request -= 5
                      print("give 5")

                  elif request < 5:
                      print("give "+ str(request))
                      request = 0

          return result


balance1 = 500
balance2 = 5000

atm1 = ATM(balance1, "sahra Bank")
atm2 = ATM(balance2, "tasille Bank")

atm1.withdraw(300)
atm1.withdraw(125)

atm1.print_nameBanke()

atm2.withdraw(200)
atm2.withdraw(78)

atm2.print_nameBanke()
