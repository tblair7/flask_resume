from flask import render_template
from flask import request, make_response
from flask_resume import app
import pandas as pd
import pickle as pckl
import os
from flask_resume import playlist_online

#from flask_wtf import FlaskForm
#from wtforms import StringField, SubmitField

from flask import Flask, render_template, request
#app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():

    resp = make_response(render_template("index.html",
                        title = 'Tyler Blair'))
    return resp

@app.route('/GatheringSteam')
def GatheringSteam():
    return render_template("gathering_steam.html")


@app.route('/GatheringSteam/suggested',methods=['POST'])
def suggested():
    if request.method == 'POST':
       suggestion = request.form['game']

       f = open("suggestions.txt","a")
       f.write(suggestion + "\n")
       f.close()

       return render_template('suggested.html',
                              suggestion = suggestion)

    else:
        return "error"


#@app.route('/', methods=['POST'])
#def my_form_post():
#    text = request.form['text']
#    processed_text = text.upper()
#    return processed_text


@app.route('/GatheringSteam/ARK')
def ARK():
    return render_template('topics.html',
                            game = 'ARK',
                            game_pic = '../static/images/ARK.jpeg',
                            plot = '../static/plots/interactive_ARK2.json',
                            accuracy = '90.8')


@app.route('/GatheringSteam/MHW')
@app.route('/GatheringSteam/Monster_Hunter_World')
def MWH():

    return render_template('topics.html',
                            game = 'Monster Hunter World',
                            game_pic = '../static/images/MHW.jpeg',
                            plot = '../static/plots/interactive_MHW.json',
                            accuracy = '84.1')

@app.route('/GatheringSteam/NMS')
@app.route('/GatheringSteam/No_Mans_Sky')
def NMS():

    return render_template('topics.html',
                            game = 'No Man\'s Sky',
                            game_pic = '../static/images/NMS.jpeg',
                            plot = '../static/plots/interactive_NMS.json',
                            accuracy = '86.2')



################ Playlist Generation ######################


@app.route('/PlaylistGeneration')
@app.route('/Playlist')
def playlist():
    return render_template('playlist_home.html')

@app.route('/PlaylistGeneration/results', methods=['POST', 'GET'])
def playlistResults():
    import json


    if request.method == 'POST':
       title = request.form['title']
       try:
           num_songs = int(request.form['num_songs'])
       except:
           num_songs = 20

       results, matches = playlist_online.songQuery(title, num_songs)

       num_results = len(matches)


       if not results:
           return render_template('playlist_no_results.html')
       elif num_results > 1:



           resp = make_response(render_template('playlist_results.html',
                                   results = results,
                                   matches = matches,
                                   num_songs = num_songs))

           resp.set_cookie('num_songs', json.dumps(num_songs))
           resp.set_cookie('query', title)
           resp.set_cookie('num_results', json.dumps(num_results))

#           for number, title in enumerate(results):
#               resp.set_cookie(number, title)
           return resp



       else:
           selection = int(1)
           playlist = playlist_online.makePlaylistMatch(matches, selection, num_songs)
           return render_template('generate_playlist.html',
                                   playlist = playlist)

    else:
        return "error"

@app.route('/PlaylistGeneration/generate', methods=['POST', 'GET'])
def playlistGenerate():
    if request.method == 'POST':

        try:
            selection = request.form['match']
        except:
            return render_template('playlist_no_results.html')

        selection = int(selection)

        num_results = int(request.cookies.get('num_results'))
        num_songs = int(request.cookies.get('num_songs'))
        title = request.cookies.get('query')

        if selection <= num_results and selection > 0:
            results, matches = playlist_online.songQuery(title, num_songs)
            playlist = playlist_online.makePlaylistMatch(matches, selection, num_songs)
            return render_template('generate_playlist.html', playlist = playlist)

        else:
            return render_template('playlist_no_results.html')

            #my_string = 'selection: ({0}) - type: ({1}) \n\
            #num_results: ({2}) - type: ({3}) \n\
            #num_songs: ({4}) - type: ({5}) \n\
            #title: ({6}) - type: ({7})'.format(selection, type(selection),
            #num_results, type(num_results), num_songs, type(num_songs),
            #title, type(title))
            #return render_template('check.html',
            #check_output = my_string)

        #title = str(request.cookies.get(selection))


        #playlist = playlist_online.makePlaylist(title, selection, num_songs)

        #return render_template('generate_playlist.html', playlist = playlist)
        #return redirect(url_for('im_user',user= user) )
