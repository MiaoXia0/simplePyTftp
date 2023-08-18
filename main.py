import threading
import tftpy
import sys

args = sys.argv[1:]
if len(args) < 1:
    FOLDER = 'C:\\'
else:
    FOLDER = args[0]
HOST = ''
if len(args) < 2:
    HOST = '0.0.0.0'
else:
    HOST = args[1]
if len(args) < 3:
    PORT = 69
else:
    PORT = int(args[2])

TFTP_SERVER = None

if __name__ == '__main__':
    # 启动tftp服务
    TFTP_SERVER = tftpy.TftpServer(FOLDER)
    threading.Thread(target=lambda: TFTP_SERVER.listen(HOST, PORT)).start()
    print(f'Listing {HOST}:{PORT}, Path: {FOLDER}')
