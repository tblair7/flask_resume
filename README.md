## Personal Website hosted on AWS
### Author: [Tyler Blair](https://www.github.com/tblair7)
----
### Website Summary  

This site is built on Python's Flask micro-framework and hosted on AWS at [tylerblair.net](http://tylerblair.net).  

The home page is my web-based resume - feel free to reach out to me on [LinkedIn](https://www.linkedin.com/in/tylerjblair) if you would discuss any opportunities or would like an electronic copy of my resume!

__Skills/Tools:__  
_Python, AWS, Flask, SQL (sqlite3), gunicorn, nginx, SSH_

----
### Projects

In addition to my resume, I have hosted two interactive projects on my site, which I encourage you to check out, though I will describe them briefly below:



#### [Gathering Steam](http://tylerblair.net/GatheringSteam)  

__Description:__  
Game ratings have the ability to affect a game's visibility, sales, and ultimately, revenue. However, Steam's rating system is binary (thumbs-up/thumbs-down) and offers a limited picture of the game's future performance. With this in mind, I developed Gathering Steam.

Utilizing sentiment analysis of Steam game reviews as a function of time, Gathering Steam has the capability of providing game developers an early alert to predicted changes in game ratings. Additionally, topics are extracted from reviews within each timeframe such that the developers can make informed decisions about additional game changes.  

__Skills/Tools:__  
_Python, AWS, Natural Language Processing (NLP), Scikit-learn (sklearn), Flask, SQL (sqlite3), Natural Language Toolkit (NLTK), Steam API, HTML, CSS_  

#### [Personalized Playlist Generation](http://tylerblair.net/PlaylistGeneration)  
__Description:__  
With a music library of over 5,000 songs, making playlists was extremely time consuming, so I often forewent the task. Realizing that I could take a data-driven approach to this problem, I created a dynamic way of making new playlists on the fly based on a song's audio features.

First, I extracted 38 features from the raw audio waveform of each song in my musical library. Next, I needed a dynamic way to select a song from my library, especially if I couldn't quite remember the exact title/artist name. I decided to place all of my song artist/titles in a SQL database at which point I could use a loosely fitted query to help me find the song I was thinking of.  

E.g., if I knew the song I wanted was by John Mayer, I could input 'Mayer', which would find the song's ID via a loose query:  
 `"SELECT ID FROM songs WHERE title LIKE %mayer%"`

By selecting the song I desired from the results, my pipeline then uses a k-Nearest Neighbors (kNN) to find the songs with audio characteristics most similar to the selected song. In this web-hosted version of this project, a new YouTube playlist is finally created so you can listen to your new playlist! However, when run locally (separate repository), copies of these songs are moved to a new directory such that they can be listened to with your media player of choice.

__Skills/Tools:__  
_Python, AWS, Natural Language Processing (NLP), Scikit-learn (sklearn), Flask, SQL (sqlite3), Natural Language Toolkit (NLTK), [Steam API](https://steamcommunity.com/dev)_  
