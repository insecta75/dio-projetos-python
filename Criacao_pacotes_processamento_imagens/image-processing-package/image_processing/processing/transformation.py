from skimage.transform import resize

def resize_image(image, proportion): #para diminuir imagens muito grandes
	assert 0 <= proportion <= 1, "Specify a valid proportion between 0 and 1."
	height = round(image.shape[0] * proportion) #round: para ser valores inteiros
	width = round(image.shape[1] * proportion)
	image_resized = resize(image, (height, width), anti_aliasing=True) #imagem sofre a alteracao de tamanho
	return image_resized
