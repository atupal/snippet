'''
function shtg_calcfilehash(a) { //mark_hash_file

'''
def file_hash(a):
    pass


    '''
	function b(j) {
		var g = "";
		for (var f = 0; f < j.length; f++) {
			var h = j.charCodeAt(f);
			g += (h + 47 >= 126) ? String.fromCharCode(" ".charCodeAt(0) + (h + 47) % 126) : String.fromCharCode(h + 47)
		}
		return g
	}
    '''
    def b(j):
        g = ""
        for f in xrange(len(j)):
            h = ord(j[f])
            g += chr(ord(' ') + (h + 47) % 126) if h + 47 >= 126 else chr(h + 47)
        return g

    '''
	function d(g) {
		var j = g.length;
		j = j - 1;
		var h = "";
		for (var f = j; f >= 0; f--) {
			h += (g.charAt(f))
		}
		return h
	}
    '''
    def d(g):
        return g[::-1]

    '''
	function c(j, h, g, f) {
		return j.substr(j.length - f + g - h, h) + j.substr(j.length - f, g - h) + j.substr(j.length - f + g, f - g) + j.substr(0, j.length - f)
	}
    '''
    def c(j, h, g, f):
        return j[len(j) - f + g - h: len(j) - f + g ] + j[len(j) - f:len(j) - f+ g - h] + j[len(j) - f + g:] + j[:len(j) - f]

    '''
	if (a.length > 32) {
		switch (a.charAt(0)) {
		case "o":
			return (b((c(a.substr(1), 8, 17, 27))));
			break;
		case "n":
			return (b(d(c(a.substr(1), 6, 15, 17))));
			break;
		case "m":
			return (d(c(a.substr(1), 6, 11, 17)));
			break;
		case "l":
			return (d(b(c(a.substr(1), 6, 12, 17))));
			break;
		case "k":
			return (c(a.substr(1), 14, 17, 24));
			break;
		case "j":
			return (c(b(d(a.substr(1))), 11, 17, 27));
			break;
		case "i":
			return (c(d(b(a.substr(1))), 5, 7, 24));
			break;
		case "h":
			return (c(b(a.substr(1)), 12, 22, 30));
			break;
		case "g":
			return (c(d(a.substr(1)), 11, 15, 21));
		case "f":
			return (c(a.substr(1), 14, 17, 24));
		case "e":
			return (c(a.substr(1), 4, 7, 22));
		case "d":
			return (d(b(a.substr(1))));
		case "c":
			return (b(d(a.substr(1))));
		case "b":
			return (d(a.substr(1)));
		case "a":
			return b(a.substr(1));
			break
    '''
    if len(a) > 32:
        t = a[0]
        if t == "o":
            return b((c(a[1:], 8, 17, 27)))
        elif t == 'n':
            return b(d(c(a[1:], 6, 15, 17)))
        elif t == 'm':
            return d(c(a[1:], 6, 11, 17))
        elif t == "l":
            return d(b(c(a[1:], 6, 12, 17)))
        elif t ==  "k":
            return c(a[1:], 14, 17, 24)
        elif t ==  "j":
            return c(b(d(a[1:])), 11, 17, 27)
        elif t ==  "i":
            return c(d(b(a[1:])), 5, 7, 24)
        elif t == "h":
            return c(b(a[1:]), 12, 22, 30)
        elif t == "g":
            return c(d(a[1:]), 11, 15, 21)
        elif t == "f":
            return c(a[1:], 14, 17, 24)
        elif t== "e":
            return c(a[1:], 4, 7, 22)
        elif t == "d":
            return d(b(a[1:]))
        elif t == "c":
            return b(d(a[1:]))
        elif t == "b":
            return d(a[1:])
        elif t == "a":
            return b(a[1:])
    else:
        return a



import urllib2
import re
def get_hash():
    url = 'http://www.shooter.cn/a/loadmain.js'
    resp = urllib2.urlopen(url).read()
    h = re.findall('shtg_filehash="([a-z0-9]*?)"', resp)
    res = re.findall('shtg_filehash\+="([a-z0-9]*?)"', resp)
    return ''.join(h) + ''.join(res)


def get_field(url):
    resp = urllib2.urlopen(url).read()
    res = re.findall('return local_downfile\(this,([0-9]+?)\)', resp)
    return res[0]


if __name__ == "__main__":
    #print  file_hash('j00000000000]dg_gba^4^000000"fp~Ar6CH8pxw"wKy5+>@wl9Ufab`h_afb`lEU`fce25hh_66cd`e`2g462g455d5f_eg7lDUbae_b`_alAnA:K]ECD0$z#p!$0ceaI0J2#F=q0A_af0b`_a0?H@s0?2|0526s0')
    #print "http://file1.shooter.cn" + file_hash('''dpFq?<$;\~#a;:!K%07ypa?l9Ua`fhg_afb`lEU`fce25hh_66cd`e`2g462g455d5f_eg7lDUbae_b`_alAnA:K]ECD0$z#p!$0ceaI0J2#F=q0A_af0b`_a0?H@s0?2|0526s000000000000000000]dg_gba^4^''')
    url = 'http://www.shooter.cn/xml/sub/246/246565.xml'
    field = get_field(url)
    hash_value = get_hash()
    url = 'http://www.shooter.cn/files/file3.php?hash=%s&fileid=%s' % (hash_value, field)
    resp = urllib2.urlopen(url).read()
    print resp
    print 'http://file1.shooter.cn' + file_hash(resp)
