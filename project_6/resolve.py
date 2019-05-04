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