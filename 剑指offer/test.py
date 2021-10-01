def get_digit_sum(x):
    s_sum = 0
    while x>0:
        s_sum += x % 10
        print(s_sum)
        x = int(x/10)

    return s_sum
get_digit_sum(33)