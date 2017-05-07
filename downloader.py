import argparse
import shutil
import urllib.request
from os import path

from pythonopensubtitles.opensubtitles import OpenSubtitles
from pythonopensubtitles.utils import File

parser = argparse.ArgumentParser()
parser.add_argument("path", help="Give the path of movie", type=str)
args = parser.parse_args()
head, tail = path.split(args.path)
head += "/"
username = "arp009"
password = "adminadmin123"
paths = head
video = tail
os = OpenSubtitles()
token = os.login(username, password)

f = File(path.join(paths, video))
hash = f.get_hash()

size = f.size

data = os.search_subtitles([{'sublanguageid': 'english', 'moviehash': hash, 'moviebytesize': size}])

down_url = data[0]["SubDownloadLink"]
file_name = data[0]["SubFileName"] + ".zip"

urllib.request.urlretrieve(down_url, file_name)

shutil.move(file_name, paths + file_name)

os.logout()
