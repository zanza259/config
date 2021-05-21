# install nordvpn linux client
# (https://support.nordvpn.com/Connectivity/Linux/1325531132/Installing-and-using-NordVPN-on-Debian-Ubuntu-Raspberry-Pi-Elementary-OS-and-Linux-Mint.htm)
sh <(curl -sSf https://downloads.nordcdn.com/apps/linux/install.sh)


# install bpytop (system monitor)
# (https://github.com/aristocratos/bpytop)
pip3 install bpytop --upgrade


# install regolith desktop (ubuntu gui only)
# (https://regolith-linux.org/)
sudo add-apt-repository ppa:regolith-linux/release
sudo apt install regolith-desktop-standard
