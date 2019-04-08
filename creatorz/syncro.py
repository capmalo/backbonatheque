import requests
import logging
from django.db import models
from django.urls import reverse

logger = logging.getLogger()
server_url = "http://localhost:8000"
was_timeout = False
errorcpt = 0
prev_errorcpt = 0

class syncro():
    def check_sync():
        """for data in error_database:
            print(data)"""
    def restart_sync():
        remote_url = server_url + reverse("major-playback-list")
        #resend previous data, if ok, delete from cache:
        #for data in error_database:
            send_data(remote_url, data)
	    if was_timeout == False and prev_errorcpt == errorcpt:
                #error_database.delete(data)
            else:
                prev_errorcpt = errorcpt
			
    def send_data(remote_url, data):
        try:
            response = requests.post(remote_url, json=data.serialize(), timeout=1)
            if response.status_code != 201:
                logger.exception("Error occured")
                error_handling(response.status_code, data)
            was_timeout = False
        except Exception as e:
            logger.exception("Timeout occured")
            timeout_handling(data)	
			
    def error_handling(error, data):
        errorcpt += 1
        #error_database.add(error)
        #error_database.add(data)

    def timeout_handling(data):
        was_timeout = True
        #error_database.add(data)
        
        
