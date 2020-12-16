import requests


class ApiError(Exception):
    pass


def send_data_via_api():
    payload = {'key12': 'value1', 'key2': 'value2'}
    request = requests.post("http://dummy.restapiexample.com/api/v1/create", data=payload)

    if request.status_code == 200:
        print("Success to send data!")
    else:
        print("{}".format(request.status_code))
        print("{}".format(dir(request)))
        print("abc {}".format(request.url))
        raise ApiError("Error GET {}".format(request.status_code))

    return


if __name__ == '__main__':
    from collections import ChainMap

    dict1 = {'one': 1, 'two': 2}
    dict2 = {'three': 3, 'four': 4}
    chain = ChainMap(dict1, dict2)
    print(chain)
    print('=' * 100)
    from types import MappingProxyType

    writable = {'one': 1, 'two': 2}
    read_only = MappingProxyType(writable)
    print(read_only['one'])

    # read_only['one'] = 23
    writable['one'] = 42
    print(read_only)
    from collections import namedtuple

    Car = namedtuple('Carr', 'color_ mileage_ automatic')
    car1 = Car('red', 3812.4, True)
    print(car1)
    print(car1.mileage_)
