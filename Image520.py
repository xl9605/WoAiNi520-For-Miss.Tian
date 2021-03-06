import cv2
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from PIL import Image
from matplotlib.font_manager import *

# 处理的所有图片及结果存放的总目录
dir = os.path.dirname(os.path.realpath(__file__))
sourDir = os.path.join(dir, '', '田梦雨')
# 拼接结果图片所在的目录
resultDir = os.path.join(dir, '', 'PIC')
# 获取指定路径下的所有图片
def getImagesName(dir):
    allPicPath = []  # 所有图片
    for root, dirs, files in os.walk(dir):
        for file in files:
            # 可自行添加图片的类型判断
            if file.endswith('.jpeg') or file.endswith('.png') or file.endswith('.jpg'):
                allPicPath.append(dir + '/' + file)
    return allPicPath
# 该队列是指我们需要输出数字图片的位置，０代表不输出图片，１代表我们就要输出照片
picMatrix = [
    [0, 0,0,0,0,0, 0,0, 0,0,0,0,0, 0,0, 0,0,0,0,0, 0],
    [0, 1,1,1,1,1, 0,0, 1,1,1,1,1, 0,0, 1,1,1,1,1, 0],
    [0, 1,0,0,0,0, 0,0, 0,0,0,0,1, 0,0, 1,0,0,0,1, 0],
    [0, 1,0,0,0,0, 0,0, 0,0,0,0,1, 0,0, 1,0,0,0,1, 0],
    [0, 1,1,1,1,1, 0,0, 1,1,1,1,1, 0,0, 1,0,0,0,1, 0],
    [0, 0,0,0,0,1, 0,0, 1,0,0,0,0, 0,0, 1,0,0,0,1, 0],
    [0, 0,0,0,0,1, 0,0, 1,0,0,0,0, 0,0, 1,0,0,0,1, 0],
    [0, 1,1,1,1,1, 0,0, 1,1,1,1,1, 0,0, 1,1,1,1,1, 0],

    [0, 0,0,0,0,0, 0,0, 0,0,0,0,0, 0,0, 0,0,0,0,0, 0],
    [0, 0,0,0,0,0, 0,0, 0,0,0,0,0, 0,0, 0,0,0,0,0, 0],
    [0, 0,0,0,0,0, 0,0, 0,0,0,0,0, 0,0, 0,0,0,0,0, 0],

    # 妹子名字矩阵
    [0, 1,1,1,1,1, 0,0, 1,1,1,1,1, 0,0, 1,0,0,0,1, 0],
    [0, 0,0,1,0,0, 0,0, 1,0,1,0,1, 0,0, 0,1,0,1,0, 0],
    [0, 0,0,1,0,0, 0,0, 1,0,1,0,1, 0,0, 0,0,1,0,0, 0],
    [0, 0,0,1,0,0, 0,0, 1,0,1,0,1, 0,0, 0,0,1,0,0, 0],
    [0, 0,0,1,0,0, 0,0, 1,0,1,0,1, 0,0, 0,0,1,0,0, 0],

    [0, 0,0,0,0,0, 0,0, 0,0,0,0,0, 0,0, 0,0,0,0,0, 0],
]
#
picMatrix = [
    [0, 0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0, 0],
    [0, 0,0,1,1,1,1,1,1,1,1,1,0,0, 0,0, 0,0,1,1,1,1,1,1,1,1,1,0,0, 0,0, 0,0,1,1,1,1,1,1,1,1,1,0,0, 0],
    [0, 0,0,1,0,0,0,0,0,0,0,0,0,0, 0,0, 0,0,0,0,0,0,0,0,0,0,1,0,0, 0,0, 0,0,1,0,0,0,0,0,0,0,1,0,0, 0],
    [0, 0,0,1,0,0,0,0,0,0,0,0,0,0, 0,0, 0,0,0,0,0,0,0,0,0,0,1,0,0, 0,0, 0,0,1,0,0,0,0,0,0,0,1,0,0, 0],
    [0, 0,0,1,0,0,0,0,0,0,0,0,0,0, 0,0, 0,0,0,0,0,0,0,0,0,0,1,0,0, 0,0, 0,0,1,0,0,0,0,0,0,0,1,0,0, 0],
    [0, 0,0,1,0,0,0,0,0,0,0,0,0,0, 0,0, 0,0,0,0,0,0,0,0,0,0,1,0,0, 0,0, 0,0,1,0,0,0,0,0,0,0,1,0,0, 0],
    [0, 0,0,1,0,0,0,0,0,0,0,0,0,0, 0,0, 0,0,0,0,0,0,0,0,0,0,1,0,0, 0,0, 0,0,1,0,0,0,0,0,0,0,1,0,0, 0],
    [0, 0,0,1,1,1,1,1,1,1,1,1,0,0, 0,0, 0,0,1,1,1,1,1,1,1,1,1,0,0, 0,0, 0,0,1,0,0,0,0,0,0,0,1,0,0, 0],
    [0, 0,0,0,0,0,0,0,0,0,0,1,0,0, 0,0, 0,0,1,0,0,0,0,0,0,0,0,0,0, 0,0, 0,0,1,0,0,0,0,0,0,0,1,0,0, 0],
    [0, 0,0,0,0,0,0,0,0,0,0,1,0,0, 0,0, 0,0,1,0,0,0,0,0,0,0,0,0,0, 0,0, 0,0,1,0,0,0,0,0,0,0,1,0,0, 0],
    [0, 0,0,0,0,0,0,0,0,0,0,1,0,0, 0,0, 0,0,1,0,0,0,0,0,0,0,0,0,0, 0,0, 0,0,1,0,0,0,0,0,0,0,1,0,0, 0],
    [0, 0,0,0,0,0,0,0,0,0,0,1,0,0, 0,0, 0,0,1,0,0,0,0,0,0,0,0,0,0, 0,0, 0,0,1,0,0,0,0,0,0,0,1,0,0, 0],
    [0, 0,0,1,1,1,1,1,1,1,1,1,0,0, 0,0, 0,0,1,1,1,1,1,1,1,1,1,0,0, 0,0, 0,0,1,1,1,1,1,1,1,1,1,0,0, 0],
    [0, 0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0, 0],

    [0, 0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0, 0],
    [0, 0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0, 0],
    [0, 0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0, 0],

    # 妹子名字矩阵
    [0, 0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0, 0,0,0,1,0,0,0,0,0,1,0,0,0, 0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0, 0],
    [0, 1,1,1,1,1,1,1,1,1,1,1,1,1, 0,0, 0,0,0,1,0,0,0,0,0,1,0,0,0, 0,0, 1,1,1,1,1,1,1,1,1,1,1,1,1, 0],
    [0, 1,0,0,0,0,0,1,0,0,0,0,0,1, 0,0, 1,1,1,1,1,1,1,1,1,1,1,1,1, 0,0, 0,0,0,0,0,0,1,0,0,0,0,0,0, 0],
    [0, 1,0,0,0,0,0,1,0,0,0,0,0,1, 0,0, 0,0,1,1,1,0,0,0,1,1,1,0,0, 0,0, 0,0,0,0,0,0,1,0,0,0,0,0,0, 0],
    [0, 1,0,0,0,0,0,1,0,0,0,0,0,1, 0,0, 0,1,0,1,0,1,0,1,0,1,0,1,0, 0,0, 1,1,1,1,1,1,1,1,1,1,1,1,1, 0],
    [0, 1,0,0,0,0,0,1,0,0,0,0,0,1, 0,0, 0,0,0,1,0,0,1,0,0,1,0,0,0, 0,0, 1,0,0,0,0,0,1,0,0,0,0,0,1, 0],
    [0, 1,0,0,0,0,0,1,0,0,0,0,0,1, 0,0, 0,0,0,0,0,1,1,0,0,0,0,0,0, 0,0, 1,0,1,1,0,0,1,0,1,1,0,0,1, 0],
    [0, 1,1,1,1,1,1,1,1,1,1,1,1,1, 0,0, 0,0,0,0,1,1,1,1,1,1,1,0,0, 0,0, 1,0,0,1,1,0,1,0,0,1,1,0,1, 0],
    [0, 1,0,0,0,0,0,1,0,0,0,0,0,1, 0,0, 0,0,0,1,1,0,0,0,1,1,0,0,0, 0,0, 1,0,0,0,0,0,1,0,0,1,0,0,1, 0],
    [0, 1,0,0,0,0,0,1,0,0,0,0,0,1, 0,0, 0,0,1,1,1,1,0,1,1,0,0,0,0, 0,0, 1,0,0,0,0,0,1,0,0,0,0,0,1, 0],
    [0, 1,0,0,0,0,0,1,0,0,0,0,0,1, 0,0, 0,1,1,0,1,1,1,1,0,0,0,0,0, 0,0, 1,0,1,1,0,0,1,0,1,1,0,0,1, 0],
    [0, 1,0,0,0,0,0,1,0,0,0,0,0,1, 0,0, 0,0,0,0,0,1,1,0,0,0,0,0,0, 0,0, 1,0,0,1,1,0,1,0,0,1,1,0,1, 0],
    [0, 1,1,1,1,1,1,1,1,1,1,1,1,1, 0,0, 0,0,0,0,1,1,0,0,0,0,0,0,0, 0,0, 1,0,0,0,0,0,1,0,0,0,0,0,1, 0],
    [0, 0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0, 0,0,0,1,1,0,0,0,0,0,0,0,0, 0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0, 0],

    [0, 0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0, 0],
]
w = len(picMatrix[0])
h = len(picMatrix)
# print(w,h)

