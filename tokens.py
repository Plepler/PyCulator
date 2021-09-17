from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
	NUMBER		= 0
	PLUS		= 1
	MINUS		= 2
	NEGATE		= 3
	MULTIPLY	= 4
	DIVIDE 		= 5
	POWER		= 6
	MODULE		= 7
	FACTORIAL	= 8
	AVERAGE		= 9
	MAXIMUM		= 10
	MINIMUM		= 11
	LBRACKET	= 12
	RBRACKET	= 13

@dataclass
class Token:
	type: TokenType
	value: any = None

	def __repr__(self):
		return self.type.name + (f"{self.value}" if self.value != None else "")