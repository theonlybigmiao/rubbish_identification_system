# 垃圾检测系统
这是一个基于yoloV5目标检测算法和Flask框架搭建的简易垃圾检测系统。前端采用html加css美化，后端使用ajax，并引入了jQuery增强网页的交互性。图像识别工作主要通过opencv库完成。

## 项目结构
```Shell
│  .gitignore
│  file 用于暂存待识别的图像文件
│  logs 自动增添存储日志
│  app.py 在此处运行
│  LICENSE
│  README.md
│  requirements.txt
│  config.py 配置全局参数
|
|——yolov5 用于检测和训练的模型数据集
│
├─static
|   css  美化样式
│      layout.css
|      sty_all.css
|      style_ele.css
|      stylesheet.css
|
|    js 与前端交互
│      client.js 图像文件上传和预览
|      init.js 
|
|    templates
|      index.html 
|      image_process.html
|
```

### 安装与部署
将本项目下载到本地，运行 pip install -r requirements.txt 即可。

## 运行测试
python3 app.py

效果见result.png

## 补充
本项目的依赖及框架也可从以下地址自行下载：
* [Flask](http://www.dropwizard.io/1.0.2/docs/) - The Web framework used
* [PyTorch](https://pytorch.org/) - Deep Learning framework.
* [YoloV5_u](https://github.com/ultralytics/yolov5) - yolov5 implement ultralytics edition
* [YoloV5](https://github.com/bubbliiiing/yolov5-pytorch) - yolov5 implement other edition (bubbliiiing in bilibili)


## 注意事项
- 上传检测的图片文件时，文件路径和文件名均不能带有中文，否则报错。
- 鉴于Flask的特性,请不要轻易更改'static'、'templates'文件夹的名称及所放内容类型。
- 本项目多采用水上垃圾数据集训练，所以在检测水面和水边垃圾时表现良好，但检测地面垃圾时效果一般。
