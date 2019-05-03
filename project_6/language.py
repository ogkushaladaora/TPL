import inspect
import typing
import copy

clone = copy.deepcopy

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
    # represents identifiers that refer to variables
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


def typify(x):
    if x is bool:
        return BoolType()
    if x is int:
        return IntType()
    return x


def expr(x):
    if type(x) is bool:
        return BoolExpr(x)
    if type(x) is int:
        return IntExpr(x)
    if type(x) is str:
        return IdExpr(x)
    return x


def decl(x):
    if type(x) is str:
        return VarDecl(x)
    return x


def field(x):
    if type(x) is tuple:
        return FieldDecl(x[0], x[1])
    return x


def init(x):
    if type(x) is tuple:
        return FieldInit(x[0], x[1])
    return x


def case(x):
    if type(x) is tuple:
        return Case(x[0], x[1], x[2])
    return x


def checked(fn):
    types = typing.get_type_hints(fn)
    if len(types) == 0:
        raise Exception(f"{fn.__name__} has no type hints")

    parms = inspect.getfullargspec(fn).args

    def wrap(*args):
        for p, a in zip(parms, args):
            t = types[p]
            if (not isinstance(a, t)):
                raise Exception(f"'{type(a).__name__}' is not an instance of '{t.__name__}'")
        return fn(*args)

    return wrap


def lookup(id : str, stk : list):
    for scope in reversed(stk):
        if id in scope:
            return scope[id]
    return None


def resolve_unary(e : Expr, stk : list):
    resolve(e.expr, stk)
    return e


def resolve_binary(e : Expr, stk : list):
    resolve(e.lhs, stk)
    resolve(e.rhs, stk)
    return e


def resolve(e : Expr, stk : list = []):

    if type(e) is BoolExpr:
        return e

    if type(e) is AndExpr:
        return resolve_binary(e, stk)

    if type(e) is OrExpr:
        return resolve_binary(e, stk)

    if type(e) is NotExpr:
        return resolve_unary(e, stk)

    if type(e) is IfExpr:
        resolve(e.cond, stk)
        resolve(e.true, stk)
        resolve(e.false, stk)
        return e

    if type(e) is IntExpr:
        return e

    if type(e) is AddExpr:
        return resolve_binary(e, stk)

    if type(e) is SubExpr:
        return resolve_binary(e, stk)

    if type(e) is MulExpr:
        return resolve_binary(e, stk)

    if type(e) is DivExpr:
        return resolve_binary(e, stk)

    if type(e) is RemExpr:
        return resolve_binary(e, stk)

    if type(e) is NegExpr:
        return resolve_unary(e, stk)

    if type(e) is EqExpr:
        return resolve_binary(e, stk)

    if type(e) is NeExpr:
        return resolve_binary(e, stk)

    if type(e) is LtExpr:
        return resolve_binary(e, stk)

    if type(e) is GtExpr:
        return resolve_binary(e, stk)

    if type(e) is LeExpr:
        return resolve_binary(e, stk)

    if type(e) is GeExpr:
        return resolve_binary(e, stk)

    if type(e) is IdExpr:
        decl = lookup(e.id, stk)
        if not decl:
            raise Exception("name lookup error")

        e.ref = decl
        return e

    if type(e) is LambdaExpr:
        newstk = stk + [{var.id:var for var in e.vars}]
        resolve(e.expr, newstk)
        return e

    if type(e) is CallExpr:
        resolve(e.fn, stk)
        for a in e.args:
            resolve(e.fn, stk)
        return e

    if type(e) is NewExpr:
        return resolve_unary(e, stk)

    if type(e) is DerefExpr:
        return resolve_unary(e, stk)

    if type(e) is AssignExpr:
        return resolve_binary(e, stk)

    if type(e) is TupleExpr:
        for x in e.elems:
            resolve(x)
        return e

    if type(e) is ProjExpr:
        resolve(e.obj)
        return e

    if type(e) is RecordExpr:
        for f in e.fields:
            resolve(f.value)
        return e

    if type(e) is MemberExpr:
        resolve(e.obj)
        return e

    if type(e) is VariantExpr:
        resolve(e.field.value)
        return e

    if type(e) is CaseExpr:
        resolve(e.expr)
        for c in e.cases:
            newstk = stk + [{c.var.id, c.var}]
            resolve(c.expr, newstk)
        return e

    print(repr(e))
    assert False


