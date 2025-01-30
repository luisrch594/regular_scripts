"""
Author: Luis Rodriguez Chaves
Beggining date: 30-1-25

This is based on something I worked before at Softtek.

In there we used a base class called Endpoint, which inherited it's behaviour to all the endpoints below. Those endpoints were used to access 
an API used for accessing a ton of information in kubernetes VMs
Python version used: 3.13


Version: 1.0
"""
import requests

class SessionManager():

    def __init__(self,url,user="",password="",auth_method="",timeout=10):
        self.url=url
        self.user=user
        self.password=password
        self.auth_method=auth_method
        self.session_=requests.Session()
        self.timeout=timeout
        
    def __str__(self):
        return f"user: {self.user}\npassword: {self.password}"
    
    def try_connection(http_method):
        def wrapper(self,*arg, **kw):
            try:
                return http_method(self,*arg, **kw)
            except requests.exceptions.HTTPError as errh:
                return errh
            except requests.exceptions.ReadTimeout as errrt:
                return errrt
            except requests.exceptions.MissingSchema as errmiss: 
                return errmiss
            except requests.exceptions.ConnectionError as conerr: 
                return conerr
            except requests.exceptions.RequestException as errex:
                return errex
            except Exception as e:
                return e
        return wrapper

    @try_connection
    def get(self):
        response=self.session_.get(url=self.url,timeout=self.timeout)
        return {response.status_code,response.text}
    
session_manager=SessionManager(url='https://jsonplaceholder.typicode.com/todo/1',user="usuario",password="password")
print(session_manager.get())