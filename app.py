from flask import Flask, request, render_template, Response
import cv2 as cv 
from PIL import Image
import numpy as np
from config import *
import os
import sys
import base64
from utils import global_manager as gm

# yolov5版本
from yolov5.yolo import YOLO

# 宏定义.
join = lambda *args: os.path.join(*args)

app = Flask(__name__, static_folder="./static", template_folder="templates")

yolo = YOLO()


@app.route("/image", methods=["POST"])
def parse_image():
    image = request.files["image"]  # 从form表单中拿出image的input.
    image_name = image.filename
    file_path = os.path.join(SAVE_PATH, image_name)
    print("filepath是"+file_path)
    image.save(file_path)
    print(image_name, "has been download in local")
    if image_name.split(".")[-1] in IMAGE_FILE:  # 是图片
        source_img = cv.imread(file_path)  # read image
        if source_img is None:
            print("Failed to read image from:", file_path)
        img = Image.fromarray(np.uint8(source_img))  # 转换为Image.
        img_torch, box_information = yolo.detect_image(img)
        # print(box_information)
        img = np.array(img_torch)
        img = np.hstack([source_img, img])
        cv.imwrite(file_path, img)

        # _, img_encoded = cv.imencode('.jpg', img)

        try:
            img_stream = ''
            with open(file_path, 'rb') as img_f:
                img_stream = img_f.read()
                img_stream = base64.b64encode(img_stream).decode()
            return render_template('./image_process.html', image_url=img_stream)
        except:
            print("image parse faild")
            return render_template('./image_process.html')

        # response = img_encoded.tobytes()
        # return Response(response=response, status=200, mimetype='image/jpg')

    return render_template("./index.html")


@app.route("/")
def main_page():
    gm.set_value("is_realtime", None)
    return render_template("./index.html")



# check file if exist.
def init():
    gm._init()  # 初始化.
    if not os.path.exists(SAVE_PATH):
        os.mkdir(SAVE_PATH)

    if not os.path.exists(LOG_PATH):
        os.mkdir(LOG_PATH)

    for ele in os.listdir(SAVE_PATH):
        ele_path = os.path.join(SAVE_PATH, ele)
        os.remove(ele_path)
    print("file dir has been empty")


# run
if __name__ == "__main__":
    init()
    app.run(host="0.0.0.0", port=5001, debug=True)
