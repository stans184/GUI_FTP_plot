import logging
import os

def setup_logger():
    logger = logging.getLogger('SAT_logger')
    logger.setLevel(logging.DEBUG)
    
    # 로그 포맷 정의
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # 파일 핸들러 추가
    file_handler = logging.FileHandler('SAT_log.log')
    file_handler.setFormatter(formatter)

    # 로거에 핸들러 추가
    logger.addHandler(file_handler)

    return logger