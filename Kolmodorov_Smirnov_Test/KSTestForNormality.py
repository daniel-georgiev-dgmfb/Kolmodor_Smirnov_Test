from logging import Logger
from scipy import stats
import time


class KSTestForNormality(Logger):
    def __init__(logger: Logger):

        def Run(arguments):
            try:
                start = time.time()
                logger.info(
                    "Kolmodorov - Smirnov test for normality has been run. Arguments:{0}", arguments)
                res = stats.kstest(arguments, 'norm')
                end = time.time()
                logger.info(
                    "Kolmodorov - Smirnov test for normality has completed. Arguments:{0}, Result: {1} Completion time: {2}", arguments, res, end - start)
                return res
            except Exception as e:
                logger.error(
                    "En exception has been thrown when running Kolmodorov - Smirnov test for normality. See inner exception for more imfomation.", e)
                raise
