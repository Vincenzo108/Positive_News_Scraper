import feedparser
from datetime import datetime, timedelta, timezone
from bs4 import BeautifulSoup

url = "News URL"
feed = feedparser.parse(url)

currDate = datetime.now(timezone.utc)
timeRange = timedelta(days=1)

for entry in feed.entries:
    publishDate = datetime.strptime(entry.published, "%a, %d, %b, %Y %H:%M:%S %z")
    if currDate - publishDate <= timeRange:

        cleanedSummary = BeautifulSoup(entry.summary)

        for paragraph in cleanedSummary.find_all("p"):
            if paragraph.get_text(" ", strip=True).startswith("The post"):
                paragraph.decompose()


        print (entry.title, ' ', entry.published)
        print (cleanedSummary.get_text(" ", strip=True))
        print (entry.link)
        print()