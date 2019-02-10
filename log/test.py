__author__ = 'jennyzhang'
from config import Config
if __name__ == '__main__':
    conf=Config()
    logger=conf.getLog()
    logger.info('foorbar')
    student="jenny"
    isStaff=True
    logger.info("student=%s,isStaff=%s",student,isStaff)

