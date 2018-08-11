from django.shortcuts import render
from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,get_user_model,login,logout
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import urllib.request, json

# Create your views here.
def index(request):
    y = urllib.request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&eventType=live&maxResults=4&topicId=Game&type=video&videoCategoryId=20&key=AIzaSyDraF24l86NJFfSpvm-zkESCEnjGr2_pck")
    search_response = json.load(y)
    videos = []
    for search_result in search_response['items']:
        videos.append(search_result['id']['videoId'])
    return render(request, 'Stream/index.html', {'videos':videos})
def home(request):

        return render(request,'Stream/index.html')

@login_required
def user_logout(request):
    logout(request)

    return  render(request,'Stream/index.html')

