from nodes import  *
from values import Number



class Interpeter:
	def visit(self, node):
		method_name = f'visit_{type(node).__name__}'
		method = getattr(self, method_name)
		return method(node)

	def visit_NumberNode(self, node):
		return Number(node.value)

	def visit_AddNode(self, node):
		return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

	def visit_SubtractNode(self, node):
		return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

	def visit_MultiplyNode(self, node):
		return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

	def visit_DivideNode(self, node):
		try:
			return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
		except Exception:
			raise Exception("Runtime Math error (division)")

	def visit_PlusNode(self, node):
		return self.visit(node.node)

	def visit_MinusNode(self, node):
		return Number(-self.visit(node.node).value)

	def visit_FactorialNode(self, node):
		fact = lambda x: 1 if x == 0 else x * fact(x-1)
		try:
			return Number(fact(self.visit(node.node).value))
		except Exception:
			raise Exception("Runtime Math error (Factorial)")