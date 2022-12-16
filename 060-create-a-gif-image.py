import imageio


def create_gif(file_names, out_file="image.gif", duration=1.5):
    images = []
    for filename in file_names:
        images.append(imageio.imread(filename))
    imageio.mimsave(out_file, images, duration=duration)