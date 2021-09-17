from dataclasses import  dataclass


@dataclass
class NumberNode:
	value: float

	def __repr__(self):
		return f"{self.value}"


@dataclass
class AddNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"[{self.node_a}+{self.node_b}]"



@dataclass
class SubtractNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"[{self.node_a}-{self.node_b}]"



@dataclass
class MultiplyNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"[{self.node_a}*{self.node_b}]"


@dataclass
class DivideNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"[{self.node_a}/{self.node_b}]"

@dataclass
class PowerNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"[{self.node_b}^{self.node_b}]"


@dataclass
class ModuleNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"[{self.node_b}%{self.node_b}]"

@dataclass
class AverageNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"[{self.node_b}@{self.node_b}]"



@dataclass
class MaximumNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"[{self.node_b}${self.node_b}]"


@dataclass
class MinimumNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"[{self.node_b}&{self.node_b}]"



# Uniary symbols #

@dataclass
class PlusNode:
	node: any
	
	def __repr__(self):
		return f"(+{self.node})"


@dataclass
class MinusNode:
	node: any
	
	def __repr__(self):
		return f"(-{self.node})"


@dataclass
class FactorialNode:
	node: any

	def __repr__(self):
		return f"(!{self.node})"


@dataclass
class NegateNode:
	node: any

	def __repr__(self):
		return f"(~{self.node})"
