# 520表白神器_python照片墙制作工具

[Introduce]
1.该程序是专门为田梦雨女神设计的５２０数字图片
2.Image520.py为该程序的主要程序
3.she.png为没有加背景的字母表白数字图片
4.TurtleCupid.py为还在尝试修改的心形

最终生成如下图片
![最终生成的图片]点开＂田梦雨的520数字图片.JPG＂或者＂田梦雨的520数字图片(字母).JPG＂预览即可

# Prepare
python3环境

# Install
```shell
pip3 install pillow opencv-python numpy math matplotlib 
```

# Use
1. Images/文件夹下放制作照片墙的图片 并保证10张及以上
2. PIC文件夹下放输出结果
3. 修改Image520.py中picMatrix变量中妹子名字矩阵picMatrix第三块，第一个picMatri的底下是首字母，第二个picMatri变量底下是中文，修改main函数中调用的save_photo_wall函数的第二个实参为你需要表白的女生的姓名
4. 命令行写法
```sh
py3 Image520.py
```
5. copy Pic目录下的图片 给妹子 ~
