# -*- coding: utf-8 -*-
"""
WordCloud  
By xixi

"""

import matplotlib.pyplot as plt
import os
from os import path
from wordcloud import WordCloud

# get the file
d = path.dirname('E:\\person\\python\\')
text = open(path.join(d,'one.txt')).read().decode('gbk')

# modify the font support the chinese
font=os.path.join(os.path.dirname('E:\\person\\python\\'), "DroidSansFallbackFull.ttf")


wordcloud = WordCloud(font_path=font).generate(text)
plt.imshow(wordcloud)
plt.axis("off")


wordcloud = WordCloud(font_path=font,max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()





