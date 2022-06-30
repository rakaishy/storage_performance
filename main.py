import requests
import json
import datetime

url = 'https://eu5.api.enterprisedata.slb.com/api/storage/v2/records'
dataPartitionId = 'sandbox-weu-des-prod-testing-e'

body = [
    {
        "kind": "BASE_KIND",
        "version": 1562066009929332,
        "acl": {
            "owners": ['data.default.viewers@' + dataPartitionId + '.enterprisedata.slb.com'],
            "viewers": ['data.default.viewers@' + dataPartitionId + '.enterprisedata.slb.com']
        },
        "legal": {
            "legaltags": [dataPartitionId + '-default-legal'],
            "otherRelevantDataCountries": ['US'],
            "status": 'compliant'
        },
        "createTime": datetime.datetime.now(),
        "createUser": 'aguerrero25@slb.com',
        "modifyTime": datetime.datetime.now(),
        "modifyUser": 'aguerrero25@slb.com',
        "ancestry": {
            "parents": []
        },
        "meta": [],
        "data": {
            "Name": 'OSDU Performance Collection',
            "Description": 'Performance related collection',
            "CreationDateTime": '2020-02-13T09:13:15.55Z',
            "Tags": ['Example Tags'],
            "SubmitterName": 'Example SubmitterName',
            "BusinessActivities": ['Example BusinessActivities'],
            "AuthorIDs": ['Example AuthorIDs'],
            "MemberIDs": [],
            "PurposeID": 'namespace:reference-data--CollectionPurpose:Project:',
            "ParentCollectionID":
                'namespace:work-product-component--PersistedCollection:PersistedCollection-911bb71f-06ab-4deb-8e68-b8c9229dc76b:',
            "HomogeneousMemberKind": 'osdu:wks:work-product-component--SeismicHorizon',
            "Author": 'Example Author',
            "ExtensionProperties": {}
        }
    }
]

with open('resources/collections.json') as collections:
    collections_data = json.load(collections);


def create_request(data_partition_id):
    create = requests.put(url, data=body)


def update_request(data_partition_id):
    update = requests.put()


print(collections_data)
