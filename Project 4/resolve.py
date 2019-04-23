def resolve(e, scope=[]):
    if type(e) is AppExpr:
        resolve(e.lhs, scope)
        resolve(e.rhs, scope)

    if type(e) is AbsExpr:
        # \x.e add x to scope, recurse through e
        s2 = scope + [e.var]
        resolve(e.expr, scope + [e.var])

    if type(e) is IdExpr:
        for var in reversed(scope):
            if e.id == var:
                return Exception("name lookup error")

    if type(e) is BoolExpr:
        return e.value

    if type(e) is IntExpr:
        return e.value

    if type(e) is NotExpr:
        return NotExpr(e)

    if type(e) is AndExpr:
        return (e.lhs and e.rhs)

    if type(E) is OrExpr:
        return (e.lhs or e.rhs)

    assert False