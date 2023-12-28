from PIL import Image
from django.conf import settings
from os import path

def trataImagem(image):
    imagelist = image.split('.')[1]
    if imagelist in ('jpg', 'png', 'jpeg'):
        caminho = path.join(settings.MEDIA_ROOT, f'notas/{image}')
        imag = Image.open(caminho)
        left, right = imag.size
        left_n = int(left * 0.5)
        right_n = int(right * 0.5)
        imag.resize((left_n, right_n))
        imag.save(caminho)


if __name__ == '__main__':
    trataImagem()