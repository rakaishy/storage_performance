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
    "Authorization"] = "Bearer Token"
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

# delete_log = asyncio.run(delete_request(record_created))

collection_log = asyncio.run(get_request(record_created))
get_end_timer = time.time()

print(str(create_finish_timer - create_start_time))
# print(delete_log)
print(collection_log)
print(str(get_end_timer - get_start_timer))
