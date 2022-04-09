from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *
from pywebio.platform.flask import webio_view
from flask import Flask, Blueprint , render_template , request ,redirect, url_for

import json
import requests
import requests,os,mechanize,random,json,time
import requests,secrets
from user_agent import generate_user_agent

code_ads = "<iframe data-aa='1971867' src='//ad.a-ads.com/1971867?size=728x90' style='width:728px; height:90px; border:0px; padding:0; overflow:hidden; background-color: transparent;'></iframe>"
def emailtwitter(email):
    urw='https://mobile.twitter.com/i/flow/password_reset'
    r = requests.Session()
    url = "https://api.twitter.com/i/users/email_available.json?email="+email
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    Host = "api.twitter.com"
    Accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    r.headers = {'User-Agent': user_agent}
    r.headers = {'Host': Host}
    r.headers = {'Accept': Accept}
    req = r.get(url).json()
    text = str(req)
    if text.find("'valid': False") == True:
        return True
    else:
        return False

def emailinstagram(email):
    url = 'https://www.instagram.com/accounts/login/ajax/'
    heade = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en,ar;q=0.9,en-US;q=0.8,vi;q=0.7',
    'content-length': '313',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'missing',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84',
    'x-asbd-id': '198387',
    'x-csrftoken': 'HpoO4isqbCMK5a6fl9CRofLsuxpwGavJ',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR2_82ibn8D_4DzDUg2jml85Kj9ruPEQVg0mDDRCksQ3pOav',
    'x-instagram-ajax': 'd26a8ffbcd2b',
    'x-requested-with': 'XMLHttpRequest',}
    tim = str(time.time()).split('.')[1]
    data = {
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:diwddeoded',
    'username': email,
    'queryParams': '{}',
    'optIntoOneTap': 'false',
    'trustedDeviceRecords': '{}',}
    ree = requests.post(url, headers=heade, data=data).json()["user"]
    if ree:
        return True
    else:
        return False

def emailmailru(email):
    headers_6 = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    url = 'https://account.mail.ru/api/v1/user/exists'
    data_6 = {'email': email}
    js = requests.post(url, data=data_6, headers=headers_6)
    if js.json()['body']['exists'] == False:
        return True
    else:
        return False

