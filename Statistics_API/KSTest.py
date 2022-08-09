from logging import Logger
from scipy import stats
from logging import Logger
import time
class KS_Test():
    def __init__(self):
        self.logger = Logger('ks');
    def run(self, arguments):
        try:
            start = time.time()
            self.logger.info("Kolmodorov - Smirnov test for normality has been run. Arguments:{0}", arguments)
            res = stats.kstest(arguments, 'norm')
            end = time.time()
            self.logger.info("Kolmodorov - Smirnov test for normality has completed. Arguments:%s0. Completion time: %s1", arguments, end - start)
            return res
        except Exception as e:
            raise;
