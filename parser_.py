from ParserError import ParserError
from tokens import TokenType
from nodes import *

class Parser:
		
	def __init__(self, tokens):
		self.tokens = iter(tokens)
		self.advance()

	def raise_error(self):
		raise ParserError("Invalid syntax")

	def advance(self):
		try:
			self.current_token = next(self.tokens)
		except StopIteration:
			self.current_token = None


	def parse(self):
		if self.current_token == None:
			return None

		result = self.level1_operators()

		if self.current_token != None:
			self.raise_error()

		return result

	# Takes care of (+ -)
	def level1_operators(self):
		result = self.level2_operators()

		while self.current_token != None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
			if self.current_token.type == TokenType.PLUS:
				self.advance()
				result = AddNode(result, self.level2_operators())
			elif self.current_token.type == TokenType.MINUS:
				self.advance()
				result = SubtractNode(result, self.level2_operators())

		return result


	def level2_operators(self):
		result = self.level3_operators()

		while self.current_token != None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
			if self.current_token.type == TokenType.MULTIPLY:
				self.advance()
				result = MultiplyNode(result, self.level3_operators())
			elif self.current_token.type == TokenType.DIVIDE:
				self.advance()
				result = DivideNode(result, self.level3_operators())

		return result


	def level3_operators(self):
		result = self.level4_operators()

		while self.current_token != None and self.current_token.type == TokenType.POWER:
			self.advance()
			result = PowerNode(result, self.level4_operators())

		return result

	def level4_operators(self):
		result = self.level5_operators()

		while self.current_token != None and self.current_token.type in (TokenType.MODULE, TokenType.FACTORIAL):
			if self.current_token.type == TokenType.MODULE:
				self.advance()
				result = ModuleNode(result, self.level5_operators())
			elif self.current_token.type == TokenType.FACTORIAL:
				self.advance()
				result = FactorialNode(self.level5_operators(result))

		return result


	def level5_operators(self, num=None):

		if num != None:
			result = num
		else:	
			result = self.level6_operators()
		

		while self.current_token != None and self.current_token.type in (TokenType.AVERAGE, TokenType.MAXIMUM, TokenType.MINIMUM):
			if self.current_token.type == TokenType.AVERAGE:
				self.advance()
				result = AverageNode(result, self.level6_operators())
			elif self.current_token.type == TokenType.MAXIMUM:
				self.advance()
				result = MaximumNode(result, self.level6_operators())
			elif self.current_token.type == TokenType.MINIMUM:
				self.advance()
				result = MinimumNode(result, self.level6_operators())

		return result


	def level6_operators(self):
		token = self.current_token



		if token.type == TokenType.LBRACKET:
			self.advance()
			result = self.level1_operators()

			if self.current_token.type != TokenType.RBRACKET:
				self.raise_error()
			
			self.advance()
			return result

		elif token.type == TokenType.NUMBER:
			self.advance()
			return NumberNode(token.value)

		elif token.type == TokenType.PLUS:
			self.advance()
			return PlusNode(self.level6_operators())

		elif token.type == TokenType.MINUS:
			self.advance()
			return MinusNode(self.level6_operators())

		elif token.type == TokenType.NEGATE:
			self.advance()
			return NegateNode(self.level6_operators())

		return None
	



	@staticmethod
	def strip_str(level1_operators : str):
		"""removes all unnecessery characters from level1_operatorsession

		Args:s
			level1_operators (str): the level1_operatorsession that will be stripped

		Raises:
			ParserError: Error if parsing failed

		Returns:
			str: The level1_operatorsession without the unnecessery characters
		"""
		try:
			temp_list = level1_operators.split()
			level1_operators = ''.join(temp_list)
			level1_operators = level1_operators.replace('\\n', '')
			level1_operators = level1_operators.replace('\\t', '')
			return level1_operators
			

		except Exception as e:
			raise ParserError("Error during parsing: {e}")


	


	
	


	
