#coding=utf-8
from SMSApiSDK.ApiSDKJsonClient import *

from SMSApiSDK.sms_service_BulkJobService import *

if __name__ == "__main__":
    try:
        print("###########################test bulkjob_service begin.#################################")
        service = sms_service_BulkJobService();
        #getAllObject
        response = service.getAllObjects({"accountFields":["all"],"campaignIds":[]})
        printJsonResponse(response)
        
        #getAllChangedObjects
        response = service.getAllChangedObjects({"accountFields":["all"],"campaignIds":[],"campaignFields":["all"],"startTime":"2016-08-01 12:00:00"})
        printJsonResponse(response)

        #cancelDownload
        response = service.cancelDownload({"fileId":"2942f4aaaf3776189651d4e3d23375f8"})
        printJsonResponse(response)

        #getFilePath
        response = service.getFilePath({"fileId":"2942f4aaaf3776189651d4e3d23375f8"})
        printJsonResponse(response)

        #getUserCache
        response = service.getUserCache({"fileId":"2942f4aaaf3776189651d4e3d23375f8"})
        printJsonResponse(response)

        #getChangedId
        response = service.getChangedId({"campaignLevel":"true","adgroupLevel":"true","keywordLevel":"true","startTime":"2016-08-31 12:00:00"})
        printJsonResponse(response)

        #getFileStatus
        response = service.getFileStatus({"fileId":"2942f4aaaf3776189651d4e3d23375f8"})
        printJsonResponse(response)

        #getChangedItemId
        response = service.getChangedItemId({"ids":[65991757],"itemType":5,"type":3,"startTime":"2016-08-01 12:00:00"})
        printJsonResponse(response)

        #getChangedScale
        response = service.getChangedScale({"changedCampaignScale":"true","changedAdgroupScale":"true","changedKeywordScale":"true","campaignIds" :[65991298],"startTime":"2016-08-01 12:00:00"})
        printJsonResponse(response)

        
        
        print("###########################test kr_service end.#################################")
    except Exception, e:
        print e
        tb.print_exc()

