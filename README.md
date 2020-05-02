# py3lsd
opencv4.1及以上版本取消了lsd算法，之前的工程需要用到lsd又想用最新版本的opencv4.1及以上的功能，这个项目可以完美替代lsd；
# 特别说明
## time： 2020-05-01
1. 作者在pip上不进行更新，导致每次都要手动修复，无法在工程中使用,所以自己上传一版优化好的；不喜勿喷；
2. [特别鸣谢：原代码](https://github.com/primetang/pylsd)

### 1. Introduction

pylsd is the python bindings for [LSD - Line Segment Detector](http://www.ipol.im/pub/art/2012/gjmr-lsd/).

### 2. Install

This package uses distutils, which is the default way of installing python modules. To install in your home directory, securely run the following:
```
git clone https://github.com/dakun333/py3lsd
cd py3lsd
[sudo] python3 setup.py install
```

Or directly through `pip3` to install it:
```
[sudo] pip3 install py3lsd
```
# 注意：这里我只是更换了包的pip下载名称，使用方式跟原作者中提及的方法相同，即import pylsd
### 3. Usage

We can use the package by using `from pylsd.lsd import lsd`, and `lines = lsd(src)` is the call format for the `lsd` function, where `src` is a Grayscale Image (`H * W` numpy.array), and the return value `lines` is the Detected Line Segment, `lines` is an `N * 5` numpy.array, each row represents a straight line, the 5-dimensional vector is:

`[point1.x, point1.y, point2.x, point2.y, width]`


According to these presentations, we can use it just like the following code ([here is the link](https://github.com/dakun333/py3lsd/tree/master/example)):

* by using cv2 module

```python
import cv2
import numpy as np
import os
from pylsd.lsd import lsd
fullName = 'car.jpg'
folder, imgName = os.path.split(fullName)
src = cv2.imread(fullName, cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
lines = lsd(gray)
for i in xrange(lines.shape[0]):
    pt1 = (int(lines[i, 0]), int(lines[i, 1]))
    pt2 = (int(lines[i, 2]), int(lines[i, 3]))
    width = lines[i, 4]
    cv2.line(src, pt1, pt2, (0, 0, 255), int(np.ceil(width / 2)))
cv2.imwrite(os.path.join(folder, 'cv2_' + imgName.split('.')[0] + '.jpg'), src)
```

* by using PIL(Image) module

```python
from PIL import Image, ImageDraw
import numpy as np
import os
from pylsd.lsd import lsd
fullName = 'house.png'
folder, imgName = os.path.split(fullName)
img = Image.open(fullName)
gray = np.asarray(img.convert('L'))
lines = lsd(gray)
draw = ImageDraw.Draw(img)
for i in range(lines.shape[0]):
    pt1 = (int(lines[i, 0]), int(lines[i, 1]))
    pt2 = (int(lines[i, 2]), int(lines[i, 3]))
    width = lines[i, 4]
    draw.line((pt1, pt2), fill=(0, 0, 255), width=int(np.ceil(width / 2)))
img.save(os.path.join(folder, 'PIL_' + imgName.split('.')[0] + '.jpg'))
```

The following is the result:

* car.jpg by using cv2 module

![](https://github.com/dakun333/py3lsd/blob/master/example/car.jpg)

![](https://github.com/dakun333/py3lsd/blob/master/example/cv2_car.jpg)

* house.png by using PIL(Image) module

![](https://github.com/dakun333/py3lsd/blob/master/example/house.png)

![](https://github.com/dakun333/py3lsd/blob/master/example/PIL_house.jpg)
