"""
Step 04
④
Get [SUPI]46697123456789, [SN-name]10011
"""
import socket
f = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
f.bind(("10.1.0.3",1))
f.listen(5)
c,addr = f.accept()
data4 = c.recv(1024) #SUPI[0:14], sn-name[14:19]
data4 = data4.decode('UTF-8')
SUPI = data4[0:14]
sn = data4[14:19]
print("STEP 04")
print("------------------------------------------------------------")
print("|                   v      v")
print("|>UE---RAN---AMF---SEAF---AUSF")
print("|>[SUPI]%s" %(SUPI))
print("|>[sn-name]%s" %(sn))
print("------------------------------------------------------------")
print("  Get [SUPI]%s, [sn-name]%s" %(SUPI, sn))

"""
Step 05
⑤ Auth. Get Request
Deiver SUCI or SUPI, SN-name to UDM
"""
#link to UDM's host
t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
t.connect(("10.1.0.4", 1))
t.send("%s%s".encode('UTF-8') %(SUPI, sn))
print("\n\n")
print("STEP 05")
print("------------------------------------------------------------")
print("|                          v      v")
print("|>UE---RAN---AMF---SEAF---AUSF---UDM")
print("|>[SUPI]%s" %(SUPI))
print("|>[sn-name]%s" %(sn))
print("------------------------------------------------------------")
print("  Deliver [SUPI]%s, [sn-name]%s to UDM" %(SUPI, sn))

"""
Step 08
⑧ Store XRES and Calculate HXRES
留存：XRES*、K_ausf
XRES* hashed into HXRES*
K_ausf推導出K_seaf
用HXRES與K_seaf替換掉原先內容，生成新AV：RAND、HXRES、K_seaf、AUTN
"""
data81 = t.recv(1024) #AV
data81 = data81.decode('UTF-8')
data82 = t.recv(1024) #SUPI ,and store it
data82 = data82.decode('UTF-8')
data83 = t.recv(1024) #AKMA
data83 = data83.decode('UTF-8')
RAND = data81[0:16]
XRES = data81[16:56] #Stroe
K_ausf = data81[56:88]
AUTN = data81[88:]
import hashlib
h = hashlib.sha1()
h.update(XRES.encode('UTF-8'))
HXRES = h.hexdigest()
# KDF function
from hashlib import sha256
import base64
import hmac
def KDF(data, key):
    key = key.encode('UTF-8')
    message = data.encode('UTF-8')
    sign = base64.b64encode(hmac.new(key, message, digestmod=sha256).digest())
    sign = str(sign, 'UTF-8')
    return sign
K_seaf = KDF(K_ausf, "20011") #KDF(K_ausf, sn-name? UDM? AUSF?)
AV = "%s%s%s%s" %(RAND, HXRES, K_seaf, AUTN)
print("STEP 08")
print(" Store: [XRES]%s, [K_ausf]%s" %(XRES, K_ausf))
print(" *[HXRES]%s" %(HXRES))

"""
Step 09
⑨ Auth. Response
Deliver AV to AMF
"""
print("STEP 09")
print(" Deliver [AV]%s to SEAF" %(AV))
c.send(AV.encode('UTF-8'))

"""
Step 16
⑯ RES* Verify response
RES* = XRES*
"""
data16 = c.recv(1024) #RES
RES = data16.decode('UTF-8')
print("STEP 16")
print(" [RES]%s" %(RES))
print(" [XRES]%s" %(XRES))
if RES == XRES:
    print(" RES = XRES, allow!")
else:
    print(" RES != XRES, NOT ALLOW!")
    c.close()

"""
Step 17
⑰ Auth. Response
Deliver Result, [SUPI], K_seaf to SEAF
"""
import time
c.send("ALLOW".encode('UTF-8')) #Result
time.sleep(1)
c.send(data82) #SUPI
time.sleep(1)
c.send(K_seaf.encode('UTF-8')) #K_seaf, why? AMF had one K_seaf already