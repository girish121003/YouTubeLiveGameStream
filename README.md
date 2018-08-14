# YouTubeLiveGameStream
Steps involved in accessing the SV page:

1) Go to Heroku Live link:
https://fierce-mesa-85443.herokuapp.com

2)Login With your google account

3) You will be prompted with the default thumbnails of currently live videos on you tube

4) Click any of the thumbnail and video will start playing

5) You can see the chat window next to the video where you send text messages with your google account

6) Close the video with power off button next to chat window top right corner

7) Thats it



Note- For now i was able to fetch data from youtube data api, parse it and get the live streaming video id, that i used to pass it 
as parameter in order to get the videos out of youtube on my single web page.I could navigate through different video. For now i have 
shown just 4 results as a demo. I can get as much results as i want and handle it accordingly. 
This Web page is using google authenication to authenticate user with google accounts.If you could provide me some more time 
i will be able to do the rest of the requirement.




Helpers:- 

1) I have used the template from one of my older project and used different animation style to animate the images in the background
2) I have installed various packages in order to interact with the Web API such as social-auth to handle the user authentication 
using gmail, i just had to add  url(r'^auth/', include('social_django.urls', namespace='social')) as my url which handeled the login 
itself
3)I have used superslides jquery and css to change the look and feel. Here is the link:- https://github.com/nicinabox/superslides 
which is what i used in my one of the project and integrated in stream viewer application too.'

Pending Work Implementation plan:-
1) For storing Alex text messages i created a database table, get the live chat out of api using youtube.livechatmessages and 
integrate those messages in my chat window so that i could handle events that whenever alex sends a message an event is 
triggered and would save the message to database.

2)Stats:- To show the stats, interacting with video id and get the statistics such as like counts , view counts, message counts
I planned grab this data from api and store it in my database and show it to Alex everytime he logs in his account. I would represent 
the data right below the thumbnails.

3)To make this application mobile responsive i would use gridvidew from bootstrap to divide the application in differnt grid and assign 
there col-size accordingly so that when a user access the application on mobile devices he will be able to see all the content on single 
screen.











