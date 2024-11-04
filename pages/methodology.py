import streamlit as st
import streamlit.components.v1 as components

# Load the HTML content
flow_chart_1_path = "pages/FlowChart1.html"
flow_chart_2_path = "pages/FlowChart2.html"
with open(flow_chart_1_path, "r") as html_file1, open(flow_chart_2_path, "r") as html_file2:
    html_content_flow_chart_1 = html_file1.read()
    html_content_flow_chart_2 = html_file2.read()
st.title("Methodology")
st.write(f"""This program outlines the approach for developing a two feature AI application, which are conservative answer generation and an interactive questionnaire functionality. The application leverages a vector database (vectordb) to store and retrieve document content for question answering and question generation.""")
         
st.write(f"""1. Feature 1: User-Generated Question Answering
            Objective: To provide comprehensive, fact-based answers to user questions related to the document without creativity or speculation.
            Approach:
            User Input: The user inputs a question.
            Answer Generation:
            The AI uses the vectordb where document embeddings are stored to retrieve relevant sections for answering.
            A low creativity parameter (temperature = 0) is set for the model to ensure that responses are factual and conservative, directly referencing the document’s content without creative embellishments.
            Using similarity search, the AI fetches document excerpts that closely align with the user’s question.
            Response Output: The AI synthesizes a response by summarizing relevant sections, ensuring it aligns strictly with the document's content. This answer is then returned to the user.
            Benefits: Ensures accurate and document-bound answers, suitable for factual and reference-based applications.""")

st.write(f"""2. Feature 2: Interactive Questionnaire
                Objective: To engage the user with dynamically generated questions based on the document content and evaluate the correctness of user-provided answers.
                Approach:
                Question Generation:
                The user initiates question generation by clicking the "Generate Question" button.
                Keyword Arrays: An array of keywords is defined to enable varied document section retrieval.
                Prompt Arrays: A set of predefined prompts introduces diversity in how questions are framed.
                To generate a question, a keyword is selected randomly from the keyword array. This keyword is used to perform a similarity_search in the vectordb, retrieving different parts of the document based on the keyword.
                A prompt is then randomly selected from the prompt array and combined with the retrieved content to formulate a unique question.
                Answer Verification:
                The user submits an answer to the generated question.
                The AI evaluates the answer by comparing it to the document content retrieved in the question generation phase.
                Feedback is provided, indicating whether the answer is correct or incorrect based on similarity scoring or strict text matching.
                Iteration: Each question generated varies due to the random selection of keywords and prompts, enabling a broad coverage of the document’s content in the questions.
                Benefits: Allows for diverse questioning and robust answer checking, enhancing user engagement and understanding of the document.""")
# Create two columns
col1, col2 = st.columns(2)

# Display each workflow in a separate column
with col1:
    st.header("Workflow 1")
    components.html(html_content_flow_chart_1, height=600, scrolling=True)

with col2:
    st.header("Workflow 2")
    components.html(html_content_flow_chart_2, height=600, scrolling=True)
