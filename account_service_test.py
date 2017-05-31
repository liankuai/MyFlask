#coding=utf-8
from SMSApiSDK.sms_service_AccountService import *

from SMSApiSDK.ApiSDKJsonClient import *


if __name__ == "__main__":
    try:
        print("###########################test account_service begin.#################################")
        service = sms_service_AccountService()
        response = service.getAccountInfo({"accountFields":["userId", "cost"]})
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        data=response["body"]["data"][0];        print(data)
        data["budget"]=88
        
        response=service.updateAccountInfo({"accountInfo":data})
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        print(data)
        print ("###########################test account_service end.#################################")
    except Exception, e:
        print e

        tb.print_exc()


