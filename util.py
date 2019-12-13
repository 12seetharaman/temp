from datetime import datetime
from data import get_value_field

def get_current_time():
    time_now = str(datetime.utcnow()).split('.')
    time_now[1] = time_now[1][:3]
    return '.'.join(time_now).replace(' ', 'T')

def check_endpoint(details: list, key_name: str) -> str:
    zero_indx = details.pop(0)
    if zero_indx['value'][-1] !=  '/':
        zero_indx['value'] = zero_indx['value'] + '/'

    if get_value_field(key_name, 'PROD') == zero_indx['value']:
        first_endpoint = 'PROD'
    elif get_value_field(key_name, 'PESUDO') == zero_indx['value']:
        first_endpoint = 'PESUDO'
    else:
        raise Exception(KeyError, 'Error')
       
    for each_item in details:
        if each_item['value'][-1] !=  '/':
            each_item['value'] = each_item['value'] + '/'
        if get_value_field(key_name, first_endpoint) != each_item['value']:
            return 'MIXED'
    return first_endpoint