# Video Split Tool

![](https://img.shields.io/badge/dependencies-python3.7-blue)

## Introduction
This is a small tool for video cropping which will separate the original video into frame images

## Requirements
```bash
$ pip install -r requirements.txt
```

## Usage
Use `--help` to get information about arguments
```bash
$ python Split.py --help
```
```angular2html
optional arguments:
  -h, --help       show this help message and exit
  --source SOURCE  input video source
  --target TARGET  input dir that save the frame images
  --frame FRAME    input the frequency to save frame images(default 10)
```
Input arguments(Example)
```bash
$ python Split.py --source Source --target Target --frame 100
```
