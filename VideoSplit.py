import cv2
from PIL import Image
import os


class VideoSplit:
    def __init__(self, sourcePath, targetPath, defaultFrame=10):
        """
        Video Split Class

        :param sourcePath: The path of your original video
        :param targetPath: The path you want to save your frame images
        :param defaultFrame: The frequency that you want to save frame images
        """
        assert os.path.isfile(sourcePath), "Source video doesn't exist!"
        try:
            if not os.path.exists(targetPath):
                os.mkdir(targetPath)
        except FileNotFoundError:
            print("False target path!")
        self.sourcePath = sourcePath
        self.targetPath = targetPath
        self.defaultFrame = defaultFrame
        self.camera = cv2.VideoCapture(self.sourcePath)

    def split(self):
        """
        Split the original video into frame
        """
        self.showResolution()
        frameCounter = 0
        imgCounter = 0
        while True:
            _, frame_lwpCV = self.camera.read()
            if frame_lwpCV is None:
                break
            if frameCounter % self.defaultFrame == 0:
                # Save img
                print('saving frame:%s' % frameCounter)
                im_pil = cv2.cvtColor(frame_lwpCV, cv2.COLOR_BGR2RGB)
                im_new = Image.fromarray(im_pil)
                sourceName = os.path.basename(self.sourcePath)
                sourceName = sourceName.split('.')
                savePath = self.targetPath + '\\%s%s.jpg' % (sourceName[0], frameCounter)
                im_new.save(savePath)
                imgCounter += 1
            frameCounter += 1

        print(str(imgCounter) + ' frame images was saved!')

    def showResolution(self):
        """
        Show resolution of your original video

        :return: resolution of your original video
        """
        size = (int(self.camera.get(cv2.CAP_PROP_FRAME_WIDTH)),
                int(self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        print('The Resolution of video is :' + repr(size))

        return repr(size)
