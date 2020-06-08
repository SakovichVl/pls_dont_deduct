def fun1(a, b, c):
    return True


def cached(function):
    cache = {}

    def cached_check(*args, **kwargs):
        key = args + tuple(kwargs.values())
        if not cache.get(key):
            print("кэшируем")
            cache[key] = function(*args, **kwargs)
        else:
            print("готово")
        return cache[key]
    return cached_check


decorator = cached(fun1)

decorator(True, True, False)
decorator(False, True, True)
decorator(True, True, False)

