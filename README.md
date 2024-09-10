Hi, this is my private repo for learning about RAG!

The setup for this repo:
    1) Web scrape articles from vg.no
    2) store scraped articles in a db
    3) Create embedding vectors for the stored articles and store them in db

UI workflow

User asks question about articles
user question embeddings are generated
a vector search is done to see if any document matches the question
The closest n documents are pulled out and used to generate the respone


Example:

User asks:

Did vg write any articles regarding the police today?

user question is embedded
vector search is done
Closest articles are found
answered based on closest articles