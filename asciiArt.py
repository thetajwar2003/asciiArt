import PIL.Image

# ASCII characters that will be used
ASCII = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]


def resize(img, new_width=100):
    """ This function resizes image

    Args:
        img (PIL.Image): image that the user inputted 
        new_width (int, optional): Defaults to 100.

    Returns:
        PIL.Image: returns the image with new size
    """

    width, height = img.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized = img.resize((new_width, new_height))
    return resized


def grayscale(img):
    """This function returns the image in grayscale

    Args:
        img (PIL.Image): image that the user inputted

    Returns:
        PIL.Image: image in grayscale
    """

    grayscale_img = img.convert("L")
    return grayscale_img


def pixelate(img):
    """This function returns the image converted to the ascii characters

    Returns:
        List: a long 1D list of ascii chars
    """

    pixels = img.getdata()
    chars = "".join([ASCII[pixel//25] for pixel in pixels])
    return chars


def main():
    # open image from user input
    path = input("Enter pathname to an image: \n")

    try:
        image = PIL.Image.open(path)
    except:
        print(path, " is not valid image path")

    # convert image ti ascii
    new_image = pixelate(grayscale(resize(image)))

    # format
    pixel_count = len(new_image)
    ascii_img = "\n".join(new_image[i:(i+100)]
                          for i in range(0, pixel_count, 100))
    print(ascii_img)

    # create a txt file with the asci art
    with open("ascii_img.txt", "w") as f:
        f.write(ascii_img)


main()
