# BetterLeagueMusic
Uses Spotify to play League of Legends music depending on your champion or game scenario.
Run "Run BetterLeagueMusic.bat" to start the program.

# Setting up the environment.txt file
This file is used to that sensitive information is kept private for all users, if you are sharing this program, do NOT share a modified environment.txt file.
### API_KEY
This is your Riot API key for League of Legends. To get your key, go to [https://developer.riotgames.com/](https://developer.riotgames.com/), log in, and copy your token. You may have to regenerate it at the bottom.
### SPOTIPY_CLIENT_ID
This is on [https://developer.spotify.com/dashboard/applications](https://developer.spotify.com/dashboard/applications). Log in, and make a new application by clicking the green "CREATE AN APP" button. You can name it whatever, but I would recommend "BetterLeagueMusic", and putting the description as "Music Bot for League of Legends".
Your client ID is under the large title of your app.
### SPOTIPY_CLIENT_SECRET
Under the client ID on the Spotify for Developers (SfD) dashboard
### SPOTIPY_REDIRECT_URI
This can also be whatever you want, but MUST be set up in the SfD dashboard. Go to "EDIT SETTINGS" -> "Redirect URIs", and put in "[https://www.google.com](https://www.google.com)", or whatever website you prefer.
### SUMMONER_NAME
Your League of Legends username. NOT your Riot ID

# Additional notes
### Region is not NA1
replace "my_region = 'na1'" with a region from [https://developer.riotgames.com/docs/lol#Platform%20Routing%20Values:~:text=Platform%20Routing%20Values](https://developer.riotgames.com/docs/lol#Platform%20Routing%20Values:~:text=Platform%20Routing%20Values)
