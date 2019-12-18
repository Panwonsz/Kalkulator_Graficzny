class Calculations:
    @staticmethod
    def sum(x,y):
        x = float(x)
        y = float(y)
        return x + y
    @staticmethod
    def subtract(x,y):
        x = float(x)
        y = float(y)
        return x - y
    @staticmethod
    def multiply(x,y):
        x = float(x)
        y = float(y)
        return x * y
    @staticmethod
    def divide(x,y):
        x = float(x)
        y = float(y)
        if (y == 0.0):
            return False
        return x / y
    @staticmethod
    def power(x,y):
        x = float(x)
        y = int(y)
        if (y==0):
            return 1.0
        else:
            outcome = x
            for i in range(y-1):
                outcome *= x
            return outcome
        if y < 0:
            return 1/outcome
        return outcome
    @staticmethod
    def square_root(x,y):
        x = float(x)
        y = int(y)
        return x**(1/y)
    @staticmethod
    def factorial(x):
        x = int(x)
        if (x==0 or x==1):
            return 1

        return x * int(Calculations.factorial(str(x-1)))
    @staticmethod
    def sinus(x):
        x = int(x)

    @staticmethod
    def cosinus(x):
        x= float(x)
        outcome = 0.0
        for n in range(53):
            if n % 2 == 0:
                outcome -= Calculations.power(str(x),str(2*n)) / Calculations.factorial(str(2*n))
            else:
                outcome += Calculations.power(str(x),str(2*n)) / Calculations.factorial(str(2*n))
        return outcome

if __name__ == '__main__':
    print(Calculations.factorial(4))
    print(Calculations.square_root(9,3))
    print(Calculations.power(3,3.5))
    print(Calculations.cosinus('4.12'))
