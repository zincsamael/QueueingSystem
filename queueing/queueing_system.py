__author__ = 'nzhang'


import threading
from threading import Thread
import sys
import time
import heapq
import random

class queueing_system(object):
    def __init__(self, capacity, server_count, terminal_count, Rho, service_rate, depart_count=100000):
        self.capacity = capacity
        self.server_count = server_count
        self.terminal_count = terminal_count
        self.rho = Rho
        self.arrival_rate = Rho*server_count*service_rate
        self.service_rate = service_rate
        self.event_list = []
        self.time_line = 0
        self.N = 0
        self.iteration = depart_count
        self.arrival = 0
        self.area = 0
        self.total_time = 0


    def __exp_rv(self, rate):
        return random.expovariate(rate)

    def get_miu(self):
        return min(self.N, self.server_count) *self.service_rate

    def get_lambda(self):
        return self.terminal_count*self.arrival_rate

    def generate_departure_time(self, time_offset):
        if self.N == 0:
            return -1
        return time_offset + self.__exp_rv(self.get_miu())

    def generate_arrival_time(self, time_offset):
        if self.N == self.capacity+self.server_count:
            return -1
        return time_offset + self.__exp_rv(self.get_lambda())

    def add_event(self, event):
        heapq.heappush(self.event_list, event)

    def pop_event(self):
        return heapq.heappop(self.event_list)

    def add_arrival_event(self, cur_time):
        new_event = (self.generate_arrival_time(cur_time), 'A')
        self.add_event(new_event)

    def add_departure_event(self, cur_time):
        new_event = (self.generate_departure_time(cur_time), 'D')
        self.add_event(new_event)

    def run(self):
        self.add_arrival_event(0)
        self.N += 1
        while self.arrival < self.iteration or self.N > 0:
            event = self.pop_event()
            cur_time = event[0]
            event_type = event[1]
            if event_type == 'A':

                if self.N<self.server_count:
                    self.add_departure_event(cur_time)
                if self.arrival < self.iteration:
                    self.add_arrival_event(cur_time)
                    self.arrival += 1
                    self.N += 1
            else:
                if self.N>self.server_count:
                    self.add_departure_event(cur_time)
                print self.event_list
                self.N -= 1





def main():
    q = queueing_system(capacity=4, server_count=2, terminal_count=10, service_rate=3, Rho=0.1)
    q.run()
    print q.arrival
    print q.N

if __name__ == '__main__':

    main()