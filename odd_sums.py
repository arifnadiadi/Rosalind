a = int(raw_input("First #: "))
b = int(raw_input("Second #: "))

def odd_sums(a,b):
    count = 0
    for i in range(a, b+1):
        if i % 2 != 0:
            count += i
    return count


print odd_sums(a,b)
