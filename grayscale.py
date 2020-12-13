from PIL import Image
import os
import numpy as np
img=Image.open("meter.jpg").convert("L")
img.save("meter_gray.jpg")
