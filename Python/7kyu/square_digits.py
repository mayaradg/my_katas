def square_digits(num):
    num = str(num)
    result = ""
    for n in num:
        result = result + str(int(n)**2) 
    return int(result)