def emailhotmail(email):
    url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + email + "&_=1604288577990"
    data = ''
    headers = {
		"Accept": "*/*",
		"Content-Type": "application/x-www-form-urlencoded",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
		"Connection": "close",
		"Host": "odc.officeapps.live.com",
		"Accept-Encoding": "gzip, deflate",
		"Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
		"Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
		"canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
		"uaid": "d06e1498e7ed4def9078bd46883f187b",
		"Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
    html = requests.get(url, data=data, headers=headers).text
    if 'Neither' in html:
        return True
    else:
        return False
def emailtiktok(email):
    url = "https://api2-t2.musical.ly/aweme/v1/passport/find-password-via-email/?version_code=7.6.0&language=ar&app_name=musical_ly&vid=43647C38-9344-40A3-AD8E-29F6C7B987E4&app_version=7.6.0&is_my_cn=0&channel=App%20Store&mcc_mnc=&device_id=6999590732555060741&tz_offset=10800&account_region=&sys_region=SA&aid=1233&screen_width=1242&openudid=a0594f8115e0a1a51e1a31490aeef9afc2409ff4&os_api=18&ac=WIFI&os_version=12.5.4&app_language=ar&tz_name=Asia/Riyadh&device_platform=iphone&build_number=76001&iid=7021194671750481669&device_type=iPhone7,1&idfa=20DB6089-D1C6-49EF-8943-9C310C8F1B5D&mas=002ed4fcfe1207217efade4142d0b05e0c845e118f07206205d6a8&as=a11664d78a2e110bd08018&ts=16347494182"
    headers = {
    'Host': 'api2-t2.musical.ly',
    'Cookie': 'store-country-code=sa; store-idc=alisg; install_id=7021194671750481669; odin_tt=7b67a77e780e497b1c89d483072f567580c860fe622a9ad519c8af998a287f424ed5f97297928981fa70ca6e8cb2648ebc46af23c9c9588a540567c77f877d307588080b16d8b92d3c3f875da9cd2291; ttreq=1$ee9fd401f276e956ba82d3ffd7392ffa6829472d',
    'Accept': '*/*',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Musically/7.6.0 (iPhone; iOS 12.5.4; Scale/3.00)',
    'Accept-Language': 'ar-SA;q=1',
    'Content-Length': '25',
    'Connection': 'close'}
    data = {
    "email":email, }
    req = requests.post(url,headers=headers,data=data)
    if "Sent successfully" in req.text:
        return True
    else:
        return False


def emailyahoo(email):
    if not "@" in str(email):
        return False
    else:
        em = str(email.split("@")[0])
        if len(em) < 3:
            return False
    eml=str(email)
    email=eml.split('@')[0]
    url = 'https://login.yahoo.com/account/module/create?validateField=yid'
    headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '17973',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'APID=UP139a7583-ebf0-11eb-b505-06ebe7a65878; B=1gu92j5gg4sv7&b=3&s=64; A1=d=AQABBCoF-2ACEDfMWHRNdZQ9oaAHUO4YHqMFEgEBAQFW_GAEYQAAAAAA_eMAAAcI53MCYZkieRg&S=AQAAAuJmx1yIDVMiY71k2AGooYk; A3=d=AQABBCoF-2ACEDfMWHRNdZQ9oaAHUO4YHqMFEgEBAQFW_GAEYQAAAAAA_eMAAAcI53MCYZkieRg&S=AQAAAuJmx1yIDVMiY71k2AGooYk; GUC=AQEBAQFg_FZhBEIc3QQ6; cmp=t=1627550703&j=0; APIDTS=1627550737; A1S=d=AQABBCoF-2ACEDfMWHRNdZQ9oaAHUO4YHqMFEgEBAQFW_GAEYQAAAAAA_eMAAAcI53MCYZkieRg&S=AQAAAuJmx1yIDVMiY71k2AGooYk&j=WORLD; AS=v=1&s=9z9sgq95&d=A6103d241|eavlddr.2Sqtm1snR4vumZPgWEv2CX8ETv8qsCVpXUOAi6BcDaqYAawFRdXZOH3x1ZhIOOPANiSybHZ1j1IBJfKp_yUQeVT2a7U2iFeceXk3DV8Yf6fdA4Mb3M_1A3WY2rpfLpkN2geA1AHRb_QuK0p_gvRBC25hCJqX6_BqNWBCQZ40y2vcTOUrMHZQRGCPbygJ4jCC1pmj16D_TNVaFo68GkkgrxHiFpLQEP9zBsfEM9g8FM8Qd3Gs8oJHQRyvyel09x3uEdniEFCXR93nRCcOMMKCI7xvW239gVcz1Gs_5hmZv6aql00Zge0HJaK6YKPDg9Q7rFfMe7pJry4gCuNMiq_bH9TeBHQEGjqLCJR_d8hcSFHxUnNah4D8.hwV7o1hyYUKQl2Pw6aVKPizRyscmuz0Rwa1LUKGV0O2ls2MSsR4g4TzVlLObvUuKBdrdIJJD3Em1NsNsXKj3uyr.XgZV3E09rJQbldIcePNMPkT7jJjydoGuIBVbqutW0MgHN5IShbRcy6cVifEmil4551or5xaGO5kNpIDCbjUmhD8.MnIfBGRlSIITVGGoQhj3l5TBA742dFc_zcZJmtF5XIrHTr_wMpbpc3ZzD1SgWTDMvySFcsTwH8DdIPhUw4c5QUfyh0kECQFV6OG2M9B06c1wayVg_OiVhy6B6u8Q5AHjbRhsacLtI8K7KxG3JA6oxXmOla3MUX35XvU2axN9DChrM3gpJlJYgmqxV454FF23dysnz4sixK8tvwUc.4EiOU_5OfNGmgZpA.MiCif_oYX3m92DAi38QIl~A',
    'Host': 'login.yahoo.com',
    'Origin': 'https://login.yahoo.com',
    'Referer': 'https://login.yahoo.com/account/create?.lang=ar-JO&src=homepage&specId=yidReg&done=https%3A%2F%2Fwww.yahoo.com',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': str(generate_user_agent()),
    'X-Requested-With': 'XMLHttpRequest'}
    data = {
    'browser-fp-data': '{"language":"en-US","colorDepth":24,"deviceMemory":8,"pixelRatio":1,"hardwareConcurrency":2,"timezoneOffset":-180,"timezone":"Asia/Baghdad","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":3,"hash":"e43a8bc708fc490225cde0663b28278c"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc.~Google SwiftShader","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":49,"hash":"411659924ff38420049ac402a30466bc"},"audio":"124.04347527516074","resolution":{"w":"1366","h":"768"},"availableResolution":{"w":"728","h":"1366"},"ts":{"serve":1627553991633,"render":1627553997166}}',
    'specId': 'yidreg',
    'crumb': 'rak/FdAmWa5',
    'acrumb': '9z9sgq95',
    'done': 'https://www.yahoo.com',
    'attrSetIndex': '0',
    'tos0': 'oath_freereg|xa|ar-JO',
    'yid': email,
    'password': 'whisper666',
    'shortCountryCode': 'AF',}
    response = requests.post(url,headers=headers,data=data).text
    if ('"yid"') in response:
        return False
    else:
        return True
def data_instagram(user):
    head = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'cookie': f'csrftoken={secrets.token_hex(8)*2}; sessionid={secrets.token_hex(8)*2};',
    'user-agent': generate_user_agent(),
    }
    l = f'https://www.instagram.com/{user}/?__a=1'
    req = requests.get(l,headers=head).json()
    user_id = str(req['logging_page_id']).split('_')[1]
    u = f'https://o7aa.pythonanywhere.com/?id={user_id}'
    head = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
    'Connection': 'keep-alive',
    'Host': 'o7aa.pythonanywhere.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.70'
    }
    O0Dev = requests.get(u,headers=head).json()["data"]
    return O0Dev

