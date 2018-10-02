from SNS.twitter import config
import json #標準のjsonモジュールの読み込み

url = "https://api.twitter.com/1.1/statuses/update.json"

print("何をつぶやきますか?")
tweet = input('>> ')
print('----------------------------------------------------')

params = {"status" : tweet}

req = config.twitter.post(url, params = params)

if req.status_code == 200:
    print("Succeed!")
else:
    print("ERROR : %d"% req.status_code)