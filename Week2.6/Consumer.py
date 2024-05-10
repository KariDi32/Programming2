# Code from Anna Sorova
from abc import ABCMeta, abstractmethod
import json
import functools
from matplotlib import pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


class Consumer(metaclass=ABCMeta):
    id_gen = 0

    def __init__(self):
        self.id = Consumer.id_gen
        Consumer.id_gen += 1

    @abstractmethod
    def update(self, json_lines):
        pass

    @staticmethod
    def build_plot(x, y, x_label, y_label, title):
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.plot(x, y)
        plt.show()
