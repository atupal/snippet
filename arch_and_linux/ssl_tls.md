# http://security.stackexchange.com/questions/70733/how-do-i-use-openssl-s-client-to-test-for-absence-of-sslv3-support

#### Test ssl v3:

```
openssl s_client -connect example.com:443 -ssl3
```

#### Scan server for supported version

```
nmap --script ssl-enum-ciphers example.com**
```
