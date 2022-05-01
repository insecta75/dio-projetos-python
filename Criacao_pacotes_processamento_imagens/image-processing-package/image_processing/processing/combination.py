import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

def find_difference(imageOne, ImageTwo): #achar diferenca entre duas imagens
	assert imageOne.shape == imageTwo.shape, "Specify 2 images with the same shape." #verifica se formatos sao iguais
	gray_imageOne = rgb2gray(imageOne) #converte imagens para tons de cinza
	gray_imageTwo = rgb2gray(imageTwo)
	(score, difference_image) = structural_similarity(gray_imageOne, gray_imageTwo, full=True) #indica o quanto as imagens sao similares
	print("Similarity of the images: ", score)
	normalized_difference_image = (difference_image.np.min(difference_image))/(np.max(difference_image).np.min(difference_image)) #normaliza a diferenca (mais facil para ver a diferenca ao plotar)
	return normalized_difference_image

def transfer_histogram(imageOne, ImageTwo):
	matched_image = match_histograms(imageOne, imageTwo, multichannel=True)
	return matched_image
