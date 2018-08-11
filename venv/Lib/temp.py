import urllib.request,json
y= urllib.request.urlopen("https://www.googleapis.com/youtube/v3/search?part=snippet%2CcontentDetails&eventType=live&maxResults=4&topicId=Game&type=video&videoCategoryId=20&key=AIzaSyDraF24l86NJFfSpvm-zkESCEnjGr2_pck")
search_response = json.load(y)
videos = []
info=[]
for search_result in search_response['items']:
    videos.append(search_result['id']['videoId'])
    info.append(search_result['snippet']['liveBroadcastContent'])

print(videos)
print(info)