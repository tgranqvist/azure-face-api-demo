import os, sys
from urllib.parse import urlparse

import requests
from PIL import Image, ImageDraw
from io import BytesIO

API_URL = 'https://northeurope.api.cognitive.microsoft.com/face/v1.0/detect'
headers={'Ocp-Apim-Subscription-Key': os.environ['FACE_API_KEY'], 'Content-Type': 'application/octet-stream'}

def main(picture_url, save = True, verbose = False):

	if verbose: print('Loading picture {0}'.format(picture_url))
	response = requests.get(picture_url);
	
	response.raise_for_status()
	image_bytes = response.content
	
	response = requests.post(API_URL, headers=headers, data=image_bytes)
	response.raise_for_status()
	faces = response.json()
	
	image = Image.open(BytesIO(image_bytes))
	image_draw = ImageDraw.Draw(image)
	
	for face in faces:
		rect = face['faceRectangle']
		x0 = rect['left']
		y0 = rect['top']
		
		x1 = rect['left'] + rect['width']
		y1 = rect['top'] + rect['height']
		
		image_draw.rectangle( [x0, y0, x1, y1] )
		
	del image_draw
	if save:
		filename = os.path.basename(urlparse(picture_url).path)
		if verbose: print('Saving file to {0}'.format(filename))
		image.save(filename)
	image.show()
		

if __name__ == '__main__':
	main(sys.argv[1] if len(sys.argv) > 1 else 'https://www.how-old.net/Images/faces2/main007.jpg')
