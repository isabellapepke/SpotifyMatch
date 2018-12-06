FROM python:3

ADD comparer.py /
ADD playlist.py /
ADD song.py /
ADD spotifyxx.py /
ADD statistics.py /
RUN pip install spotipy

CMD ["python", "spotifyxx.py"]
