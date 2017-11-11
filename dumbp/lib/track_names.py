## add track number to the track title, so the song order
## will be correct in my phone

import glob
import os
import re

from mutagen.mp3 import EasyMP3 as MP3

root_path = os.environ["PHONE_MUSIC_PATH"]
filenames = glob.glob(root_path+'*/*/*.mp3')
title_check = re.compile('^\d{2}')

# print filenames


for fn in filenames:
  audio = MP3(fn)
  title = audio["title"][0]

  if audio.has_key("tracknumber"):
    track = audio["tracknumber"]
    if len(track):
      tracknumber = format(int(track[0].split('/')[0].encode('ascii','ignore')), '02d')

  # check if the track name has already been changed

  if tracknumber and not title_check.match(title):
    title = tracknumber + ' ' + title
    audio["title"] = title
    print "update "+title
    audio.save()
  
