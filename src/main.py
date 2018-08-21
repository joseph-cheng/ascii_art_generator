from PIL import Image
import sys
import math
import argparse

# Takes an RGB colour and converts it to an ascii char to print
def colour_to_char(colour, available_chars):
    brightness = max(colour)/255
    return available_chars[math.floor(brightness/(1/len(available_chars)))-1]

#Takes an image path and given the max width, returns a resized image keeping aspect ratio with the given max width
def load_image(path, max_width):
    im = Image.open(path)
    width, height = im.size
    resize = max_width/width
    im.thumbnail((max_width, int(height*resize)))
    return im






def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("image", help="image to convert to ascii art")
    parser.add_argument("width", help="width of resulting ascii art in characters", type=int)
    parser.add_argument("-i", "--inverse", help="change black to white and vice versa", action="store_true")
    args = parser.parse_args()
    #String of chars ordered by darkest to lightest
    chars = "@W%#+l=*dko-:. "
    if args.inverse:
        chars = chars[::-1]
    #chars = " .:=+*#%@"
    input_file = args.image

    #it is divided by 2 because I duplicate each character because each character is not as wide as it is tall
    width = args.width/2
    im = load_image(input_file, width)

    final = ""
    line_number = 0
    #Loop through each pixel and add the right character to a string.
    for it, pixel in enumerate(im.getdata()):
        if it // (width) != line_number:
            final += "\n"
            line_number += 1
        final += 2 * colour_to_char(pixel, chars)


    print(final)
    

if __name__ == "__main__":
    main()
