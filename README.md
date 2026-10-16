# Positive-News-Scraper
A web scraper that finds positive news to help counter some of the negativity that comes from daily life.

## 1. Using feedparser to access the RSS feed.

<img width="439" height="148" alt="Screenshot 2026-10-15 095946" src="https://github.com/user-attachments/assets/a3896837-e0fe-4b59-a5b3-0f6099cd39b6" />

I am using `feedparser` to access the RSS feed from [goodnewsnetwork.org](https://www.goodnewsnetwork.org/) where I will be pulling my daily good news from.

## 2. Using datetime as a filter.
<img width="735" height="317" alt="Screenshot 2026-10-15 121536" src="https://github.com/user-attachments/assets/2caf6453-d323-4368-8b9a-3159cd7f4aa7" />

I am using `datetime` to filter the entries by only those whose publish dates are within 24 hours of running the program.

## 3. Using BeautifulSoup to clean up the summary.
<img width="730" height="517" alt="Screenshot 2026-10-15 123703" src="https://github.com/user-attachments/assets/22dd0067-3fff-4019-b3d3-204d25d61cdd" />

I am using `BeautifulSoup`, we can strip the HTML tags and entry summaries to deliver a cleaner and easier to read entry summary.

#### The final result is a program that prints news article titles, cleaned-up summaries, and the link to the full articles published within the last 24 hours using RSS feeds.
