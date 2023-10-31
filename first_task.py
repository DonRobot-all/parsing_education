import requests

response = requests.get('https://www.example.com')
print(response.text)




# Response {
#     status_code: 200,
#     headers: {...},
#     url: 'https://httpbin.org/get',
#     text: '...',
#     content: b'...',
#     json: <method>,
#     elapsed: <datetime.timedelta>,
#     ...
# }