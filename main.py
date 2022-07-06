import requests
import json
from requests.structures import CaseInsensitiveDict
import asyncio
import time

url = "https://eu5.api.enterprisedata.slb.com/api/storage/v2/records"
urlSearch = ""

headers = CaseInsensitiveDict()
headers["accept"] = "application/json"
headers["data-partition-id"] = "sandbox-weu-des-prod-testing-e"
headers[
    "Authorization"] = "Bearer eyJ0eXAiOiAiSldUIiwgImFsZyI6ICJSUzI1NiIsICJraWQiOiAiTVRZMU56QTNNamd3TXc9PSJ9.eyJpYXQiOiAxNjU3MTI1NjY3LCAiZXhwIjogMTY1NzEyOTI2NywgImlzcyI6ICJodHRwczovL2NzaS5zbGIuY29tL3YyIiwgImF1ZCI6IFsiYmQzMWU1MDMzMGUwNDkwMDhjMWJlMGQ3M2JlM2I3NWEiLCAiNmE2MzhlZWE0MzFlNDdjYjgyYjM1ZGRiZjZlMmYzNzgiLCAiOTYzZjJjYzY5MTVlNDc5ZmEwZmNiNzNlYzJlYzkwZTciLCAiNTdjNzRkMGRiYzJmNDJhYjg4MWY2NmU3OWY5NDMxY2UiLCAiZGUtc2F1dGgtdjItc2NvcGUtc2VydmljZS1kYXRhbGFrZS5zbGJzZXJ2aWNlLmNvbSIsICI1ZGQyNzlmOWY5ZDE0MjMxOGZjZjlkN2NhZjg1NDZlNCJdLCAic3ViIjogImFndWVycmVybzI1QHNsYi5jb20iLCAiZW1haWwiOiAiYWd1ZXJyZXJvMjVAc2xiLmNvbSIsICJkZXNpZCI6ICJhZ3VlcnJlcm8yNS1zbGItY29tLTkyYmUwYjQwQGRlc2lkLmRlbGZpLnNsYi5jb20iLCAic3ViaWQiOiAieW43RkN4SUdXR2g1MGtsbVowZXMwckFnTzJZWjgyaVhFSlJrT3BHUlplOCIsICJhenAiOiAiYmQzMWU1MDMzMGUwNDkwMDhjMWJlMGQ3M2JlM2I3NWEiLCAianRpIjogImF0LjMyNTc4OGVkNjNlNjRiYmY5YmVlODI1NDhiNTI1MTE2IiwgIm9pZCI6ICIxOWRlZmY1Ny1jMjZhLTQ2ZDAtOTYwZS1kNjQ2NDVhZDU2OTgiLCAidGlkIjogIjQxZmYyNmRjLTI1MGYtNGIxMy04OTgxLTczOWJlODYxMGMyMSJ9.aVkysx6fHOW2-ZVWkpzNOV0HTSfJGtzwhoEQhw6QsKv6okXtGfMSUXD227Uk28i9K5ZqFKIBnvw8Z3gqyuu62-Sx7Tf2eenDq4VAEm9LuxF3Omdd7k8NLbe-yG-fEYInDAEmj9NObgYKfzE_jGEa9ibY2m4oYurO4mXP7PXJjg8TBC-ToGwya0cThCHySsAVCq0YE59ycTbVPfs89flHmK4ror_zMJmUZTsARyOwLilUzXB8m6QBuWTv_VIsJcUyyz6viAmTqa41qy0rSwYh9L139VdCeFoQ6jwclr4OLwemGeM85jAsE0Og43OY-yrIn62XPMbcA3BZHBk1u_tYdg"
headers["Content-Type"] = "application/json"

with open('resources/base_collections_request.json') as base_collections:
    collections_no_data = json.load(base_collections)

with open('resources/updated_collections_request.json') as filled_collections:
    collections_with_data = json.load(filled_collections)


async def create_request():
    create = requests.put(url, headers=headers, json=collections_no_data)
    return json.loads(create.text)


async def update_request():
    update = requests.put(url, headers=headers, json=collections_with_data)
    return json.loads(update.text)


async def get_request(record_id):
    collection = requests.get(url + '/' + record_id, headers=headers)
    return json.loads(collection.text)


async def delete_request(record_id):
    collection = requests.delete(url + '/' + record_id, headers=headers)
    return collection.status_code


# generate new collection empty to be updated
create_start_time = time.time()
create_log = asyncio.run(create_request())
record_created = create_log['recordIds'][0]

# uses new generated id to update the collection
collections_with_data[0]['id'] = record_created
update_log = asyncio.run(update_request())
create_finish_timer = time.time()

# get the updated collection to verify is the update is already published
get_start_timer = time.time()
asyncio.run(get_request(record_created))
get_end_timer = time.time()

# delete_log = asyncio.run(delete_request(record_created))

collection_log = asyncio.run(get_request(record_created))

print(str(create_finish_timer - create_start_time))
print(str(get_end_timer - get_start_timer))
# print(delete_log)
print(collection_log)
