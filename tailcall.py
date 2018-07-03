#  ==== crazy tailcall stuff - do not use ====  #
# performance is terrible
def _ispartial(node):
    try:
        return isinstance(node, tuple) and callable(node[0])
    except IndexError:
        return False


def _mkframe(node):
    frame = []
    while _ispartial(node[-1]):
        frame.append(node[:-1])
        node = node[-1]
    return frame, node


def computeframe(frame, val):
    while frame:
        call, *args = frame.pop()
        val = call(*args, val)
    return val


def tco(initial):
    stack = []
    val = initial
    while _ispartial(val):
        frame, (tailcall, *args) = _mkframe(val)
        stack.append(frame)
        val = tailcall(*args)

    while stack:
        val = computeframe(stack.pop(), val)

    return val
