#coding=utf-8
import random
import string

from SMSApiSDK.sms_service_CreativeService import *

from SMSApiSDK.ApiSDKJsonClient import *

BEAN_COUNT = 2;
SUCCESS = "success";
ADGROUPID = 2028594121L;
IDTYPE = 7;
ISTMP = 0;
DESC1 = "add_creative_by_requelqi";
MODIFY_DESC1 = "modify_creative_by_requelqi";
URL = "https://www.baidu.com";
def random_name():
    return string.join(random.sample(['a','b','c','d','e','f','g','h','i','j','k','l','m','n'], 12)).replace(" ","");
def parse_ids(datas):
    ids=[]
    for data in datas:
        ids.append(data["creativeId"])
    return ids
if __name__ == "__main__":
    try:
        print("###########################test creative_service begin.#################################")
        r_name=random_name()
        service =sms_service_CreativeService()
        #addCreative
        response = service.addCreative({"creativeTypes":[{"title":r_name,"adgroupId":ADGROUPID,"description1":DESC1,"pcDestinationUrl":URL}]})
        #assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        datas=response["body"]["data"]
        #getCreative
        ids=parse_ids(datas)
        response=service.getCreative({"creativeFields":["title", "creativeId", "description1", "pcDestinationUrl"],"idType":IDTYPE,"ids":ids,"getTemp":ISTMP}) 
        #assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        datas=response["body"]["data"]
        #updateCreative
        for data in datas:
            data["title"]=random_name()
            data["description1"]=MODIFY_DESC1
        response=service.updateCreative({"creativeTypes":datas})
        #assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        #deleteCreative
        ids=parse_ids(datas)
        response=service.deleteCreative({"creativeIds":ids})
        #assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        printJsonResponse(response)
        print("###########################test creative_service end.#################################")
    except Exception, e:
        print e
        tb.print_exc()

