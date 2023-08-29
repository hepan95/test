import requests,json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def test_Added0117( hz_id="4d16a4af1ff64e9aa854e54db9e2d5f7", customerDelegateCode="20230829102835"):  # 客户委托号
    url = "https://ict-uat.cloudlinkscm.com/api/platform/receiveOrderPort/list"
    headers = {'Content-Type': 'application/json',
               'Cookie': 'token={}'.format("68bd5d4d-d11b-4433-9930-3407109b668c:7a8ac917-bd3a-4218-9aa1-66441f8ee37d")}
    data = {"itemFrom": 0, "itemTo": 10,
            "filter": {"customerDelegateCode": customerDelegateCode, "customerId": hz_id, "tagKey": "all",
                       "taskUnitCodeType": "container"}}
    A = requests.request("POST", url, headers=headers, data=json.dumps(data), verify=False)
    returnMsg = A.json()["returnMsg"]
    print(A.json())
    data1 = A.json()["result"]["data"]
    # print(data1)
test_Added0117()