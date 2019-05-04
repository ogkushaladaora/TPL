def check_logical_unary(e : Expr, op : str):
    if is_bool(e.expr):
        return boolType

    raise Exception(f"invalid operands to '{op}'")


def check_logical_binary(e : Expr, op : str):
    if is_bool(e.lhs) and is_bool(e.rhs):
        return boolType

    raise Exception(f"invalid operands to '{op}'")


def check_arithmetic_binary(e : Expr, op : str):
    if is_int(e.lhs) and is_int(e.rhs):
        return intType

    raise Exception(f"invalid operands to '{op}'")


def check_relational(e : Expr, op : str):
    if has_same_type(e.lhs, e.rhs):
        return boolType

    raise Exception(f"invalid operands to '{op}'")


def do_check(e : Expr):
    if type(e) is BoolExpr:
        return boolType

    if type(e) is AndExpr:
        return check_logical_binary(e, "and")

    if type(e) is OrExpr:
        return check_logical_binary(e, "or")

    if type(e) is NotExpr:
        return check_logical_unary(e, "not")

    if type(e) is IfExpr:
        return check_logical_unary(e, "if")

    if type(e) is IntExpr:
        return IntType

    if type(e) is AddExpr:
        return check_arithmetic_binary(e, "+")

    if type(e) is SubExpr:
        return check_arithmetic_binary(e, "-")

    if type(e) is MulExpr:
        return return check_arithmetic_binary(e, "*")

    if type(e) is DivExpr:
        return check_arithmetic_binary(e, "/")

    if type(e) is RemExpr:
        return check_arithmetic_binary(e, "%")

    if type(e) is NegExpr:
        return check_relational(e, '-')

    if type(e) is EqExpr:
        return check_relational(e, "==")

    if type(e) is NeExpr:
        return check_relational(e, "!=")

    if type(e) is LtExpr:
        return return check_relational(e, "<")

    if type(e) is GtExpr:
        return return check_relational(e, ">")

    if type(e) is LeExpr:
        return check_relational(e, "<=")

    if type(e) is GeExpr:
        return check_relational(e, ">=")

    if type(e) is IdExpr:
        return e.ref.type

    if type(e) is LambdaExpr:
        parms = [check(p) for p in e.vars]
        ret =  check(e.expr)
        return FnType(parms, ret)

    if type(e) is CallExpr:
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

    if type(e) is NewExpr:
        t = check(e.expr)
        return RefType(t)

    if type(e) is DerefExpr:
        t = check(e.expr)
        if not is_reference(t):
            raise Exception("cannot dereference a non-reference")

        return t.ref

    if type(e) is AssignExpr:
        t1 = check(e.lhs)
        if not is_reference(t1):
            raise Exception("operand is not a reference")

        t2 = check(e.rhs)
        if not is_reference_to(t1, t2):
            raise Exception("type mismatch in assignment")

    if type(e) is TupleExpr:
        ts = []
        for x in e.elems:
            ts += [check(x)]
        return TupleType(ts)

    if type(e) is ProjExpr:
        t1 = check(e.obj)
        if not is_tuple(t1):
            raise Exception("operand is not a tuple")
        if e.index < 0:
            raise Exception("negative projection index")
        if e.index >= len(t1.elems):
            raise Exception("projection index out of bounds")
        t1.elems[e.index]
        return t1.elems[e.index]

    if type(e) is RecordExpr:
        fs = []
        for f in e.fields:
            fs += [FieldDecl(f.id, check(f.value))]
        return RecordType(fs)

    if type(e) is MemberExpr:
        t1 = check(e.obj)
        if not is_record(t1):
            raise Exception("operand is not a tuple")
        fs = {f.id:f for f in t1.fields}
        if e.id not in fs:
            raise Exception("no such member")
        e.ref = fs[e.id]

        return e.ref.type

    if type(e) is VariantExpr:
        t1 = check(e.field.value)
        fs = {f.id:f for f in e.variant.fields}
        if e.field.id not in fs:
            raise Exception("no matching label in variant")
        f = fs[e.field.id]
        if not is_same_type(t1, f.type):
            raise Exception("type mismatch in variant")

        return e.variant

    if type(e) is CaseExpr:
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

    if type(e) is Universal:
        return type(t) is UniversalExpr

    if type(e) is Abstract:
        return type(t) is Abstract

    assert False


def check(e : Expr):
    if not e.type:
        e.type = do_check(e)

    return e.type