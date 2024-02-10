import requests

url = 'http://localhost:5000/'
r = requests.post(url, json={'Sepal_Length':2, 'Sepal_Width':9, 'Petal_Length':6, 'Petal_Width':1})

print(r.json())