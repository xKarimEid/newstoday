
def create_prompt(user_question):
    prompt = f"""
        The table articles is created the following way:

        CREATE TABLE IF NOT EXISTS articles
                        (article_id INTEGER PRIMARY KEY,
                        event_datetime datetime NOT NULL, 
                        header TEXT UNIQUE,
                        newspaper text NOT NULL, 
                        url text UNIQUE,
                        article text NOT NULL)
                        '''
        Data is inserted into the table from different newspapers. 
        
        A query will fetch all the relevant rows from the table and a LLM will process the article to see if the article
        contains an answer to the users question. 
        Create the query that fetches the relevant rows to be processed by an LLM to answer the following question:

        {user_question}
        """
    return prompt

def call_model(model, prompt):
    resp = model.generate_content(prompt)
    query = resp.text
    
