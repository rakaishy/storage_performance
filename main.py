import requests
import json
from requests.structures import CaseInsensitiveDict
import asyncio

url = "https://eu5.api.enterprisedata.slb.com/api/storage/v2/records"

headers = CaseInsensitiveDict()
headers["accept"] = "application/json"
headers["data-partition-id"] = "sandbox-weu-des-prod-testing-e"
headers[
    "Authorization"] = "Bearer eyJ0eXAiOiAiSldUIiwgImFsZyI6ICJSUzI1NiIsICJraWQiOiAiTVRZMU56QTNNamd3TXc9PSJ9.eyJpYXQiOiAxNjU3MTIyODU4LCAiZXhwIjogMTY1NzEyNjQ1OCwgImlzcyI6ICJodHRwczovL2NzaS5zbGIuY29tL3YyIiwgImF1ZCI6IFsiYmQzMWU1MDMzMGUwNDkwMDhjMWJlMGQ3M2JlM2I3NWEiLCAiNmE2MzhlZWE0MzFlNDdjYjgyYjM1ZGRiZjZlMmYzNzgiLCAiOTYzZjJjYzY5MTVlNDc5ZmEwZmNiNzNlYzJlYzkwZTciLCAiNTdjNzRkMGRiYzJmNDJhYjg4MWY2NmU3OWY5NDMxY2UiLCAiZGUtc2F1dGgtdjItc2NvcGUtc2VydmljZS1kYXRhbGFrZS5zbGJzZXJ2aWNlLmNvbSIsICI1ZGQyNzlmOWY5ZDE0MjMxOGZjZjlkN2NhZjg1NDZlNCJdLCAic3ViIjogImFndWVycmVybzI1QHNsYi5jb20iLCAiZW1haWwiOiAiYWd1ZXJyZXJvMjVAc2xiLmNvbSIsICJkZXNpZCI6ICJhZ3VlcnJlcm8yNS1zbGItY29tLTkyYmUwYjQwQGRlc2lkLmRlbGZpLnNsYi5jb20iLCAic3ViaWQiOiAieW43RkN4SUdXR2g1MGtsbVowZXMwckFnTzJZWjgyaVhFSlJrT3BHUlplOCIsICJhenAiOiAiYmQzMWU1MDMzMGUwNDkwMDhjMWJlMGQ3M2JlM2I3NWEiLCAianRpIjogImF0LjA5NzEwNDI4OWYwYjQ1ZGNhYjdhMjRjMmI4NzE2NDBmIiwgIm9pZCI6ICIxOWRlZmY1Ny1jMjZhLTQ2ZDAtOTYwZS1kNjQ2NDVhZDU2OTgiLCAidGlkIjogIjQxZmYyNmRjLTI1MGYtNGIxMy04OTgxLTczOWJlODYxMGMyMSJ9.inJaYM0wYo67F-dcQBxExrhrlefnnRns4M7MSszUl8_pDAT87FV37cHQb0nvQjClkEa_Kwti1J8GuI3bAYpbtrvnGVSZ7RgrLTNk4M24erj3lq1UHfXQy9MWtoWeFgGMl1x2Ni_aYfid76_qM4ikfhxkD5HJ6Vx8URdVHdfE4Pc6wiVJsGwfLCCZmuJ_VHWJmuG7jWYSlyhvC4jJywst-tKNCqmEAJ0_n_2xw-z8OJD1Eb9fXoP3OGP0a6MN5_Bz1IP5UeUDmyCrADqroNcX16YIvMmsvpQo95yoel1p3P50r374m0-T_fsw_g2Lkdsk82Scp3pamw50ihcpri_ufQ"
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
    return json.loads(collection.text)


create_log = asyncio.run(create_request())
record_created = create_log['recordIds'][0]

# uses new generated id to update the collection
collections_with_data[0]['id'] = record_created
update_log = asyncio.run(update_request())

delete_log = asyncio.run(delete_request(record_created))

# get the updated collection to verify is the update is already published
collection_log = asyncio.run(get_request(record_created))

print(create_log)
print(update_log)
print(collection_log)
print(delete_log)
