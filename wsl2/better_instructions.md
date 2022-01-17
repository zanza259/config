1) Create a startup file in Linux at /etc/init-wsl:
#!/bin/sh
echo booting
service ssh start
and make the script executable
chmod +x /etc/init-wsl

2) Schedule executing this file at windows boot or log on
test

Since wsl.exe is able to run commands inside the wsl distro, we simply schedule to run this file through the command wsl -u root /etc/init-wsl. If you have multiple distros, you might want to specify which one with a -d flag, for instance wsl -d Ubuntu-20.04 -u root /etc/init-wsl
