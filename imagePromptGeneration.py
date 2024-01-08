import re

class ImagePromptGeneration:
    def __init__(self, client):
        self.client = client
    
    def promptsProcessing(self, prompts):
        allImagePrompts = []
        # Your input text
        input_text = prompts # Replace with your actual text

        # Regular expression to match lines starting with 'Generate'
        pattern = r"Generate.*"

        # Find all matches
        matches = re.findall(pattern, input_text)

        # Printing or processing the matches
        for match in matches:
            allImagePrompts.append(match)
        
        return allImagePrompts

    def generateImagePrompts(self, abstractPoints):
        imagePrompts = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """You are a prompt generator assistant for my DALL-E text to image model, skilled in generating suitable and correct
                prompts for any text given you. When given a series of texts, you have to generate a DALL-E image prompt 
                for each of the given points in the text.
                The format for your response for each prompt is fixed and given below:
                Prompt: The prompt text beginning with 'Generate an image'"""},
                {"role": "user", "content": abstractPoints}
            ]
        )

        imagePromptsText = imagePrompts.choices[0].message.content
        processedPrompts = self.promptsProcessing(imagePromptsText)

        return processedPrompts
