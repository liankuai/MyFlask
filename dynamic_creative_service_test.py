#coding=utf-8
import random
import string

from SMSApiSDK.sms_service_DynamicCreativeService import *

from SMSApiSDK.ApiSDKJsonClient import *

SUCCESS = "success";
IDTYPE = 13;
CAMPAIGNID=66779620L;
ADGROUPID=2028594121L;
URL = "https://www.baidu.com";
def random_name():
    return string.join(random.sample(['a','b','c','d','e','f','g','h','i','j','k','l','m','n'], 12)).replace(" ","");
def parse_ids(datas):
    ids=[]
    for data in datas:
        ids.append(data["dynCreativeId"])
    return ids
if __name__ == "__main__":
    try:
        print("###########################test dynamic_creative_service begin.#################################")
        r_name=random_name()
        service =sms_service_DynamicCreativeService()
        #addDynCreative
        #add_data={"campaignId":CAMPAIGNID,"bindingType":3,"dynCreativeFragments":[{"title":random_name(),'url':URL,'murl':URL}]};
        add_data={"dynCreativeTypes":[{"campaignId":CAMPAIGNID,"adgroupId":ADGROUPID,"bindingType":3,"title":random_name(),'url':URL,'murl':URL}]}
        response = service.addDynCreative(add_data);
        printJsonResponse(response)
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        datas=response["body"]["data"]
        #getDynCreative
        ids=parse_ids(datas)
        response=service.getDynCreative({"dynCreativeFields":["dynCreativeId", "campaignId", "adgroupId", "bindingType", "bindingType","url","murl"],"idType":IDTYPE,"ids":ids}) 
        printJsonResponse(response)
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        datas=response["body"]["data"]
        #updateDynCreative
        for data in datas:
            data["title"]=random_name()
        response=service.updateDynCreative({"dynCreativeTypes":datas})
        printJsonResponse(response)
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        #deleteDynCreative
        ids=parse_ids(datas)
        response=service.deleteDynCreative({"dynCreativeIds":ids})
        printJsonResponse(response)
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        #printJsonResponse(response)
        print("###########################test dynamic_creative_service end.#################################")
    except Exception, e:
        print e
        tb.print_exc()

