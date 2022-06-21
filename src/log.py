class Log(object):
    def __init__(self, ip, status_code, bytes):
        self.ip = ip
        self.status_code = status_code
        self.bytes = bytes

    def get_ip(self):
        return self.ip

    def get_status_code(self):
        return self.status_code

    def get_bytes(self):
        return self.bytes