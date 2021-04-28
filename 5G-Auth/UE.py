"""
Step 01
① Registration Request
UE send registration request to AUSF and ARPF, include SUCI or 5G-GUTI.
"""
import socket
#link to RAN's host
t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
t.connect(("10.1.0.2", 1))
#deliver [SUPI]46697123456789 to AMF
#SUPI = IMSI(國際移動使用者辨識碼 in SIM卡), 466 = TW(MCC), 97 = Taiwan Mobile(MNC), 123456789 = identifer num(MSIN)
SUPI = "46697123456789"
t.send(SUPI.encode('UTF-8'))
print("STEP 01") #
print("------------------------------------------------------------")
print("| v")
print("|>UE---RAN---AMF")
print("|>[SUPI]%s" %(SUPI))
print("------------------------------------------------------------")
print("  UE deliver [SUPI]%s to AMF" %(SUPI))
print("  , and pass by RAN, then get the [sn-name]10011 from RAN")
data1 = t.recv(1024)
print("  UE get [MSG]%s" %(data1.decode('UTF-8')))
print("  Connect success!")

"""
Step 12
⑫ Calculate Auth. Response (RES*)
將UE本身的 Key, 與得到的 RAND, AUTN 傳給 USIM 並進行驗證 MAC = XMAC
USIM 自行生成 RES
手機從 RES 推導出 RES*
CK || IK 推導出 K_ausf
K_ausf 推導出 K_seaf
傳遞：RES*
"""
#USIM self
Key = "0000000000000000" #Key = 128 bits
f1 = "111111111111111111111111"
f2 = "22222222"
f3 = "3333333333333333"
f4 = "4444444444444444"
SQN = "010101" #SQN = 48 bits
AMF = "10" #AMF = 16 bits
#UE Get!
data121 = t.recv(1024) #RAND Get!
RAND = data121.decode('UTF-8')
data122 = t.recv(1024) #AUTN Get!
AUTN = data122.decode('UTF-8')
data123 = t.recv(1024) #ngKSI Get!
ngKSI = data123.decode('UTF-8')
MAC = int(f1)^int("%s%s%s" %(SQN, RAND, AMF)) #MAC = f1(SQN || RAND || AMF)
#Algorithm in UE
CK = int(f3)^int(RAND) #CK = 128 bits
IK = int(f4)^int(RAND) #IK = 128 bits
K_ausf = "%s%s" %(CK, IK) #K_ausf = CK || IK
RES = int(f2)^int(RAND) #RES = 64 bits
XMAC = int(f1)^int("%s%s%s" %(SQN, RAND, AMF)) #XMAC = f1(SQN || RAND || AMF)
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
K_seaf = KDF(K_ausf, "20011") #KDF(K_ausf, sn-name), sn-name = UDM's? AUSF's? UE's?
print("STEP 12")
print(" [XMAC]%s" %(XMAC))
print(" [MAC]%s" %(MAC))
if XMAC == MAC:
    print(" XMAC = MAC, allow!")
else:
    print(" XMAC != MAC , NOT ALLOW!")
    t.close()
print(" *[RES]%s" %(RES))

"""
Step 13
⑬ Auth. Response
Deliver RES to SEAF near by AMF
"""
RES = "%s" %(RES)
t.send(RES.encode('UTF-8'))
print("STEP 13")
print(" Deliver [RES]%s to AMF" %(RES))