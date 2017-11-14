import os
import sys
import argparse
from PIL import Image


def get_arguments():
    program_usage = """
    image_resize.py [-h]
                (([--width WIDTH] [--height HEIGHT]) | [--scale SCALE])
                [-o OUTPUT_IMAGE_PATH]
                image_path

    """
    parser = argparse.ArgumentParser(usage=program_usage)
    parser.add_argument('image_path', help='path to image to be resized')
    parser.add_argument('--width', type=int, help='new width')
    parser.add_argument('--height', type=int, help='new height')
    parser.add_argument('--scale', type=float, help='scale of resizing')
    parser.add_argument('-o', '--output_image_path',
                        help='path for resized image'
                        )
    return parser.parse_args()


def get_new_size(initial_size, scale, width, height):
    init_width, init_height = initial_size
    if scale:
        return tuple(int(dimension * scale) for dimension in initial_size)
    elif width and height:
        return width, height
    elif width:
        return width, int(width / init_width * init_height)
    elif height:
        return int(height / init_height * init_width), height


def get_output_image_path(output_path, input_path, image_size):
    if output_path is None:
        file_name, file_ext = os.path.splitext(input_path)
        output_path = '{}__{}x{}{}'.format(file_name, *image_size, file_ext)
    return output_path


def verify_arguments(scale, width, height, image_size):
    if not any((scale, width, height)):
        print('{} {}'.format(
                    'error: the following arguments are required:',
                    '--scale or (--width and/or --height)'
                             )
              )
        sys.exit(1)
    if scale and (width or height):
        print('error: --scale and --width|--height are mutually exclusive')
        sys.exit(1)
    if height and width:
        init_width, init_height = image_size
        difference = 10 ** (-5)
        if abs(width / height - init_width / init_height) > difference:
            print('{} {}'.format(
                            'warning: new width / height ratio',
                            'is in conflict with initial'
                                 )
                  )


if __name__ == '__main__':
    args = get_arguments()
    image = Image.open(args.image_path)
    verify_arguments(args.scale, args.width, args.height, image.size)
    new_size = get_new_size(image.size, args.scale, args.width, args.height)
    resized_image = image.resize(new_size)
    output_image_path = get_output_image_path(
                                        args.output_image_path,
                                        args.image_path,
                                        new_size,
                                              )
    resized_image = image.save(output_image_path)
