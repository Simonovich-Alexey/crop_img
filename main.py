import os
from tqdm import tqdm
from PIL import Image, ImageOps


def crop(*size):
    path_input = os.path.join(os.getcwd() + r'\input_img')
    path_output = os.path.join(os.getcwd() + r'\output_img')
    file_list = tqdm(os.listdir(path_input))
    for i in file_list:
        try:
            with Image.open(f'{path_input}\\{i}') as img:
                ImageOps.fit(img, size).save(f'{path_output}\\{i}')
        except OSError:
            print('Что-то пошло не так!')


if __name__ == '__main__':

    crop(800, 800)
