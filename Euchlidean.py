a = int(input("What's the first number? "))
b = int(input("What's the second number? "))


def euklid(a, b):
    a_list = []
    b_list = []
    rest = 1
    a_list.append(a)
    b_list.append(b)
    q_list = []

    while rest != 0:
        rest = a % b
        q = (a - rest) / b
        q_list.append(q)
        a = b
        b = rest
        a_list.append(a)
        b_list.append(b)

    ggT = b_list[len(b_list) - 2]
    return ggT


print((euklid(a, b)))
