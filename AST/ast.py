class expr:
	# The expression language (EL) consists of the following strings:
	#
	# e ::= true
	#		false
	#		net e1
	#		e1 and e2
	#		e1 or e2
	pass

classs boolexpr(expr):
	def __init__(self val):
		self.value = val

classs notexpr(expr):
	def __init__(self e):
		self.value = e

classs andexpr(expr):

	def __init__(self, lhs, rhs):

		self.lhs = lhs
		self.rhs = rhs

classs orexpr(expr):
	def __init__(self, lhs, rhs):
		self.lhs = lhs
		self.rhs = rhs