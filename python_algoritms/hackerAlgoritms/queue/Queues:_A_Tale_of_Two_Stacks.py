"""
Queues: A Tale of Two Stacks
https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues
Elaborar un quee first in and first out con array y clases
"""


class MyQueue(object):
    def __init__(self):
        self.total = []

    def peek(self):
        return self.total[0]

    def pop(self):
        self.total.pop(0)

    def put(self, value):
        self.total.append(value)


queue = MyQueue()
t = int(input())  # input de hacker rank
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
