import requests


def main():
    url = "https://platform-qa.staging.kuaishou.com/ksauto/hongmei"
    data = {
        "platform": "ios",
        "sdk_name": "poi_sdk",
        "mr_link": "000",
        "coverage_threshold": "97.66%",
        "case_success_rate": "777",
        "success": "1"
    }
    response = requests.post(url, json=data)
    return response.text


res = main()
print(res)