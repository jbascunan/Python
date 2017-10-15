import requests

if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    payload = {'nombre': 'jose', 'curso': 'python'}
    response = requests.post(url, json=payload)
    print(response.url)

    if response.status_code == 200:
        print(response.content)
