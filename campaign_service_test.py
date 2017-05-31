#coding=utf-8
import random
import string

from SMSApiSDK.sms_service_CampaignService import *

from SMSApiSDK.ApiSDKJsonClient import *


def random_name():
    return string.join(random.sample(['a','b','c','d','e','f','g','h','i','j','k','l','m','n'], 12)).replace(" ","");
def parse_ids(datas):
    ids=[]
    for data in datas:
        ids.append(data["campaignId"])
    return ids
if __name__ == "__main__":
    try:
        print("###########################test campaign_service begin.#################################")
        r_name=random_name()
        service =sms_service_CampaignService()

        #addCampaign
        response = service.addCampaign({"campaignTypes":[{"campaignName":r_name}]})
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        datas=response["body"]["data"]

        #getCampagin
        ids=parse_ids(datas)
        response=service.getCampaign({"campaignFields":["campaignName", "campaignId"],"campaignIds":ids})
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        datas=response["body"]["data"]

        #updateCampaign
        for data in datas:
            data["campaignName"]=random_name()
        response=service.updateCampaign({"campaignTypes":datas})
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        datas=response["body"]["data"]

        #deleteCampaign
        ids=parse_ids(datas)
        response=service.deleteCampaign({"campaignIds":ids})
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        #printJsonResponse(response)
        print("###########################test campaign_service end.#################################")
    except Exception, e:
        print e
        tb.print_exc()

