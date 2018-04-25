# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import codecs
import argparse
import sys
import numpy as np
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from utils import render_fonts_image
import arabic_reshaper
from bidi.algorithm import get_display


text_to_be_reshaped = 'بش'
reshaped_text = arabic_reshaper.reshape('بش')
bidi_text = get_display(text_to_be_reshaped)

image = Image.new("RGB", (64, 64), (255, 255, 255))
draw = ImageDraw.Draw(image)
draw.text((0, 0), bidi_text, (0, 0, 0), font=ImageFont.truetype('AlQalam Miki.ttf', 10))
gray = image.convert('L')
bitmap = np.asarray(gray)
image.save('check.png')