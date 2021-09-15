from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
	NUMBER		= 0
	PLUS		= 1
	MINUS		= 2
	MULTIPLY	= 3
	DIVIDE 		= 4
	POWER		= 5
	MODULE		= 6
	FACTORIAL	= 7
	AVERAGE		= 8
	MAXIMUM		= 9
	MINIMUM		= 10
	LBRACKET	= 11
	RBRACKET	= 12

@dataclass
class Token:
	type: TokenType
	value: any = None

	def __repr__(self):
		return self.type.name + (f"{self.value}" if self.value != None else "")