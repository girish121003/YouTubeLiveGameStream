import urllib.request,json
# y = urllib.request.urlopen(
#         "https://www.googleapis.com/youtube/v3/search?part=snippet&eventType=live&maxResults=4&topicId=Game&type=video&videoCategoryId=20&key=AIzaSyDraF24l86NJFfSpvm-zkESCEnjGr2_pck")
# search_response = json.load(y)
# videos = {}
# for search_result in search_response['items']:
#     videos[search_result['id']['videoId']] = search_result['snippet']['thumbnails']['medium']['url']
# for video,url in videos.items():
#     print(video)
#     print(url)
y = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/liveChat/messages?liveChatId=EiEKGFVDYm9NWF9VTmdhUEJzVU9JZ2FzbjMtURIFL2xpdmU&part=snippet&key=AIzaSyDraF24l86NJFfSpvm-zkESCEnjGr2_pck")
search_response = json.load(y)
storeChat=''
storeUser=''
for search_result in search_response['items']:
    if(search_result['snippet']['authorChannelId']=='UC-NBvmi1c6uj2C0JOrSFNbQ'):
        storeChat=search_result['snippet']['displayMessage']
        storeUser=search_result['snippet']['authorChannelId']

print(storeChat)
print(storeUser)

