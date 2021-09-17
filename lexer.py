from tokens import TokenType, Token


DIGITS = '0123456789'

class Lexer:
	
	def __init__(self, text):
		self.text = iter(text)
		self.advance()

	def advance(self):
		try:
			self.current_char = next(self.text)
		except  StopIteration:
			self.current_char = None

	def generate_tokens(self):
		while self.current_char != None:
			if self.current_char == '.' or self.current_char in DIGITS:
				yield self.generate_number()
			elif self.current_char == '+':
				self.advance()
				yield Token(TokenType.PLUS)
			elif self.current_char == '-':
				self.advance()
				yield Token(TokenType.MINUS)
			elif self.current_char == '~':
				self.advance()
				yield Token(TokenType.NEGATE)
			elif self.current_char == '*':
				self.advance()
				yield Token(TokenType.MULTIPLY)
			elif self.current_char == '/':
				self.advance()
				yield Token(TokenType.DIVIDE)
			elif self.current_char == '^':
				self.advance()
				yield Token(TokenType.POWER)
			elif self.current_char == '%':
				self.advance()
				yield Token(TokenType.MODULE)
			elif self.current_char == '!':
				self.advance()
				yield Token(TokenType.FACTORIAL)
			elif self.current_char == '@':
				self.advance()
				yield Token(TokenType.AVERAGE)
			elif self.current_char == '&':
				self.advance()
				yield Token(TokenType.MINIMUM)
			elif self.current_char == '$':
				self.advance()
				yield Token(TokenType.MAXIMUM)
			elif self.current_char == '[':
				self.advance()
				yield Token(TokenType.LBRACKET)
			elif self.current_char == ']':
				self.advance()
				yield Token(TokenType.RBRACKET)
			else:
				raise Exception(f"Illegal character '{self.current_char}'")


	def generate_number(self):
		decimal_point_count = 0
		number_str = self.current_char
		self.advance()

		while self.current_char != None and (self.current_char == '.' or self.current_char in DIGITS):
			
			if self.current_char == '.':
				decimal_point_count += 1
				if decimal_point_count > 1:
					break

			number_str += self.current_char
			self.advance()

		if number_str.startswith('.'):
			number_str = '0' + number_str
		if number_str.endswith('.'):
			number_str += '0'

		# Create the token
		return Token(TokenType.NUMBER, float(number_str))