def emailfacebook(email):
    if not "@" in str(email):
        return False
    else:
        em = str(email.split("@")[0])
        if len(em) < 4:
            return False
    uagent = ['Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2729.25 Safari/537.36','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.1; Win64; x64; Trident/6.0)','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2895.29 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2922.81 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2788.96 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2888.99 Safari/537.36','Mozilla/5.0 (X11; Linux i686 on x86_64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2859.17 Safari/537.36','Mozilla/5.0 (X11; Linux i686; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 5.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; WOW64; Trident/4.0)','Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2795.88 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2697.41 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2942.30 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2876.87 Safari/537.36','Mozilla/5.0 (X11; Linux i686 on x86_64; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2744.73 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2797.1 Safari/537.36','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.1; WOW64; Trident/5.0)','Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2882.73 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2654.78 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2745.37 Safari/537.36','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2793.49 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2818.37 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2677.17 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2933.98 Safari/537.36','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 10.0; Win64; x64; Trident/4.0)','Mozilla/5.0 (Windows NT 5.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Windows NT 5.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2797.13 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2920.53 Safari/537.36','Mozilla/5.0 (X11; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 10.0; Win64; x64; Trident/4.0)','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.1; WOW64; Trident/5.0)','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.1; Win64; x64; Trident/5.0)','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2908.96 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2889.60 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 10.0; Win64; x64; Trident/6.0)','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2866.69 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2696.92 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2834.86 Safari/537.36','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)','Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.20 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2652.42 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2867.77 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2975.58 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2693.55 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2791.71 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2786.24 Safari/537.36','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2640.77 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2731.60 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2677.65 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2626.61 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; Win64; x64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Windows NT 6.1; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (Windows NT 6.3; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (X11; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (X11; Linux i686 on x86_64; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2868.96 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2656.15 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2732.4 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2723.12 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2708.31 Safari/537.36','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2981.77 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2949.76 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2895.69 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2685.94 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2879.53 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.96 Safari/537.36','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0)','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.1; Win64; x64; Trident/5.0)','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2808.22 Safari/537.36','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2658.37 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2821.60 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2851.25 Safari/537.36','Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2984.68 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (X11; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.12 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2902.83 Safari/537.36','Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2699.23 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 6.2; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2763.46 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2686.70 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2736.64 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2741.25 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2971.88 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (X11; Linux i686; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (X11; Linux i686 on x86_64; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2638.11 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2942.97 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2971.27 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (Windows NT 6.3; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2687.3 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2748.92 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.17 Safari/537.36','Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2707.22 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2803.68 Safari/537.36','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.3; Win64; x64; Trident/5.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.2; Win64; x64; Trident/4.0)','Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2658.9 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2950.6 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2977.48 Safari/537.36','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.3; WOW64; Trident/5.0)','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2914.60 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2699.19 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.2; Win64; x64; Trident/4.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2909.66 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (Windows NT 5.1; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2873.8 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (X11; Linux i686 on x86_64; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2686.85 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2828.4 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2714.72 Safari/537.36','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 10.0; WOW64; Trident/5.0)','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; WOW64; Trident/4.0)','Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2865.84 Safari/537.36','Mozilla/5.0 (X11; Linux i686; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2760.96 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2767.89 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2760.40 Safari/537.36','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.3; Trident/5.0)','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0)','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2826.35 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2879.14 Safari/537.36','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)','Mozilla/5.0 (Windows NT 5.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2738.49 Safari/537.36','Mozilla/5.0 (X11; Linux i686 on x86_64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2771.1 Safari/537.36','Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2881.24 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2837.61 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2906.53 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2869.18 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2757.36 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2933.3 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2825.19 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2964.46 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (X11; Linux i686 on x86_64; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (Windows NT 10.0; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2682.73 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (Windows NT 6.2; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2801.53 Safari/537.36','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2719.69 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2728.29 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (X11; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (Windows NT 5.1; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2729.70 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; Win64; x64; Trident/6.0)','Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Windows NT 5.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2964.39 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2829.91 Safari/537.36','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 10.0; WOW64; Trident/5.0)','Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2904.31 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2884.12 Safari/537.36','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)','Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2942.11 Safari/537.36','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; WOW64; Trident/6.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2722.74 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.83 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2975.98 Safari/537.36','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; WOW64; Trident/5.0)','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2882.62 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2971.90 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2707.71 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2652.59 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2807.89 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2874.34 Safari/537.36','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2875.52 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2975.16 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2774.19 Safari/537.36','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (X11; Linux i686; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2726.77 Safari/537.36','Mozilla/5.0 (X11; Linux i686 on x86_64; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2800.56 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2755.59 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2626.37 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; Linux i686 on x86_64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2700.36 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2834.90 Safari/537.36','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; Win64; x64; Trident/5.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2650.3 Safari/537.36','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; Trident/6.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2911.22 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.3; WOW64; Trident/4.0)','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2746.63 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2919.68 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2895.27 Safari/537.36','Mozilla/5.0 (X11; Linux i686 on x86_64; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2731.9 Safari/537.36','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; WOW64; Trident/5.0)','Mozilla/5.0 (X11; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.1; WOW64; Trident/6.0)','Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2853.83 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2681.54 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2903.83 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2750.45 Safari/537.36','Mozilla/5.0 (X11; Linux i686 on x86_64; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (Windows NT 5.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 10.0; WOW64; Trident/4.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2936.64 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2871.31 Safari/537.36','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Windows NT 10.0; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2879.68 Safari/537.36','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Win64; x64; Trident/6.0)','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2720.90 Safari/537.36','Mozilla/5.0 (X11; Linux i686; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 10.0; WOW64; Trident/5.0)','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2851.38 Safari/537.36','Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2918.88 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2675.39 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2649.81 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2874.87 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2845.16 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 10.0; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2776.56 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.74 Safari/537.36','Mozilla/5.0 (X11; Linux i686; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 6.2; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2711.77 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Windows NT 5.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2670.5 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Windows NT 5.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Windows NT 5.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2955.1 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2916.18 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2765.29 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2935.41 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 10.0; Trident/4.0)','Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2853.79 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2959.46 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2863.86 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2772.67 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Windows NT 5.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2774.43 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2782.50 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2850.54 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2925.49 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2954.67 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2871.59 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2665.1 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2633.40 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2860.86 Safari/537.36','Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2817.82 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2902.35 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2900.15 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2727.86 Safari/537.36','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.2; WOW64; Trident/4.0)','Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2774.93 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (X11; Linux i686 on x86_64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 5.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2656.70 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; Win64; x64; Trident/5.0)','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 10.0; Trident/5.0)','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2803.87 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2982.21 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2875.33 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 10.0; Win64; x64; Trident/4.0)','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2632.73 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2705.55 Safari/537.36','Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2943.10 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2724.64 Safari/537.36','Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2746.21 Safari/537.36','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.3; WOW64; Trident/4.0)','Mozilla/5.0 (Windows NT 6.2; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2897.13 Safari/537.36','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 5.1; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2658.24 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2889.4 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2898.50 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2738.41 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (Windows NT 10.0; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2951.47 Safari/537.36','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.1; WOW64; Trident/5.0)','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2907.5 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2905.54 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2881.85 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2739.54 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2667.96 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2954.87 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; Win64; x64; Trident/6.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2645.88 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2823.75 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (X11; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2884.13 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2644.90 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (X11; Linux i686; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2874.89 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2967.35 Safari/537.36','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2904.61 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 5.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2915.12 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2896.95 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2646.30 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2653.54 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 6.1; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2694.86 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 5.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2669.21 Safari/537.36','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Win64; x64; Trident/4.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2769.20 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 10.0; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2694.40 Safari/537.36','Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2667.6 Safari/537.36','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; Win64; x64; Trident/6.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2783.70 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2844.53 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (Windows NT 5.1; Win64; x64; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2920.84 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2781.14 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2663.25 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2637.10 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (Windows NT 5.1; Win64; x64; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2805.96 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2660.24 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2723.17 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2670.32 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2831.25 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2669.89 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2800.55 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2648.39 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2736.50 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2816.70 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2683.44 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2630.64 Safari/537.36','Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2674.75 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.1; WOW64; Trident/6.0)','Mozilla/5.0 (Windows NT 5.1; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2794.26 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2797.48 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2958.88 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2768.21 Safari/537.36','Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2752.71 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2958.2 Safari/537.36','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)','Mozilla/5.0 (Windows NT 5.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2761.14 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2688.71 Safari/537.36','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; WOW64; Trident/5.0)','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; Win64; x64; Trident/5.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2690.98 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2701.68 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2720.41 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2927.50 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (Windows NT 5.1; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2739.69 Safari/537.36','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; WOW64; Trident/6.0)','Mozilla/5.0 (Windows NT 5.1; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)','Mozilla/5.0 (Windows NT 5.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; Linux i686; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2940.22 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.1; WOW64; Trident/6.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2694.43 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2746.80 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2858.14 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2893.57 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2888.81 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2877.85 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2842.50 Safari/537.36','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)','Mozilla/5.0 (Windows NT 5.1; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2654.62 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2666.80 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Windows NT 5.1; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 10.0; WOW64; Trident/6.0)','Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 5.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2879.95 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2964.11 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Windows NT 10.0; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 5.1; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2740.36 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2657.48 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2662.75 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2811.43 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2668.73 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2847.12 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2911.3 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2891.17 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2649.16 Safari/537.36','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.3; Trident/5.0)','Mozilla/5.0 (X11; Linux i686 on x86_64; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Windows NT 6.2; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2731.45 Safari/537.36','Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2854.21 Safari/537.36','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.1; WOW64; Trident/6.0)','Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2901.7 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; WOW64; Trident/4.0)','Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2896.86 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2668.76 Safari/537.36','Mozilla/5.0 (X11; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2779.47 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2745.69 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2792.95 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2739.33 Safari/537.36','Mozilla/5.0 (X11; Linux i686 on x86_64; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (X11; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 6.2; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Windows NT 5.1; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2914.68 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 10.0; Win64; x64; Trident/5.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2780.91 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2667.0 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2715.86 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2656.58 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2708.78 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2745.30 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2911.96 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2912.54 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2755.97 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2801.61 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2737.56 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2765.51 Safari/537.36','Mozilla/5.0 (X11; Linux i686; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2659.84 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2679.74 Safari/537.36','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (X11; Linux i686; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2644.34 Safari/537.36','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; WOW64; Trident/6.0)','Mozilla/5.0 (Windows NT 6.2; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2741.62 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2845.64 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (X11; Linux i686 on x86_64; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2980.10 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 6.1; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2937.31 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2733.7 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2851.44 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2635.55 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2726.32 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2877.42 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2984.16 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.61 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (X11; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2948.63 Safari/537.36','Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2813.90 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2751.83 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2708.56 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2706.78 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (X11; Linux i686 on x86_64; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2741.21 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2732.18 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2694.3 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2816.89 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2716.8 Safari/537.36','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2821.96 Safari/537.36',]
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent', random.choice(uagent))]
    br.open("https://mbasic.facebook.com/login/identify/?ctx=recover&search_attempts=0&ars=facebook_login&alternate_search=0&toggle_search_mode=1")
    br._factory.is_html= True
    br.select_form(nr=0)
    br.form["email"] = email
    br.submit()
    urb = br.geturl()
    if "https://mbasic.facebook.com/login/identify/?ctx=recover&search_attempts=1&ars=facebook_login&alternate_search=1" in urb:
        return False
    elif "https://mbasic.facebook.com/login/identify/?ctx=recover&c=%2Flogin%2F&search_attempts=1&ars=facebook_login&alternate_search=1&show_friend_search_filtered_list=0&birth_month_search=0&city_search=0" in urb:
        return False
    else:
        return True
