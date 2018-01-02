// Ref: https://www.systutorials.com/4876/how-to-configure-ios-for-iphone-and-ipad-to-use-socks-proxy-created-by-ssh/

function FindProxyForURL(url, host)
{
    // Configurations
    var httpProxy = "PROXY 192.168.1.1:8088; DIRECT"

    // Ref: https://jixun.moe/2017/02/24/oversea-netease-cloud-music-by-hosts/
    // The above shExpMatch for 163 or 126 doesn't work, mabye * just match one word
    if (host == 'music.163.com'
     || host == 'ip.ws.126.net'
     || host == 'music.httpdns.c.163.com'
     || host == 'm10.music.126.net')
    {
        return "DIRECT";
    }

    return httpProxy;
}
