class Expr:
    # The expression language (EL) consists of the following strings:
    #
    # e ::= true
    #       false
    #       net e1
    #       e1 and e2
    #       e1 or e2
    #
    # v ::= true
    #       false
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


class IdExpr(Expr):
    # represents identifiers that refer to variables
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return self.id


class VarDecl:
    # represents the declaration of a variable
    # not an expression, it is a declaration of a name
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return self.id


class AbsExpr(Expr):
    # represents abstractions
    # form \\x.e1
    def ___init___(self, var, e1):
        self.var = var
        self.expr = e1

    def __str__(self):
        return f"\\{self.var}.{self.expr}"


class AppExpr(Expr):
    # represents application
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def __str__(self):
        return f"{self.lhs} {self.rhs}"


def same(e1, e2):
    # returns true when e1 and e2 are the same string?
    # or when are not the same

    # quick reject
    if type(e1) is not type(e2):
        return False

    # now we know e1 and e2 are the same type

    if type(e1) is BoolExpr:
        return e1.value == e2.value

    if type(e1) is NotExpr:
        return same(e1.expr, e2.expr)

    if type(e1) is AndExpr:
        return same(e1.lhs, e2.lhs) and same(e2.rhs, e2.rhs)

    if type(e1) is OrExpr:
        return same(e1.lhs, e2.lhs) and same(e2.rhs, e2.rhs)


def same_str(e1, e2):
    return str(e1) == str(e2)


# step
def is_value(e):
    """returns true if e is a value, ie irreducible"""
    return type(e) is BoolExpr


def is_reducible(e):
    return not is_value(e)


def step_not(e):
    if type(e) is NotExpr:
        # ------------------ Not-T
        # not true ->false
        # ------------------Not-F
        # not false -> true
        # ------------------
        # Alternative for above:
        #
        # not v1 -> `not [v1]`
        #
        # e1 -> e1`
        # ------------------
        # not e1 -> not e1`
        if type(e.expr) is bool:
            # if is_value(e.Expr)
            if e.expr.value == True:  # not true
                return BoolExpr(False)
            else:
                return BoolExpr(True)  # not false

    return NotExpr(step(e.expr))


def step_and(e):
    # ----------------------And-V
    # v1 and v2 -> `[v1] and [v2]`
    #
    #        e1 -> e1`
    # ----------------------And-L
    # e1 and e2 -> e1` and v2
    #
    #        e2 ->e2`
    # ----------------------And-R
    # v1 and e2 -> v1 and e2`
    # v1 and e2 -> v1 and e2`
    if is_value(e.lhs) and is_value(e.rhs):
        # implement the truth table
        return BoolExpr(e.lhs.value and e.rhs.value)

    if is_reducible(e.lhs):  # applies and-l
        return AndExpr(step(e.lhs), e.rhs)

    if is_reducible(e.rhs):  # applies and-r
        return AndExpr(e.lhs, step(e.rhs))

    assert False


def step_or(e):
    # ----------------------or-V
    # v1 and v2 -> `[v1] and [v2]`
    #
    #        e1 -> e1`
    # ----------------------or-L
    # e1 and e2 -> e1` and v2
    #
    #        e2 ->e2`
    # ----------------------or-R
    # v1 and e2 -> v1 and e2`
    if is_value(e.lhs) and is_value(e.rhs):
        # implement the truth table
        return BoolExpr(e.lhs.value and e.rhs.value)

    if is_reducible(e.lhs):  # applies or-l
        return OrExpr(step(e.lhs), e.rhs)

    if is_reducible(e.rhs):  # applies or-r
        return OrExpr(e.lhs, step(e.rhs))

    assert False


def step(e):
    """compute the net state of the program"""
    assert is_reducible(e)

    if type(e) is NotExpr:
        return step_not(e)

    if type(e) is AndExpr:
        return step_and(e)

    if type(e) is OrExpr:
        return step_or(e)


def reduce(e):
    while is_reducible(e):
        e = step(e)
    return e
