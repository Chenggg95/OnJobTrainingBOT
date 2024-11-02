import streamlit as st


st.set_page_config(layout="centered", page_title="About us")

st.title("About Us")

st.write(
    f"""We are Air Force Engineer from the Republic of Singapore Air Force.  Our primary job is to maintain and ensure that the aircraft is fit for flying to protect Singapore from adversary threats.
             The new maintenance crew members are required to learn the maintenance manual as part of their on-job training and induction to the maintenance flight.
             Currently, the crew members feel that the manual is hard to understand as there is too much content. Also, searching the manual to answer our doubt is very difficult as there is too much content to look through.
             Hence, the goal of this project is to make learning of the materials easier to understand for on job trainings. We are intending to use AI to accelerate their learnings, making the induction process easier."""
)
st.write(
    f"""The AI will answer questions from the OJTs when they ask anything related to the materials. E.g what are the dimensions of the F15-SG? The bot would answer accordingly. Since it’s an AI bot, if the user were to prompt “Quiz me anything about the Fuel/ECS system of the F15-SG”, the bot should be able to operate like a “quiz bot”, guiding the user on the correct answer and all that. Overall, this AI bot should be able to act like a teacher towards the user paraphrasing technical jargon, answering questions and quizzing would be the prime functions it should be able to execute."""
)
