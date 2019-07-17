import requests

lc = 10
hr = 10

response = requests.post("http://192.10.24.4:32133/swarm", {"locust_count":lc, "hatch_rate":hr})
print(response.content)