def is_same_type(t1 : Type, t2 : Type):
    if type(t1) is not type(t2):
        return False

    if type(t1) is BoolType:
        return True
    
    if type(t1) is IntType:
        return True

    if type(t1) is FnType:
        for a, b in zip(t1.parms, t2.parms):
            if not is_same_type(a, b):
                return False
        return is_same_type(t1.ret, t2.ret)

    if type(t1) is RefType:
        return is_same_type(t1.ref, t2.ref)

    assert False


def is_bool(t : Type):
    return t == boolType;


def is_int(t : Type):
    return t == intType;


def is_function(t : Type):
    return type(t) is FnType


def is_reference(t : Type):
    return type(t) is RefType


def is_reference_to(t : Type, u : Type):
    return is_reference(t) and is_same_type(t.ref, u)


def is_tuple(t : Type):
    return type(t) is TupleType


def is_record(t : Type):
    return type(t) is RecordType


def is_variant(t : Type):
    return type(t) is VariantType


def has_same_type(e1 : Expr, e2 : Expr):
    return is_same_type(check(e1), check(e2))


def has_bool(e : Expr):
    return is_same_type(check(e), boolType)


def has_int(e : Expr):
    return is_same_type(check(e), intType)


def check_bool(e : Expr):
    return boolType


def check_int(e : Expr):
    return intType


def check_logical_unary(e : Expr, op : str):
    if is_bool(e.expr):
        return boolType

    raise Exception(f"invalid operands to '{op}'")


def check_logical_binary(e : Expr, op : str):
    if is_bool(e.lhs) and is_bool(e.rhs):
        return boolType

    raise Exception(f"invalid operands to '{op}'")


def check_and(e : Expr):
    return check_logical_binary(e, "and")


def check_or(e : Expr):
    return check_logical_binary(e, "or")


def check_arithmetic_binary(e : Expr, op : str):
    if is_int(e.lhs) and is_int(e.rhs):
        return intType

    raise Exception(f"invalid operands to '{op}'")


def check_add(e : Expr):
    return check_arithmetic_binary(e, "+")


def check_sub(e : Expr):
    return check_arithmetic_binary(e, "-")


def check_mul(e : Expr):
    return check_arithmetic_binary(e, "*")


def check_div(e : Expr):
    return check_arithmetic_binary(e, "/")


def check_rem(e : Expr):
    return check_arithmetic_binary(e, "%")


def check_relational(e : Expr, op : str):
    if has_same_type(e.lhs, e.rhs):
        return boolType

    raise Exception(f"invalid operands to '{op}'")  


def check_eq(e : Expr):
    return check_relational(e, "==")


def check_ne(e : Expr):
    return check_relational(e, "!=")


def check_lt(e : Expr):
    return check_relational(e, "<")


def check_gt(e : Expr):
    return check_relational(e, ">")


def check_le(e : Expr):
    return check_relational(e, "<=")


def check_ge(e : Expr):
    return check_relational(e, ">=")


def check_id(e : Expr):
    return e.ref.type


def check_lambda(e : Expr):
    parms = [check(p) for p in e.vars]
    ret =  check(e.expr)
    return FnType(parms, ret)


def check_call(e : Expr):
    t = check(e.fn)
    if not is_function(t):
        raise Exception("invalid function call")

    if len(e.args) < len(t.parms):
        raise Exception("too few arguments")
    if len(e.args) > len(t.parms):
        raise Exception("too many arguments")

    for i in range(len(e.args)):
        arg = check(e.args[i])
        parm = t.parms[i]
        if not is_same_type(arg, parm):
            raise Exception("parameter/argument mismatch")

    return t.ret


def check_new(e : Expr):
    t = check(e.expr)
    return RefType(t)

