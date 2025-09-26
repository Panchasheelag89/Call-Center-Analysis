import os
import asyncio
from deepgram import Deepgram
from dotenv import load_dotenv

load_dotenv()
DG_KEY = os.getenv("DEEPGRAM_API_KEY")
dg_client = Deepgram(DG_KEY)

async def diarize_audio(audio_path):
    """Audio me speakers ko alag kar ke return karta hai"""
    try:
        with open(audio_path, "rb") as f:
            source = {"buffer": f, "mimetype": "audio/m4a"}
            options = {"punctuate": True, "diarize": True, "model": "nova"}
            response = await dg_client.transcription.prerecorded(source, options)
            return response  # poora response, jisme speaker info hai
    except Exception as e:
        print("Diarization failed:", e)
        return None
