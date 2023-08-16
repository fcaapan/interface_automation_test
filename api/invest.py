import logging

from config import BASE_HOST


class Invest(object):
    def __init__(self,ses):
        self.ses =ses

    def invest(self,id,amount,depositCertificate=-1):
        url =BASE_HOST+"/trust/trust/tender"
        form_data ={"id":642,"depositCertificate":depositCertificate,"amount":amount}
        req =self.ses.post(url =url,data=form_data)
        logging.info(f"投资返回的数据是{req.json()}")
        return req
    def third_invest(self,url,for_data):
        req =self.ses.post(url=url,data=for_data)
        return req