def check_deref(e : Expr):
    t = check(e.expr)
    if not is_reference(t):
        raise Exception("cannot dereference a non-reference")

    return t.ref


def check_assign(e : Expr):
    t1 = check(e.lhs)
    if not is_reference(t1):
        raise Exception("operand is not a reference")

    t2 = check(e.rhs)
    if not is_reference_to(t1, t2):
        raise Exception("type mismatch in assignment")


def check_tuple(e : Expr):
    ts = []
    for x in e.elems:
        ts += [check(x)]
    return TupleType(ts)


def check_proj(e : Expr):
    t1 = check(e.obj)
    if not is_tuple(t1):
        raise Exception("operand is not a tuple")
    if e.index < 0:
        raise Exception("negative projection index")
    if e.index >= len(t1.elems):
        raise Exception("projection index out of bounds")
    t1.elems[e.index]
    return t1.elems[e.index]


def check_record(e : Expr):
    fs = []
    for f in e.fields:
        fs += [FieldDecl(f.id, check(f.value))]
    return RecordType(fs)


def check_member(e : Expr):
    t1 = check(e.obj)
    if not is_record(t1):
        raise Exception("operand is not a tuple")
    fs = {f.id:f for f in t1.fields}
    if e.id not in fs:
        raise Exception("no such member")
    e.ref = fs[e.id]

    return e.ref.type


def check_variant(e : Expr):
    t1 = check(e.field.value)
    fs = {f.id:f for f in e.variant.fields}
    if e.field.id not in fs:
        raise Exception("no matching label in variant")
    f = fs[e.field.id]
    if not is_same_type(t1, f.type):
        raise Exception("type mismatch in variant")

    return e.variant


def check_case(e : Expr):
    t1 = check(e.expr)
    if not is_variant(t1):
        raise Exception("operand is not a variant")

    fs = {f.id:f for f in t1.fields}

    t2 = None
    for c in e.cases:
        if c.id not in fs:
            raise Exception("no matching case label in variant")
        f = fs[c.id]
        c.var.type = f.type

        t = check(c.expr)
        if not t2:
            t2 = t
        else:
            if not is_same_type(t, t2):
                raise Exception("case type mismatch")

    return t2


def do_check(e : Expr):
    if type(e) is BoolExpr:
        return check_bool(e)

    if type(e) is AndExpr:
        return check_logical_binary(e, "and")

    if type(e) is OrExpr:
        return check_logical_binary(e, "or")

    if type(e) is NotExpr:
        return check_logical_unary(e, "not")

    if type(e) is IfExpr:
        return check_if(e)

    if type(e) is IntExpr:
        return check_int(e)

    if type(e) is AddExpr:
        return check_add(e)

    if type(e) is SubExpr:
        return check_sub(e)

    if type(e) is MulExpr:
        return check_mul(e)

    if type(e) is DivExpr:
        return check_div(e)

    if type(e) is RemExpr:
        return check_rem(e)

    if type(e) is NegExpr:
        return check_neg(e)

    if type(e) is EqExpr:
        return check_eq(e)

    if type(e) is NeExpr:
        return check_ne(e)

    if type(e) is LtExpr:
        return check_lt(e)

    if type(e) is GtExpr:
        return check_gt(e)

    if type(e) is LeExpr:
        return check_le(e)

    if type(e) is GeExpr:
        return check_ge(e)

    if type(e) is IdExpr:
        return check_id(e)

    if type(e) is LambdaExpr:
        return check_lambda(e)

    if type(e) is CallExpr:
        return check_call(e)

    if type(e) is NewExpr:
        return check_new(e)

    if type(e) is DerefExpr:
        return check_deref(e)

    if type(e) is AssignExpr:
        return check_assign(e)

    if type(e) is TupleExpr:
        return check_tuple(e)

    if type(e) is ProjExpr:
        return check_proj(e)

    if type(e) is RecordExpr:
        return check_record(e)

    if type(e) is MemberExpr:
        return check_member(e)

    if type(e) is VariantExpr:
        return check_variant(e)

    if type(e) is CaseExpr:
        return check_case(e)

    if type(e) is Universal:
        return check_universal(e)

    assert False


