from podgen import Podcast, Episode, Media
from datetime import timedelta
# Create the Podcast
p = Podcast(
   name="Chapo Cheaters Club",
   description="Just taking"
               "what isn't mine",
   website="http://www.not-even-real.com",
   explicit=False,
)

p.image = "http://192.168.1.115:8000/logo.jpg"

p.episodes += [
   Episode(
     title="clover wish",
     media=Media("http://192.168.1.115:8000/fake_podcast.mp3",size=11680472,
                       duration=timedelta(minutes=4, seconds=36)), 
     summary="Text",
   ),

   Episode(
     title="Chapo Traphouse 471",
     media=Media("http://192.168.1.115:8000/CTH471_edit_mixdown.output.mp3", size=70623031,
                       duration=timedelta(hours=1, minutes=38, seconds=4)),
     summary="Thanks Lars",
   ),

      Episode(
     title="Heavenly Caffeteria",
     
     media=Media("http://192.168.1.115:8000/caffeteria.mp3", size=2979885,
                       duration=timedelta(minutes=1, seconds=29)),
     summary="bunny go fuwafuwa",
   ),
]


rss = p.rss_str()
p.rss_file('assets/rss.xml') #, minimize=True)
