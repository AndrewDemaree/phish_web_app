The pages app allows easier management of all pages/urls associated with the site. 

Url path is pulled from this app to the django project upon deployment. 

Inital pages added to this app are Home and About. 

Random page pulls a random image from static/media/images file to show a random image.
This is where images are stored upon a submission from the user. 
The 'djanog-random-image-from-folder' third party django app is utilized to acomplish this.
A spotify Web Playback SDK is used to allow users authenticated through Spotify to play a pre-set Phish playlsit from Spotify.
A new random image is displayed with every refresh; the playlist defaults to the first song in the Spotify playlsit upon refresh. 
