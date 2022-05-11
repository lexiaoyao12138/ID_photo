# 设置照片大小

from PIL import Image
import os

class ImageReize:

    picture = [
        (250, 350),
        (350, 490),
    ]

    # file path
    def file_name(self, name):
        return os.path.join(os.path.dirname(__file__), name)

    def image_set(self, imageName):
        file          = self.file_name(imageName)
        image         = Image.open(file)
        image         = image.convert('RGB')
        width, height = image.size
        image_copy    = image.copy()

        imageF = image_copy.resize(self.picture[0])
        imageF.save('_need.jpg')


if __name__ == '__main__':
   im = ImageReize()
   im.image_set('reba.jpg')