def emailgmail(email):
    url = 'https://android.clients.google.com/setup/checkavail'
    h = {
    'Content-Length':'98',
    'Content-Type':'text/plain; charset=UTF-8',
    'Host':'android.clients.google.com',
    'Connection':'Keep-Alive',
    'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',}
    d = json.dumps({
    'username':email,
    'version':'3',
    'firstName':'AbaLahb',
    'lastName':'AbuJahl'})
    res = requests.post(url,data=d,headers=h)
    if res.json()['status'] == 'SUCCESS':
        return True
    else:
        return False
class gmail():
    def __init__(self):
        put_html(code_ads)
        text = textarea("Check Email Gmail ",placeholder="Entar Email ",required=True,readonly=False,help_text=None)
        list_email = text.split("\n")
        put_tabs(
        [
        {'title': 'Success',
    'content':[put_scrollable(put_scope('True'), height=300, keep_bottom=True),put_button("Download",onclick=self.chd,color="success")]},
        {'title': 'Not Success',
    'content':[put_scrollable(put_scope('False'), height=300, keep_bottom=True),put_button("Download",onclick=self.chd2,color="danger")]},
        {'title': 'All Email',
    'content':[put_scrollable(put_scope('All'), height=300, keep_bottom=True)]},
        ]
        )
        put_html(code_ads)
        self.u = False
        self.listaTrue = []
        self.listaFalse = []
        for email in list_email:
            chem = emailgmail(email)
            if chem:
                self.listaTrue.append(email)
                put_success(email,scope="True")
            else:
                self.listaFalse.append(email)
                put_error(email,scope="False")
            put_warning(email,scope="All")
            
        else:
            self.u = True
            popup('Note', [
            put_success("The scan is complete, now you can download the attachments"),
        put_buttons(['Close'], onclick=lambda _: close_popup())
    ])
    def chd(self):
        if self.u:
            email = str(self.getemail())
            download(name='ToolsFree.txt',content=bytes(email,"ascii"))
            toast("Done")
        else:
            toast("I am waiting for the examination to be completed")
    def chd2(self):
        if self.u:
            email = str(self.getemail2())
            download(name='ToolsFree.txt',content=bytes(email,"ascii"))
            toast("Done")
        else:
            toast("I am waiting for the examination to be completed")
    def getemail(self):
        email = []
        for i in self.listaTrue:
            email.append(i)
            email.append("\n")
        emails = "".join(email)
        return emails
    def getemail2(self):
        email = []
        for i in self.listaFalse:
            email.append(i)
            email.append("\n")
        emails = "".join(email)
        return emails


