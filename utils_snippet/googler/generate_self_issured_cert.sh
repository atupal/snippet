openssl genrsa -aes256 -out vpn.atupal.org.orig.key 4096
openssl rsa -in vpn.atupal.org.orig.key -out vpn.atupal.org.key
openssl req -new -key vpn.atupal.org.key -out vpn.atupal.org.csr
openssl x509 -req -days 365 -in vpn.atupal.org.csr -signkey vpn.atupal.org.key -out vpn.atupal.org.crt
