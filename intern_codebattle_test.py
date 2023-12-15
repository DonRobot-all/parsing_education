def reverse_string(string):
    first_position = 0
    result = ''
    for character in range(len(string)):
        if not string[character].isalpha():
            slice = string[first_position:character]
            first_position = character + 1
            if slice:
                if slice[0].isupper():
                    result += ''.join(reversed(slice)).capitalize()
                else:
                    result += ''.join(reversed(slice)).lower()
            result += string[character]
    return result


if __name__ == '__main__':
    string = input()
    print(reverse_string(string))
