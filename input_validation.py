import os
from pytube import YouTube, Playlist

def validate_youtube_url(url):
    """
        returns True if a video/playlist exist and false if video/playlist doesn't exist or playlist is empty. 
    """
    try:
        video = YouTube(url)
        return True
    except Exception as e:
        try:
            playlist = Playlist(url)
            if playlist.video_urls:
                return True
            else:
                return None
        except Exception as e:
            return None