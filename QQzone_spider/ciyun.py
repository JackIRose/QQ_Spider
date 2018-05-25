#coding:utf-8
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
import jieba
import numpy as np
from PIL import Image

#读入背景图片
abel_mask = np.array(Image.open("输入背景图片路径"))

#读取要生成词云的文件
text_from_file_with_apath = open('输入存储文字的文件路径',encoding='gbk').read()

my_wordcloud = WordCloud(
            background_color='white',    # 设置背景颜色
            mask = abel_mask,        # 设置背景图片
            max_words = 200,            # 设置最大现实的字数
            stopwords = STOPWORDS,        # 设置停用词
            width=1600,
            height=800,
            font_path = 'C:/Users/Windows/fonts/simkai.ttf',# 设置字体格式，如不设置显示不了中文
            max_font_size = 200,            # 设置字体最大值
            random_state = 30,            # 设置有多少种随机生成状态，即有多少种配色方案
                scale=.5
                ).generate(text_from_file_with_apath)

# 根据图片生成词云颜色
image_colors = ImageColorGenerator(abel_mask)

# 以下代码显示图片
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()