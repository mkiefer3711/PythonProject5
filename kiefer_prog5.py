# Function that will add two fractions together
def add(x,y):
    # Variables for the positions of the fractions
    a = x[0]
    b = x[1]
    c = y[0]
    d = y[1]
    # Calculates the numerator based on a formula
    Numerator = (a*d) + (b*c)
    # Calculates the denominator based on a formula
    Denominator = (b*d)
    # Calls reducedfraction function to get the reduced version of the fraction
    ReducFrac = reducedfraction(Numerator,Denominator)
    print()
    print(a , "/" , b , "+ " , c , "/" , d , "= " , ReducFrac[0] , "/" , ReducFrac[1])
    
# Function that will multiply two fractions together
def mpy(x,y):
    # Variables for the positions of the fractions
    a = x[0]
    b = x[1]
    c = y[0]
    d = y[1]
    # Calculates the numerator based on a formula
    Numerator = (a*c)
    # Calculates the denominator based on a formula
    Denominator = (b*d)
    # Calls reducedfraction function to get the reduced version of the fraction
    ReducFrac = reducedfraction(Numerator,Denominator)
    print(a , "/" , b , "x " , c , "/" , d , "= " , ReducFrac[0] , "/" , ReducFrac[1])
    print()


# Function to get the greatest common denominator
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Function for reducing the fraction
def reducedfraction(n,d):
    f = 2
    # Get absolute value of numerator and denominator
    x = abs(n)
    y = abs(d)
    # Calls gcd function to get greatest common denominator
    f = gcd(x,y)
    # Use the gcd to get the reduced numerator and denominator
    x = x // f
    y = y // f
    # Set numerator and denominator back to negative if they were negative to begin with
    if n < 0:
        x = -x
    if d < 0:
        y = -y
    return x, y

# Main function where program starts    
def main():
    Fraction_One = str(100)
    Fraction_Two = str(100)
    print("The fraction 0/0 stops the program")
    print()
    # While loop to allow multiple inputs
    while Fraction_One != "0/0":
        Fraction_One = input("What is the first fraction? ")
        # If statement ends program if fraction entered is 0/0
        if Fraction_One == "0/0":
            return print("\nDone!")
        Fraction_Two = input("What is the second fraction? ")
        # Splits fraction one and fraction two into tuples
        FracOne = Fraction_One.split("/")
        FracTwo = Fraction_Two.split("/")
        TupleOne = (int(FracOne[0]), int(FracOne[1]))
        TupleTwo = (int(FracTwo[0]), int(FracTwo[1]))
        # Calls the add function and the mpy function for the created tuples
        add(TupleOne, TupleTwo)
        mpy(TupleOne, TupleTwo)
    
    
# Calls the main function    
main()