import sys
import argparse
from Lexer import FlipLexer
from Parser import FlipParser

from fpdf import FPDF

class FlipExecute:
	def __init__(self, tree, pages):
		self.pages = pages
		self.walkTree(tree)
		# print(self.pages)

	def walkTree(self, node):

		if isinstance(node, int):
			return node
		if isinstance(node, str):
			return node

		if node is None:
			# print("Syntax error")
			sys.exit()
			return None

		if node[0] == 'photo_assign':
			print("Adding file " + str(node[3])  + " to pages "+ str(node[1]) + " to " + str(node[2]))
			self.pages.append([node[1], node[2], node[3]])


if __name__ == '__main__':
	lexer = FlipLexer()
	parser = FlipParser()
	pages = []

	# parser = argparse.ArgumentParser(description='FlipBook')

	# parser.add_argument('source_file', type=str,
    #                 help='Source file')

	# parser.add_argument('-o', type=str, nargs='?',
    #                 help='Output pdf file, <filename>.pdf', default="default.pdf")
	
	# args = parser.parse_args()

	output_dir = "outputs/"
	images_dir = "images/"
	outout_file = "required.pdf"

	if len(sys.argv) >= 4:
		outout_file = sys.argv[3] 

	file1 = open(sys.argv[1], 'r')
	Lines = file1.readlines()

	for text in Lines:
		tree = parser.parse(lexer.tokenize(text))
		FlipExecute(tree, pages)

	print("Final pages = " + str(pages))

	pages.sort(key=lambda x: x[0])

	pdf = FPDF()
	pdf.set_auto_page_break(0)

	prevPage = 0

	for page in pages:

		if (page[0] != 1 + prevPage):
			sys.exit("Error: Please check if you've a missing page number or overlapping page numbers")

		for i in range(page[0], page[1]+1):
			try:
				pdf.add_page()
				pdf.image(images_dir + page[2], w=190, h=280)
			except:
				sys.exit(f"Error: Please check if file {page[2]} exists")
		prevPage = page[1]
	
	pdf.output(output_dir + outout_file, "F")
		
	