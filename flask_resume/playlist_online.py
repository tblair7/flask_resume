def songQuery(title, num_songs):
    import sqlite3
    conn = sqlite3.connect('flask_resume/YT_songs_short.db')

    title_insert = '%' + title + '%'

    matches = conn.execute("""SELECT TITLE FROM SONGS WHERE TITLE LIKE (?)""", (title_insert,)).fetchall()
    if len(matches) > 0:
        numbers = range(1,len(matches)+1)
        results = zip(matches,numbers)
    else:
        results = ''

    return results, matches



def makePlaylistMatch(matches, selection, num_songs):

    import pickle as pckl
    import pandas as pd
    import requests

    from sklearn.metrics import pairwise_distances
    import shutil, os
    import string
    import sqlite3

    conn = sqlite3.connect('flask_resume/YT_songs_short.db')

    desired_song = conn.execute("""SELECT ID FROM SONGS WHERE TITLE LIKE (?)""", (matches[selection-1][0],)).fetchall()

    features_df = pckl.load(open('flask_resume/static/data/features_df_norm.pckl','rb'))

    min_dists = pairwise_distances(features_df.loc[desired_song[0][0]].values.reshape(1,-1), features_df.values)
    neighbor_indices = min_dists.argsort()[0][:num_songs]

    yt_ids = ','.join(features_df.iloc[neighbor_indices].index.tolist())
    yt_url = 'http://www.youtube.com/watch_videos?video_ids=' + yt_ids

    r = requests.get(yt_url)
    yt_embed = r.url.split('list=')[1]

    return yt_url, yt_embed # if a dataframe of the related titles is desired.

def makePlaylist(matches, selection, num_songs):

    import pickle as pckl
    import pandas as pd
    import requests

    from sklearn.metrics import pairwise_distances
    import shutil, os
    import string
    import sqlite3

    conn = sqlite3.connect('flask_resume/YT_songs_short.db')

    desired_song = conn.execute("""SELECT ID FROM SONGS WHERE TITLE LIKE (?)""", (matches[selection-1][0],)).fetchall()

    features_df = pckl.load(open('flask_resume/static/data/features_df_norm.pckl','rb'))

    min_dists = pairwise_distances(features_df.loc[desired_song[0][0]].values.reshape(1,-1), features_df.values)
    neighbor_indices = min_dists.argsort()[0][:num_songs]

    yt_ids = ','.join(features_df.iloc[neighbor_indices].index.tolist())
    yt_url = 'http://www.youtube.com/watch_videos?video_ids=' + yt_ids

    r = requests.get(yt_url)
    yt_embed = r.url.split('list=')[1]

    return yt_url, yt_embed# if a dataframe of the related titles is desired.


#url_base = 'http://www.youtube.com/watch_videos?video_ids='
#urls = ','.join(a.index.values)
#url_full = url_base + urls
