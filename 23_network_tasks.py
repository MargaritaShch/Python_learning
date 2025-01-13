#Network
import urllib.parse
import urllib.request
import gzip
from io import BytesIO
import requests
import json
import shutil

print("Task 1======================================")
with urllib.request.urlopen("http://www.python.org/")  as f:
    print(f.read(300))

#code- decode
# print("Task 2======================================")
# with urllib.request.urlopen("http://www.python.org/") as f:
#     raw_data = f.read(100)  # Читаем данные
#     try:
#         # Попытка расшифровать gzip, если данные сжаты
#         with gzip.GzipFile(fileobj=BytesIO(raw_data)) as gzip_file:
#             decoded_data = gzip_file.read()
#             print(decoded_data.decode("utf-8"))
#     except OSError:
#         # Если данные не сжаты, декодируем напрямую
#         print(raw_data.decode("utf-8"))

#method resp
print("Task 3======================================")
resp = urllib.request.urlopen("http://www.python.org/")
print(resp.readlines())

print("Task 4======================================")
BASE_URL = "https://webhook.site/e3673057-de6c-433b-a14a-fd2649aed134"

params = urllib.parse.urlencode({'spam':1, 'eggs': 2, 'beacon': 3})
url = BASE_URL + "?%s" % params
print("Мы сформирвали следующий URL:", url)
urllib.request.urlopen(url).close()

print("Task 4======================================")
BASE_URL = "https://webhook.site/e3673057-de6c-433b-a14a-fd2649aed134"

params = urllib.parse.urlencode({'spam':1, 'eggs': 2, 'beacon': 5}).encode('utf-8')
print("Мы сформирвали следующий URL:", url)
urllib.request.urlopen(BASE_URL, params).close()

#libriry request
#GET запрос
print("Task 5======================================")
response = requests.get("https://httpbin.org/get")
print(response.content)
print(response.json())
print(response.headers)
print(response.headers.get("Server"))

#POST запрос
print("Task 6======================================")
response = requests.post(BASE_URL, data = {"some_param":124})
print(response)
s = json.dumps({"some_param":124})
print(s)
response = requests.post(BASE_URL, json=s)
print(response)

#Auth
print("Task 7======================================")
response = requests.get("https://httpbin.org/basic-auth/user/passwd", auth = ("user", "passwd"))
print(response.json())
print(response.content)

#Ecxeption
print("Task 8======================================")
#Timeout
#ConnectTimeout
# response = requests.get("https://httpbin.org/user-agent", timeout=(0.00001, 10))
# print(response)#ConnectTimeout

 #ReadTimeout
# response = requests.get("https://httpbin.org/user-agent", timeout=(10, 0.00001))
# print(response) #ReadTimeout

#ConnectionError
# print(requests.get("http://urldoesnotexistforsure.bom"))#ConnectionError

#HTTPError
response = requests.get("https://httpbin.org/status/500")
print(response.status_code)

try:
    response = requests.get("https://httpbin.org/status/500")
    response.raise_for_status()
except:
    print("Oops. Http Error occured")
    # print("Response is: {content}".format(content = err.response.content))

#download file
print("Task 9======================================")
r = requests.get("https://httpbin.org/", stream = True)
if r.status_code == 200:
    with open("get_query_result.txt", "wb")  as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)