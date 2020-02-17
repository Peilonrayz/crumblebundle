from .helpers import Dict
from .dependency import dependency


def item_value(path, tags=None, extensions=None, fn=None, dependency=dependency):
    def wrapper(fn):
        dependency.add_node(path, fn, tags, extensions)
    return wrapper if fn is None else wrapper(fn)


def value(path, output, default='', name=None, tags=None, extensions=None):
    def fn(input):
        ret = {}
        Dict.set(ret, output, input.value(name, output, default))
        return ret
    if name is None:
        name = ' '.join(s.replace('_', ' ').title() for s in path.split('.')[-1].split())
    fn.__name__ = fn.__qualname__ = name
    return item_value(path, tags, extensions, fn)


def option(path, output, options, default=None, name=None, tags=None, extensions=None):
    def fn(input):
        ret = {}
        Dict.set(ret, output, input.option(name, output, options, default))
        return ret

    if default is None:
        default = options[0]
    if name is None:
        name = ' '.join(s.replace('_', ' ').title() for s in path.split('.')[-1].split())
    fn.__name__ = fn.__qualname__ = name
    return item_value(path, tags, extensions, fn)


def multiple(path, output, options, default=None, name=None, tags=None, extensions=None):
    def fn(input):
        ret = {}
        Dict.set(ret, output, input.multiple(name, output, options, default))
        return ret

    if default is None:
        default = options[0]
    if name is None:
        name = ' '.join(s.replace('_', ' ').title() for s in path.split('.')[-1].split())
    fn.__name__ = fn.__qualname__ = name
    return item_value(path, tags, extensions, fn)
