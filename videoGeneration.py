import math
import numpy as np
from moviepy.editor import concatenate, ImageClip, VideoFileClip, AudioFileClip, CompositeAudioClip

class VideoGeneration:
    def __init__(self, audioDuration):
        self.audioDuration = audioDuration

    def combineImages(self, generatedImages):
        clips = []

        for i in range(int(self.audioDuration // 40)):
            for image in generatedImages:
                clips.append(ImageClip(np.array(image)).set_duration(3))

        for i in range(math.ceil((self.audioDuration % 40) / 4)):
            clips.append(ImageClip(np.array(generatedImages[i])).set_duration(3))

        video = concatenate(clips, method="compose")
        video.write_videofile('plainVideo.mp4', fps=24)

    def overlayAudioOnVideo(self):
        videoclip = VideoFileClip("./plainVideo.mp4")
        audioclip = AudioFileClip("./speech.mp3")

        new_audioclip = CompositeAudioClip([audioclip])
        videoclip.audio = new_audioclip
        videoclip.write_videofile("output.mp4")