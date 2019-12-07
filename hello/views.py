'''
Created on Dec 06, 2019

@author: Deepak Kanthi
'''

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import requests
from .models import Greeting
from .forms import RTSPForm
import base64

#opencv
import numpy as np
import cv2

print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe('MobileNetSSD_deploy.prototxt.txt', 'MobileNetSSD_deploy.caffemodel')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

def index(request):
    """
     main view for base url

    : param request: request from html
    :return: html page using template image_rtsp.html

    """
    person_count=0
    rtsp_url='/static/example1.mp4'
    image_url='/static/default2.jpeg'
    if request.method == 'POST':
        form = RTSPForm(request.POST)
        if form.is_valid():
            rtsp_url = form.cleaned_data['rtsp_url']
            print('rtsp_url', rtsp_url)
    else:
        form=RTSPForm()

    return render(request, "image_rtsp.html" ,{'form':form ,
                                               'rtsp_url':rtsp_url ,
                                               'image_url':image_url ,
                                               'person_count':person_count})

@csrf_exempt
def upload_base64_image(request):
    """
           Save current frame get from Ajax
           And call get_person_count method


           :param request : stream of data
           :type a: stream
           :return: No of person in the Frame/Image
           :rtype: int

           :Example:

            upload_base64_image(request)
           5
        """
    if request.method == 'POST':
        image_base64_data = request.POST['sample_image_data']
        #print ('image_base64_data ', image_base64_data)

        image_base64_data = base64.b64decode(image_base64_data)
        filename = 'saved_image.png'  # I assume you have a way of picking unique filenames
        with open(filename, 'wb') as f:
            f.write(image_base64_data)
        pcount=get_person_count()

        return HttpResponse(str(pcount))  # Sending an success response
    else:
        return HttpResponse("Request method is not a GET")



def get_person_count(file_name="saved_image.png"):
    """
        apply forward propagation of CNN
        and returns the person count .

        :param file_name : name of file
        :type file_name : string
        :return: No of person in the Frame/Image
        :rtype: int

        :Example:
         >>>get_person_count(saved_image.png)
        5
    """

    CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
               "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
               "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
               "sofa", "train", "tvmonitor"]
    COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
    default_confidence = 0.1

    frame=cv2.imread(file_name)
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),0.007843, (300, 300), 127.5)

    # pass the blob through the network and obtain the detections and # predictions
    net.setInput(blob)
    detections = net.forward()
    totalPerson = 0
    # loop over the detections
    for i in np.arange(0, detections.shape[2]):
        # extract the confidence (i.e., probability) associated with
        # the prediction
        confidence = detections[0, 0, i, 2]

        # filter out weak detections by ensuring the `confidence` is
        # greater than the minimum confidence
        if confidence > default_confidence:
            # extract the index of the class label from the
            # `detections`, check if has person class
            idx = int(detections[0, 0, i, 1])
            try :
                if CLASSES[idx] != "person":
                    continue
                else:
                    totalPerson += 1
            except Exception as e :
                print("Exception : " , e)

    person_count=totalPerson
    print("person_count", person_count)
    return person_count

