import os
from dotenv import load_dotenv
from cloud_signin import login
from cloud_query import send_request

load_dotenv()
base_url = os.environ.get("SITE_URL")

credentials = {
    "email": os.environ.get("EMAIL"),
    "password": os.environ.get("PASSWORD"),
}

if __name__ == '__main__':
    login_cookies = login(base_url, credentials)
    print(login_cookies)
