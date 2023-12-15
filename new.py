def reverse(string: str):
    dct = {}
    shit = ['!', '.', '?', ',']
    
    for symbol in string:
        if symbol.lower() == symbol.upper():
            dct[symbol] = string.index(symbol)

    str_without_shit = ''

    for letter in range(0, len(string)):
        if string[letter] not in shit:
            str_without_shit += string[letter]

    lst_string = str_without_shit.split(' ')
    answer = ''

    for word in range(0, len(lst_string)):
        answer += lst_string[word][::-1] + ' '

    answer = list(answer)
    answer.remove(' ')

    for symbol in dct:
        answer.insert(dct[symbol], symbol)
        
    return ''.join(answer)


print(reverse('тевирП! онваД ен ьсиледив.'))