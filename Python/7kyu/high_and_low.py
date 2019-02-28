def high_and_low(numbers):    
    list_numbers = numbers.split(" ")
    numbers = []
    for i in list_numbers:
        numbers.append(int(i))
    return str(max(numbers)) + " " + str(min(numbers)) 