def check(e : Expr):
    if not e.type:
        e.type = do_check(e)

    return e.type


def subst(e, s):
    if type(e) is BoolExpr:
        return e

    if type(e) is AndExpr:
        e1 = subst(e.lhs, s)
        e2 = subst(e.rhs, s)
        return AndExpr(e1, e2)

    if type(e) is OrExpr:
        e1 = subst(e.lhs, s)
        e2 = subst(e.rhs, s)
        return OrExpr(e1, e2)

    if type(e) is NotExpr:
        e1 = subst(e.expr, s)
        return NotExpr(e1)

    if type(e) is IfExpr:
        e1 = subst(e.cond, s)
        e2 = subst(e.true, s)
        e3 = subst(e.false, s)
        return IfExpr(e1, e2, e3)

    if type(e) is IdExpr:
        if e.ref in s:
            return s[e.ref]
        else:
            return e

    if type(e) is AbsExpr:
        e1 = subst(e.expr, s)
        return AbsExpr(e.var, e1)

    if type(e) is AppExpr:
        e1 = subst(e.lhs, s)
        e2 = subst(e.rhs, s)
        return AppExpr(e1, e2)

    if type(e) is LambdaExpr:
        e1 = subst(e.expr, s)
        return LambdaExpr(e.vars, e1)

    if type(e) is CallExpr:
        e0 = subst(e.fn, s)
        args = list(map(lambda x: subst(x, s), e.args))
        return CallExpr(e0, args)

    assert False


def is_value(e):
    return type(e) in (BoolExpr, AbsExpr, LambdaExpr)


def is_reducible(e):
    return not is_value(e)


def step_and(e):
    if is_reducible(e.lhs):
        return AndExpr(step(e.lhs), e.rhs)

    if is_reducible(e.rhs):
        return AndExpr(e.lhs, step(e.rhs))

    return BoolExpr(e.lhs.val and e.rhs.val)


def step_or(e):
    if is_reducible(e.lhs):
        return OrExpr(step(e.lhs), e.rhs)

    if is_reducible(e.rhs):
        return OrExpr(e.lhs, step(e.rhs))

    return BoolExpr(e.lhs.val or e.rhs.val)


def step_not(e):
    if is_reducible(e.expr):
        return NotExpr(step(e.expr))

    return BoolExpr(not e.expr.val)


def step_if(e):
    if is_reducible(e.cond):
        return NotExpr(step(e.cond), e.true, e.false)

    if e.cond.val:
        return e.true
    else:
        return e.false


def step_app(e):
    if is_reducible(e.lhs):
        return AppExpr(step(e.lhs), e.rhs)

    if type(e.lhs) is not AbsExpr:
        raise Exception("application of non-lambda")

    if is_reducible(e.rhs): # App-2
        return AppExpr(e.lhs, step(e.rhs))

    s = {
        e.lhs.var: e.rhs
    }
    return subst(e.lhs.expr, s);


def step_call(e):
    if is_reducible(e.fn):
        return CallExpr(step(e.fn), e.args)

    if len(e.args) < len(e.fn.vars):
        raise Exception("too few arguments")
    if len(e.args) > len(e.fn.vars):
        raise Exception("too many arguments")

    for i in range(len(e.args)):
        if is_reducible(e.args[i]):
            return CallExpr(e.fn, e.args[:i] + [step(e.args[i])] + e.args[i+1:])

    s = {}
    for i in range(len(e.args)):
        s[e.fn.vars[i]] = e.args[i]

    return subst(e.fn.expr, s);


def step(e):
    assert isinstance(e, Expr)
    assert is_reducible(e)

    if type(e) is AndExpr:
        return step_and(e)

    if type(e) is OrExpr:
        return step_or(e)

    if type(e) is NotExpr:
        return step_not(e)

    if type(e) is IfExpr:
        return step_if(e)

    if type(e) is AppExpr:
        return step_app(e)

    if type(e) is CallExpr:
        return step_call(e)

    assert False


