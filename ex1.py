

def num_option (n):
    sum = 0
    if n == 0 :
        return 1

    for i in range ( n-1 , 0 , -1):
        sum += i
        sum = sum + num_option(n-i-1)


    return sum



print(num_option (3))
