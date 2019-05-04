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