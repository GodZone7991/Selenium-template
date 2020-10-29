import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
import robobrowser
import re
import json
import os
import random

#MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; U; en-gb; KFTHWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.16 Safari/535.19"
MOBILE_USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
FB_AUTH = "EAAFZBA07PuwABAC35GqtXc5rZBkBQD7dcZCxWkLvfUozHtOYCbDKMALFZBB4fd6HyZA4XPchOX0sF1s2D7v9HP4oy0DwQEPu60arZABElG0CZAgseimZB8LOlE2JZCXqLxqMQLtGodseEzZC02QV7k24DJ9X6PPUZCfAfSaP0yeUvZCxgQDRk9ARyZBNnZCd88GZA9EfSJ7RO5nUeb4r56mNiAoEZC4lfNB7FnxRK2wZCkrFGA4YnZBwZDZD"

def get_access_token(email, password):
    s = robobrowser.RoboBrowser(user_agent=MOBILE_USER_AGENT, parser = "lxml")
    s.open(FB_AUTH)
    ##submit login form##
    f = s.get_form()
    f["pass"] = password
    f["email"] = email
    s.submit_form(f)
    ##click the 'ok' button on the dialog informing you that you have already authenticated with the Tinder app
    f = s.get_form()
    s.submit_form(f, submit=f.submit_fields['__CONFIRM__'])
    ##get access token from the html response##
    access_token = re.search(r"access_token=([\w\d]+)", s.response.content.decode()).groups()[0]
    # print s.response.content.decode()
    return access_token

def get_login_credentials():
    print("Checking for credentials..")
    if os.path.exists('auth.json'):
        print("Auth.json existed..")
        with open("auth.json") as data_file:
            data = json.load(data_file)
            if "email" in data and "password" in data and "FBID" in data:
                return (data["email"], data["password"], data["FBID"])
            else:
                print ("Invalid auth.json file")

    print ("Auth.json missing or invalid. Please enter your credentials.")
    return (input("Enter email ..\n"), input("Enter password..\n"))