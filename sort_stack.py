# -*- coding: utf-8 -*-

from queue import LifoQueue


def sort_stack(stack):
    """
    Sort a stack using a temporary stack.
    :param stack: input stack
    :return: sorted stack.
    """
    tmp_stack = LifoQueue()
    while not stack.empty():
        tmp = stack.get()

        while not tmp_stack.empty() and int(tmp_stack.queue[-1]) > int(tmp):
            stack.put(tmp_stack.get())

        tmp_stack.put(tmp)

    return tmp_stack


if __name__ == "__main__":
    stack = LifoQueue()
    stack.queue = [34, 3, 31, 98, 92, 32]

    print("Sorted stack: ")
    print(sort_stack(stack).queue)
