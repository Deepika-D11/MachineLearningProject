
import streamlit as st
from chatbot import chatbot
from death_rates import death_rates
from Emotion_Detection import emotion_detection
from hate_speech import hate_speech
from World_GDP import world_gdp

# Main Streamlit app layout
st.title("Multi-Project Dashboard")

# Sidebar for navigation
option = st.sidebar.selectbox("Choose a project",
                              ["Chatbot", "Death Rates", "Emotion Detection", "Hate Speech Detection", "World GDP"])

# Display content based on selection
if option == "Chatbot":
    chatbot.main()  # Call main function of chatbot
elif option == "Death Rates":
    death_rates.main()  # Call main function of death rates
elif option == "Emotion Detection":
    emotion_detection.main()  # Call main function of emotion detection
elif option == "Hate Speech Detection":
    hate_speech.main()  # Call main function of hate speech detection
elif option == "World GDP":
    world_gdp.main()  # Call main function of world GDP
