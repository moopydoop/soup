import os
import requests



# requests.post(url, data)

URL = "https://sentry.io/api/0/projects/meredith/soup/codeowners/"

def get_file():
    with open('./.github/CODEOWNERS', 'rt') as f:
        print("hello")
        data = f.read()
    print(data)
    # f.close()
    return (data, f)

def upload_file(file_data, f):
    token = os.environ.get("SENTRY_AUTH_TOKEN")
    code_mapping_id = os.environ.get("SENTRY_CODE_MAPPING_ID")
    headers = {"Authentication": f"Bearer {token}"}
    data = {
        "codeMappingId": code_mapping_id,
        "raw": file_data,
    }
    try:
        resp = requests.post(URL, headers=headers, data=data)
        resp.raise_for_status()
    except Exception as e:
        print(code_mapping_id)
        print(f"something happened {str(e)}")

    print(resp.status_code)
    f.close()


file_data, f = get_file()
upload_file(file_data, f)