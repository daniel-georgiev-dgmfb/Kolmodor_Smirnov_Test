from logging import Logger
import hashlib
import time
class Hash():
    def __init__(self):
        self.logger = Logger('cryptography');
    def generate(self, text, hashAlg):
        try:
            start = time.time()
            self.logger.info("Hash generation has been run. Arguments:{0}", text)
            hashObject = hashlib.new(hashAlg, text.encode('utf-8'))
            digest = hashObject.hexdigest()
            end = time.time()
            self.logger.info("Hash generation has completed. Arguments:%s0. Completion time: %s1", text, end - start)
            return digest
        except Exception as e:
            raise;
