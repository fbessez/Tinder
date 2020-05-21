#!python
import json

with open('api_endpoints.json', 'r') as endpoints_file:
  endpoint_data = json.loads(endpoints_file.read())
  with open('api_endpoints.py', 'w') as f:
    f.write('API_ENDPOINTS=' + str(endpoint_data))