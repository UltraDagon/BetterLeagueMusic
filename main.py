import os
import time
import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from riotwatcher import LolWatcher, ApiError

# Load environment variables
for env in open('environment.txt').readlines():
    if 'Enabled:' in env:
        if str(env[env.index(':')+1:].lower().replace("\n", "")) in ['false', 'f', '0']:
            print("\'environment.txt\' is disabled. This can be changed within the file.")
            break
    else:
        os.environ[env[0:env.index('=')]] = env[env.index('=')+1:]

# Keys
api_key = os.environ.get('API_KEY')

# League
watcher = LolWatcher(api_key)
my_region = 'na1'
ids = {'266': 'Aatrox', '103': 'Ahri', '84': 'Akali',
       '166': 'Akshan', '12': 'Alistar', '32': 'Amumu',
       '34': 'Anivia', '1': 'Annie', '523': 'Aphelios',
       '22': 'Ashe', '136': 'Aurelion Sol', '268': 'Azir',
       '432': 'Bard', '200': "Bel'Veth", '53': 'Blitzcrank',
       '63': 'Brand', '201': 'Braum', '51': 'Caitlyn',
       '164': 'Camille', '69': 'Cassiopeia', '31': "Cho'Gath",
       '42': 'Corki', '122': 'Darius', '131': 'Diana',
       '119': 'Draven', '36': 'Dr. Mundo', '245': 'Ekko',
       '60': 'Elise', '28': 'Evelynn', '81': 'Ezreal',
       '9': 'Fiddlesticks', '114': 'Fiora', '105': 'Fizz',
       '3': 'Galio', '41': 'Gangplank', '86': 'Garen',
       '150': 'Gnar', '79': 'Gragas', '104': 'Graves',
       '887': 'Gwen', '120': 'Hecarim', '74': 'Heimerdinger',
       '420': 'Illaoi', '39': 'Irelia', '427': 'Ivern',
       '40': 'Janna', '59': 'Jarvan IV', '24': 'Jax',
       '126': 'Jayce', '202': 'Jhin', '222': 'Jinx', '145': "Kai'Sa",
       '429': 'Kalista', '43': 'Karma', '30': 'Karthus',
       '38': 'Kassadin', '55': 'Katarina', '10': 'Kayle',
       '141': 'Kayn', '85': 'Kennen', '121': "Kha'Zix",
       '203': 'Kindred', '240': 'Kled', '96': "Kog'Maw",
       '7': 'LeBlanc', '64': 'Lee Sin', '89': 'Leona',
       '876': 'Lillia', '127': 'Lissandra', '236': 'Lucian',
       '117': 'Lulu', '99': 'Lux', '54': 'Malphite', '90': 'Malzahar',
       '57': 'Maokai', '11': 'Master Yi', '21': 'Miss Fortune',
       '62': 'Wukong', '82': 'Mordekaiser', '25': 'Morgana',
       '267': 'Nami', '75': 'Nasus', '111': 'Nautilus',
       '518': 'Neeko', '76': 'Nidalee', '56': 'Nocturne',
       '20': 'Nunu & Willump', '2': 'Olaf', '61': 'Orianna',
       '516': 'Ornn', '80': 'Pantheon', '78': 'Poppy', '555': 'Pyke',
       '246': 'Qiyana', '133': 'Quinn', '497': 'Rakan', '33': 'Rammus',
       '421': "Rek'Sai", '526': 'Rell', '888': 'Renata Glasc',
       '58': 'Renekton', '107': 'Rengar', '92': 'Riven', '68': 'Rumble',
       '13': 'Ryze', '360': 'Samira', '113': 'Sejuani', '235': 'Senna',
       '147': 'Seraphine', '875': 'Sett', '35': 'Shaco', '98': 'Shen',
       '102': 'Shyvana', '27': 'Singed', '14': 'Sion', '15': 'Sivir',
       '72': 'Skarner', '37': 'Sona', '16': 'Soraka', '50': 'Swain',
       '517': 'Sylas', '134': 'Syndra', '223': 'Tahm Kench',
       '163': 'Taliyah', '91': 'Talon', '44': 'Taric', '17': 'Teemo',
       '412': 'Thresh', '18': 'Tristana', '48': 'Trundle',
       '23': 'Tryndamere', '4': 'Twisted Fate', '29': 'Twitch',
       '77': 'Udyr', '6': 'Urgot', '110': 'Varus', '67': 'Vayne',
       '45': 'Veigar', '161': "Vel'Koz", '711': 'Vex', '254': 'Vi',
       '234': 'Viego', '112': 'Viktor', '8': 'Vladimir',
       '106': 'Volibear', '19': 'Warwick', '498': 'Xayah',
       '101': 'Xerath', '5': 'Xin Zhao', '157': 'Yasuo',
       '777': 'Yone', '83': 'Yorick', '350': 'Yuumi', '154': 'Zac',
       '238': 'Zed', '221': 'Zeri', '115': 'Ziggs', '26': 'Zilean',
       '142': 'Zoe', '143': 'Zyra'}

summoner_name = os.environ.get('SUMMONER_NAME')
# summoner_name =
champion = 'None'
old_champion = 'None'
player = {'championId': 'None'}

# Spotify
scope = "user-read-playback-state,user-modify-playback-state"
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


def play_song(search):
    search = spotify.search(search+" League of Legends")
    track_id = search['tracks']['items'][0]['id']
    spotify.start_playback(uris=['spotify:track:' + str(track_id)])
    spotify.repeat('context')


def get_player_info():
    me = watcher.summoner.by_name(my_region, summoner_name)
    url = f'https://{my_region}.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{me["id"]}?api_key={api_key}'
    current_game = json.loads(requests.get(url).text)
    if 'status' in current_game:
        return 'NoActiveGame'

    players = current_game["participants"]
    for p in players:
        if p['summonerName'] == summoner_name:
            return p


sleep_time = 15
while 1 == 1:
    player = get_player_info()
    if spotify.current_playback() is None:
        print("Please start and pause any song on Spotify to activate the session")
        time.sleep(sleep_time)
        continue

    if player == 'NoActiveGame':
        print("No Active Game")
        if spotify.current_playback()['is_playing']:
            spotify.pause_playback()
        champion = "None"
        old_champion = "None"
        time.sleep(sleep_time)
        continue

    old_champion = champion
    champion = ids[str(player["championId"])]
    print("Current Champion: " + champion)
    if old_champion != champion:
        play_song(champion)
        print("Now playing: "+champion)

    time.sleep(sleep_time)
