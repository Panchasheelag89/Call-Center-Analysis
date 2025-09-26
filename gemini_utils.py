import asyncio
from transcription import transcribe_audio
from diarization import diarize_audio
from sentiment_analysis import analyze_sentiment
from topic_classification import classify_topics
from transformers import pipeline

summarizer=pipeline("summarization")

def generate_summary(text):
    return summarizer(text, max_length=100, min_length=30, do_sample=False)[0]['summary_text']

audio_path = r'D:\Call Center Analysis\AUDIO-File.m4a'

async def main():
    transcript = await transcribe_audio(audio_path)
    diarization = await diarize_audio(audio_path)
    sentiment = analyze_sentiment(transcript)
    topics = classify_topics([transcript])
    summary = generate_summary(transcript)
    
    print("Transcript:", transcript)
    print("Diarization:", diarization)
    print("Sentiment:", sentiment)
    print("Topics:", topics)
    print("Summary:", summary)

asyncio.run(main())
