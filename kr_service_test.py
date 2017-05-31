#coding=utf-8
from SMSApiSDK.sms_service_KRService import *

from SMSApiSDK.ApiSDKJsonClient import *

if __name__ == "__main__":
    try:
        print("###########################test kr_service begin.#################################")
        service = sms_service_KRService();
        
        #getFilePath
        response = service.getFilePath({"fileId":"ea4468779865b8959110ac89d97b20fa"});
        printJsonResponse(response)

        #getFileStatus
        response = service.getFileStatus({"fileId":"ea4468779865b8959110ac89d97b20fa"});
        printJsonResponse(response)

        #getKRCustom
        response = service.getKRCustom({"idType":3,"id":67633301});
        printJsonResponse(response)

        #getKRByQuery
        response = service.getKRByQuery({"queryType":1,"query":"flower"});
        printJsonResponse(response)

        #getEstimatedDataByBid
        response = service.getEstimatedDataByBid({"words":[{"word":"flower","bid":50.0}]});
        printJsonResponse(response)

        #getEstimatedData
        response = service.getEstimatedData({"words":[{"word":"flower","bid":50.0}]});
        printJsonResponse(response)

        #getKRFileIdByWords
        response = service.getKRFileIdByWords({"seedWords":["nice"]});
        printJsonResponse(response)
        
        
        print("###########################test kr_service end.#################################")
    except Exception, e:
        print e
        tb.print_exc()

