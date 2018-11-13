import cv2

def load_and_display_image(filename):
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()