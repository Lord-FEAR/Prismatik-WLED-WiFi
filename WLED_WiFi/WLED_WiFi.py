import lightpack, socket, configparser, os
from time import sleep
import sys

class WLED_WiFi:
    def __init__(self):
        self.loadConfig()
        self.lp = lightpack.Lightpack()
        self.status = False
        try:
            self.lp.connect()
        except lightpack.CannotConnectError as e:
            print(repr(e))
            sys.exit(1)
    
    def loadConfig(self):
        self.scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.config = configparser.ConfigParser()
        self.config.read(self.scriptDir + '/WLED_WiFi.ini')
        self.fps = self.config.getint('WLED', 'FPS')
        self.udpBroadcastIp = self.config.get('WLED', 'UDP_IP_ADDRESS')
        self.udpPort = self.config.getint('WLED', 'UDP_PORT_NO')

    def run(self):
        while(True):
            d = self.lp.getColoursFromAll()
            v = [2, 2]
            for i in d:
                v.append(d[i][0])
                v.append(d[i][1])
                v.append(d[i][2])
            Message = bytes(v)
            clientSock = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
            clientSock.sendto (Message, (self.udpBroadcastIp, self.udpPort))
            sleep(1/self.fps)

warls = WLED_WiFi()
warls.run()