from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

def home(request):
	data=requests.get("https://api.nasa.gov/planetary/apod?api_key=5kChZsxp5F3AqEqMbDkilrHfH1c2OLcFgXBbgnNI")
	dataa=data.json()
	img=dataa['url']
	return render(request,"app/home.html",{"dataa":dataa})
	
