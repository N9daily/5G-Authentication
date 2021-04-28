"""
Step 06
⑥ [SUCI or SUPI de-concealment], Authentication Method Selection and Generate AV
Key、SN-name、SQN、
以下集結成向量AV：
RAND、XRES*、KAUSF、AUTNUDM(包含SQN⊕AK, AMF, MAC)
"""
import socket
f = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
f.bind(("10.1.0.4",1))
f.listen(5)
c,addr = f.accept()
data6 = c.recv(1024) #SUPI[0:14], sn-name[14:19]
data6 = data6.decode('UTF-8')
SUPI = data6[0:14]
sn = data6[14:19]
print("STEP 06")
print("------------------------------------------------------------")
print("|                          v      v     v")
print("|>UE---RAN---AMF---SEAF---AUSF---UDM---ARPF")
print("|>[SUPI]%s" %(SUPI))
print("|>[sn-name]%s" %(sn))
print("------------------------------------------------------------")
if sn == "10011":
    print("  RAN's sn-name is allowed!")
    print("  Because SUPI, so use 5G-AKA to authenticate")
else:
    print("--NOT ALLOW!--")
    exit()
print("------------------------------------------------------------")
print("|      _____________________RAND____________________       |")
print("|      |                      |      |      |      |       |")
print("|      |  Key         AMF___  |  Key |      |  Key |       |")
print("|      |   |                | |   |  |      |   |  |       |")
print("|      f5__|    ______SQN___|_f1__⊥__f2     f3__⊥__f4      |")
print("|      |       |              |      |      |      |       |")
print("|      v       |              v      v      v      v       |")
print("|      AK_____xor           MAC-A   XRES    CK     IK      |")
print("|              |                                           |")
print("|              v                                           |")
print("|           SQN⊕AK                                         |")
print("------------------------------------------------------------")
#Because transfer of data = SUPI, no need to pass to SIDF
#Check [SUPI]46697123456789 in ARPF, which Key = 1000000000000001
Key = "1000000000000001" #Key = 128 bits

#Related KDF -> HMAC-256(Algorithem)

#Key changes to CK and IK
import random
RAND = random.randint(0, 9999999999999999)
RAND = "%s" %(RAND)
RAND = RAND.zfill(16) #RAND = 128 bits
f3 = "3333333333333333"
f4 = "4444444444444444"
CK = int(f3)^int(RAND) #CK = 128 bits
IK = int(f4)^int(RAND) #IK = 128 bits
K_ausf = "%s%s" %(CK, IK) #K_ausf = CK || IK
f5 = "555555"
AK = int(f5)^int(RAND) #AK = 48 bits
f2 = "22222222"
XRES = int(f2)^int(RAND) #XRES = 64 bits
SQN = "010101" #SQN = 48 bits
AMF = "10" #AMF = 16 bits
xor = int(SQN)^int(AK) #xor = SQN ^ AK
f1 = "111111111111111111111111"
MAC = int(f1)^int("%s%s%s" %(SQN, RAND, AMF)) #MAC = f1(SQN || RAND || AMF)
AUTN = "%s%s%s" %(xor, AMF, MAC)
AV = "%s%s%s%s" %(RAND, XRES, K_ausf, AUTN)
AKMA = str(int(K_ausf)^int("1231")) #AKMA = 0x00 0x04 , XXXXXXXXX
print(" *[XRES]%s" %(XRES))

"""
Step 07
⑦ Auth. Get Response
Deliver AV to AUSF
"""
import time
print("STEP 07")
print(" Deliver [sn-name]30022, [AV]%s, [SUPI]%s, [AKMA]%s to AUSF" %(AV, SUPI, AKMA)) #[UDM's sn-name]30022 is needed to deliver to AUSF?, if AKMA is used, then send it.
c.send(AV.encode('UTF-8')) #AV
time.sleep(1)
c.send(SUPI.encode('UTF-8')) #SUPI
time.sleep(1)
c.send(AKMA.encode('UTF-8')) #AKMA
"""AKMA Ref:https://www.etsi.org/deliver/etsi_ts/133500_133599/133535/16.00.00_60/ts_133535v160000p.pdf"""
