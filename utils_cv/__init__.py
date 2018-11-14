import cv2


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