class email_facebook():
    def __init__(self):
        put_html(code_ads)
        text = textarea("Check Email Facebook ",placeholder="Entar Email ",required=True,readonly=False,help_text=None)
        list_email = text.split("\n")
        put_tabs(
        [
        {'title': 'Success',
    'content':[put_scrollable(put_scope('True'), height=300, keep_bottom=True),put_button("Download",onclick=self.chd,color="success")]},
        {'title': 'Not Success',
    'content':[put_scrollable(put_scope('False'), height=300, keep_bottom=True),put_button("Download",onclick=self.chd2,color="danger")]},
        {'title': 'All Email',
    'content':[put_scrollable(put_scope('All'), height=300, keep_bottom=True)]},
        ]
        )
        put_html(code_ads)
        self.u = False
        self.listaTrue = []
        self.listaFalse = []
        for email in list_email:
            chem = emailfacebook(email)
            if chem:
                self.listaTrue.append(email)
                put_success(email,scope="True")
            else:
                self.listaFalse.append(email)
                put_error(email,scope="False")
            put_warning(email,scope="All")
            
        else:
            self.u = True
            popup('Note', [
            put_success("The scan is complete, now you can download the attachments"),
        put_buttons(['Close'], onclick=lambda _: close_popup())
    ])
    def chd(self):
        if self.u:
            email = str(self.getemail())
            download(name='ToolsFree.txt',content=bytes(email,"ascii"))
            toast("Done")
        else:
            toast("I am waiting for the examination to be completed")
    def chd2(self):
        if self.u:
            email = str(self.getemail2())
            download(name='ToolsFree.txt',content=bytes(email,"ascii"))
            toast("Done")
        else:
            toast("I am waiting for the examination to be completed")
    def getemail(self):
        email = []
        for i in self.listaTrue:
            email.append(i)
            email.append("\n")
        emails = "".join(email)
        return emails
    def getemail2(self):
        email = []
        for i in self.listaFalse:
            email.append(i)
            email.append("\n")
        emails = "".join(email)
        return emails
        
        
