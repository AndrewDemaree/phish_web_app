from django.shortcuts import render
from.credentials import REDIRECT_URI, CLIENT_SECRET, CLIENT_ID
from rest_framework.views import APIView
from requests import Request, post
from rest_framework import status
from rest_framework.response import Response

class AuthURL(APIView):
    def get(self, request, format=None):
        #returns a url that we can go to to authorize the app
        #doesn't actually send the request
        scopes = 'user-read-playback-state user-modify-playback-state user-read-currently-playing'
        # scopes link https://developer.spotify.com/documentation/general/guides/authorization/scopes/

        url = Request('GET', 'https://accounts.spotify.com/authorize', params={
            #parameters are outlined in the API authentication workflow
            'scope': scopes,
            'response_type': 'code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID
        }).prepare().url

        return Response({'url': url}, status=status.HTTP_200_OK)


#need to create a redirect uri or callback
#when the request gets sent to the AuthURL URL the information gets returned to this URL
#code and state are returned
#then send another request to get the access tokens

def spotify_callback(request, format=None):
    #might make this a view in the future
    code = request.GET.get('code') #the code from spotify
    error = request.GET.get('error')

    response = post('https://accounts.spotify.com/api/token', data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }).json()

    # values below are taken from the returned json file from spotify
    access_token = response.get('access_token')
    token_type = response.get('token_type')
    refresh_token = response.get('refresh_token')
    expires_in = response.get('expires_in')
    error = response.get('error')
    # need to store the access tokens and refresh tokens, so make class in models.py
 