mw = 100

# 设计数字图片的背景，画出心形曲线，并且输出汉字，
def woaini520BG(girlName):
    t = np.linspace(0, math.pi, 1000)
    x = np.sin(t)
    y = np.cos(t) + np.power(x, 2.0 / 3)  # 心型曲线的参数方程

    plt.figure(figsize=[w, h + 1], facecolor='pink')
    plt.scatter(x, y, c=y, cmap=plt.cm.Reds, edgecolor='none', s=50)
    plt.scatter(-x, y, c=y, cmap=plt.cm.Reds, edgecolor='none', s=40)  # 渐变颜色曲线

    plt.fill_between(-x, x, y, facecolor='red')
    plt.fill_between(x, -x, y, facecolor='red')
    plt.axis([-2, 2, -2, 2])  # 坐标轴范围
    plt.xlabel('love', fontsize=14)
    plt.ylabel('you', fontsize=14)
    # print(plt.rcParams['font.sans-serif'])

    # 定义自定义字体，文件名从1.b查看系统中文字体中来
    # 解决负号'-'显示为方块的问题，打开自定义的字体，自定义字体存放在该项目所在目录的ｆfont目录下
    myfont = FontProperties(fname='./Font/HYCoffee_Bold.ttf')
    matplotlib.rcParams['axes.unicode_minus'] = False
    # 使用自定义的字体，并设置字体粗体，以及字体大小
    plt.title(" %s　I Love You"%(girlName), fontweight='bold', fontproperties=myfont, fontsize=60)
    # 不显示网格线
    plt.axis('off')
    savefileName = resultDir + '/%s的520数字图片的背景.PNG'%(girlName)
    plt.savefig(savefileName)
    firstSaveFileName = Image.open(savefileName)
    width = firstSaveFileName.size[0]  # 长度
    height = firstSaveFileName.size[1]  # 宽度
    # 初始做出来的背景是白色的底，为了烘托出少女心，将白色背景换成粉红色，循环遍历每个像素点，如果是（２５５，２５５，２５５）即这个像素点是白色，就替换像素点为粉色
    for i in range(0, width):  # 遍历所有长度的点
        for j in range(0, height):  # 遍历所有宽度的点
            data = (firstSaveFileName.getpixel((i, j)))  # 打印该图片的所有点
            # print (data)#打印每个像素点的颜色RGBA的值(r,g,b,alpha)
            # print (data[0])#打印RGBA的r值
            if (data[0] == 255 and data[1] == 255 and data[2] == 255):  # RGBA的r值大于170，并且g值大于170,并且b值大于170
                firstSaveFileName.putpixel((i, j), (255, 192, 203))  # 则这些像素点的颜色改成粉色
    firstSaveFileName.save(savefileName)
    return savefileName

