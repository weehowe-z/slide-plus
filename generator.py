#!/usr/bin/env python
import os
import sys
import commands

def pptx_to_pdf(pptx_name, quality = "100"):
	pdf_name = pptx_name.split(".")[0] + ".pdf"
	os.system("unoconv --export Quality=100 " + pptx_name + " " + pdf_name)
	print "PDF created"
	return pdf_name

def pdf_to_img(pdf_name, density = "100", size = "default"):
	# os.system("convert -density 400 test.pdf -resize 2000x1500 img%d.jpg")
	os.system("convert -density 400 " + pdf_name + " img/img%d.jpg")
	os.system("rm -f " + pdf_name)
	(status, file_num) = commands.getstatusoutput("ls img/ | wc -l")
	print "Images created"
	return int(file_num)

def generate(img_num):
	template = open('template.html')
	output = open('index.html', 'w')
	try:
		content = template.read( )
		slides = ""
		for i in xrange(0,img_num):
			slides += "\t\t\t\t<section data-background=\"img/img" + str(i) +".jpg\"></section>\n"
		new_content = content.replace("###content###",slides)
		output.write(new_content)
	finally:
		template.close( )
		output.close()
		print "Slides created"

def main():
	if (len(sys.argv)!=2):
		print "please specify file path"
		sys.exit(-1)
	else:
		path = sys.argv[1]

	# pptx_name = path.split("/")[-1]
	pptx_name = path
	pdf_name = pptx_to_pdf(pptx_name)
	img_num = pdf_to_img(pdf_name)
	generate(img_num);

if __name__ == '__main__':
	main()
