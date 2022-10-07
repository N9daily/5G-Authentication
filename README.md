# NEW LOG: 2022-09-28
## INTRO
### 1. New version, Ubuntu 2022 & apple m1 (arm64)
> Virtual Machine: [UTM](https://mac.getutm.app)  
> Ubuntu Version: [Ubuntu Server 22.04.1 LTS](https://cdimage.ubuntu.com/releases/22.04/release/ubuntu-22.04.1-live-server-arm64.iso?_ga=2.232931869.2065210953.1664353438-201900941.1664353438)  
> *Ubuntu Server will be installed and upgraded to desktop version after steps.*

### 2. Setup UTM & Ubuntu Server 22.04.1 LTS
> Create a new virtualization at UTM and installs Ubuntu 22.04.1 LTS by selecting ubuntu-22.04.1-live-server-arm64.iso.  
> When setups over, you need to quit the ISO and restart Ubuntu 22.04.1 LTS.  
> Enter your ID and password and install Ubuntu GUI as the follow:  
```bash
$ sudo apt-get install ubuntu-desktop
```
> Reboot the virtual system.

### 3. Setup Anaconda
> The python version is 3.10, but Ryu has to run lower than python 3.9, so we setup Anaconda to choose the python 3.9 of enviroment.  
> Download: [Anaconda, ARM64](https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-aarch64.sh)  
> Go to the folder where you download and executes process as follow:  
```bash
$ source ~/anaconda3/bin/activate root  
$ anaconda-navigator
```

### 4. Optional
1. Chrome:
> Because that can't execute chrome installing, so chooses to install chromium.  
```bash
$ sudo apt install --assume-yes chromium-browser
```
2. Visual Studio Code:
> [VScode.deb](https://az764295.vo.msecnd.net/stable/74b1f979648cc44d385a2286793c226e611f59e7/code_1.71.2-1663189619_arm64.deb "ARM64"), then choose the ARM64.  
> Setup it!

***

## Detail of Building Steps
### 01. 
![avatar](https://drive.google.com/file/d/1-uAl-cEUfqq9PybbVQfD4FCk8FPms53-/view)
> UTM＞建立新虛擬機  
### 02. 
![avatar](https://drive.google.com/file/d/10gqcr4WQwQscGYBySca_umLAHT171IhH/view?usp=sharing)
> 虛擬化  
### 03. 
![avatar](https://drive.google.com/file/d/11T-CbvWvtHHHrfbzYy7aBgrkSK11s7Bc/view?usp=sharing)
> Linux  
### 04. 
![avatar](https://drive.google.com/file/d/12T5m1JrqDWjIfHlCTTc5YvHgpmYSLB0P/view?usp=sharing)
> 瀏覽  
> ＊點選「下載Ubuntu Server for ARM」可以連結至Ubuntu官網下載ARM架構的Ubuntu，附上連結https://ubuntu.com/download/server/arm  
### 05. 
![avatar](https://drive.google.com/file/d/12Z3nqpighlZ6gem6sH8AYmLM1tsUxBLh/view?usp=sharing)
> 選擇從Ubuntu官網下載的Ubuntu-22.04.1-live-server-arm64.iso＞下一步  
### 06. 
![avatar](https://drive.google.com/file/d/13MfGb1G2ww3vYKRp70E3kzYNIQjD4mxD/view?usp=sharing)
> 我選擇 4096 MB、4 CPU核心數＞下一步＞40GB＞下一步  
> ＊隨使用者電腦硬件自行調整  
### 07. 
![avatar](https://drive.google.com/file/d/14KBhO2zSa3Px_dA_levkbTIyS1Iez40E/view?usp=sharing)
> 下一步  
### 08. 
![avatar](https://drive.google.com/file/d/14e33dWwC3F4YfXlEiAM4z2t8bc1QTOPC/view?usp=sharing)
> 名稱隨自己喜歡做調整＞儲存  
### 09. 
![avatar](https://drive.google.com/file/d/14t_jpedMhCxrkvQDoqb284p-DUJz6iN-/view?usp=sharing)
> 點選播放按鈕運行  
### 10. 
![avatar](https://drive.google.com/file/d/168RlXfHX4oOGFlRZCW4JEskcAhbu9dju/view?usp=sharing)
> Try or Install Ubuntu Server  
### 11. 
![avatar](https://drive.google.com/file/d/17VPsWsOxMstyUXrMODKUOCQx4df28m3r/view?usp=sharing)
> English＞Enter/Done   
### 12. 
![avatar](https://drive.google.com/file/d/181O9xWM67Gq3KmGIptuuWgEmIW7adsJQ/view?usp=sharing)
> (X) Ubuntu Server＞Enter/Done  
### 13. 
![avatar](https://drive.google.com/file/d/18w_QYaSu85aulR8fO6PNV3P1PeA6LSO7/view?usp=sharing)
> Continue  
### 14. 
![avatar](https://drive.google.com/file/d/1ABguWdG0zn3baKergit0uNQ8R9qBf1DZ/view?usp=sharing)
> 自行設定內容＞Enter/Done  
### 15. 
![avatar](https://drive.google.com/file/d/1B5CFSc6Uu0O2KaOB4xJF-WOeeIH5VY8S/view?usp=sharing)
> 等待執行完畢
### 16. 
![avatar](https://drive.google.com/file/d/1Bqtj3FODSiifvlEWu3F1d_B8itopnsTR/view?usp=sharing)
> Reboot Now  
### 17. 
![avatar](https://drive.google.com/file/d/1DFCrZb_rY1RHR4pEpxsqn-041Ajuz-vP/view?usp=sharing)
> 之後視窗會變為黑畫面＞選擇此視窗右上方數來第二個icon「Drive image options」＞選擇CD/DVD (ISO)＞退出  
### 18. 
![avatar](https://drive.google.com/file/d/1D_xsi6m9ELjQ32C0oi0ZC9MkEUr76Mlg/view?usp=sharing)
> 選擇左上方第三個icon「Restarts the VM」  
### 19. 
![avatar](https://drive.google.com/file/d/1EmeG75lAgR9QKNvIsUVUdWbCfi4gCwJb/view?usp=sharing)
> 輸入使用者名稱與密碼  
### 20. 
![avatar](https://drive.google.com/file/d/1Eyd0BrsHwxIS6QqMVb4Pu65leadpiUtp/view?usp=sharing)
```bash
$ sudo apt-get install ubuntu-desktop
```
> ＊安裝UI介面  
### 21. 
![avatar](https://drive.google.com/file/d/1H4qNaiMXHIW9hfi3niujTYUV7RbBeWUY/view?usp=sharing)
> Enter/OK  
### 22. 
![avatar](https://drive.google.com/file/d/1IC00Dg1W5uw8EppxggSn6jFwAuvA2EZK/view?usp=sharing)
```bash
$ sudo reboot
```
### 23. 
![avatar](https://drive.google.com/file/d/1KM_iXS4lWIjMALZOtu03VWSFYQ5eOR2G/view?usp=sharing)
> 輸入密碼  
### 24. 
![avatar](https://drive.google.com/file/d/1Ne4ScxYeShHwoAjZU9Fplxh3Aqx9xwgs/view?usp=sharing)
```bash
$ sudo apt-get update
```
```bash
$ sudo apt-get upgrade
```
> ＊更新並升級系統  
### 25. 
![avatar](https://drive.google.com/file/d/1PbfFKJX1_Swbz_BVT6WVwgSLaR4QxCAu/view?usp=sharing)
```bash
$ sudo apt-get install --assume-yes chromium-browser
```
> ＊安裝Chromium瀏覽器  
### 26. 
![avatar](https://drive.google.com/file/d/1QpNAkf_h1m5mJEMi_Yw8Hc9n4t8rv30u/view?usp=sharing)
> 好了會重新登入Ubuntu＞Enter/OK  
### 27. 
![avatar](https://drive.google.com/file/d/1RQGFove5AmUJlJzpFsYeuyC_0_-1umkm/view?usp=sharing)
```bash
$ sudo passwd root
```
> ＞輸入想要的root密碼＞再次輸入想要的root密碼  
> ＊建制root密碼  
### 28. 
![avatar](https://drive.google.com/file/d/1XYBdLxxl4BELT-9gS1cBxAcwpaqgXk7c/view?usp=sharing)
> 至Anaconda官網下載Linux ARM 64的版本（鼠標位置）＞右鍵＞save link as ...＞內建位置（Downloads）  
> ＊由於內建安裝的python為3.10.6版本，導致接下來運行的作業環境安裝不了，我使用Anaconda來建制python3.9的環境  
### 29. 
![avatar](https://drive.google.com/file/d/1XpUzVIRd4dxwJkP3hwVuFlL__CWU6t2t/view?usp=sharing)
> 在Downloads開啟Terminal  
### 30.
![avatar](https://drive.google.com/file/d/1Y8vrA2ifpCS4vmkFi6wwdRu8TokL8Gi4/view?usp=sharing)
```bash
$ bash Anaconda3-2022.05-Linux-aarch64.sh
```
> ＞Enter＞yes  
### 31.
![avatar](https://drive.google.com/file/d/1ZzFMkShdW7CsgQMLbxWRitXMTUlhqh6B/view?usp=sharing)
```bash
$ sudo apt update
```
```bash
$ sudo apt upgrade
```
### 32.
![avatar](https://drive.google.com/file/d/1_VPYPy5qAEZOERGsqsMvlyZTZl_7AAeE/view?usp=sharing)
```bash
$ source ~/anaconda3/bin/activate root
```
> ＊使用root執行  
```bash
$ anaconda-navigator
```
> ＊執行Anaconda，若需要更新則更新它，Lunch Navigator  
### 33.
![avatar](https://drive.google.com/file/d/1c_ew5SY9Uxa3KGJtoXSACwfzSXnqqBo0/view?usp=sharing)
> 選擇鼠標位置Environments  
### 34.
![avatar](https://drive.google.com/file/d/1d0tvewvVzxFgWfqWipS7akACBBUdlW7K/view?usp=sharing)
> Open Terminal  
### 35.
![avatar](https://drive.google.com/file/d/1dL779WKudSOkcnoAGT-7nuC9x9GMmu6e/view?usp=sharing)
> 確認一下python的版本，為我們所需要的3.9  
### 36.
![avatar](https://drive.google.com/file/d/1euWKbecX09qRtVGbflWvHo92840ZlfDl/view?usp=sharing)
```bash
$ sudo apt-get update
```
```bash
$ sudo apt-get upgrade
```
```bash
$ sudo apt-get install -y git
```
```bash
$ git clone https://github.com/mininet/mininet
```
```bash
$ sudo ./mininet/util/install.sh -n3
```
```bash
$ sudo apt-get install openvswitch-switch
```
```bash
$ sudo mn
```
> ＊安裝Mininet，目的為建立拓樸，確認是否能使用，如圖所示  
### 37.
![avatar](https://drive.google.com/file/d/1fw_HbHAaL5ohXT1xIGMNY_GjLAt2dblk/view?usp=sharing)
```bash
$ exit
```
> ＊退出mininet，接下來為安裝Ryu準備  
```bash
$ sudo apt-get install -y libxml2-dev libxslt1-dev libffi-dev libssl-dev zlib1g-dev python3-pip python3-eventlet python3-routes python3-webob python3-paramiko gcc python3-dev
```
```bash
$ pip3 install msgpack-python eventlet==0.15.2
```
```bash
$ pip3 install six --upgrade
```
```bash
$ pip3 install oslo.config q --upgrade
```
### 38.
![avatar](https://drive.google.com/file/d/1q4MV98h6IdqLPWwUcTabRcZ4waVcXBjM/view?usp=sharing)
```bash
$ cd ~
```
```bash
$ git clone https://github.com/faucetsdn/ryu
```
```bash
$ cd ryu
```
```bash
$ pip3 install .
```
```bash
$ ryu-manager --verbose ryu.app.ofctl_rest
```
> ＊安裝Ryu，並且試運行  
### 39.
![avatar](https://drive.google.com/file/d/1qSpJhBir8jg6BOrn0B55y9GhGjULNNWj/view?usp=sharing)
```bash
$ cd ~/mininet/custom
```
```bash
$ git clone https://github.com/N9daily/5G-Authentication.git
```
> ＊下載我所製作的5G-AKA package，包含5G-AKA所用到的function：UE、RAN、AMF、SEAF、AUSF、UDM，及5G拓樸與加解密ex.py（可以在其中試需求修改加解密辦法）  
### 40.
![avatar](https://drive.google.com/file/d/1qiGpzJsZFQtGNAiZyHCwd2Zh3s_PgqN5/view?usp=sharing)
> 使用Anaconda開啟兩個Terminal  
```bash
$ ryu-manager ryu.app.simple_switch_13
```
> ＊第一個使用Ryu控制器  
```bash
$ cd ~/mininet/custom/5G-Authentication/5G-Auth/
```
```bash
$ sudo mn --custom 5gtopo.py --topo mytopo --controller=remote,ip=127.0.0.1,port=6633 --switch ovs,protocols=OpenFlow13
```
> ＊第二個使用Mininet拓樸  
### 41.
![avatar](https://drive.google.com/file/d/1sMfpoKb5lI2bSsXxsnO-q1ssrF43Ob_C/view?usp=sharing)
```bash
$ pingall
```
> ＊確認拓樸的節點皆有連線成功  
### 42.
![avatar](https://drive.google.com/file/d/1u7OeyDkwGlcoVGKXROswdvc3vyIV4M59/view?usp=sharing)
```bash
$ xterm UE RAN AMF AUSF UDM
```
> ＊開啟各個節點的終端機  
### 43.
![avatar](https://drive.google.com/file/d/1y8AFKqyElfaX82PDnubOJu2Vl1bMP6xl/view?usp=sharing)
> 在各個終端機上輸入對應的名稱  
```bash
$ sudo python3 UDM.py
```
> ＊在UDM終端機中輸入UDM.py、在AUSF終端機中輸入AUSF.py，依此類推  
### 44.
![avatar](https://drive.google.com/file/d/1yl1SIaxKZCzNZTi6UE_y46iO53sApE5A/view?usp=sharing)
![avatar](https://drive.google.com/file/d/1zdbBYJJ02bYAPTe40eMwUKCycQgwaBUK/view?usp=sharing)
> 依順序UDM＞AUSF＞AMF＞RAN＞UE的順序按下Enter鍵執行，即可觀察5G-AKA傳遞的步驟  
