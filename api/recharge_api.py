import logging

from config import BASE_HOST


class RechargeApi(object):
    def __init__(self,ses):
        self.ses =ses

    def recharge_verify(self,r):
        url =BASE_HOST+f"/common/public/verifycode/{r}"
        req=self.ses.get(url=url)
        logging.info(req)

        return req

    def recharge(self,amount,vailcoade,paymentType="chinapnrTrust",formStr="reForm"):
        url =BASE_HOST+"/trust/trust/recharge"
        form_dict={"paymentType": paymentType,
         "amount": amount,
         "formStr": formStr,
         "valicode": vailcoade}
        req =self.ses.post(url=url,data=form_dict)
        logging.info(req)

        return req
    def third_recharge(self,url,form_dict):
        req=self.ses.post(url=url,data=form_dict)
        logging.info(req.text)
        return req




