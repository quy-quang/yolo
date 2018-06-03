# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

import sys
sys.path.insert(0, '/home/quy-quang/cuoiKy/darknet/python')
import darknet

# Create your views here.
import os
import string
import random
import math
import cv2

#import base64

net = darknet.load_net("/home/quy-quang/cuoiKy/darknet/cfg/yolov3.cfg", "/home/quy-quang/cuoiKy/darknet/yolov3.weights", 0)
meta = darknet.load_meta("/home/quy-quang/cuoiKy/darknet/cfg/coco.data")

def helloworld(request):
    return HttpResponse("Hello World")

def add(request):
    if request.method == "GET":
        a = int(request.GET['a'])
        b = int(request.GET['b'])
        return HttpResponse(a+b)
    else:
        return HttpResponse("Non supported method")

def max_elm(request):
    if request.method == "GET":
        arr = request.GET['arr']
        arr = [int(it) for it in arr.split(',')]
        return HttpResponse(max(arr))
    else:
        return HttpResponse("Non supported method")

def detect(request):
    if request.method == "POST":
		#filename = str(request.FILES['file'])
		filename = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(64)) + '.jpg'
		handle_uploaded_file(request.FILES['file'], filename)
		path = "/home/quy-quang/cuoiKy/web_api_basic/helloworld/media/" + filename
		r = darknet.detect(net, meta, path)
		#ve hinh voi r tren hinh filename
		im = cv2.imread(path)
		for res in r:
			cv2.rectangle(im, (int(res[2][0] - res[2][2]/2), int(res[2][1] - res[2][3]/2)), (int(res[2][0] + res[2][2]/2), int(res[2][1] + res[2][3]/2)), (0, 255, 0), 1)
			cv2.putText(im, res[0], (int(res[2][0] - res[2][2]/2), int(res[2][1] - res[2][3]/2)), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 0), 1, cv2.LINE_AA)
		cv2.imwrite(path,im)
		with open(path, "rb") as ff:
			return HttpResponse(ff.read(), content_type="image/jpeg")
    else:
        return HttpResponse("@@")

def upload(request):
    if request.method == "POST":
		#filename = str(request.FILES['file'])
		filename = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(64)) + '.jpg'
		handle_uploaded_file(request.FILES['file'], filename)
		return HttpResponse("%s saved"%(filename))
    else:
        return HttpResponse("@@")

def handle_uploaded_file(file, filename):
    if not os.path.exists('media/'):
        os.mkdir('media/')
 
    with open('media/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)


