**Fraud Shield**
This Streamlit app allows users to identify potentially fraudulent financial news articles.

**Features:**
- Text input for entering news article or headline.
- Clickable button to initiate the search.
- Automatic analysis of the input text using OpenAI language model.
- Identification of potentially fraudulent content based on analysis.
- Differentiates between "Scam" and other types of content.
- Utilizes Google SERP tool for additional analysis.

**Usage:**
1. Enter the text of the news article or headline in the provided text input field.
2. Click the "Search" button to initiate the analysis.
3. The app will provide feedback indicating whether the content is identified as a "Scam" or not.

**Dependencies:**
- Streamlit
- LangChain (including llms, agents, and tools modules)
- OpenAI API key (stored securely using Streamlit Secrets)
- Google SERP tool for additional analysis

**Setup:**
1. Install the required dependencies.
2. Obtain an OpenAI API key and store it securely in Streamlit Secrets.
3. Ensure access to Google SERP tool.
4. Run the Python script to start the Streamlit app.

**Credits:**
This code was created by Raj Narayanan

**Github:**
[https://github.com/raju-2003](https://github.com/raju-2003)

**Explore and identify potentially fraudulent financial news articles with Fraud Shield!**
