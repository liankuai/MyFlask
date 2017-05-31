#coding=utf-8
from SMSApiSDK.ApiSDKJsonClient import *

from SMSApiSDK.sms_service_ReportService import *

if __name__ == "__main__":
    try:
        print("###########################test report_service begin.#################################")
        service=sms_service_ReportService()
        #getRealTimeData
        response=service.getRealTimeData({"realTimeRequestType":{"performanceData":["impression","click","cost","cpc","ctr","cpm","conversion"],"levelOfDetails":2,"startDate":"2016-08-31 12:00:00","endDate":"2016-09-01 10:00:00","unitOfTime":1,"reportType":2}})
        printJsonResponse(response)
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)

        #getRealTimeQueryData
        response=service.getRealTimeQueryData({"realTimeQueryRequestType":{"performanceData":["impression","click"],"levelOfDetails":7,"startDate":"2016-08-31 12:00:00","endDate":"2016-09-01 10:00:00","unitOfTime":5,"reportType":6}});
        printJsonResponse(response)
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)

        #getRealTimePairData
        response=service.getRealTimePairData({"realTimePairRequestType":{"performanceData":["impression","click"],"levelOfDetails":12,"startDate":"2016-08-31 12:00:00","endDate":"2016-09-01 10:00:00","unitOfTime":5,"reportType":15}})
        printJsonResponse(response)
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)

        #getProfessionalReportId
        response=service.getProfessionalReportId({"reportRequestType":{"performanceData":["impression","click","cost","cpc","ctr","cpm","conversion"],"levelOfDetails":2,"startDate":"2016-08-20 12:00:00","endDate":"2016-08-31 12:00:00","unitOfTime":1,"reportType":2}})
        printJsonResponse(response)

        #getReportState
        response=service.getReportState({"reportId":"f61202ebad335c46832e5a158ea4905a"})
        printJsonResponse(response)
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        #getReportFileUrl
        response=service.getReportFileUrl({"reportId":"f61202ebad335c46832e5a158ea4905a"})
        printJsonResponse(response)
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        
        
        print("###########################test report_service end.#################################")
    except Exception, e:
        print e
        tb.print_exc()