class yahoo():
    def __init__(self):
        put_html(code_ads)
        text = textarea("Check Email Yahoo ",placeholder="Entar Email ",required=True,readonly=False,help_text=None)
        list_email = text.split("\n")
        put_tabs(
        [
        {'title': 'Success',
    'content':[put_scrollable(put_scope('True'), height=300, keep_bottom=True),put_button("Download",onclick=self.chd,color="success")]},
        {'title': 'Not Success',
    'content':[put_scrollable(put_scope('False'), height=300, keep_bottom=True),put_button("Download",onclick=self.chd2,color="danger")]},
        {'title': 'All Email',
    'content':[put_scrollable(put_scope('All'), height=300, keep_bottom=True)]},
        ]
        )
        put_html(code_ads)
        self.u = False
        self.listaTrue = []
        self.listaFalse = []
        for email in list_email:
            chem = emailyahoo(email)
            if chem:
                self.listaTrue.append(email)
                put_success(email,scope="True")
            else:
                self.listaFalse.append(email)
                put_error(email,scope="False")
            put_warning(email,scope="All")
            
        else:
            self.u = True
            popup('Note', [
            put_success("The scan is complete, now you can download the attachments"),
        put_buttons(['Close'], onclick=lambda _: close_popup())
    ])
    def chd(self):
        if self.u:
            email = str(self.getemail())
            download(name='ToolsFree.txt',content=bytes(email,"ascii"))
            toast("Done")
        else:
            toast("I am waiting for the examination to be completed")
    def chd2(self):
        if self.u:
            email = str(self.getemail2())
            download(name='ToolsFree.txt',content=bytes(email,"ascii"))
            toast("Done")
        else:
            toast("I am waiting for the examination to be completed")
    def getemail(self):
        email = []
        for i in self.listaTrue:
            email.append(i)
            email.append("\n")
        emails = "".join(email)
        return emails
    def getemail2(self):
        email = []
        for i in self.listaFalse:
            email.append(i)
            email.append("\n")
        emails = "".join(email)
        return emails
        
        
class email_tiktok():
    def __init__(self):
        text = textarea("Check Email TikTok ",placeholder="Entar Email ",required=True,readonly=False,help_text=None)
        list_email = text.split("\n")
        put_tabs(
        [
        {'title': 'Success',
    'content':[put_scrollable(put_scope('True'), height=300, keep_bottom=True),put_button("Download",onclick=self.chd,color="success")]},
        {'title': 'Not Success',
    'content':[put_scrollable(put_scope('False'), height=300, keep_bottom=True),put_button("Download",onclick=self.chd2,color="danger")]},
        {'title': 'All Email',
    'content':[put_scrollable(put_scope('All'), height=300, keep_bottom=True)]},
        ]
        )
        self.u = False
        self.listaTrue = []
        self.listaFalse = []
        for email in list_email:
            chem = emailtiktok(email)
            if chem:
                self.listaTrue.append(email)
                put_success(email,scope="True")
            else:
                self.listaFalse.append(email)
                put_error(email,scope="False")
            put_warning(email,scope="All")
            
        else:
            self.u = True
            popup('Note', [
            put_success("The scan is complete, now you can download the attachments"),
        put_buttons(['Close'], onclick=lambda _: close_popup())
    ])
    def chd(self):
        if self.u:
            email = str(self.getemail())
            download(name='ToolsFree.txt',content=bytes(email,"ascii"))
            toast("Done")
        else:
            toast("I am waiting for the examination to be completed")
    def chd2(self):
        if self.u:
            email = str(self.getemail2())
            download(name='ToolsFree.txt',content=bytes(email,"ascii"))
            toast("Done")
        else:
            toast("I am waiting for the examination to be completed")
    def getemail(self):
        email = []
        for i in self.listaTrue:
            email.append(i)
            email.append("\n")
        emails = "".join(email)
        return emails
    def getemail2(self):
        email = []
        for i in self.listaFalse:
            email.append(i)
            email.append("\n")
        emails = "".join(email)
        return emails
        
        
