from logging import Logger
from scipy import stats
import time
class KolmogorovSmirnovTest(Logger):
    def __init__(self):
        this.logger = Logger
        def run():
            try:
                start = time.time()
                logger.info("Kolmodorov - Smirnov test for normality has been run. Arguments:{0}", arguments)
                res = stats.kstest(arguments, 'norm')
                end = time.time()
                logger.info("Kolmodorov - Smirnov test for normality has completed. Arguments:{0}. Completion time: {1}", arguments, end - start)
                return res
            except Exception as e:
                logger.error("En exception has been thrown when running Kolmodorov - Smirnov test for normality. See inner exception for more imfomation.", e)
                raise