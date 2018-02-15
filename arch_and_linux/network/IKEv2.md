https://github.com/jawj/IKEv2-setup/blob/master/setup.sh

Note:
1. Don't need setup the timezone and ssh settings in that script.
2. Before generating the certificate, shouldn't reject in iptables. (The 80 port is needed for certificate requeset validation).
3. Letsencrypt doesn't allow issue certificate for Azure domains such as xxx.cloudapp.net. Need to use your own domain.
3. For the .mobileconfig file, need open using Safari on iOS.
