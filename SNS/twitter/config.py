# Consumer Key (API Key) B9LiKGwrkLuUe6EyBJhreUoEx
# Consumer Key (API Key) B9LiKGwrkLuUe6EyBJhreUoEx
#Consumer Secret (API Secret) n7Tg6WRLlsv1clxXunZsrBDP4MS5GNEi8cutfe5Ul5S5yrK1Mc
#Access Token 1020967780315566080-MlZcns2q6e4tNCAgXzwPg2gQb0oJoh
#Access Token Secret Mxqn5lP97bt2F3pic31zCrSDbkIvqMZueASErxpCYz9Ph
#Access Level Read and write
#Owner GotoApi
#Owner ID 1020967780315566080

#アクセスキーはconfig_orgを参照せよ
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

from SNS.twitter import config

import json #標準のjsonモジュールとconfig.pyの読み込み
from requests_oauthlib import OAuth1Session #OAuthのライブラリの読み込み

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS) #認証処理