def reduce(e):
    while not is_value(e):
        e = step(e)
        print(e)
    return e


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


def eval_binary(e : Expr, stack : dict, heap : list, fn : object):
    v1 = evaluate(e.lhs, stack, heap)
    v2 = evaluate(e.rhs, stack, heap)
    return fn(v1, v2)


def eval_unary(e : Expr, stack : dict, heap : list, fn : object):
    v1 = evaluate(e.lhs, stack, heap)
    return fn(v1)


def eval_bool(e : Expr, stack : dict, heap : list):
    return e.value


def eval_and(e : Expr, stack : dict, heap : list):
    return eval_binary(e, stack, heap, lambda v1, v2: v1 and v2)


def eval_or(e : Expr, stack : dict, heap : list):
    return eval_binary(e, stack, heap, lambda v1, v2: v1 or v2)


def eval_not(e : Expr, stack : dict, heap : list):
    return eval_unary(e, stack, heap, lambda v1: not v1)


def eval_cond(e, stack, heap : list):
    if evaluate(e.cond):
        return evaluate(e.true);
    else:
        return evaluate(e.false);


def eval_int(e : Expr, stack : dict, heap : list):
    return e.value


def eval_add(e : Expr, stack : dict, heap : list):
    return eval_binary(e, stack, heap, lambda v1, v2: v1 + v2)


def eval_sub(e : Expr, stack : dict, heap : list):
    return eval_binary(e, stack, heap, lambda v1, v2: v1 - v2)


def eval_mul(e : Expr, stack : dict, heap : list):
    return eval_binary(e, stack, heap, lambda v1, v2: v1 * v2)


def eval_div(e : Expr, stack : dict, heap : list):
    return eval_binary(e, stack, heap, lambda v1, v2: v1 / v2)


def eval_rem(e : Expr, stack : dict, heap : list):
    return eval_binary(e, stack, heap, lambda v1, v2: v1 % v2)


def eval_neg(e : Expr, stack : dict, heap : list):
    return eval_binary(e, stack, heap, lambda v1: -v1)


def eval_eq(e : Expr, stack : dict, heap : list):
    return eval_binary(e, stack, heap, lambda v1, v2: v1 == v2)


def eval_ne(e : Expr, stack : dict, heap : list):
    return eval_binary(e, stack, heap, lambda v1, v2: v1 != v2)


def eval_lt(e : Expr, stack : dict, heap : list):
    return eval_binary(e, stack, heap, lambda v1, v2: v1 < v2)


def eval_gt(e : Expr, stack : dict, heap : list):
    return eval_binary(e, stack, heap, lambda v1, v2: v1 > v2)


def eval_le(e : Expr, stack : dict, heap : list):
    return eval_binary(e, stack, heap, lambda v1, v2: v1 <= v2)


def eval_ge(e : Expr, stack : dict, heap : list):
    return eval_binary(e, stack, heap, lambda v1, v2: v1 >= v2)


def eval_id(e : Expr, stack : dict, heap : list):
    return stack[e.ref]


def eval_lambda(e : Expr, stack : dict, heap : list):
    return Closure(e, stack)


def eval_call(e : Expr, stack : dict, heap : list):
    c = evaluate(e.fn, stack, heap)
    
    if type(c) is not Closure:
        raise Exception("cannot apply a non-closure to an argument")

    args = []
    for a in e.args:
        args += [evaluate(a, stack, heap)]

    env = clone(c.env)
    for i in range(len(args)):
        env[c.abs.vars[i]] = args[i]

    return evaluate(c.abs.expr, env, heap)


def eval_new(e : Expr, stack : dict, heap : list):
    v1 = evaluate(e.expr, stack, heap)
    l1 = Location(len(heap))
    heap += [v1]
    return l1


def eval_deref(e : Expr, stack : dict, heap : list):
    l1 = evaluate(e.expr, stack, heap)
    if type(l1) is not Location:
        raise Exception("invalid reference")
    return heap[l1.index]


