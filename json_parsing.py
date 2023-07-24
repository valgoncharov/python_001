import requests

response = requests.post("https://petstore.swagger.io/v2/store/order")
print(response.status_code)
print(response.text)