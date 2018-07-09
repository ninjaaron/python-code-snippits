class Trigger:
    def __init__(self, func):
        self.func = func

    def __repr__(self):
        self.func()
        return ''

    def __truediv__(self, other):
        return self.func(other)

    def __getattr__(self, name):
        return self.func(name)

    def __getitem__(self, name):
        return self.func(name)


class Cmd:
    def __init__(self, cmd, mode=None):
        self.cmd = shlex.split(cmd) if isinstance(cmd, str) else cmd
        self.mode = mode

    def __pos__(self):
        return ep.grab(self.cmd)

    def __neg__(self):
        ep.run(self.cmd)

    def __repr__(self):
        -self
        return 'None'

    def __getitem__(self, value):
        if isinstance(value, (int, slice)):
            return (+self)[value]
        return Cmd(self.cmd+glob(os.path.expanduser(value)))

    def __getattr__(self, name):
        if name.startswith('_'):
            return Cmd(self.cmd+['-'+name[1:]])
        return self[name]

    def __call__(self, *args, **kwargs):
        return ep.grab(self.cmd, *args, **kwargs)

    def __iter__(self):
        return iter(+self)

    def __sub__(self, flag):
        return self.F/flag

    def __truediv__(self, value):
        return self[value]

    def __or__(self, func):
        return tuple(map(func, +self))

    def __dir__(self):
        return ep.grab('ls').tuple


# some example usage
def funky_junk():

    @Trigger
    def c(hint=None):
        os.chdir(dirlog.get_and_update(hint))
        -(sh/'ls --color=auto')

    @Trigger
    def vs(cmd):
        if inspect.ismodule(cmd):
            -(sh/env.PAGER/cmd.__file__)
            return
        what = +sh.which[cmd]
        if what.len > 1:
            ep.run([env.PAGER, '-c', 'set ft=sh'], stdin=what)
        else:
            sh/env.PAGER/what

    f = Trigger(lambda s: s.format(**inspect.stack()[2][0].f_locals))
    h = Trigger(lambda func=None: help() if func is None else help(func))
    sh = Trigger(lambda c: Cmd(c))
    ls, e, clear, view = sh/'ls --color=auto', sh.permedit, sh.clear, sh.vimpager
    ll, la, lla = ls._l, ls._a, ls._la
    rm = sh.rm._r
    globals().update(locals())