# 将需要处理的图片集的路径名的集合传入本函数的imgList参数内，用于制作数字图片
# 将需要对哪个女生表白的女生的姓名传入本函数的girlNam参数内
def save_photo_wall(imgList,girlName):
    # 需要获取我们一共有多少张图片可以用来制作数字图片
    imgCount = len(imgList)
    # 根据我们需要写的字的大小，设置我们底层的画布大小
    toImage = Image.new('RGBA', (100 * w, 100 * (h + 1)),"pink")
    # 将我们设计好的心形背景图打开并且复制到我们的画布上
    backgroundIMG = Image.open(woaini520BG(girlName))
    toImage.paste(backgroundIMG, (0,200))
    # backgroundIMG.show()

    imgIndex = 0
    needImgNum = 0
    for y in range(h):
        for x in range(w):
            try:
                # 碰到１就输出照片，
                if picMatrix[y][x] == 1:
                    # print(x, y, needImgNum % imgCount)
                    needImgNum = needImgNum + 1
                    fromImage = Image.open(imgList[needImgNum % imgCount])
                    fromImage = fromImage.resize((100, 100), Image.ANTIALIAS)
                    toImage.paste(fromImage, (x * mw, y * mw))
                    # print("正在输出第%s图片！"%imgIndex)
                    imgIndex = imgIndex + 1
                else :
                    pass
            except IOError:
                pass
    print("一共使用了%s张图片！" % (imgIndex-1))

    # toImage.show()


    savefileName = resultDir + '/%s的520数字图片.PNG'%(girlName)
    toImage.save(savefileName)
    print('制作的520数字照片已保存!!保存位置:' + '\n\t' + savefileName)
    print('保存的文件名是:' + os.path.split(savefileName)[-1])
    cv2.imread(savefileName)
    savefileName = resultDir + '/%s的520数字图片.JPG'%(girlName)
    toImage = toImage.convert('RGB')
    toImage.save(savefileName)
    print('制作的520数字照片已保存!!保存位置:' + '\n\t' + savefileName)
    print('保存的文件名是:' + os.path.split(savefileName)[-1])

if __name__ == '__main__':
    save_photo_wall(getImagesName(sourDir),"田梦雨")

