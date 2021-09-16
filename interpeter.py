from nodes import  *
from values import Number



class Interpeter:
	def visit(self, node):
		method_name = f'visit_{type(node).__name__}'
		method = getattr(self, method_name)
		return method(node)

	def visit_NumberNode(self, node) -> Number:
		return Number(node.value)

	def visit_AddNode(self, node) -> Number:
		return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

	def visit_SubtractNode(self, node) -> Number:
		return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

	def visit_MultiplyNode(self, node) -> Number:
		return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

	def visit_DivideNode(self, node) -> Number:
		try:
			return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
		except Exception:
			raise Exception("Runtime Math error (division)")

	def visit_PlusNode(self, node) -> Number:
		return self.visit(node.node)

	def visit_MinusNode(self, node) -> Number:
		return Number(-self.visit(node.node).value)

	def visit_FactorialNode(self, node) -> Number:
		fact = lambda x: 1 if x == 0 else x * fact(x-1)
		try:
			return Number(fact(self.visit(node.node).value))
		except Exception:
			raise Exception("Runtime Math error (Factorial)")

	def visit_PowerNode(self, node) -> Number:
		return Number(pow(self.visit(node.node_a).value, self.visit(node.node_b).value))

	def visit_ModouleNode(self, node) -> Number:
		return Number(self.visit(node.node_a).value % self.visit(node.node_b).value)

	def visit_AverageNode(self, node) -> Number:
		return Number((self.visit(node.node_a).value + self.visit(node.node_b).value) / 2.0 )

	def visit_MaximumNode(self, node) -> Number:
		return Number(max(self.visit(node.node_a).value, self.visit(node.node_b).value) )

	def visit_MinimumNode(self, node) -> Number:
		return Number(min(self.visit(node.node_a).value, self.visit(node.node_b).value) )

	