class email_hotmail():
    def __init__(self):
        put_html(code_ads)
        text = textarea("Check Email Hotmail ",placeholder="Entar Email ",required=True,readonly=False,help_text=None)
        list_email = text.split("\n")
        put_tabs(
        [
        {'title': 'Success',
    'content':[put_scrollable(put_scope('True'), height=300, keep_bottom=True),put_button("Download",onclick=self.chd,color="success")]},
        {'title': 'Not Success',
    'content':[put_scrollable(put_scope('False'), height=300, keep_bottom=True),put_button("Download",onclick=self.chd2,color="danger")]},
        {'title': 'All Email',
    'content':[put_scrollable(put_scope('All'), height=300, keep_bottom=True)]},
        ]
        )
        put_html(code_ads)
        self.u = False
        self.listaTrue = []
        self.listaFalse = []
        for email in list_email:
            chem = emailhotmail(email)
            if chem:
                self.listaTrue.append(email)
                put_success(email,scope="True")
            else:
                self.listaFalse.append(email)
                put_error(email,scope="False")
            put_warning(email,scope="All")
            
        else:
            self.u = True
            popup('Note', [
            put_success("The scan is complete, now you can download the attachments"),
        put_buttons(['Close'], onclick=lambda _: close_popup())
    ])
    def chd(self):
        if self.u:
            email = str(self.getemail())
            download(name='ToolsFree.txt',content=bytes(email,"ascii"))
            toast("Done")
        else:
            toast("I am waiting for the examination to be completed")
    def chd2(self):
        if self.u:
            email = str(self.getemail2())
            download(name='ToolsFree.txt',content=bytes(email,"ascii"))
            toast("Done")
        else:
            toast("I am waiting for the examination to be completed")
    def getemail(self):
        email = []
        for i in self.listaTrue:
            email.append(i)
            email.append("\n")
        emails = "".join(email)
        return emails
    def getemail2(self):
        email = []
        for i in self.listaFalse:
            email.append(i)
            email.append("\n")
        emails = "".join(email)
        return emails
        
        
class email_mailru():
    def __init__(self):
        put_html(code_ads)
        text = textarea("Check Email Mailru ",placeholder="Entar Email ",required=True,readonly=False,help_text=None)
        list_email = text.split("\n")
        put_tabs(
        [
        {'title': 'Success',
    'content':[put_scrollable(put_scope('True'), height=300, keep_bottom=True),put_button("Download",onclick=self.chd,color="success")]},
        {'title': 'Not Success',
    'content':[put_scrollable(put_scope('False'), height=300, keep_bottom=True),put_button("Download",onclick=self.chd2,color="danger")]},
        {'title': 'All Email',
    'content':[put_scrollable(put_scope('All'), height=300, keep_bottom=True)]},
        ]
        )
        put_html(code_ads)
        self.u = False
        self.listaTrue = []
        self.listaFalse = []
        for email in list_email:
            chem = emailmailru(email)
            if chem:
                self.listaTrue.append(email)
                put_success(email,scope="True")
            else:
                self.listaFalse.append(email)
                put_error(email,scope="False")
            put_warning(email,scope="All")
            
        else:
            self.u = True
            popup('Note', [
            put_success("The scan is complete, now you can download the attachments"),
        put_buttons(['Close'], onclick=lambda _: close_popup())
    ])
    def chd(self):
        if self.u:
            email = str(self.getemail())
            download(name='ToolsFree.txt',content=bytes(email,"ascii"))
            toast("Done")
        else:
            toast("I am waiting for the examination to be completed")
    def chd2(self):
        if self.u:
            email = str(self.getemail2())
            download(name='ToolsFree.txt',content=bytes(email,"ascii"))
            toast("Done")
        else:
            toast("I am waiting for the examination to be completed")
    def getemail(self):
        email = []
        for i in self.listaTrue:
            email.append(i)
            email.append("\n")
        emails = "".join(email)
        return emails
    def getemail2(self):
        email = []
        for i in self.listaFalse:
            email.append(i)
            email.append("\n")
        emails = "".join(email)
        return emails
        
        



