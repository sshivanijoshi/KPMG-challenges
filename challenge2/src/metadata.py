import requests
import json

metadata_url = 'http://169.254.169.254/latest/'


def expand_jsontree(url, arr):
    result = {}
    for item in arr:
        new_url = url + item
        r = requests.get(new_url)
        text = r.text
        if item[-1] == "/":
            list_of_values = r.text.splitlines()
            result[item[:-1]] = expand_jsontree(new_url, list_of_values)
        elif is_valid_json(text):
            result[item] = json.loads(text)
        else:
            result[item] = text
    return result


def metadata():
    path = ["meta-data/"]
    result = expand_jsontree(metadata_url, path)
    return result


def metadata_json():
    metadata = metadata()
    metadata_json = json.dumps(metadata, indent=4, sort_keys=True)
    return metadata_json


def is_valid_json(json):
    try:
        json.loads(json)
    except ValueError:
        return False
    return True


if __name__ == '__main__':
    print(get_metadata_json())