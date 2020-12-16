import operator
import sys

print('Python %s on %s' % (sys.version, sys.platform))


def div(tu_so, mau_so):
    if mau_so == 0:
        return 'Mau so phai khac 0.'
    return operator.truediv(tu_so, mau_so)


DISPATCH_DICT = {
    'add': operator.add,
    'sub': operator.sub,
    'mul': operator.mul,
    'div': div
}


def dispatch_dict(operator_, x, y):
    return DISPATCH_DICT.get(operator_, lambda: None)(x, y)


if __name__ == '__main__':
    print(dispatch_dict('mul', 5, 6))
    print(dispatch_dict('add', 4, 6))
    print(dispatch_dict('sub', 4, 6))
    # print(dispatch_dict('unknow', 4, 6))
    print(dispatch_dict('div', 5, 3))
    print(dispatch_dict('div', 5, 0))
    print('=' * 100)
    print(dispatch_dict.__code__.co_varnames)