class email_instagram():
    def __init__(self):
        put_html(code_ads)
        text = textarea("Check Email Instagram ",placeholder="Entar Email ",required=True,readonly=False,help_text=None)
        list_email = text.split("\n")
        put_tabs(
        [
        {'title': 'Success',
    'content':[put_scrollable(put_scope('True'), height=300, keep_bottom=True),put_button("Download",onclick=self.chd,color="success")]},
        {'title': 'Not Success',
    'content':[put_scrollable(put_scope('False'), height=300, keep_bottom=True),put_button("Download",onclick=self.chd2,color="danger")]},
        {'title': 'All Email',
    'content':[put_scrollable(put_scope('All'), height=300, keep_bottom=True)]},
        ]
        )
        put_html(code_ads)
        self.u = False
        self.listaTrue = []
        self.listaFalse = []
        for email in list_email:
            chem = emailinstagram(email)
            if chem:
                self.listaTrue.append(email)
                put_success(email,scope="True")
            else:
                self.listaFalse.append(email)
                put_error(email,scope="False")
            put_warning(email,scope="All")
            
        else:
            self.u = True
            popup('Note', [
            put_success("The scan is complete, now you can download the attachments"),
        put_buttons(['Close'], onclick=lambda _: close_popup())
    ])
    def chd(self):
        if self.u:
            email = str(self.getemail())
            download(name='ToolsFree.txt',content=bytes(email,"ascii"))
            toast("Done")
        else:
            toast("I am waiting for the examination to be completed")
    def chd2(self):
        if self.u:
            email = str(self.getemail2())
            download(name='ToolsFree.txt',content=bytes(email,"ascii"))
            toast("Done")
        else:
            toast("I am waiting for the examination to be completed")
    def getemail(self):
        email = []
        for i in self.listaTrue:
            email.append(i)
            email.append("\n")
        emails = "".join(email)
        return emails
    def getemail2(self):
        email = []
        for i in self.listaFalse:
            email.append(i)
            email.append("\n")
        emails = "".join(email)
        return emails
        
        

class email_twitter():
    def __init__(self):
        put_html(code_ads)
        text = textarea("Check Email Twitter ",placeholder="Entar Email ",required=True,readonly=False,help_text=None)
        list_email = text.split("\n")
        put_tabs(
        [
        {'title': 'Success',
    'content':[put_scrollable(put_scope('True'), height=300, keep_bottom=True),put_button("Download",onclick=self.chd,color="success")]},
        {'title': 'Not Success',
    'content':[put_scrollable(put_scope('False'), height=300, keep_bottom=True),put_button("Download",onclick=self.chd2,color="danger")]},
        {'title': 'All Email',
    'content':[put_scrollable(put_scope('All'), height=300, keep_bottom=True)]},
        ]
        )
        put_html(code_ads)
        self.u = False
        self.listaTrue = []
        self.listaFalse = []
        for email in list_email:
            chem = emailtwitter(email)
            if chem:
                self.listaTrue.append(email)
                put_success(email,scope="True")
            else:
                self.listaFalse.append(email)
                put_error(email,scope="False")
            put_warning(email,scope="All")
            
        else:
            self.u = True
            popup('Note', [
            put_success("The scan is complete, now you can download the attachments"),
        put_buttons(['Close'], onclick=lambda _: close_popup())
    ])
    def chd(self):
        if self.u:
            email = str(self.getemail())
            download(name='ToolsFree.txt',content=bytes(email,"ascii"))
            toast("Done")
        else:
            toast("I am waiting for the examination to be completed")
    def chd2(self):
        if self.u:
            email = str(self.getemail2())
            download(name='ToolsFree.txt',content=bytes(email,"ascii"))
            toast("Done")
        else:
            toast("I am waiting for the examination to be completed")
    def getemail(self):
        email = []
        for i in self.listaTrue:
            email.append(i)
            email.append("\n")
        emails = "".join(email)
        return emails
    def getemail2(self):
        email = []
        for i in self.listaFalse:
            email.append(i)
            email.append("\n")
        emails = "".join(email)
        return emails
        
        

import os
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *
from pywebio.platform.flask import webio_view
from flask import Flask, Blueprint , render_template , request ,redirect, url_for
app = Flask(__name__)
@app.route("/")
def start():
    return render_template("home.html")
if __name__ == "__main__":
    app.add_url_rule(
    '/gmail','Gmail',webio_view(gmail),
    methods=['GET','POST','OPTIONS']
    )
    app.add_url_rule(
    '/facebook','facebook_email',webio_view(email_facebook),
    methods=['GET','POST','OPTIONS']
    )
    app.add_url_rule(
    '/yahoo','yahoo',webio_view(yahoo),
    methods=['GET','POST','OPTIONS']
    )
    app.add_url_rule(
    '/tiktok','tiktokemail',webio_view(email_tiktok),
    methods=['GET','POST','OPTIONS']
    )
    app.add_url_rule(
    '/hotmail','hotmail',webio_view(email_hotmail),
    methods=['GET','POST','OPTIONS']
    )
    app.add_url_rule(
    '/mailru','mailru',webio_view(email_mailru),
    methods=['GET','POST','OPTIONS']
    )
    app.add_url_rule(
    '/instagram','emailinstagram',webio_view(email_instagram),
    methods=['GET','POST','OPTIONS']
    )
    app.add_url_rule(
    '/twitter','emailtwitter',webio_view(email_twitter),
    methods=['GET','POST','OPTIONS']
    )
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))