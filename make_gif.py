import cv2
import numpy as np
import skvideo.io
import matplotlib.pyplot as plt 
from scipy.io import loadmat, savemat
import tifffile as tif

class Pygif(object):
	def __init__(self):
		self.cell_length = 100 #default

	def make_gif(self, video):
		videopart = np.zeros((int(self.cell_length), 1080, 720, 3), dtype=np.uint8)
		videopart = videopart.astype('int32')
		i=0
		print(i)
		for frame in video:
			videopart[i,:,:,:] = frame
			i+=1
			if i == (self.cell_length):
				break
		videopart = videopart[:, 250:,100:,:]
		videopart = videopart[:,:750,:575,:]

		return videopart

	def main(self):

			filepath = 'D:/Celerity_Net/'

			filename = 'fakebathy_0_WC_7'

			video = skvideo.io.vreader(filepath + filename + '.avi')

			gif = self.make_gif(video)

			gif = gif.astype('int32')

			skvideo.io.vwrite("D:/Celerity_Net/output.gif", gif)


if __name__ == '__main__':

	Pygif = Pygif()
	Pygif.main()