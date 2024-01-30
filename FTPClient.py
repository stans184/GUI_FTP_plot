import ftplib

class FTPClient:
    # client object creat
    def __init__(self, host):
        self.host = host[2]
        self.username = host[0]
        self.password = host[1]
        self.connection = None

    # FTP connect
    def connect(self):
        try:
            self.connection = ftplib.FTP(self.host)
            self.connection.login(user=self.username, passwd=self.password)
            print("FTP 연결 성공")
        except ftplib.all_errors as e:
            print(f"FTP 연결 실패: {e}")

    # FTP disconnect
    def disconnect(self):
        if self.connection:
            self.connection.quit()
            print("FTP 연결 종료")
       
    # move directory     
    def move(self):
        return 0