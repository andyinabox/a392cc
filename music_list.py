import glob
from sys import argv
import os

from mutagen.mp3 import EasyMP3 as MP3

# print argv

if len(argv) > 1:
  path = argv[1]
else:
  path = os.path.dirname(os.path.realpath(__file__)) + '/test/'

os.chdir(path)

print path

filenames = glob.glob('*.mp3')

print filenames


files = []

class MusicFile:
  def __init__(self, filename, metadata):
    self.filename = filename
    self.metadata = metadata

class MusicLibrary:

  artists = {}
  albums = {}
  titles = {}
  tracks = {}

  def __init__(self):



  def add(music_file):




for fn in filenames:
  md = MP3(fn)
  f = MusicFile(fn, md)
  files.append(f)

# print files

for f in files:
  print "----"
  print f.filename
  md = f.metadata
  artist = md["artist"][0]
  album = md["album"][0]
  title = md["title"][0]
  track = md["tracknumber"][0].split("/")

  print artist
  print album
  print title
  print(track[0]+" of "+track[1])
  print " "

