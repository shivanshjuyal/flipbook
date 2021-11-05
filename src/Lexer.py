from sly import Lexer

class FlipLexer(Lexer):
	tokens = { NAME, NUMBER, COMMENT}
	ignore = '\t '

	@_(r'\d+')
	def NUMBER(self, t):
		t.value = int(t.value)
		return t
	
	# @_(r'([^\\s]+(\\.(?i)(jpe?g|png|gif|bmp))$)')
	# def IMAGE(self, t):
	# 	print("Image enountered")
	# 	return t
    	
	@_(r'[a-zA-Z0-9_-]+[\\.][a-zA-Z]+')
	def NAME(self, t):
		return t


	@_(r'//.*')
	def COMMENT(self, t):
		# print("Comment encountered")
		return t

	@_(r'\n+')
	def newline(self, t):
		self.lineno = t.value.count('\n')
	
	@_(r'[a-zA-Z0-9_]+')
	def INVALID(self, t):
        
		return None

    
