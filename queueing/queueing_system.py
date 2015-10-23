__author__ = 'nzhang'


import threading
from threading import Thread
import sys
import time
import heapq
import random

class queueing_system(object):
    def __init__(self, capacity, server_count, terminal_count, arrival_rate, service_rate):
        self.capacity = capacity
        self.server_count = server_count
        self.terminal_count = terminal_count
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate
        self.event_list = []
        self.time_line = 0
        self.N = 0


    def __exp_rv(self, rate):
        return random.expovariate(rate)


    def generate_departure_time(self, time_offset):
        if self.N == 0:
            return -1
        return time_offset + self.__exp_rv((self.capacity-len(self.event_list))*self.arrival_rate)

    def generate_arrival_time(self, time_offset):
        if self.N == self.capacity+self.server_count:
            return -1
        return time_offset + self.__exp_rv((self.capacity-len(self.event_list))*self.arrival_rate)
        pass

    def run(self):
        pass


def main():
    pass

if __name__ == '__main__':

    main()