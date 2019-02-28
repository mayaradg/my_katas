def is_isogram(string):
    string = string.lower()
    list = []
    for l in string:
        if(l in list):
            return False
        else:
            list.append(l)
    return True