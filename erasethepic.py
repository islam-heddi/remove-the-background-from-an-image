from PIL import Image
from rembg import remove

input_path = 'download.png'
ouput_path = 'output.png'

INPUT = Image.open(input_path)

OUTPUT = remove(INPUT)

OUTPUT.save(ouput_path)