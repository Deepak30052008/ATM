class Automated_Teller_Machine :
    def __init__(self,pinNumber,card):
        self.pinNumber:input(pinNumber)
        self.card:card
    
    def BalanceEnquiry(self,enquiry):
        self.enquiry:enquiry
        print(enquiry)

    def CashWithdrawl(self,cash):
        self.cash:cash

ATM=Automated_Teller_Machine(4564654511,"cardEntered")
ATM.BalanceEnquiry($8000)
ATM.CashWithdrawl(input("Enter the amount you want to withdraw within the amount:"))
print("withdrawal complete")
