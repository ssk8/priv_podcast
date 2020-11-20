from podgen import Podcast, Episode, Media
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from datetime import timedelta
import os

host_address = "http://192.168.1.136:8000/"
base_dir = "/home/pi/priv_podcast"
pod_dir ="assets"

def find_pods():
    file_list = [f for f in os.listdir(os.path.join(base_dir, pod_dir)) if
            f.endswith('.mp3')]
    return sorted(file_list)


p = Podcast(
   name="Chapo Cheaters Club",
   description="Just taking"
               "what isn't mine",
   website=host_address,
   explicit=False,
)

p.image = host_address + "logo.jpg"

for pod in find_pods():
    audio = MP3(os.path.join(base_dir, pod_dir, pod), ID3=EasyID3)
    title = audio["title"]
    size = os.path.getsize(os.path.join(base_dir, pod_dir, pod))
    duration = timedelta(seconds=audio.info.length)
    print(f'{pod}, {title}, {size}, {duration}')
    p.episodes += [Episode(title=title, media=Media(f"{host_address}{pod}", size=size, duration=duration), summary="summary goes here")]

rss = p.rss_str()
p.rss_file(os.path.join(base_dir, pod_dir, 'rss.xml'))
