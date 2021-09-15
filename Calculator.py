from interpeter import Interpeter
from ParserError import ParserError
from lexer import Lexer
import traceback
from parser_ import Parser

# Test string:
# 1 % [2 + !3 * 8] @ 2 $ -321.123 - ~12 + 221 & 1000 ^ -1

def main():
	
	while True:
		
		try:
			expr = input("> ")
			expr = Parser.strip_str(expr)
			lexer = Lexer(expr)
			tokens = lexer.generate_tokens()
			parser = Parser(tokens)
			tree = parser.parse()
			if not tree: continue
			interpeter = Interpeter()
			value = interpeter.visit(tree)
			print(value)


		except ParserError as e:
			print("ParserError: ", str(e))

		except Exception as e:
			print(type(e), end ='')
			print(" occured\n" + str(e))
			traceback.print_exc()



if __name__ == '__main__':
	main()