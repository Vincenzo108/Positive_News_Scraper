# Positive-News-Scraper
A web scraper that finds positive news to help counter some of the negativity that comes from daily life.

## 1. Using feedparser to access the RSS feed.

<img width="439" height="148" alt="Screenshot 2026-10-15 095946" src="https://github.com/user-attachments/assets/d3e1ef4e-f81d-4c5a-bf81-38cfecec149a" />

I am using `feedparser` to access the RSS feed from [goodnewsnetwork.org](https://www.goodnewsnetwork.org/) where I will be pulling my daily good news from.
Make sure that the url is using the website's RSS url or it will not work.

## 2. Using datetime as a filter.
<img width="735" height="317" alt="Screenshot 2026-10-15 121536" src="https://github.com/user-attachments/assets/259766c9-269b-4116-9970-1e897aee054f" />

I am using `datetime` to filter the entries by only those whose publish dates are within 24 hours of running the program.

## 3. Using BeautifulSoup to clean up the summary.
<img width="730" height="517" alt="Screenshot 2026-10-15 123703" src="https://github.com/user-attachments/assets/1079c54d-0ac2-457f-b718-1d6adb8b733e" />

I am using `BeautifulSoup`, we can strip the HTML tags and entry summaries to deliver a cleaner and easier to read entry summary.

#### The final result is a program that prints news article titles, cleaned-up summaries, and the link to the full articles published within the last 24 hours using RSS feeds.
Example Output:
<img width="1521" height="297" alt="Screenshot 2026-10-16 121149" src="https://github.com/user-attachments/assets/4b964c00-505e-4729-8288-ed9a83f9afda" />
