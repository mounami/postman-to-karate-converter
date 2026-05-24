import json

postman_json = '{"name":"Get User", "method":"GET"}'
parsed = json.loads(postman_json)
print(parsed['name'])

def create_request(name, method):
    return {
        'name': name,
        'method': method
    }

request = create_request('Get User', 'GET')
print(request['name'])
