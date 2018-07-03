"""immutable, singly-linked list based on tuples. For why, I don't know.
There are no classes. It just passes tuples around functions.

The only functions you really need are `make` and `iter`. `make` packs
*args into nested tuples. `iter` yeilds them back in order.

`car`, `cdr` and `cons` are simply wrappers on `llist[0]`, `llist[1]` and
`(val, llist)` respectively.

Might be useful if Python ever implements tailcall elimination. HA!
"""


def make(*args):
    llist = ()
    for arg in reversed(args):
        llist = (arg, llist)
    return llist


def iter(llist):
    while llist:
        head, llist = llist
        yield head


def car(llist):
    return llist[0]


def cdr(llist):
    return llist[1]


def cons(val, llist):
    return (val, llist)
