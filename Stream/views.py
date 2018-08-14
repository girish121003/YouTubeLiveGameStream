from django.shortcuts import render
from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,get_user_model,login,logout
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import urllib.request, json
from Stream.models import UserInfo
from django.views.decorators.clickjacking import xframe_options_exempt,xframe_options_sameorigin

# Create your views here.

def index(request):
    #Requested Data from Youtube.Search in order to get the videoId and Thumbnails
    get_Json = urllib.request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&eventType=live&maxResults=4&topicId=Game&type=video&videoCategoryId=20&key=AIzaSyDraF24l86NJFfSpvm-zkESCEnjGr2_pck")
    get_VideoId_ThumbnailURL = json.load(get_Json)
    videos = {}
    # Looping the JSON data to get the video id stores as  key and Thumbnail stores as value inside videos dictionary
    for search_result in get_VideoId_ThumbnailURL['items']:
        videos[search_result['id']['videoId']] = search_result['snippet']['thumbnails']['medium']['url']

    return render (request, 'Stream/index.html', {'videos':videos})



def home(request):
    return render(request,'Stream/index.html')

@login_required
def user_logout(request):
    logout(request)
    return  render(request,'Stream/index.html')

