from pydub import AudioSegment

class TextToSpeech:
    def __init__(self, client, abstractPoints, researchPaperTitle):
        self.client = client
        self.abstractPoints = abstractPoints
        self.researchPaperTitle = researchPaperTitle

    def generateVoiceoverScript(self):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """You are a research scientist assistant, skilled in explaining complex academic \\
                concepts with simplicity and creative flair. When given the title and key points from any academic 
                research paper, you are able to create a short voiceover script of about 1 minute 30 seconds in the style of David Attenborough. You must 
                only provide the content for the voiceover, nothing else in your response like background music or the name of David David Attenborough. 
                You must generate the script with around 300 words only."""},
                {"role": "user", "content": """Title: """ + self.researchPaperTitle + """ \n"""
                """Key Points: """ + self.abstractPoints}
            ]
        )

        voiceoverScript = completion.choices[0].message.content
        return voiceoverScript


    def generateSpeechFromText(self):
        speech_file_path = "./speech.mp3"
        voiceoverScript = self.generateVoiceoverScript()
        response = self.client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=voiceoverScript
        )

        response.stream_to_file(speech_file_path)

    def getAudioDuration(self):
        # Load your MP3 file
        audio = AudioSegment.from_mp3("./speech.mp3")

        # Calculate the duration in milliseconds
        durationMilliseconds = len(audio)

        # Convert the duration to seconds
        durationSeconds = durationMilliseconds / 1000

        return durationSeconds