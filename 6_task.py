import requests
import time
from requests.exceptions import Timeout

url = 'http://httpbin.org/get'

proxies = {
    'http': 'http://200.12.55.90:80',
    'https': 'http://200.12.55.90:80'
}
start = time.perf_counter()
try:
    requests.get(url=url, proxies=proxies)
except Timeout as _ex:
    print(time.perf_counter() - start)
except requests.exceptions.ProxyError as _ex:
    print(time.perf_counter() - start)



# import requests
# import time
# from requests.exceptions import Timeout

# url = 'http://httpbin.org/get'

# proxies = {
#     'http': 'http://200.12.55.90:80',
#     'https': 'http://200.12.55.90:80'
# }
# start = time.perf_counter()
# try:
#     requests.get(url=url, proxies=proxies, timeout=1)
# except Timeout as _ex:
#     print(_ex)
#     print(time.perf_counter()- start)
# except requests.exceptions.ProxyError:
#     # print(_ex)
#     print(time.perf_counter()- start)