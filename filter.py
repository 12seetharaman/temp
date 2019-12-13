from data import check_application_name

def get_details_by_env(app_details: dict, env_name: str, key_name: str, inc_global: bool = False) -> list:
    values = []
    for each_item in app_details['applicationValues']:
        if check_application_name(each_item['applicationName'], env_name.lower(), key_name):
            values.append(each_item)
    if inc_global:
        values.append(app_details['globalValue'])
    print(values)
    return values
