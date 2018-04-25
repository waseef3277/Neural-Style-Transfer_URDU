# -*- coding: utf-8 -*-
import io
text_string = "آ ا ب پ ت ٹ ث ج چ ح خ د ڈ ذ ر ڑ ز ژ س ش ص ض ط ظ ع غ ف ق ک گ ل م ن ں و ؤ ء ہ ھ ئ ی ے"

chars = ['آ', 'ا', 'ب', 'پ', 'ت', 'ٹ', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ڈ', 'ذ', 'ر', 'ڑ', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'ں', 'و', 'ؤ', 'ء', 'ہ', 'ھ', 'ئ', 'ی', 'ے']

with io.open("urduCharset.txt", "w", encoding="utf-8") as f:
    for x in range(len(chars)):
        f.write(chars[x])
        f.write(" ")

    for x in range(len(chars)):
        for y in range(len(chars)):
            f.write(chars[x]+chars[y])
            f.write(" ")

'''
    for x in range(len(chars)):
        for y in range(len(chars)):
            for z in range(len(chars)):
                f.write(chars[x]+chars[y]+chars[z])
                f.write("\n")
'''






