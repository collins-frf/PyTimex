import cv2
import numpy as np
import skvideo.io
import matplotlib.pyplot as plt 
from scipy.io import loadmat, savemat
import tifffile as tif

class PyTimex(object):
	def __init__(self):
		self.timetxt = []
		self.time_range = []
		self.cell_length = 8000 #default

	def make_tenth_timex(self, video, frame):
		videopart = np.zeros((int(.1*self.cell_length), 1200, 720, 3), dtype=np.uint8)
		videopart = videopart.astype('int32')
		print(videopart.shape)
		i=0
		for frame in video:
			videopart[i,:,:,:] = frame
			i+=1
			if i == (.10*self.cell_length):
				break
		videopart = videopart[:, 25:,72:,:]
		videopart = videopart[:,:1075,:575,:]
		timex = np.mean(videopart, axis=0)
		timex = timex[:,:512,:]
		timex = timex.astype('int32')

		print(timex.shape)
		return timex, videopart[100, :, :, :]

	def main(self):
		for wave_condition in range(45):
			wave_condition+=1
			for bathy_no in range(99):
				try:
					bathy_no+=0
					print("bathy_no: " + str(bathy_no))
					filepath = 'I:/WC' + str(wave_condition) + '/'
					filepath = 'G:/'
					filename = 'bathy_' + str(bathy_no) + '_WC_' + str(wave_condition)
					#filename = 'fakebathy_0_2017-02-28T00.15.00.Z'
					#self.timetxt = np.loadtxt(filepath + "fakebathy_" + str(bathy_no) + "_WC_" + str(wave_condition) + ".mat.txt")
					#time_range = self.timetxt[-1] - self.timetxt[0]
					#self.cell_length = len(self.timetxt)
					#print("time_range in seconds: " + str(time_range))

					#rt of the video at a time due to memory issues
					video = skvideo.io.vreader(filepath + filename + '.avi')

					timexa, snap = self.make_tenth_timex(video, 0)
					timexb, snap = self.make_tenth_timex(video, .1*self.cell_length)
					timexc, snap = self.make_tenth_timex(video, .2*self.cell_length)
					timexd, snap = self.make_tenth_timex(video, .3*self.cell_length)
					timexe, snap = self.make_tenth_timex(video, .4*self.cell_length)
					timexf, snap = self.make_tenth_timex(video, .5*self.cell_length)
					timexg, snap = self.make_tenth_timex(video, .6*self.cell_length)
					timexh, snap = self.make_tenth_timex(video, .7*self.cell_length)
					timexi, snap = self.make_tenth_timex(video, .8*self.cell_length)
					timexj, snap = self.make_tenth_timex(video, .9*self.cell_length)

					timex = timexa+ timexb+ timexc+ timexd + timexe + timexf + timexg+ timexh + timexi + timexj

					timex = timex/10.0
					timex = timex.astype('int32')

					tif.imsave('./timex/%s_rbathy_WC_%s.tiff' % (bathy_no, wave_condition), timex)
					tif.imsave('./snap/%s_rbathy_WC_%s.tiff' % (bathy_no, wave_condition), snap)
				except:
					continue

if __name__ == '__main__':

	PyTimex = PyTimex()
	PyTimex.main()