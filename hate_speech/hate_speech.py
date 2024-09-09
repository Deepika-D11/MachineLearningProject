import streamlit as st
from pysentimiento import create_analyzer
import matplotlib.pyplot as plt

# Initialize analyzers
emotion_analyzer = create_analyzer(task='emotion', lang='en')
hate_speech_analyzer = create_analyzer(task='hate_speech', lang='en')

# Function for emotion detection
def emotion_detection(text):
    result = emotion_analyzer.predict(text)
    return result.output, result.probas

# Function for hate speech detection
def hatespeech_detection(text):
    result = hate_speech_analyzer.predict(text)
    return result.probas

# Mapping emotions to emojis
emotion_emoji = {
    "joy": "😊",
    "sadness": "😢",
    "anger": "😠",
    "surprise": "😲",
    "disgust": "🤢",
    "fear": "😨",
    "neutral": "😐"
}

# Main function to be called in the Streamlit app
def main():
    st.title("Sentiment and Hate Speech Detection")

    # Text input
    text_input = st.text_area("Enter your text here:", "")

    if st.button('Analyze'):
        if text_input:
            # Analyze emotion
            emotion, emotion_probas = emotion_detection(text_input)
            # Analyze hate speech
            hate_speech_probas = hatespeech_detection(text_input)

            # Display emotion results with emojis
            st.subheader("Emotion Analysis")
            emoji_display = emotion_emoji.get(emotion, "😐")
            st.markdown(f"**Emotion Detected:** {emotion.capitalize()} {emoji_display}")
            st.bar_chart(emotion_probas)  # Show probabilities as a bar chart

            # Display hate speech results
            st.subheader("Hate Speech Analysis")
            hate_speech_labels = ["Not Hate Speech", "Hate Speech"]
            hate_speech_probabilities = [hate_speech_probas["NOT_HS"], hate_speech_probas["HS"]]

            fig, ax = plt.subplots()
            ax.barh(hate_speech_labels, hate_speech_probabilities, color=["green", "red"])
            ax.set_xlim(0, 1)
            ax.set_xlabel("Probability")
            st.pyplot(fig)

            # Show detailed probabilities
            st.write(f"**Not Hate Speech Probability:** {hate_speech_probas['NOT_HS']:.2f}")
            st.write(f"**Hate Speech Probability:** {hate_speech_probas['HS']:.2f}")
        else:
            st.write("Please enter some text to analyze.")

# Ensure that main() is called when this script is executed
if __name__ == '__main__':
    main()