def eval_assign(e : Expr, stack : dict, heap : list):
    v2 = evaluate(e.rhs, stack, heap)
    l1 = evaluate(e.lhs, stack, heap)
    if type(l1) is not Location:
        raise Exception("invalid reference")
    heap[l1.index] = v2


def eval_tuple(e : Expr, stack : dict, heap : list):
    vs = []
    for x in e.elems:
        vs += [evaluate(x, stack, heap)]
    return Tuple(vs)


def eval_proj(e : Expr, stack : dict, heap : list):
    v1 = evaluate(e.obj, stack, heap)
    return v1.values[e.index]


def eval_record(e : Expr, stack : dict, heap : list):
    fs = []
    for f in e.fields:
        fs += [Field(f.id, evaluate(f.value, stack, heap))]
    return Record(fs)


def eval_member(e : Expr, stack : dict, heap : list):
    v1 = evaluate(e.obj, stack, heap)
    return v1.select[e.id]


def eval_variant(e : Expr, stack : dict, heap : list):
    v1 = evaluate(e.field.value)
    return Variant(e.field.id, v1)


def eval_case(e : Expr, stack : dict, heap : list):
    v1 = evaluate(e.expr, stack, heap)
    case = None
    for c in e.cases:
        if c.id == v1.tag:
            case = c
            break
    assert case != None

    env = clone(stack)
    env[c.var] = v1.value
    return evaluate(c.expr, env, heap)


def evaluate(e : Expr, stack : dict = {}, heap = []):
    if type(e) is BoolExpr:
        return eval_bool(e, stack, heap)

    if type(e) is AndExpr:
        return eval_and(e, stack, heap)

    if type(e) is OrExpr:
        return eval_or(e, stack, heap)

    if type(e) is NotExpr:
        return eval_not(e, stack, heap)

    if type(e) is IfExpr:
        return eval_if(e, stack, heap)

    if type(e) is IntExpr:
        return eval_int(e, stack, heap)

    if type(e) is AddExpr:
        return eval_add(e, stack, heap)

    if type(e) is SubExpr:
        return eval_sub(e, stack, heap)

    if type(e) is MulExpr:
        return eval_mul(e, stack, heap)

    if type(e) is DivExpr:
        return eval_div(e, stack, heap)

    if type(e) is RemExpr:
        return eval_rem(e, stack, heap)

    if type(e) is NegExpr:
        return eval_neg(e, stack, heap)

    if type(e) is EqExpr:
        return eval_eq(e, stack, heap)

    if type(e) is NeExpr:
        return eval_ne(e, stack, heap)

    if type(e) is LtExpr:
        return eval_lt(e, stack, heap)

    if type(e) is GtExpr:
        return eval_gt(e, stack, heap)

    if type(e) is LeExpr:
        return eval_le(e, stack, heap)

    if type(e) is GeExpr:
        return eval_ge(e, stack, heap)

    if type(e) is LambdaExpr:
        return eval_lambda(e, stack, heap)

    if type(e) is CallExpr:
        return eval_call(e, stack, heap)

    if type(e) is NewExpr:
        return eval_new(e, stack, heap)

    if type(e) is DerefExpr:
        return eval_deref(e, stack, heap)

    if type(e) is AssignExpr:
        return eval_assign(e, stack, heap)

    if type(e) is TupleExpr:
        return eval_tuple(e, stack, heap)

    if type(e) is ProjExpr:
        return eval_proj(e, stack, heap)

    if type(e) is RecordExpr:
        return eval_record(e, stack, heap)

    if type(e) is MemberExpr:
        return eval_member(e, stack, heap)

    if type(e) is VariantExpr:
        return eval_variant(e, stack, heap)

    if type(e) is CaseExpr:
        return eval_case(e, stack, heap)

    if type(e) is UniversalExpr:
        return eval_universal(e, stack, heap)

    assert False


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


def IsUniversal(t : type):
    return type(t) is UniversalExpr


def check_universal(e : Expr):
    return IsUniversal(e)


def eval_universal(e : Expr, stack : dict, heap : list):
    v1 = evaluate(e.field.value)