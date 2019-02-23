def alphabet_position(text):
    text = text.lower()
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    result = ""
    for letter in text:
        if(letter in alphabet):
            result = result + str(alphabet.index(letter)+1) + " "
    result = result[0:len(result)-1]
    return result
        