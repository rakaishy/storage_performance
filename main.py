import requests
import json
from requests.structures import CaseInsensitiveDict
import asyncio

url = "https://eu5.api.enterprisedata.slb.com/api/storage/v2/records"

headers = CaseInsensitiveDict()
headers["accept"] = "application/json"
headers["data-partition-id"] = "sandbox-weu-des-prod-testing-e"
headers[
    "Authorization"] = "Bearer eyJ0eXAiOiAiSldUIiwgImFsZyI6ICJSUzI1NiIsICJraWQiOiAiTVRZMU5qVTFORFF3T0E9PSJ9.eyJpYXQiOiAxNjU2NjEwMDU5LCAiZXhwIjogMTY1NjYxMzY1OSwgImlzcyI6ICJodHRwczovL2NzaS5zbGIuY29tL3YyIiwgImF1ZCI6IFsiZGlnaXRhbHJlc3ZjLWRpZ2l0YWxyZS5zbGJzZXJ2aWNlLmNvbSIsICI0NTU1NzE3NmMwMTU0Mzk5OTljZDI0NTQ2MTM1NGU5NiIsICJjY20tdXNlci1jb250ZXh0LWNmc3NlcnZpY2Uuc2xic2VydmljZS5jb20iLCAiNzY2MDVmYTQ1MWM3NGU0YWI0M2FjNjY0MTFjMDhmMDUiLCAic2VydmljZS1pZGVudGl0eS1leHBsb3JlcGxhbi5zbGJzZXJ2aWNlLmNvbSIsICJkYXRhLWFuYWx5dGljcy1jZHMuc2xic2VydmljZS5jb20iLCAiYTYyNjMyODMxMzk0NDYwMWJhMjZjZDFmZmJhZjZhNTMiLCAiZWRhMzM4ZDhhNDgyNDNmNzhhNWIzMTI2YTk2ODQxMzMiLCAiZGU2OTFiNDhlNjQ2NGRhZDk3MjQxNDE0MzRjMzg5MGIiLCAiOTYzZjJjYzY5MTVlNDc5ZmEwZmNiNzNlYzJlYzkwZTciLCAic2VydmljZS1lZXN5LnNsYnNlcnZpY2UuY29tIiwgImRlLXNhdXRoLXYyLXNjb3BlLXNlcnZpY2UtZGF0YWxha2Uuc2xic2VydmljZS5jb20iLCAicHJvZC1uYW0tc2VydmljZXMtZmRwbGFuLnNsYnNlcnZpY2UuY29tIiwgInByb2QtZXUtc2VydmljZXMtZmRwbGFuLnNsYnNlcnZpY2UuY29tIiwgInNlcnZpY2UtcGV0cmVsc3RvcmFnZS5zbGJzZXJ2aWNlLmNvbSIsICIzNTIyY2U0OTQyZTQ0ZGRkOTM3OThlNTQ5ZDgzZjcxMyIsICIxNDFlZWNkM2NmNDk0YTdiYThlNTY0NTczODI3YzFhOCIsICIxYzMxMzliNjY0MTg0YTA4YTI5MWVjMmUxOWY5YTlhMyIsICJmd2stZHJpbGxwbGFuLnNsYnNlcnZpY2UuY29tIiwgInByb2R1Y3Rpb24tZGF0YS1mb3VuZGF0aW9uLXByb2QtZ2xvYmFsLWNsaWVudC1pZCIsICJlZGYxN2QxZjhjYzM0NjFkOGJhM2YxYTk4Y2U3YmUxYiJdLCAic3ViIjogImFndWVycmVybzI1QHNsYi5jb20iLCAiZW1haWwiOiAiYWd1ZXJyZXJvMjVAc2xiLmNvbSIsICJkZXNpZCI6ICJhZ3VlcnJlcm8yNS1zbGItY29tLTkyYmUwYjQwQGRlc2lkLmRlbGZpLnNsYi5jb20iLCAic3ViaWQiOiAieW43RkN4SUdXR2g1MGtsbVowZXMwckFnTzJZWjgyaVhFSlJrT3BHUlplOCIsICJhenAiOiAibGl2ZS1kZXZwb3J0YWwtYXBpZ2VlZGV2cG9ydGFsLnNsYmFwcC5jb20iLCAianRpIjogImF0LmE1MmQwOGEzMzE5ODRmZjRhMGVmZWNhZGFiNWFkNGVmIiwgIm9pZCI6ICIxOWRlZmY1Ny1jMjZhLTQ2ZDAtOTYwZS1kNjQ2NDVhZDU2OTgiLCAidGlkIjogIjQxZmYyNmRjLTI1MGYtNGIxMy04OTgxLTczOWJlODYxMGMyMSJ9.GLD1FGgfdx0I99HwrlXmTUgxwUkB8sKTpmMFfLXyvGdA7iE41VU-YPu6JCIkrykneULq4o4uWCpBzwXtkFsILubRjCW7GhuCwA33Q42qH3BH7467NonC8t2L0VrhpvzKOUk-G2lmh_muuaVJaTlP19AedWfuMzFF9FWFGukYI1mF6wzJDfYs5kNApac_oaqEhJs-sin9rymyI6Fn8O58qTiSShXerq6og3g6vpLCUmcpgHmrdm6NLvUmrbiPNk8WibFReMZwlYMiTuMM_b71rVfABRAXdO-s4SNu7Bqb8lPdV9ScdNcW3cYXDbdEPShoZ4_2RKRkpkqO_wHcciWjZQ"
headers["Content-Type"] = "application/json"

with open('resources/base_collections_request') as base_collections:
    collections_no_data = json.load(base_collections)

with open('resources/updated_collections_request.json') as filled_collections:
    collections_with_data = json.load(filled_collections)


async def create_request():
    create = requests.put(url, headers=headers, json=collections_no_data)
    return json.loads(create.text)


async def update_request():
    update = requests.put(url, headers=headers, json=collections_with_data)
    return json.loads(update.text)


create_log = asyncio.run(create_request())

collections_with_data[0]['id'] = create_log['recordIds'][0]
update_log = asyncio.run(update_request())

print(create_log)
print(update_log)