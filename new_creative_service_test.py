#coding=utf-8
import random
import string

from SMSApiSDK.sms_service_NewCreativeService import *

from SMSApiSDK.ApiSDKJsonClient import *

BEAN_COUNT_INNER = 1;
SUBLINKINFO_COUNT = 3;
SUCCESS = "success";
ADGROUPID =2034621703;
IDTYPE = 12;
IDTYPE_ADGROUP = 5;
PHONE_ID_TYPE = 9;
BRIDGE_ID_TYPE = 5;
ISTMP = 0;
ECALLGROUPID=1395
ECALL_ID_TYPE=23
URL = "https://www.baidu.com";
def random_name():
    return string.join(random.sample(['a','b','c','d','e','f','g','h','i','j','k','l','m','n'], 12)).replace(" ","");
def parse_ids(datas):
    ids=[]
    for data in datas:
        ids.append(data["sublinkId"])
    return ids
def parse_phone_ids(datas):
    ids=[]
    for data in datas:
        ids.append(data["phoneId"])
    return ids
def parse_bridge_ids(datas):
    ids=[]
    for data in datas:
        ids.append(data["bridgeId"])
    return ids
def parse_ecall_ids(datas):
    ids=[]
    for data in datas:
        ids.append(data["ecallId"])
    return ids
if __name__ == "__main__":
    try:
        print("###########################test new_creative_service begin.#################################")
        r_name=random_name()
        service =sms_service_NewCreativeService()
        #addSublink
        add_data={"sublinkTypes":[{"sublinkInfos":[],"adgroupId":ADGROUPID,"device":0}]};
        for i in range(SUBLINKINFO_COUNT):
            add_data["sublinkTypes"][0]["sublinkInfos"].append({"description":random_name(),"destinationUrl":URL})
        response = service.addSublink(add_data);
        print response
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        datas=response["body"]["data"]
        #getSublink
        ids=parse_ids(datas)
        response=service.getSublink({"sublinkFields":["adgroupId", "sublinkInfos", "sublinkId"],"idType":IDTYPE,"ids":ids,"getTemp":ISTMP,"device":0})
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        datas=response["body"]["data"]
        #updateSublink
        for data in datas:
            for info in data["sublinkInfos"]:
                info["description"]=random_name()
        response=service.updateSublink({"sublinkTypes":datas})
        printJsonResponse(response)
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        #deleteSublink
        ids=parse_ids(datas)
        response=service.deleteSublink({"sublinkIds":ids})
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        #printJsonResponse(response)


        #addPhone
        phone_data={"phoneTypes":[{"phoneNum":"010-50817103","adgroupId":ADGROUPID}]}
        response=service.addPhone(phone_data)
        print response
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        datas=response["body"]["data"]
        #getPhone
        ids=parse_phone_ids(datas)
        response=service.getPhone({"ids":ids,"idType":9,"phoneFields":["phoneId","phoneNum","adgroupId","pause","status"]})
        print response
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        datas=response["body"]["data"]
        #updatePhone
        for data in datas:
            data["phoneNum"]="010-67896543"
        response=service.updatePhone({"phoneTypes":datas})
        print response
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)

        #addBridge
        bridge_data={"bridgeTypes": [{"adgroupId": ADGROUPID,"pause":"true"}]}
        response=service.addBridge(bridge_data)
        print response
       # assert(response["header"]["desc"]=="failures" and response["header"]["status"]==2)
        datas=response["body"]["data"]
        #getBridge
        ids=parse_bridge_ids(datas)
        response=service.getBridge({"ids":ids,"idType":10,"bridgeFields":["bridgeId","adgroupId","pause","status"]})
        print response
       # assert(response["header"]["desc"]=="failures" and response["header"]["status"]==2)
        datas=response["body"]["data"]
        #updateBridge
        response=service.updateBridge({"bridgeTypes":datas})
        print response
       # assert(response["header"]["desc"]=="failures" and response["header"]["status"]==2)

        #getEcallGroup
        response=service.getEcallGroup()
        printJsonResponse(response)
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        #addEcall
        ecall_data={"ecallTypes":[{"adgroupId":ADGROUPID,"ecallGroupId":ECALLGROUPID}]}
        response=service.addEcall(ecall_data)
        printJsonResponse(response)
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        #getEcall
        datas=response["body"]["data"]
        ids=parse_ecall_ids(datas)
        response=service.getEcall({"ids":ids,"idType":ECALL_ID_TYPE,"ecallFields":["ecallId","ecallGroupName"]})
        printJsonResponse(response)
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        #updateEcall
        datas=response["body"]["data"]
        response=service.updateEcall({"ecallTypes":datas})
        printJsonResponse(response)
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        print("###########################test new_creative_service end.#################################")
    except Exception, e:
        print e
        tb.print_exc()

