
x = int(input("Enter the first number "))
y = int(input("Enter exponent "))
z = int(input("Enter the modulus range "))


def mod_expo(x,y,z):

    k = x**y
    n = k % z
    print(n)

mod_expo(x,y,z)
