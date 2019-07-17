import requests

lc = 10
hr = 15

response = requests.post("http://192.10.24.4:32133/swarm", {"locust_count":lc, "hatch_rate":hr})
print(response.content)

i = 1
while i == 1 :
  i = 1
