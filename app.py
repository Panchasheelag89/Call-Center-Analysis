import streamlit as st, asyncio
from transcription import transcribe_audio
from diarization import diarize_audio
from sentiment_analysis import analyze_sentiment
from topic_classification import classify_topics
from gemini_utils import generate_summary

st.title("📞 Call Center Analysis Dashboard")
uploaded_file = st.file_uploader("Upload Call Recording", type=["mp3","wav","m4a"])

if uploaded_file:
    audio_path="temp_audio.m4a"
    with open(audio_path,"wb") as f: f.write(uploaded_file.read())
    
    transcript = asyncio.run(transcribe_audio(audio_path))
    diarization = asyncio.run(diarize_audio(audio_path))
    sentiment = analyze_sentiment(transcript)
    topics = classify_topics([transcript])
    summary = generate_summary(transcript)
    
    st.subheader("Transcript"); st.write(transcript)
    st.subheader("Diarization"); st.write(diarization)
    st.subheader("Sentiment"); st.write(sentiment)
    st.subheader("Topics"); st.write(topics)
    st.subheader("Summary"); st.write(summary)
