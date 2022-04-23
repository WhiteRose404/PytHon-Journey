
a ,b = 32,8

print('Addition: ',a + b)
print('Subtractino: ',a - b)
print('Multiplication: ',a * b)
print('Division: ',a / b)
print('Floor Division: ',a // b)
print('Modulas: ',a % b)
print('Exponentiation : ',a ** b)

# The same goes for other operator
# Let's build some intersting tool using these tools

# Like other languges python also have function
# to define an function all you need is to type def and the name 
# of the function 
# def functionName(var,...):
#    """Documention"""
#    //Code
# 
    
def pgcd(a,b):
    if b==0: return a
    return pgcd(b,a%b)


def ppcm(a,b):
    """ a*b = pgcd(a,b) * ppcm(a,b) """
    return abs(a*b)//pgcd(a,b)


print(pgcd(a,b))
print(ppcm(a,b))
