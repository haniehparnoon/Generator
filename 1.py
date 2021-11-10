def outer_func(n):
    def find_divisor():
        for i in range(1, n):
            if n % i == 0:
                yield i
    perfect = 0
    for i in find_divisor():
        #print(i)
        perfect += i
    if perfect > n:
        print("Greater: perfect > number")

    elif perfect < n:
        print("Lesser: perfect < number")

    else:
        print("Perfect: perfect = number")


num = int(input("enter number"))
outer_func(num)

