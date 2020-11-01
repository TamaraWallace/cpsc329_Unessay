import requests

url = ""

bin_id = open('binID.txt', 'r').read()
url = "https://postb.in/b/" + bin_id

r = requests.get(url)
print("Get status code: (200=Success)")
print(r)
print(r.text)
