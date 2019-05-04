import classes.py

clone = copy.deepcopy

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


import resolve.py


import isdefs.py


import check.py


import reduc.py


import evaluate.py
