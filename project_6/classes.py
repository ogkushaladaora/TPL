import inspect
import typing
import copy

class Expr:
    # The expression language (EL) consists of the following strings:
    #
    # e ::= true
    #       false
    #       not e1
    #       e1 and e2
    #       e1 or e2
    #
    # v ::= true
    #       false
    pass


class Type:
    # represents bool and int types
    pass


class Value:
    # values boot and ints
    pass


class BoolExpr(Expr):
    def __init__(self, val):
        self.value = val

    def __str__(self):
        return "true" if self.value == True else "false"


class NotExpr(Expr):
    def __init__(self, e):
        self.value = e

    def __str__(self):
        return f"(not {self.Expr})"


class AndExpr(Expr):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def __str__(self):
        return f"({self.lhs} and {self.rhs})"


class OrExpr(Expr):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def __str__(self):
        return f"({self.lhs} or {self.rhs})"


class IfExpr(Expr):
    Expr.__init__(self)
    self.cond = expr(e1)
    self.true = expr(e2)
    self.false = expr(e3)

        def __str__(self):
    return f"(if {self.cond} then {self.true} else {self.false})"


class IdExpr(Expr):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return self.id


class IntExpr(Expr):
    def __init__(self, val):
        Expr.__init__(self)
        self.value = val

    def __str__(self):
        return str(self.value)


class AddExpr(Expr):
    def __init__(self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs = expr(rhs)

    def __str__(self):
        return f"({self.lhs} + {self.rhs})"


class SubExpr(Expr):
    def __init__(self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs = expr(rhs)

    def __str__(self):
        return f"({self.lhs} + {self.rhs})"


class MulExpr(Expr):
    def __init__(self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs = expr(rhs)

    def __str__(self):
        return f"({self.lhs} - {self.rhs})"


class DivExpr(Expr):
    def __init__(self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs = expr(rhs)

    def __str__(self):
        return f"({self.lhs} / {self.rhs})"


class RemExpr(Expr):
    def __init__(self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs = expr(rhs)

    def __str__(self):
        return f"({self.lhs} % {self.rhs})"


class NegExpr(Expr):
    def __init__(self, e1):
        Expr.__init__(self)
        self.expr = expr(e1)

    def __str__(self):
        return f"(-{self.expr})"


class EqExpr(Expr):
    def __init__(self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs = expr(rhs)

    def __str__(self):
        return f"({self.lhs} == {self.rhs})"


class NeExpr(Expr):
    def __init__(self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs = expr(rhs)

    def __str__(self):
        return f"({self.lhs} != {self.rhs})"


class LtExpr(Expr):
    def __init__(self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs = expr(rhs)

    def __str__(self):
        return f"({self.lhs} < {self.rhs})"


class GtExpr(Expr):
    def __init__(self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs = expr(rhs)

    def __str__(self):
        return f"({self.lhs} > {self.rhs})"


class LeExpr(Expr):
    def __init__(self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs = expr(rhs)

    def __str__(self):
        return f"({self.lhs} <= {self.rhs})"


class GeExpr(Expr):
      def __init__(self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs = expr(rhs)
    def __str__(self):
        return f"({self.lhs} >= {self.rhs})"


class LambdaExpr(Expr):
    def __init__(self, vars, e1):
         Expr.__init__(self)
         self.vars = list(map(decl, vars))
         self.expr = expr(e1)

   def __str__(self):
         parms = ",".join(str(v) for v in self.vars)
         return f"\\({parms}).{self.expr}"


class CallExpr(Expr):
    def __init__(self, fn, args):
        Expr.__init__(self)
        self.fn = expr(fn)
        self.args = list(map(expr, args))

    def __str__(self):
        args = ",".join(str(a) for a in self.args)
        return f"{self.fn} ({args})"


class PlaceholderExpr(Expr):
    def __init__(self):
        Expr.__init__(self)

    def __str__(self):
        return "_"


class NewExpr(Expr):
    def __init__(self, e):
        Expr.__init__(self)
        self.expr = expr(e)

    def __str__(self):
        return f"new {self.expr}"


class DerefExpr(Expr):
    def __init__(self, e):
        Expr.__init__(self)
        self.expr = expr(e)

    def __str__(self):
        return f"*{self.expr}"


class AssignExpr(Expr):
    def __init__(self, e1, e2):
        Expr.__init__(self)
        self.lhs = expr(e1)
        self.rhs = expr(e2)

    def __str__(self):
        return f"{self.lhs} = {self.rhs}"


class TupleExpr(Expr):
    def __init__(self, es):
        Expr.__init__(self)
        self.elems = list(map(expr, es))

    def __str__(self):
        es = ",".join(str(e) for e in self.elems)
        return f"{{{es}}}"


class ProjExpr(Expr):
    def __init__(self, e1, n):
        Expr.__init__(self)
        self.obj = e1
        self.index = n

    def __str__(self):
        return f"{str(self.obj)}.{self.index}"


class RecordExpr(Expr):
    def __init__(self, fs):
        Expr.__init__(self)
        self.fields = list(map(init, fs))

    def __str__(self):
        fs = ",".join(str(e) for e in self.fields)
        return f"{{{fs}}}"


class MemberExpr(Expr):
    def __init__(self, e1, id):
        Expr.__init__(self)
        self.obj = e1
        self.id = id
        self.Ref = None

    def __str__(self):
        return f"{str(self.obj)}.{self.id}"


class VariantExpr(Expr):
    def __init__(self, f, t):
        Expr.__init__(self)
        self.field = init(f)
        self.variant = typify(t)

    def __str__(self):
        return f"<{str(self.field)}> as {str(self.type)}"


class Case:
    def __init__(self, id, n, e):
        self.id = id
        self.var = VarDecl(n, None)
        self.expr = expr(e)
    
    def __str__(self):
        return f"<{str(self.id)}={str(self.var)}> => {str(self.expr)}"


class CaseExpr(Expr):
    def __init__(self, e, cs):
        Expr.__init__(self)
        self.expr = expr(e)
        self.cases = list(map(case, cs))

    def __str__(self):
        cs = " | ".join([str(c) for c in self.cases])
        return f"case {str(self.expr)} of {cs}"


class Closure:
    def __init__(self, abs, env):
        self.abs = abs
        self.env = clone(env)

    def __str__(self):
        return f"<{str(self.abs)}>"


class Location:
    def __init__(self, ix):
        self.index = ix

    def __str__(self):
        return f"@{self.index}"


class Tuple:
    def __init__(self, vs : list):
        self.values = vs

    def __str__(self):
        vs = ",".join([str(v) for v in self.values])
        return f"{{{vs}}}"


class Field:
    def __init__(self, n, v):
        self.id = n
        self.value = v

    def __str__(self):
        return f"{self.id}={self.value}"


class Record:
    def __init__(self, fs : list):
        self.fields = fs
        self.select = {f.id:f.value for f in fs}

    def __str__(self):
        fs = ",".join([str(e) for e in self.fields])
        return f"{{{fs}}}"


class Variant:
    def __init__(self, l, v):
        self.tag = l
        self.value = v

    def __str__(self):
        return f"<{self.tag}={self.value}>"


class UniversalExpr(Expr):
    def __init__(self, types, variables):
        self.types = types
        self.variables = variables

    def __str__(self):
        return f"{self.types} + " " + {self.variables}"


class Abstract(Expr):
    def __init__(self, datums):
        self.data = datums

    def __str__(self):
        return f"{self.data} in Abstract Form"