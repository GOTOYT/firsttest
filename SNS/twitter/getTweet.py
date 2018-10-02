from SNS.twitter import config
import json #標準のjsonモジュールの読み込み

url = "https://api.twitter.com/1.1/search/tweets.json" #tweet取得エンドポイント

keyword = '秋刀魚'
print('----------------------------------------------------')


params = {'q' : keyword, 'count' : 100}

req = config.twitter.get(url, params = params)

if req.status_code == 200:
    search_timeline = json.loads(req.text)
    for tweet in search_timeline['statuses']:
        print(tweet['user']['name'] + '::' + tweet['text'])
        print(tweet['created_at'])
        print('----------------------------------------------------')
else:
    print("ERROR: %d" % req.status_code)