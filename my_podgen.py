from podgen import Podcast, Episode, Media
# Create the Podcast
p = Podcast(
   name="365 days of plops",
   description="Every shit I take "
               "you get to hear it",
   website="http://example.org/animals-alphabetically",
   explicit=False,
)

p.image = "https://github.com/ssk8/365days_of_plops/raw/main/pooping.jpg"

p.episodes += [
   Episode(
     title="Title",
     media=Media("https://wwww.com", 11932295),
     summary="Text",
   ),

   Episode(
     title="Title",
     media=Media("https://wwww.com", 11932295),
     summary="Text",
   ),

      Episode(
     title="Title",
     media=Media("https://wwww.com", 11932295),
     summary="Text",
   ),
]


rss = p.rss_str()
p.rss_file('rss.xml') #, minimize=True)