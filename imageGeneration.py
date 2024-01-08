import time
import requests
from PIL import Image
from io import BytesIO

class ImageGeneration:
    def __init__(self, client):
        self.client = client

    def generateImageURLs(self, imagePrompts):
        imageURLs = []
        for i, promptText in enumerate(imagePrompts):
            response = self.client.images.generate(
                model="dall-e-2",
                prompt=promptText,
                size="1024x1024",
                quality="standard",
                n=1,
            )
            imageURLs.append(response.data[0].url)
            if i == 4:
                sleepTime = 30
                print(f"Sleeping for {sleepTime} seconds")
                time.sleep(sleepTime)
        
        return imageURLs

    def fetchImageFromURL(self, imagePrompts):
        allImages = []
        imageURLs = self.generateImageURLs(imagePrompts)
        for url in imageURLs:
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            allImages.append(img)

        return allImages