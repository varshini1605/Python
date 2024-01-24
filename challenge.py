class STOCKS:
    def __init__(self,s,company,price):
        self.s=s 
        self.c=company
        self.p=price

    def get_price(self):
        #print(s,":",c,"--",p)
        return f"{self.s}:{self.c}--{self.p}"

S1=STOCKS("MICRO","Microsoft",95)
print(S1.get_price())