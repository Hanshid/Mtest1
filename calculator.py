class Calculator:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y
    def sub(self):
        return self.x-self.y
    def mul(self):
        return self.x*self.y
    def div(self):
        return self.x/self.y

class UseCalculator(Calculator):
    x=int(input(" first number: "))
    y=int(input(" second number: "))
    obj=Calculator(x,y)
    choice=1
    while choice!=0:
        print("0. Exit")
        print("1. Add")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice=int(input("Enter choice: "))
        if choice==1:
            print("Result: ",obj.add())
        elif choice==2:
            print("Result: ",obj.sub())
        elif choice==3:
            print("Result: ",obj.mul())
        elif choice==4:
            print("Result: ",round(obj.div(),2))
        elif choice==0:
            print("Exiting!")
        else:
            print("syntax error!!")
    print()
