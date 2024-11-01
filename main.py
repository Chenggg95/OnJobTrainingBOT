import streamlit as st
from helper_functions import llm
from helper_functions.utility import check_password
from logics import queryhandler

# Check if the password is correct.  
if not check_password():  
    st.stop()

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="On Job Training Material Website"
)
# endregion <--------- Streamlit App Configuration --------->
st.title("On Job Training Material Website")
feature = st.radio("Select an option:", ("Ask a question", "Generate questions from the document"))

if feature == "Ask a question":
        user_question = st.text_input("What is your question?")
        if st.button("Get Answer"):
            answer = queryhandler.answer_user_question(user_question)
            st.write("Answer:", answer)

elif feature == "Generate questions from the document":
    # Button to generate a question
    if st.button("Generate Question"):
        question = queryhandler.generate_questions_from_document()
        st.session_state['generated_question'] = question  # Store question in session state

    # Display the generated question if it exists in session state
    if 'generated_question' in st.session_state:
        st.write("Generated Question:")
        st.subheader(f"Question: {st.session_state['generated_question']}")
        
        # User input for their answer
        user_answer = st.text_input("Your Answer:")

        # Button to submit the answer
        if st.button("Check Answer"):
            # Retrieve the stored question for checking
            question = st.session_state['generated_question']
            # Check the answer using the AI
            result = queryhandler.check_answer(question, user_answer)
            st.write("Answer: ", result)
                