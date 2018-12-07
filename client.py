from kinto_http import Client
from kinto_http.patch_type import BasicPatch, MergePatch, JSONPatch
credentials = ('admin', 's3cr3t')

client = Client(server_url='http://localhost:8888/v1',
                auth=credentials)

client.create_bucket(id='payments')

client.update_bucket(id='payments', permissions={"read": ["account: admin"]})

#To create a group.
client.create_group(id='receipts', bucket='payments', data={'members': ['admin', 'nhihieu']})


#To create a collection.
client.create_collection(id='receipts', bucket='payments')

#You can pass a python dictionary to create the record.
client.create_record(data={'status': 'done', 'title': 'Todo #1'},
                     permissions={'read': ['group:groupid']},
                     collection='receipts', bucket='payments')


# You can use id to specify the record id when creating it.
client.create_record(id='todo2', data={'status': 'doing', 'title': 'Todo #2'},
                     collection='receipts', bucket='payments')

# Or modify some fields in an existing record.
client.patch_record(changes=MergePatch({'assignee': 'hieu'}), id='todo2', collection='receipts', bucket='payments')

# To delete an existing record.
client.delete_record(id='todo2',
                      collection='receipts', bucket='payments')


