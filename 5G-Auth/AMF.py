"""
Step 02
②
RAN get [SUPI]46697123456789, and send back [MSG]200ACK!
"""
import socket
f = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
f.bind(("10.1.0.2",1))
f.listen(5)
c,addr = f.accept()
data = c.recv(1024)
SUPI = data.decode('UTF-8')
sn = "10011" #get from RAN
c.send("200ACK!".encode('UTF-8'))
print("STEP 02")
print("------------------------------------------------------------")
print("|             v     v")
print("|>UE---RAN---AMF---SEAF")
print("|>[SUPI]%s" %(SUPI))
print("|>[sn-name]10011") #get from RAN
print("------------------------------------------------------------")
print("  RAN get [SUPI]%s" %(SUPI))
print("  Take [SUPI]%s to SEAF near by AMF" %(data.decode('UTF-8')))
print("  Send back 200ACK! to UE")

"""
Step 03
③ Auth. Request
SUCI or SUPI, SN-name
[SN-name]00001
"""
#link to AUSF's host
t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
t.connect(("10.1.0.3", 1))
data3 = "%s%s" %(SUPI, sn)
t.send(data3.encode('UTF-8'))
print("\n\n")
print("STEP 03")
print("------------------------------------------------------------")
print("|                   v      v")
print("|>UE---RAN---AMF---SEAF---AUSF")
print("|>[SUPI]%s" %(SUPI))
print("|>[sn-name]%s" %(sn))
print("------------------------------------------------------------")
print("  Delivor [SUPI]%s, [sn-name]%s to AUSF" %(SUPI, sn))

"""
Step 10
⑩
Store HXRES and K_seaf
"""
data10 = t.recv(1024) #AV
data10 = data10.decode('UTF-8')
RAND = data10[0:16]
HXRES = data10[16:35] #Store
K_seaf = data10[35:data10.find("=")+1] #Store
AUTN = data10[data10.find("=")+1:]
print("STEP 10")
print(" Store: [HXRES]%s, [K_seaf]%s" %(HXRES, K_seaf))
print(" *[HXRES]%s" %(HXRES))

"""
Step 11
⑪ Auth. Request
Deliver RAND, AUTN, ngSKI to UE
"""
import time
c.send(RAND.encode('UTF-8'))
time.sleep(1)
c.send(AUTN.encode('UTF-8'))
time.sleep(1)
#ngSKI = 000[0]0000 -> KSI_amf -> native security context
#ngSKI = 000[1]0000 -> KSI_asme -> mapped security context
#000[0] ~ 110[0] -> possible values for the NAS key set identifier
#111[0] -> no key is available
#What means after [0]?
ngSKI = "00000000"
c.send(ngSKI.encode('UTF-8'))
"""ABBA (Anti-Bidding-down Between Architectures) parameter. This parameter allows the 5G system to enforce that a UE cannot access the network using older mechanisms that have had vulnerabilities associated with them."""
print("STEP 11")
print(" Deliver [RAND]%s, [AUTN]%s, [ngSKI]%s to UE" %(RAND, AUTN, ngSKI))

"""
Step 14
⑭ Calculate HRES* and compare to HXRES*
"""
data14 = c.recv(1024) #RES
RES = data14.decode('UTF-8')
import hashlib
h = hashlib.sha1()
h.update(RES.encode('UTF-8'))
HRES = h.hexdigest()
print("STEP 14")
print(" [RES]%s" %(RES))
print(" [HRES]%s" %(HRES))
print(" [HXRES]%s" %(HXRES))
if HRES == HXRES:
    print(" HRES = HXRES, allow!")
else:
    print(" HRES != HXRES , NOT ALLOW!")
    c.close()

"""
Step 15
⑮ Auth. Request
Deliver RES to AUSF
"""
t.send(data14) #RES
print("STEP 15")
print(" Deliver [RES]%s to AUSF" %(RES))

"""
Step Final
AV 內的 K_seaf 成為錨點 Key
K_seaf 推導出 K_amf
將 ngKSI 和 K_amf 發給 AMF 使用
"""
dataf1 = t.recv(1024)
Result = dataf1.decode('UTF-8')
dataf2 = t.recv(1024)
SUPI = dataf2.decode('UTF-8')
dataf3 = t.recv(1024) #AMF had K_seaf already?
if Result == "ALLOW":
    print("Link between AMF and AUSF is ALLOW")
else:
    print("Link between AMF and AUSF isn't ALLOW")
    t.close()
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
K_amf = KDF(K_seaf, SUPI) #K_amf = KDF(K_seaf, SUPI) ,ABBA is?
print("K_amf and ngKSI pass to AMF from SEAF")