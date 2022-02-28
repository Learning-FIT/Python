import sys
import os
import cv2

def main():
    if len(sys.argv) == 3:
        image_file = sys.argv[1]
        if not os.path.exists(image_file):
            print('指定されたファイルが見つかりません')
            exit(2)

        try:
            rotate = float(sys.argv[2])
        except ValueError as e:
            print(e)
            exit(3)
    else:
        print('usage: python rotate.py 画像ファイルパス 回転度数')
        exit(1)

    image = cv2.imread(image_file)

    center = (image.shape[1] / 2, image.shape[0] / 2)
    size = (image.shape[1], image.shape[0])

    rotate = cv2.getRotationMatrix2D(center, rotate, 1.0)
    image_rotate = cv2.warpAffine(image, rotate, size, flags=cv2.INTER_CUBIC)

    cv2.imwrite('rotate.jpg', image_rotate)

if __name__ == '__main__':
    main()
