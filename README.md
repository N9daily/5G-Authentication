# New version, Ubuntu2022 & apple m1 (arm64)
> Virtual Machine: [UTM](https://mac.getutm.app)
> Ubuntu Version: [Ubuntu Server 22.04.1 LTS](https://cdimage.ubuntu.com/releases/22.04/release/ubuntu-22.04.1-live-server-arm64.iso?_ga=2.232931869.2065210953.1664353438-201900941.1664353438)
> *Ubuntu Server is installed and upgraded to desktop version later.*

# Setup UTM & Ubuntu Server 22.04.1 LTS
> Create a new virtualization at UTM and installs Ubuntu 22.04.1 LTS by selecting ubuntu-22.04.1-live-server-arm64.iso.
> When setups over, you need to quit the ISO and restart Ubuntu 22.04.1 LTS.
> Enter your ID and password and install Ubuntu GUI as the follow:
> $ sudo apt-get install ubuntu-desktop
> Reboot the virtual system.

# Setup Anaconda
> The python version is 3.10, but Ryu has to run lower than python 3.9, so we setup Anaconda to choose the python 3.9 of enviroment.

# Optional
## 1. Chrome:
> Because that can't executes chrome installing, so chooses to install chromium.
> $ sudo apt install --assume-yes chromium-browser
## 2. Visual Studio Code:
> [VScode.deb](https://az764295.vo.msecnd.net/stable/74b1f979648cc44d385a2286793c226e611f59e7/code_1.71.2-1663189619_arm64.deb "ARM64")
