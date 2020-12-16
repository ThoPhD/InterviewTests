class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)


class NewRepeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value


class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value


class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value


def repeater(message):
    while True:
        yield message


def bounded_repeater(message, max_repeats):
    return (message for _ in range(max_repeats))


def call_repeater(message, function_id=1):
    repeater_ = Repeater(message)

    if function_id == 2:
        repeater_ = NewRepeater(message)
    elif function_id == 3:
        repeater_ = BoundedRepeater(message, 4)
    elif function_id == 4:
        repeater_ = repeater('HI')
    elif function_id == 5:
        repeater_ = bounded_repeater(message, 4)

    for item in repeater_:
        print(item)


if __name__ == "__main__":
    call_repeater('Hello', 5)
