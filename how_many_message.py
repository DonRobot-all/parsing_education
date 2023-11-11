import requests

people_messages = {}

url = 'https://parsinger.ru/3.4/3/dialog.json'

response = requests.get(url=url)
answer = response.json()
people_messages[answer['username']] = 1
messages = answer.get('comments')


def how_many(messages):
    for i in messages:
        if i['username'] in people_messages:
            people_messages[i['username']] += 1
            how_many(i.get('comments'))
        else:
            people_messages[i['username']] = 1
            how_many(i.get('comments'))
    return 0


how_many(messages)



def key_sort(e):
    print(e)
    return -e[1], e[0]


a = dict(sorted(people_messages.items(), key=key_sort))
print(a)
# message = answer.get('comments')
# print(message[1].get('comments'))
# print(answer['comments'][0]['comments'])