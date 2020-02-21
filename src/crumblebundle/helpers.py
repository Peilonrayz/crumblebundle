import copy
import re
import warnings

DICT_KEY_SPLIT = re.compile(r"(?<!\\)\.")
_SENTINEL = object()


class Dict:
    @classmethod
    def _key(cls, key):
        return DICT_KEY_SPLIT.split(key)

    @classmethod
    def _escape_key(cls, key):
        return key.replace(".", r"\.")

    @classmethod
    def get(cls, obj, key, default=_SENTINEL):
        node = obj
        keys = list(enumerate(cls._key(key)))
        for i, k in keys:
            if k not in node:
                if default is _SENTINEL:
                    raise KeyError("{} doesn't exist".format(".".join(keys[:i])))
                else:
                    return default
            node = node[k]
        return node

    @classmethod
    def has(cls, obj, key):
        node = obj
        keys = list(enumerate(cls._key(key)))
        for i, k in keys:
            if k not in node:
                return False
            node = node[k]
        return True

    @classmethod
    def set(cls, obj, key, value):
        node = obj
        *keys, key = cls._key(key)
        for i, k in enumerate(keys):
            if k not in node:
                break
            node = node[k]
            if not isinstance(node, dict):
                raise TypeError("{} is not a dictionary".format(".".join(keys[:i])))

        node = obj
        for k in keys:
            node = node.setdefault(k, {})
        node[key] = value

    @classmethod
    def keys(cls, obj):
        for key, value in obj.items():
            key = cls._escape_key(key)
            if isinstance(value, dict):
                itered = False
                for nested in cls.keys(value):
                    itered = True
                    yield key + "." + nested

                if not itered:
                    yield key
            else:
                yield key

    @classmethod
    def _merge_check(cls, obj, from_obj, keys=()):
        for key, value in from_obj.items():
            keys = keys + (key,)
            if key not in obj:
                pass
            elif isinstance(value, dict) != isinstance(obj[key], dict):
                path = ".".join(cls._escape_key(k) for k in keys)
                raise ValueError("{path} type mismatch".format(path=path))
            else:
                cls._merge_check(obj[key], value, keys)

    @classmethod
    def merge(cls, obj, from_obj):
        cls._merge_check(obj, from_obj)

        for key, value in from_obj.items():
            if key not in obj:
                obj[key] = copy.deepcopy(value)
            elif isinstance(value, dict):
                cls.merge(obj[key], value)
            else:
                warnings.warn("Two crumbles are setting to the same path")
                obj[key] = value
