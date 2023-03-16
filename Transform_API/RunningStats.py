from scipy import stats
import numpy as np
from numpy import array, asarray, ma
from logging import Logger
import time
class RunningStats():
    def __init__(self):
        self.logger = Logger('runningstats');
    def skew(self, arguments):
        try:
            start = time.time()
            self.logger.info("Skew function has been run. Arguments:{0}", arguments)
            res = stats.skew(arguments)
            end = time.time()
            self.logger.info("Skew function has completed. Arguments:%s0. Completion time: %s1", arguments, end - start)
            return res
        except Exception as e:
            raise;
    def kurtosis(self, arguments):
        try:
            start = time.time()
            self.logger.info("Kurtosis function has been run. Arguments:{0}", arguments)
            res = stats.kurtosis(arguments)
            end = time.time()
            self.logger.info("Kurtosis function has completed. Arguments:%s0. Completion time: %s1", arguments, end - start)
            return res
        except Exception as e:
            raise;
    def mode(self, arguments):
        try:
            start = time.time()
            self.logger.info("Mode function has been run. Arguments:{0}", arguments)
            res = stats.mode(arguments)
            end = time.time()
            self.logger.info("Mode function has completed. Arguments:%s0. Completion time: %s1", arguments, end - start)
            return res
        except Exception as e:
            raise;
    def median(self, arguments):
        try:
            start = time.time()
            self.logger.info("Median function has been run. Arguments:{0}", arguments)
            res = np.median(arguments)
            end = time.time()
            self.logger.info("Median function has completed. Arguments:%s0. Completion time: %s1", arguments, end - start)
            return res
        except Exception as e:
            raise;


