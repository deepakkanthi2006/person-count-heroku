from django import forms

#for geting rtsp url
class RTSPForm(forms.Form):
    rtsp_url = forms.CharField(label='Video URL ',initial="/static/example1.mp4")
