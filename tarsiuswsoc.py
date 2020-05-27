import websocket
import time
import requests

class IoTLab(object):

    def __init__(self, alamat=None, nama=None):
        self.maxa = 0
        self.maxb = 0
        self.namaku = nama
        print('Menghubungi server... ')
        self.urla = "ws://"+alamat+":82"
        try:
            self.xyz = requests.post(url = 'http://api.weris.link/dodoku.php', 
                                     data = {'temp': nama, 'bit': 'MASUK', 'i': self.urla, 'y': 'xx'})
            self.ws = websocket.WebSocket()
            self.ws.connect(self.urla)
            print('Terhubung di: http://'+alamat)
        except requests.ConnectionError:
            print("No connection, cek lagi alamat IP...")
        time.sleep(1)
        
    def versi(self):
        return self.read('VER')

    @property
    def FB(self):
        self._FB = json.loads(json.dumps(requests.post(url = self.urlf).json()))
        return self._FB
    
    @property
    def Y1(self):
        self._YY1 = self.ws.recv().split( )
        self._Y1 = self._YY1[0]
        return self._Y1
    
    @property
    def Y2(self):
        self._YY2 = self.ws.recv().split( )
        self._Y2 = self._YY2[1]
        return self._Y2
    
    @property
    def Y3(self):
        self._YY3 = self.ws.recv().split( )
        self._Y3 = self._YY3[2]
        return self._Y3
    
    @property
    def USER(self):
        self._YY4 = self.ws.recv().split( )
        self._Y4 = self._YY4[3]
        return self._Y4
    
    @property
    def VER(self):
        self._YY2 = json.loads(json.dumps(requests.post(url = self.urlf).json()))
        self._VER = self._YY2['ver']
        return self._VER

    def tutup(self):
        self.ws.close()
        self.xyz = requests.post(url = 'http://api.weris.link/dodoku.php', 
                                     data = {'temp': self.namaku, 'bit': 'KELUAR', 'i': self.urla, 'y': self._Y4})
        return
    
    def MA_MA(self,ma,mb):
        self.pwma, self.pwmb = self.LIM(ma, mb)
        pw1 = self.ws.send("MAMA {} MBMA {}".format(self.pwma, self.pwmb))
        return
    def MA_MU(self,ma,mb):
        self.pwma, self.pwmb = self.LIM(ma, mb)
        pw1 = self.ws.send("MAMA {} MBMU {}".format(self.pwma, self.pwmb))
        return
    def MA_ST(self,ma,mb):
        self.pwma, self.pwmb = self.LIM(ma, mb)
        pw1 = self.ws.send("MAMA {} MBST {}".format(self.pwma, self.pwmb))
        return
    
    def MU_MA(self,ma,mb):
        self.pwma, self.pwmb = self.LIM(ma, mb)
        pw1 = self.ws.send("MAMU {} MBMA {}".format(self.pwma, self.pwmb))
        return
    def MU_MU(self,ma,mb):
        self.pwma, self.pwmb = self.LIM(ma, mb)
        pw1 = self.ws.send("MAMU {} MBMU {}".format(self.pwma, self.pwmb))
        return
    def MU_ST(self,ma,mb):
        self.pwma, self.pwmb = self.LIM(ma, mb)
        pw1 = self.ws.send("MAMU {} MBST {}".format(self.pwma, self.pwmb))
        return
    
    def ST_MA(self,ma,mb):
        self.pwma, self.pwmb = self.LIM(ma, mb)
        pw1 = self.ws.send("MAST {} MBMA {}".format(self.pwma, self.pwmb))
        return
    def ST_MU(self,ma,mb):
        self.pwma, self.pwmb = self.LIM(ma, mb)
        pw1 = self.ws.send("MAST {} MBMU {}".format(self.pwma, self.pwmb))
        return
    @property
    def ST_ST(self):
        pw1 = self.ws.send("MAST 0 MBST 0")
        return
    
    def Jedah(self, pwma):
        time.sleep(pwma)
        return

    def U1(self,pwm1):
        pw1 =  self.ws.send("U1 {} U1 0".format(pwm1))
        return
        
    def U2(self,pwm1):
        pw1 =  self.ws.send("U2 {} U2 0".format(pwm1))
        return
    
    def LIM(self, wma, wmb):
        if wma <100:
            self.maxa = wma
        else:
            self.maxa = 100  
        if wmb <100:
            self.maxb = wmb
        else:
            self.maxb = 100 
        return 250+(self.maxa*2), 250+(self.maxb*2)

