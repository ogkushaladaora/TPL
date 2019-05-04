def eval_binary(e : Expr, stack : dict, heap : list, fn : object):
    v1 = evaluate(e.lhs, stack, heap)
    v2 = evaluate(e.rhs, stack, heap)
    return fn(v1, v2)


def eval_unary(e : Expr, stack : dict, heap : list, fn : object):
    v1 = evaluate(e.lhs, stack, heap)
    return fn(v1)


def eval_cond(e, stack, heap : list):
    if evaluate(e.cond):
        return evaluate(e.true);
    else:
        return evaluate(e.false);


def evaluate(e : Expr, stack : dict = {}, heap = []):
    if type(e) is BoolExpr:
        return e.value

    if type(e) is AndExpr:
        return eval_binary(e, stack, heap, lambda v1, v2: v1 and v2)

    if type(e) is OrExpr:
        return eval_binary(e, stack, heap, lambda v1, v2: v1 or v2)

    if type(e) is NotExpr:
        return eval_unary(e, stack, heap, lambda v1: not v1)

    if type(e) is IfExpr:
        return eval_binary(e, stack, heap, lambda v1, v2: v1 ? v2)

    if type(e) is IntExpr:
        return e.value

    if type(e) is AddExpr:
        return eval_binary(e, stack, heap, lambda v1, v2: v1 + v2)

    if type(e) is SubExpr:
        return eval_binary(e, stack, heap, lambda v1, v2: v1 - v2)

    if type(e) is MulExpr:
        return eval_binary(e, stack, heap, lambda v1, v2: v1 * v2)

    if type(e) is DivExpr:
        return eval_binary(e, stack, heap, lambda v1, v2: v1 / v2)

    if type(e) is RemExpr:
        return eval_binary(e, stack, heap, lambda v1, v2: v1 % v2)

    if type(e) is NegExpr:
        return eval_binary(e, stack, heap, lambda v1: -v1)

    if type(e) is EqExpr:
        return eval_binary(e, stack, heap, lambda v1, v2: v1 == v2)

    if type(e) is NeExpr:
        return eval_binary(e, stack, heap, lambda v1, v2: v1 != v2)

    if type(e) is LtExpr:
        return eval_binary(e, stack, heap, lambda v1, v2: v1 < v2)

    if type(e) is GtExpr:
        return eval_binary(e, stack, heap, lambda v1, v2: v1 > v2)

    if type(e) is LeExpr:
        return eval_binary(e, stack, heap, lambda v1, v2: v1 <= v2)

    if type(e) is GeExpr:
        return eval_binary(e, stack, heap, lambda v1, v2: v1 >= v2)

    if type(e) is IdExpr:
        return stack[e.ref]

    if type(e) is LambdaExpr:
        return Closure(e, stack)

    if type(e) is CallExpr:
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

    if type(e) is NewExpr:
        v1 = evaluate(e.expr, stack, heap)
        l1 = Location(len(heap))
        heap += [v1]
        return l1

    if type(e) is DerefExpr:
        l1 = evaluate(e.expr, stack, heap)
        if type(l1) is not Location:
            raise Exception("invalid reference")
        return heap[l1.index]

    if type(e) is AssignExpr:
        v2 = evaluate(e.rhs, stack, heap)
        l1 = evaluate(e.lhs, stack, heap)
        if type(l1) is not Location:
            raise Exception("invalid reference")
        heap[l1.index] = v2

    if type(e) is TupleExpr:
        vs = []
        for x in e.elems:
            vs += [evaluate(x, stack, heap)]
        return Tuple(vs)

    if type(e) is ProjExpr:
        v1 = evaluate(e.obj, stack, heap)
        return v1.values[e.index]

    if type(e) is RecordExpr:
        fs = []
        for f in e.fields:
            fs += [Field(f.id, evaluate(f.value, stack, heap))]
        return Record(fs)

    if type(e) is MemberExpr:
        v1 = evaluate(e.obj, stack, heap)
        return v1.select[e.id]

    if type(e) is VariantExpr:
        v1 = evaluate(e.field.value)
        return Variant(e.field.id, v1)

    if type(e) is CaseExpr:
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

    if type(e) is UniversalExpr:
        v1 = evaluate(e.field.value)
        return v1

    if type(e) is Abstract:
        return type(e)

    assert False
