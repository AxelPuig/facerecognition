import cv2
import numpy as np
from imutils import paths
import face_recognition_models
import argparse
import pickle
import os


ap= argparse.ArgumentParser()
ap.add_argument("-i","--dataset",required=True,
        help="path to input directory of faces + images")
ap.add_argument("--e","--encodings",required=True,
                help="path to serialized db of facial encodings")
ap.add_argument("-d","--detection-method",type=str,default="cnn",
                help="face detection model to use: either 'hog' or 'cnn'")
args = vars(ap.parse_args())
