import cv2
import numpy as np


def load_and_display_image(filename):
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def process_image(filename):
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    print(img.shape)
    longueur, largeur, _ = img.shape
    matricederotation = cv2.getRotationMatrix2D((longueur, largeur / 2), 90, 1)
    dst = cv2.warpAffine(img, matricederotation, (longueur, largeur))
    cv2.imshow('image', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def translation_image(filename):
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    hauteur, longueur, _ = img.shape
    M = np.float32([[1, 0, 100], [0, 1, 50]])
    dst = cv2.warpAffine(img, M, (longueur + 100, hauteur + 50))
    cv2.imshow('img', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
