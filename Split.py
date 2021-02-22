from VideoSplit import VideoSplit
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, help='input video source')
    parser.add_argument('--target', type=str, help='input dir that save the frame images')
    parser.add_argument('--frame', type=int, default=10, help='input the frequency to save frame images(default 10)')
    opt = parser.parse_args()

    videoSplit = VideoSplit(opt.source, opt.target, opt.frame)
    videoSplit.split()
