import os
from tqdm import tqdm
from PIL import Image, ImageOps


def check_folder(path):
    if os.path.exists(path) is not True:
        os.mkdir(path)
        print('Дириктория создана!')

    return path


def crop(*size):
    path_input = check_folder(os.path.join(os.getcwd() + r'\input_img'))
    path_output = check_folder(os.path.join(os.getcwd() + r'\output_img'))

    if len(os.listdir(path_input)) > 1:
        file_list = tqdm(os.listdir(path_input))
        for i in file_list:
            try:
                with Image.open(f'{path_input}\\{i}') as img:
                    ImageOps.fit(img, size).save(f'{path_output}\\{i}')
            except OSError:
                print('Что-то пошло не так!')

            os.remove(f'{path_input}\\{i}')

    else:
        print('Дириктория пустая')


if __name__ == '__main__':

    crop(800, 800)
