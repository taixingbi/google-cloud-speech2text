import os
import io

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/h/kindom/Kaden-API-a97f83b977be.json"

from google.cloud import speech
client = speech.SpeechClient()
print("client", client)

# gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"
# audio = speech.RecognitionAudio(uri=gcs_uri)

# speech_file= "data/demo.wav"
speech_file= "data/00.wav"

with io.open(speech_file, "rb") as audio_file:
    content = audio_file.read()

audio = speech.RecognitionAudio(content=content)

config = speech.RecognitionConfig(
    # encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code="en-US",
)

response = client.recognize(config=config, audio=audio)

for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))

print("done")