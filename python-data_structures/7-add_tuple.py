#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > 2:
        tuple_a = tuple_a[0:2]
    elif len(tuple_a) == 1:
        la = list(tuple_a)
        la.append(0)
        tuple_a = tuple(la)
    elif len(tuple_a) == 0:
        tuple_a = (0, 0)
    if len(tuple_b) > 2:
        tuple_b = tuple_b[0:2]
    elif len(tuple_b) == 1:
        lb = list(tuple_b)
        lb.append(0)
        tuple_b = tuple(lb)
    elif len(tuple_b) == 0:
        tuple_b = (0, 0)
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
