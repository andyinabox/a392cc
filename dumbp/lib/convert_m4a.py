# go through source folder and convert all .m4a files
# to mp3

import glob
import os

from ffmpy import FFmpeg

root_path = os.environ["PHONE_MUSIC_PATH"]
glob_path = root_path + "*/*/*.m4a"

def m4a2mp3(f):
  input_path = f
  output_path = f.replace('m4a', 'mp3')
  ff = FFmpeg(
    inputs = { input_path : None },
    outputs = { output_path : '-acodec libmp3lame -ab 128k'}
  )
  print ff.cmd
  ff.run()

m4as = glob.glob(glob_path)

for f in m4as:
  m4a2mp3(f)

