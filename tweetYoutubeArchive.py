import os
import time
import datetime
import requests
import twitter


#youtubeのAPIKey
API_KEY = ''
#youtubeChannelID
CHANNEL_ID = ''

# 取得したキーとアクセストークンを設定する
# twitterのAPIKey
auth = twitter.OAuth(consumer_key="",
                     consumer_secret="",
                     token="",
                     token_secret="")

t = twitter.Twitter(auth=auth)

base_url = 'https://www.googleapis.com/youtube/v3'
url = base_url + '/search?key=%s&channelId=%s&part=snippet,id&order=date&maxResults=50'
infos = []

for i in range(5):
    flag = False
    #time.sleep(30)
    response = requests.get(url % (API_KEY, CHANNEL_ID))
    if response.status_code != 200:
        print('エラーで終わり')
        break
    result = response.json()
    for item in result['items']:
         if item['snippet']['liveBroadcastContent'] == 'live':
            # 重複ツイートを避ける用
            m = str(datetime.datetime.today())
            m += '\n'
            m += 'https://www.youtube.com/watch?v=' + item['id']['videoId']
            # twitterへメッセージを投稿する
            t.update_status(m)
            flag = True
            break
    if flag:
        break