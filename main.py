import streamlit as st
import os
from langchain.llms import OpenAI
from langchain.agents import AgentExecutor, AgentType, initialize_agent, load_tools  # type: ignore
from langchain.tools import BaseTool
from typing import List



def main():
    st.title("Fraud Sheild")
    search = st.text_input("Identify Financial Faudulent News")
    
    if st.button("Search"):
        res = fraud(search)
        if res == "Scam":
            st.error(res)
        else:
            st.success(res)
    
def fraud(search):
     # Create a new instance of the OpenAI class
    llm = OpenAI(
        openai_api_key=st.secrets["OPENAI_API_KEY"],
        max_tokens=200,
        temperature=0,
        client=None,
        model="text-davinci-003",
        frequency_penalty=1,
        presence_penalty=0,
        top_p=1,
    )

    # Load the tools
    tools: List[BaseTool] = load_tools(["google-serper"], llm=llm)

    # Create a new instance of the AgentExecutor class
    agent: AgentExecutor = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=False,
    )

    # Create the template
    template = """Analyze this message : {topic} in all social media apps . Give me the profile id of the person who posted this message."""

    # Generate the response
    response: str = agent.run(template.format(topic=search))

    # Print the response
    print(response)

    # # Convert the response to a dictionary
    # result = json.loads(response)

    return response



if __name__ == "__main__":
    main()