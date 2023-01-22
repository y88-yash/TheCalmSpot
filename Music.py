from dotenv import load_dotenv
load_dotenv()
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials #spotify api
import tkinter as tk
import webbrowser
import Emo
from Emo import *



def open_spotify(url):
    webbrowser.open(url, new = 2),
def create_label(text):
    return tk.Label(master = frm_recommendations, text= text)
def create_button(text, url):
    return tk.Button(master = frm_recommendations, text =text, command = lambda :open_spotify(url))
def clear(*args):
    args.destroy()
def display_recommendations (response):
    lb1_track_name = tk.Label(master = frm_recommendations, text = 'Track Name')
    lb1_artist_name = tk. Label(master = frm_recommendations, text = 'Artist Name')
    lb1_play_it= tk.Label(master = frm_recommendations, text = 'Play It')
    lb1_track_name.grid(row=0, column=0)
    lb1_artist_name.grid(row=0, column=1)
    lb1_play_it.grid(row=0, column=2)

    for idx,track in enumerate(response['tracks']):
        lb1_track_name_recommended=create_label(track['name'])
        lb1_track_name_recommended.grid(row= idx + 1, column=0)
        lbl_artist_name_recommended = create_label(track['artists'][0]['name'])
        lbl_artist_name_recommended.grid(row=idx + 1, column=1)
        btn_plat_it_recommended = create_button('Play It', track['external_urls']['spotify'])
        btn_plat_it_recommended.grid(row = idx + 1, column = 2, padx = 10)


def get_recommendations():
    #  sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials("7e519fa0c6544986bc49e4504c978243","b30ae34e35a74bdb8847b76a0cd2c8b3"))

    search = ent_search.get()
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials("7e519fa0c6544986bc49e4504c978243","b30ae34e35a74bdb8847b76a0cd2c8b3"))
    result = sp.search(q = search, limit=1)
    id_list = [result['tracks']['items'][0]['id']]
    recommendations = sp.recommendations(seed_tracks = id_list, limit = 10)
    display_recommendations(recommendations)


window = tk.Tk()
frm_search_field = tk.Frame(master = window, width = 100)
frm_recommendations = tk.Frame(master = window)
frm_search_field.pack()
frm_recommendations.pack()
ent_search = tk.Entry(master=frm_search_field, width = 25)
btn_get_recommendations = tk.Button(master=frm_search_field,text='Get recommendations',command=get_recommendations)
ent_search.grid(row = 0, column = 0, pady = 10, padx = 10)
btn_get_recommendations.grid(row = 0, column = 1, pady = 10, padx = 10)
window.mainloop()

