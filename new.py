# numbers = [1, 2, 3]
# search = 4

# for number in numbers:
#     if number == search:
#         print('найдено')
#         break
# else:
#     print('не найдено')


# a = 8
# b = 4
# print(a, b)
# a, b = b, a
# print(a, b)


# a = 3400
# b = 4_234_325_251
# print(type(a))
# print(type(b))
# print(type(a) == type(b))


# # eval()
# # exec()
# a = 3
# b = eval('a + 2')
# print(b)
# exec('c = a ** 2')
# print(c)


# def example():
#     ...


# def example_two():
#     pass


# print(bool(...))
# print(bool(None))

# i = input().lower().split()
# i = 'Привет как дела Привет дела хорошо'.lower().split()
# b = []
# for a in i:
#     a = str(a.split(' ')).lower
#     if a == a:
#         len[a] = len[a]
#     b.append(len[a])
# print(b)


# a = [1, 2, 3]
# a[0] = a
# print(a)


# a = {
#     'name': 'Даниил',
#     'age': 13
# }
# a.update(
#     {
#         'age': 15,
#         'status': 'отличник'
#     }
# )
# print(a)
# print('status' in a)
# print('second_name' in a)


# # Compress sentences

# a = 'ПривЕт'
# print(a.lower())


# string = "THE ONE BUMBLE BEE one bumble the bee".lower().split()
# result = []
# for word in string:
#     if word not in result:
#         result.append(word)
# print(result)
# result_numbers = []
# for word in string:
#     result_numbers.append(result.index(word))
# print(result_numbers)

# result_numbers_two = ''.join(str(result.index(word)) for word in string)
# print(result_numbers_two)


def count_letters(text):
    # text = text.lower().split()

    # splitted_text = text.split()

    # res = ''

    # for el in splitted_text:
    #     res += str(splitted_text.index(el))

    # return res
    return ''.join(str(text.lower().split().index(el)) for el in text.lower().split())
print(count_letters('THE ONE BUMBLE BEE one bumble the bee'))