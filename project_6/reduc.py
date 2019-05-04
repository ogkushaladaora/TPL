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