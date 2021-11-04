from sly import Parser
import sys
from Lexer import FlipLexer

class FlipParser(Parser):
	#tokens are passed from lexer to parser
	tokens = FlipLexer.tokens

	@_('COMMENT')
	def photo_assign(self, p):
		return ('Comment')

	@_('NUMBER NUMBER NAME')
	def photo_assign(self, p):
		# print("Encountered photo assign")
		if p.NUMBER0 > p.NUMBER1:
        		sys.exit("Start page must be less than or equal to end page")
		return ('photo_assign', p.NUMBER0, p.NUMBER1, p.NAME)
	
	@_('NUMBER NUMBER NAME COMMENT')
	def photo_assign(self, p):
		# print("Encountered photo assign")
        
		return ('photo_assign', p.NUMBER0, p.NUMBER1, p.NAME)

    # @_('NUMBER NUMBER NUMBER')
	# def photo_assign(self, p):
	# 	print("Invalid syntax at line. NUMBER NUMBER FILENAME is the right format")
	# 	return ('error')
