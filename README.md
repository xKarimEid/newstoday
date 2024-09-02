Hi, this is my private repo for learning how to webscrape!

Web scrape articles of vg.no
Take one article and summarize it using gemini


General thought:

Scrape newspages for articles, store them in sqlite

User asks:

Did vg write any articles regarding the police today?

LLM

Here is the table of articles stores in SQLlite, write a query that filters the rows that will be fed into a LLM which will get the information the user is asking about. 

Get query from LLM

Perform query on database

for each row in the query ask the LLM if it contains information relevant to what the user is asking. 

Components:

chatcomponent (frontend)
sqlite
LLM (API)
orchestrator (templates)
Scraper