import logging

from config import BASE_HOST


class OpenAccountApi(object):
    def __init__(self,ses):
        self.ses =ses


    def realname(self,real_name,card_id):
        '''
        实名认证
        :param real_name:
        :param card_id:
        :return:
        '''
        form_dict={'realname': real_name,
         'card_id ': card_id}
        url =BASE_HOST+"/member/realname/approverealname"
        req =self.ses.post(url =url,data=form_dict,files={"a":"b"})
        logging.info(f"实名认证的信息{req.json()}")
        return req

    def open_account(self):
        '''
        开户操作
        :return:
        '''
        url =BASE_HOST+"/trust/trust/register"
        req =self.ses.post(url =url)
        logging.info(f"实名认证的信息{req.json()}")
        return req

    def thrid_open_account(self,url,form_dict):
        '''
        第三方开户
        :param url:
        :param form_dict:
        :return:
        '''
        req = self.ses.post(url=url,data=form_dict)
        logging.info(f"实名认证的信息{req.text}")
        return req





