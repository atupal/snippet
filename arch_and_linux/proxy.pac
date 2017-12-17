// Ref: https://www.systutorials.com/4876/how-to-configure-ios-for-iphone-and-ipad-to-use-socks-proxy-created-by-ssh/

function FindProxyForURL(url, host)
{
    // Configurations
    var socksProxy = "SOCKS 192.168.1.1:8087";

    return socksProxy;
}
