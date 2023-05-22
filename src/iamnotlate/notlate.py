import time
from time import struct_time

from typing import TypeAlias
_TimeTuple: TypeAlias = tuple[int, int, int, int, int, int, int, int, int]

INFO = {
    'M': (60, 60, 17, '%02d'),
    'H': (60, 3600, 14, '%02d'),
    'd': (24, 86400, 11, '%02d'),
    'b': (7, 604800, 8, '%2d'),
}

__TODO = ['gmtime', 'localtime', 'mktime',
          'strftime', 'strptime', 'struct_time']


class notLate:
    def __init__(self, deadline: float, w: int = 'M') -> None:
        'Mon May 22 05:26:15 2023'
        'Mon May 22 05:26:68 2023'
        'Mon May 22 05:68:15 2023'
        'Mon May 22 25:26:15 2023'
        'Mon May 35 05:26:15 2023'
        '012345678901234567890'
        if w not in INFO:
            raise ValueError('w:%d not in "MHdb"' % w)
        self.w = w
        self.__mul, self.__dr, self.__il, self.__fmt = INFO[w]
        self.__ir = self.__il + 2
        self.deadline = deadline

        self.altzone = time.altzone
        self.daylight = time.daylight
        self.timezone = time.timezone
        self.tzname = time.tzname

        self.time = time.time
        self.time_ns = time.time_ns
        self.monotonic = time.monotonic
        self.monotonic_ns = time.monotonic_ns
        self.perf_counter = time.perf_counter
        self.perf_counter_ns = time.perf_counter_ns
        self.process_time = time.process_time
        self.process_time_ns = time.process_time_ns
        self.thread_time = time.thread_time
        self.thread_time_ns = time.thread_time_ns
        self.get_clock_info = time.get_clock_info
        self.sleep = time.sleep

    def asctime(self, t: _TimeTuple | struct_time = ...) -> str:
        if t is Ellipsis:
            return self.ctime()
        return self.ctime(time.mktime(t))

    def ctime(self, secs: float | None = ...) -> str:
        if secs is Ellipsis:
            secs = time.time()
        if secs < self.deadline:
            return time.ctime(secs)
        n = (secs - self.deadline) // self.__dr + 1
        secs -= n*self.__dr
        s = time.ctime(secs)
        return s[:self.__il] + self.__fmt % (int(s[self.__il:self.__ir]) + n * self.__mul) + s[self.__ir:]
