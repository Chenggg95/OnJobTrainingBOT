from helper_functions import llm
from langchain.retrievers.multi_query import MultiQueryRetriever
from document import documentloader
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import random

from dotenv import load_dotenv
import os
import streamlit as st

if load_dotenv('.env'):
   # for local development
   OPENAI_KEY = os.getenv('OPENAI_API_KEY')
else:
   OPENAI_KEY = st.secrets['OPENAI_API_KEY']

chat = ChatOpenAI(api_key=os.getenv('OPENAI_API_KEY'), 
                  openai_api_base="https://litellm.govtext.gov.sg/",
                  model='gpt-4o-prd-gcc2-lb', 
                  temperature=0.1, 
                  default_headers={"user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/81.0"})
vectordb = documentloader.load_and_split_document()
retriever_multiquery = MultiQueryRetriever.from_llm(retriever=vectordb.as_retriever(), llm = chat)
qa_chain_multiquery= RetrievalQA.from_llm(
    retriever=retriever_multiquery,
    llm = chat
)

def answer_user_question(question):
    print("answering user question")
    delimiter = "```"
    response = qa_chain_multiquery.invoke(question)
    
    #system_message = f"""Based on the following context, answer this question: {context} \nQuestion: {question}"""

    # messages =  [
    #     {'role':'system',
    #     'content': system_message},
    #     {'role':'user',
    #     'content': f"{delimiter}{question}{delimiter}"},
    # ]

    # response = llm.get_completion_by_messages(messages)
    return response.get("result")

def generate_questions_from_document():
    print("generating question")
    documents = vectordb.similarity_search(" ", k=5)
    document_content = " ".join(doc.page_content for doc in documents)
    # Prepare the prompt for question generation
    delimiter = "```"
    # Introduce some randomness in the prompt for different questions each time
    variations = [
        "Generate a question based on the following content:",
        "Create an insightful question from this content:",
        "What question could we ask from this content?",
    ]
    
    prompt_intro = random.choice(variations)  # Choose a random intro for the prompt
    message = f"{prompt_intro}\n\n{document_content}\n\nQuestion:"
    messages = [
        {
            'role': 'user',
            'content': f"{delimiter}{message}{delimiter}"
        },
            ]
    
    response = llm.get_completion_by_messages(messages)
    return response

def check_answer(question, user_answer):
    delimiter = "```"
    message = f"Is the following answer correct for the question: '{question}'? If the user's answer is wrong, please provide the correct answer.\nUser's answer: {user_answer}\n"
    messages = [
        {
            'role': 'user',
            'content': f"{delimiter}{message}{delimiter}"
        },
            ]
    
    response = llm.get_completion_by_messages(messages)
    return response