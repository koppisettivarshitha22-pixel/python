class car:
    def __init__(self,company,model):
       self.company=company
       self.model=model
    def display(self):
        print("the company is :",self.company)
        print("the model is :",self.model)
c1=car("honda","grand i10")
c1.display()
    
