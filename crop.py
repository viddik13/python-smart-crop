import os
import argparse

from smartcrop import smart_crop


def main(image_file_path, crop_width, crop_height, output_folder_cropped_image):
    if os.path.isfile(image_file_path): # Does bob.txt exist?  Is it a file, or a directory?
        filename = os.path.basename(image_file_path)
        outpath = os.path.join(output_folder_cropped_image, filename)
        smart_crop(image_file_path, crop_width, crop_height, outpath, False)

    elif os.path.isdir(image_file_path):
        with os.scandir(image_file_path) as it:
            for image_file in it:
                outpath = os.path.join(output_folder_cropped_image, image_file.name)
                smart_crop(image_file.path, crop_width, crop_height, outpath, False)

    else:
        print("Error: input path not a file or directory?")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Image smart crop")
    parser.add_argument("image_file_path", type=str, help="Input image or directory of images path")
    parser.add_argument("crop_width", type=int, help="Crop width")
    parser.add_argument("crop_height", type=int,  help="Crop height")
    parser.add_argument("out_folder", type=str,  help="Crop height")

    args = parser.parse_args()

    main(args.image_file_path, args.crop_width, args.crop_height, args.out_folder)

