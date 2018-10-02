from SNS.twitter import config
import json #標準のjsonモジュールの読み込み

url = "https://api.twitter.com/1.1/statuses/user_timeline.json" #タイムライン取得エンドポイント

params ={'count' : 5} #取得数
res = config.twitter.get(url, params = params)

if res.status_code == 200: #正常通信出来た場合
    timelines = json.loads(res.text) #レスポンスからタイムラインリストを取得
    for line in timelines: #タイムラインリストをループ処理
        print(line['user']['name']+'::'+line['text'])
        print(line['created_at'])
        print('*******************************************')
else: #正常通信出来なかった場合
    print("Failed: %d" % res.status_code)