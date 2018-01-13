// Ref: https://www.systutorials.com/4876/how-to-configure-ios-for-iphone-and-ipad-to-use-socks-proxy-created-by-ssh/

function FindProxyForURL(url, host)
{
    // Configurations
    var socksProxy = "SOCKS 192.168.1.1:8087; DIRECT";

    /*
    // Ref: https://findproxyforurl.com/example-pac-file/
    // If the hostname matches, send direct.
    if (dnsDomainIs(host, "localhost") ||
        shExpMatch(host, "(*.163.com|163.com)") ||
        shExpMatch(host, "(*.yeah.net|yeah.net)") ||
        shExpMatch(host, "(*.126.net|126.net)") ||
        dnsDomainIs(host, "ip.ws.126.net"))
        return "DIRECT";

    // If the requested website is hosted within the internal network, send direct.
    if (isPlainHostName(host) ||
        shExpMatch(host, "*.local") ||
        isInNet(dnsResolve(host), "10.0.0.0", "255.0.0.0") ||
        isInNet(dnsResolve(host), "172.16.0.0",  "255.240.0.0") ||
        isInNet(dnsResolve(host), "192.168.0.0",  "255.255.0.0") ||
        isInNet(dnsResolve(host), "127.0.0.0", "255.255.255.0"))
        return "DIRECT";
    */
    // Ref: https://jixun.moe/2017/02/24/oversea-netease-cloud-music-by-hosts/
    // The above shExpMatch for 163 or 126 doesn't work, mabye * just match one word
    if (host == 'music.163.com'
     || host == 'ip.ws.126.net'
     || host == 'music.httpdns.c.163.com'
     || host == 'm10.music.126.net')
    {
        return "DIRECT";
    }

    return socksProxy;
}
