https://github.com/jawj/IKEv2-setup/blob/master/setup.sh

Note:
- Don't need setup the timezone, mail and ssh settings in that script.
- For CloudFlare proxying, need to remove the CDN setting.
- Before generating the certificate, shouldn't reject all traffic in iptables. (The 80 port is needed for certificate requeset validation).
- Letsencrypt doesn't allow issue certificate for Azure domains such as xxx.cloudapp.net. Need to use your own domain.
- The emall address in the script useless (sending the instructions...), just delete the "mail" command.
- In firewall setting, open 80 (TCP) and 500 (UDP), 4500 (UDP) portal. After certificate is issued, the 80 port can be deleted.
- For the .mobileconfig file, need open using Safari on iOS.
- To auto start the server, change auto=add to auto=start in /etc/ipsec.conf on the *server*
