import asyncio
import os
from deepgram import Deepgram
from dotenv import load_dotenv

load_dotenv() #env file se variables ko Python ke environment me load karta hai, taki hum unhe os.getenv() se use kar saken.
DG_key = os.getenv('DEEPGRAM_API_KEY')
dg_client = Deepgram(DG_key)

audio_path = r'D:\Call Center Analysis\AUDIO-File.m4a'

async def transcribe_audio(audio_path):
    try:
        with open(audio_path, 'rb') as f:
            source = {'buffer':f, 'mimetype':'audio/m4a'}
            options = {'punctuate':True, 'model':'nova'}
            response = await dg_client.transcription.prerecorded(source, options)
            transcript = response['results']['channels'][0]['alternatives'][0]['transcript']
            return transcript

    except exception as e:
        print('Transcription failed',e)   
        return" "


