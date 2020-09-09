from google import GoogleKeywordScreenshooter
from responsive import ResponsiveScreenShot
#g = GoogleKeywordScreenshooter("coldplay", "screenshots", 3)

# g.start()
# g.finish()

r = ResponsiveScreenShot(urls=["https://nomadcoders.co/"])
r.start()
r.finish()
