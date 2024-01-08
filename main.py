import os
from openai import OpenAI
from fetchResearchPaper import FetchResearchPaper
from abstractSegmentation import AbstractSegmentation
from imagePromptGeneration import ImagePromptGeneration
from imageGeneration import ImageGeneration
from textToSpeech import TextToSpeech
from videoGeneration import VideoGeneration

class ResearchGAN:
    def __init__(self):
        self.client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
    
    def generate(self):
        fetchResearchPaperObject = FetchResearchPaper()
        researchPaperTitle, researchPaperSummary = fetchResearchPaperObject.fetchResearchPaper()

        abstractSegmentationObject = AbstractSegmentation(self.client)
        abstractPoints = abstractSegmentationObject.generateAbstractPoints(researchPaperTitle, researchPaperSummary)

        imagePromptGenerationObject = ImagePromptGeneration(self.client)
        imagePrompts = imagePromptGenerationObject.generateImagePrompts(abstractPoints)

        imageGenerationObject = ImageGeneration(self.client)
        generatedImages = imageGenerationObject.fetchImageFromURL(imagePrompts)

        textToSpeechObject = TextToSpeech(self.client, abstractPoints, researchPaperTitle)
        textToSpeechObject.generateSpeechFromText()
        audioDuration = textToSpeechObject.getAudioDuration()

        videoGenerationObject = VideoGeneration(audioDuration)
        videoGenerationObject.combineImages(generatedImages)
        videoGenerationObject.overlayAudioOnVideo()

researchGANObject = ResearchGAN()
researchGANObject.generate()






