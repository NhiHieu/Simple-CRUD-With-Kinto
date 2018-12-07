from kinto_http import Client
credentials = ('admin', 's3cr3t')

client = Client(server_url='http://localhost:8888/v1',
                auth=credentials)
info = client.server_info()
print(info)
