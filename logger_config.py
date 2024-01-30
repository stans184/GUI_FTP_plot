import logging
import os
import datetime

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
    
    # 로그 파일 유지 관리
    manage_log_file('SAT_log.log', 15)

    return logger

def manage_log_file(log_file_path, retention_days):
    retention_date = datetime.datetime.now() - datetime.timedelta(days=retention_days)
    updated_log_lines = []

    with open(log_file_path, 'r') as file:
        for line in file:
            date_str = line.split()[0]
            log_date = datetime.datetime.strptime(date_str, '%m/%d/%Y')

            if log_date > retention_date:
                updated_log_lines.append(line)

    with open(log_file_path, 'w') as file:
        file.writelines(updated_log_lines)