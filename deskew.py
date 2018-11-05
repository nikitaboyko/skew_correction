from skew_detection import detect_skew
from skimage import io
import optparse,json
import numpy as np
import matplotlib.pyplot as plt
# from skew_detect import SkewDetect
from skimage import io
from skimage.transform import rotate

"""
importing config.json
"""
with open('config.json', 'r') as f:
    config = json.load(f)

class Deskew:

    def __init__(self, input_file_path, display_image, output_file_path, rot_angle = 0):

        self.input_file_path = input_file_path
        self.display_image = display_image
        self.output_file_path = output_file_path
        self.rot_angle = rot_angle
        self.skew_obj = detect_skew(self.input_file_path)

    def deskew(self):
        global config
        debug = config['debug']
        img = io.imread(self.input_file_path)
        res = self.skew_obj.process_file()
        if debug: print(res)
        angle = res['Estimated Angle']
        if angle >= 0 and angle <= 90:
            rot_angle = angle - 90 + self.rot_angle
        if angle >= -45 and angle < 0:
            rot_angle = angle - 90 + self.rot_angle
        if angle >= -90 and angle < -45:
            rot_angle = 90 + angle + self.rot_angle

        rotated = rotate(img, rot_angle, resize=True)

        if self.display_image:
            self.display(rotated)

        if self.output_file_path:
            self.saveImage(rotated*255)

    def saveImage(self, img):
        path = self.skew_obj.check_path_exists(self.output_file_path)
        io.imsave(path, img.astype(np.uint8))

    def display(self, img):

        plt.imshow(img)
        plt.show()

    def run(self):

        if self.input_file_path:
            self.deskew()


if __name__ == '__main__':

    parser = optparse.OptionParser()

    parser.add_option(
        '-i',
        '--input',
        default=None,
        dest='input_file_path',
        help='Input file name')
    parser.add_option(
        '-d', '--display',
        default=None,
        dest='display_image',
        help="display the rotated image")
    parser.add_option(
        '-o', '--output',
        default=None,
        dest='output_file_path',
        help='Output file name')
    parser.add_option(
        '-r', '--rotate',
        default=0,
        dest='rot_angle',
        help='Rotate the image to desired axis',
        type=int)
    options, args = parser.parse_args()
    deskew_obj = Deskew(
        options.input_file_path,
        options.display_image,
        options.output_file_path,
        options.rot_angle)

    deskew_obj.run()
