import requests
import json
from urllib.parse import urlencode


def get_explore_json(host, port=80, force='true'):
    cookies = {
        "JSESSIONID": "534399BC981ED06ECE0B517ABB8835B5",
        "language": "zh-CN",
        "session": ".eJwlzTEOwyAMQNG7eGbAJNiQyyAXbLVq1EiQTFXuXqTu_-l_oVjX8YTt7Jc6KK8GG5jQgkw5ekEJzDEZrr4u0WfKmiI4qKNbOY-3fmZP9vAcuVVsnpuFVTD6yjnVNZMkFCNUajjdflTZdZoJHVxD-38Z4P4BEgEn8A.DVm6QQ.3a0cB2zBGYX969_CU2ghzHy9GIg"
    }

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "keep-alive",
        "content-type": "application/json",
        "Cookie": "session=.eJwlzTEOwyAMQNG7eGbAJNiQyyAXbLVq1EiQTFXuXqTu_-l_oVjX8YTt7Jc6KK8GG5jQgkw5ekEJzDEZrr4u0WfKmiI4qKNbOY-3fmZP9vAcuVVsnpuFVTD6yjnVNZMkFCNUajjdflTZdZoJHVxD-38Z4P4BEgEn8A.DVm6QQ.3a0cB2zBGYX969_CU2ghzHy9GIg; language=zh-CN; JSESSIONID=534399BC981ED06ECE0B517ABB8835B5",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    }

    host = 'http://{}:{}/'.format(host, port)
    path = 'sci/superset/explore_json/table/{}'
    with open('D:\\home\\pivot_viz\\form_data.json', 'r') as f:
        content = f.read()
        form_data = json.loads(content)
        print(form_data['datasource'].split('__')[0])
        url = host + path.format(form_data['datasource'].split('__')[0]) + '?' + urlencode({'form_data': content, 'force': force})
        print(url)
    res = requests.get(url, headers=headers, cookies=cookies)

    print(res.status_code)
    with open('D:\\home\\pivot_viz\\response.json', 'w', encoding='utf8') as f:
        f.write(res.content.decode())
    return json.loads(res.content.decode()).get('query')


if __name__ == '__main__':
    # sql = get_explore_json('10.122.22.113')
    # sql = get_explore_json('10.122.27.44', 8088)
    sql = get_explore_json('127.0.0.1', 8088)
    # sql = get_explore_json('10.122.27.44', 8013)
    print(sql)
