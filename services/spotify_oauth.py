import spotipy
from spotipy.oauth2 import SpotifyOAuth

#le tue credenziali le trovi nella dashboard di prima
SPOTIFY_CLIENT_ID = "3a9130b1a74740e4a1ef72b187a3d597"
SPOTIFY_CLIENT_SECRET = "42089d774c5d4b3a9896fa6ff7e94ab1"
SPOTIFY_REDIRECT_URI = "https://5000-minasiluca-spotipyrefac-aex9icopweb.ws-eu117.gitpod.io/callback" #dopo il login andiamo qui

#config SpotifyOAuth per l'autenticazione e redirect uri
sp_oauth = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-read-private", #permessi x informazioni dell'utente
    show_dialog=True #forziamo la richiesta di inserire new credenziali
)

def get_spotify_object (token_info):
    return spotipy.Spotify(auth=token_info['access_token'])