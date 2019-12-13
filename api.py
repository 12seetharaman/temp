import requests
from requests_ntlm import HttpNtlmAuth
import json
from data import get_value_field
from util import get_current_time

def get_env_details(key_name: str, env_name: str, prod_or_pesudo: str) -> str:
    
    #(TODO): Update key id with respective id value
    key_ids = {
        'AffiliateId': 'f30babe0-800a-468c-b500-64a0f0ceb488',
        'ChannelName': '1a33a2dc-b551-42eb-9f73-66585aba6d63',
        'ContentServiceEndpoint': 'f9f7d1d8-4b67-42ce-8455-8f578c9203cc',
        'LocalizationService': '3ac17112-7cdc-452c-a0ff-71149c1100fd',
        'PaymentService': 'dd6c74b8-411c-4b55-95eb-a41f09914a03',
        'SalesChannelManagementService': 'c08cca18-ca24-43fe-b6ed-efafc53c5e43',
        'BaseUrl': 'b43e60eb-c025-46cc-9c49-87a46d532c01',
        'Mercury-RedirectUrl': '3064242b-c622-46d7-8ed7-ccea70f01c3e',
        'MyPlan-RedirectUrl': '442ecf5a-1b4e-4f67-9333-f0c638757032'
    }

    key_id = key_ids[key_name]

    if env_name in ['QA2', 'QA4', 'QA12']:
        env_link = 'https://admin.qa'
    elif env_name == "PROD_TEST":
        env_link = 'https://prodtest.admin.int'
    else:
        env_link = "https://admin." + env_name.lower()

    get_request_link = "https://admin." + \
        str(env_link) + ".xfinity.com/configAdmin/api/items/" + \
        str(key_id) + "/values"

    #(TODO) app_details = get api call content.content (get api call with get_request_link)
    response=requests.get(str(env_link) + ".xfinity.com/configAdmin/api/items/" + str(key_id) + "/values", auth=HttpNtlmAuth('cable\\pramac003c','2019#oct'))
    # https://prodtest.admin.
    #(TODO) app_details = get api call content.content (get api call with get_request_link)
    print(response)

    detail = response.content
    #print(detail)
    #app_details=detail
    app_details= json.loads(detail)
    #print(app_details)
    return app_details, key_name

def update_with_post(app_ids_to_post: list, env_name: str, key_name: str, prod_or_pesudo: str) -> list:

    env_link = ''
    if env_name.upper() in ['QA2', 'QA4', 'QA12']:
        env_link = 'qa'
    else:
        env_link = env_name.lower()

    value_link = get_value_field(key_name, prod_or_pesudo)

    results = []

"""
    for each_app_id in app_ids_to_post:
        data = each_app_id 
        #Load dictionary from json if not dict
        data['value'] = value_link
        data['modifyDate'] = get_current_time()

        post_link = "https://admin." + env_link + ".xfinity.com/configAdmin/api/items/" \
                    + data['configurationItemId'] + '/values/' + data['id']

        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        login_info = HttpNtlmAuth('cable\\pramac003c','2019#oct')
        response = requests.put(post_link, auth=login_info, data=json.dumps(data), headers=headers)
        
        results.append(str(response.status_code) + ' : ' + str(response.text))
    print(results)
    return results
"""
   

