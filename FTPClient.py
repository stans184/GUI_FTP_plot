import ftplib

from logger_config import setup_logger

class FTPClient:
    # client object creat
    def __init__(self, host):
        self.host = host[2]
        self.username = host[0]
        self.password = host[1]
        self.connection = None
        self.logger = setup_logger()

    # FTP connect
    def connect(self):
        try:
            self.connection = ftplib.FTP(self.host)
            self.connection.login(user=self.username, passwd=self.password)
            self.logger.info(f"{self.username} FTP 연결 성공")
        except ftplib.all_errors as e:
            self.logger.error(f"{self.username} FTP 연결 실패: {e}")

    # FTP disconnect
    def disconnect(self):
        if self.connection:
            self.connection.quit()
            self.logger.info(f"{self.username} FTP 연결 종료")
       
    # move directory     
    def move_directory(self):
        return 0
    
    # scan file list
    def scan_files(self):
        return 0