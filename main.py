
from PIL import Image

from pylibjpeg import decode

from os import walk

from os import makedirs

import argparse

def listImages(root_dir):

	return ["{}/{}".format(path, file) for path, _, files in walk(root_dir) for file in files]

class DecodeImage():

	def __new__(cls, image):

		for func in [cls.jpeg, cls.general]:
			try:
				return func(image)
			except:
				continue

	def jpeg(image):

		with open(image, "rb") as f:

			return Image.fromarray(decode(f))

	def general(image):

		return Image.open(image)

def convertImages(images, save_dir, suffix):

	length = max(len(image) for image in images)

	for image in images:

		path, file = image.rsplit("/", 1)

		path = "/".join([save_dir, *path.split("/", 1)[1:]])

		file = "{}.{}".format(file.rsplit(".", 1)[0], suffix)

		output = "{}/{}".format(path, file)

		makedirs(path, exist_ok = True)

		try:

			DecodeImage(image).save(output)

			print(" {:<{}} --> {}".format(image, length, output))

		except:

			print(" {:<{}}     failed!".format(image, length))

def main(args):

	images = listImages(root_dir = args.root_dir)

	convertImages(images = images, save_dir = args.save_dir, suffix = args.suffix)

if __name__ == "__main__":

	parser = argparse.ArgumentParser()

	parser.add_argument("root_dir", type = str)

	parser.add_argument("save_dir", type = str, default = "result", nargs = "?")

	parser.add_argument("--suffix", type = str, default = "png")

	args = parser.parse_args()

	main(args)
