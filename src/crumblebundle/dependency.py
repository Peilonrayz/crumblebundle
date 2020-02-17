import collections
import functools

from .base_input import ReqInput, Input
from .helpers import Dict


from jinja2 import Environment


PartialNode = collections.namedtuple('PartialNode', 'path fn tags extensions')
Node = collections.namedtuple('Node', 'path fn tags supplies requires')


class MockDict(collections.defaultdict):
    def __missing__(self, key):
        self[key] = ret = type(self)()
        return ret

    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value


class Instance:
    def __init__(self, dependency):
        self.dependency = dependency
        self.input = Input(self)
        self.cookiecutter = {}


class Dependency:
    def __init__(self, building, config):
        self.building = building
        self.config = config
        self.fns, self.env = self.build_functions()
        self._requirements = None

    def build_functions(self):
        fns = []
        extensions = set(self.config.get('_extensions', []))
        env = Environment(extensions=list(extensions))
        for (path, fn, tags, exts) in self.building.fns:
            if exts:
                exts = set(exts)
                if exts - extensions:
                    extensions.update(exts)
                    env = Environment(extensions=list(extensions))
            requirements = MockDict()
            supplies = list(Dict.keys(fn.__wrapped__(ReqInput(requirements, self.config, env))))
            requirements = list(Dict.keys(requirements))
            fns.append(Node(path, fn, tags, supplies, requirements))
        if extensions:
            self.config['_extensions'] = list(extensions)
        return fns, env

    def run(self):
        try:
            instance = Instance(self)
            for fn in self.fns:
                output = fn.fn(instance)
                Dict.merge(instance.cookiecutter, output)
            if '_copy_without_render' in self.config:
                instance.cookiecutter['_copy_without_render'] = self.config['_copy_without_render']
            if '_extensions' in self.config:
                instance.cookiecutter['_extensions'] = self.config['_extensions']
            return instance
        except KeyboardInterrupt:
            raise KeyboardInterrupt() from None  # Clean traceback


class BuildingDependency:
    def __init__(self):
        self.tags = []
        self.fns = []

    def add_node(self, path, fn, tags, extensions):
        @functools.wraps(fn)
        def inner(instance):
            return fn(instance.input)
        self.fns.append(PartialNode(path, inner, tags, extensions))

    def build(self, config):
        return Dependency(self, config)


dependency = BuildingDependency()
