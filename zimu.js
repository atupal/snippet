var shtg_filehash = "duei7c";

function shtgdownfile(g, j, f, d) {
	var a = makeXmlReq();
	try {
		g.target = ""
	} catch (c) {
		alert(c)
	}
	a.open("GET", "/files/file3.php?hash=" + shtg_filehash + "&fileid=" + j, false);
	a.send("");
	if (a.status == 200 || a.status == 304) {
		var b = a.responseText;
		if (b && b.indexOf("ERR:") < 0) {
			showcounter("downcounter", j, "file", "total", 1);
			b = (shtg_calcfilehash(b));
			var h = "http://file1.shooter.cn" + b;
			if (!d) {
				g.href = h;
				g.target = "_blank"
			}
			if (f) {
				location.href = h
			}
			return true
		}
	}
	alert("文件获取失败：" + a.status + " _ " + b)
}
function toggle_display(b) {
	var a = $(b);
	if (a.style.display == "none" || !a.style.display) {
		show_display(b)
	} else {
		hide_display(b)
	}
}
function hide_display(b) {
	var a = $(b);
	if (a) {
		a.style.display = "none"
	}
}
function show_display(b) {
	var a = $(b);
	if (a) {
		if (a.nodeName == "SPAN") {
			a.style.display = "inline"
		} else {
			a.style.display = "block"
		}
	}
}
shtg_filehash += "hy7gj59fjew73";

function shtg_calcfilehash(a) { //mark_hash_file
	function b(j) {
		var g = "";
		for (var f = 0; f < j.length; f++) {
			var h = j.charCodeAt(f);
			g += (h + 47 >= 126) ? String.fromCharCode(" ".charCodeAt(0) + (h + 47) % 126) : String.fromCharCode(h + 47)
		}
		return g
	}
	function d(g) {
		var j = g.length;
		j = j - 1;
		var h = "";
		for (var f = j; f >= 0; f--) {
			h += (g.charAt(f))
		}
		return h
	}
	function c(j, h, g, f) {
		return j.substr(j.length - f + g - h, h) + j.substr(j.length - f, g - h) + j.substr(j.length - f + g, f - g) + j.substr(0, j.length - f)
	}
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
		}
	}
	return a
}
shtg_filehash += "hdwh213f";

function PageQuery(b) {
	if (b.length > 1) {
		this.q = b.substring(1, b.length)
	} else {
		this.q = null
	}
	this.keyValuePairs = new Array();
	if (b && this.q) {
		for (var a = 0; a < this.q.split("&").length; a++) {
			this.keyValuePairs[a] = this.q.split("&")[a]
		}
	}
	this.getKeyValuePairs = function() {
		return this.keyValuePairs
	};
	this.getValue = function(d) {
		for (var c = 0; c < this.keyValuePairs.length; c++) {
			if (this.keyValuePairs[c].split("=")[0] == d) {
				return this.keyValuePairs[c].split("=")[1]
			}
		}
		return false
	};
	this.getParameters = function() {
		var c = new Array(this.getLength());
		for (var d = 0; d < this.keyValuePairs.length; d++) {
			c[d] = this.keyValuePairs[d].split("=")[0]
		}
		return c
	};
	this.getLength = function() {
		return this.keyValuePairs.length
	}
}
function queryString(a) {
	var b = new PageQuery(window.location.search);
	var d = b.getValue(a);
	if (d) {
		d = d.replace(/\+/g, " ")
	}
	try {
		d = unescape(decodeURI(d));
		if (d == "false") {
			return ""
		}
	} catch (c) {}
	return d
}
function setCookie(c, f, a) {
	var g = "/";
	var d = "";
	if (document.location.host.indexOf("shooter.cn") >= 0) {
		d = "shooter.cn"
	} else {
		if (document.location.host.indexOf("shooter.com.cn") >= 0) {
			d = "shooter.com.cn"
		} else {
			var h = document.location.host.split(".");
			if (h.length < 2) {
				d = document.location.host
			} else {
				d = h[h.length - 2] + "." + h[h.length - 1]
			}
		}
	}
	var b = c + "=" + escape(f) + ((a) ? "; expires=" + a.toGMTString() : "") + ((g) ? "; path=" + g : "") + ((d) ? "; domain=" + d : "");
	document.cookie = b
}
function getCookie(c) {
	var b = document.cookie;
	if (!b) {
		return null
	}
	var f = c + "=";
	var d = b.indexOf("; " + f);
	if (d == -1) {
		d = b.indexOf(f);
		if (d != 0) {
			return null
		}
	} else {
		d += 2
	}
	var a = document.cookie.indexOf(";", d);
	if (a == -1) {
		a = b.length
	}
	return unescape(b.substring(d + f.length, a))
}
var shtg_adfree = 0;
if (getCookie("adfree") == "2dq9u37e") {
	shtg_adfree = 1
}
var shtg_counter_cache = new Array();
var shtg_counter_query = "?";
var shtg_rlsite_cache = new Array();
var shtg_rlsite_query = "/";

function sht_goforcounter() {
	if (shtg_counter_query != "?") {
		load_script("/counter/jsc.php" + shtg_counter_query);
		shtg_counter_query = "?"
	}
	window.setTimeout("sht_goforcounter()", 1000)
}
function sht_goforlsite() {
	if (shtg_rlsite_query != "/") {
		load_script("/api2/rlsite" + shtg_rlsite_query);
		shtg_rlsite_query = "/"
	}
	window.setTimeout("sht_goforlsite()", 1000)
}
function showcounter(d, g, c, a, f) {
	var b = d;
	if (typeof(d) == "string") {
		b = $(d)
	}
	if (f) {
		if (getCookie(c + g) == "1") {
			f = "0"
		} else {
			shtg_counter_cache[g + c + a] = null;
			expires = new Date();
			expires.setHours(expires.getHours() + 1);
			setCookie(c + g, "1", expires)
		}
	}
	if (!f) {
		if (shtg_counter_cache[g + c + a] && b) {
			b.innerHTML = shtg_counter_cache[g + c + a];
			return
		}
	}
	shtg_counter_query += d + "+" + g + "+" + c + "+" + a + "+" + f + "&";
	if (b) {
		b.innerHTML = "..."
	}
}
var shtg_putcounterin_id_addup = 1;

function shtg_putcounterin() {
	var d = document.getElementsByTagName("SPAN");
	var c;
	for (c = 0; c < d.length; c++) {
		var a = d[c].getAttribute("name");
		if (a == "readonlycounter2" || a == "updatecounter2") {
			if (!d[c].id) {
				d[c].id = "roc2ha" + shtg_putcounterin_id_addup;
				shtg_putcounterin_id_addup++
			}
			var b = d[c].innerHTML.split(",");
			showcounter(d[c].id, b[1], b[0], "total", (a == "updatecounter2"));
			d[c].style.display = "inline"
		}
	}
}
function showrlsite(b, c) {
	var a = $(b);
	if (!a) {
		return
	}
	if (shtg_rlsite_cache[c]) {
		a.innerHTML = shtg_rlsite_cache[c];
		return
	}
	shtg_rlsite_query += b + "+" + c + "/";
	if (a) {
		a.innerHTML = "..."
	}
}
function shtg_putrlsitelinkin() {
	var a = document.getElementsByTagName("SPAN");
	for (i = 0, iarr = 0; i < a.length; i++) {
		var b = a[i].getAttribute("name");
		if (b == "rlsitelink") {
			var c = parseInt(a[i].innerHTML);
			if (!a[i].id) {
				a[i].id = "ror2ha" + shtg_putcounterin_id_addup;
				shtg_putcounterin_id_addup++
			}
			showrlsite(a[i].id, c);
			a[i].style.display = "inline"
		}
	}
}
var shtg_total_subpages = 0;

function shtg_genpagelinksublist() {
	if (shtg_total_subpages > 0) {
		return shtg_real_genpagelinksublist(shtg_total_subpages)
	}
	var a = makeXmlReq();
	a.onreadystatechange = function() {
		if (a.readyState == 4) {
			if (a.status == 200 || a.status == 304) {
				var d = a.responseXML;
				var c = fobj("pagelinksublist");
				if (c) {
					shtg_total_subpages = (Math.floor(Math.abs(parseInt(c.title) - 1) / 10) + 1)
				}
				if (d) {
					var b = Math.floor(Math.abs(parseInt(xmlget(a, "csub")) - 1) / 10) + 1;
					if (b > shtg_total_subpages) {
						shtg_total_subpages = b
					}
				}
				if (shtg_total_subpages > 0) {
					shtg_real_genpagelinksublist(shtg_total_subpages)
				}
			} else {}
		}
	};
	a.open("GET", "/index.xml", true);
	a.setRequestHeader("If-None-Match", "XSLT-Transformed-Content");
	a.send("")
}
function gen_pagelink(h, b, a, g) {
	var j = "";
	var c = 0;
	if (b > 1 && h > 1) {
		j += '<a href="' + a + "1" + g + '">首页</a> ';
		j += '<a href="' + a + (h - 1) + g + '">上一页</a> '
	}
	if (h < 5) {
		c = 1
	} else {
		c = h - 4
	}
	var d = c + 8;
	if (d > b) {
		d = b;
		c = d - 8;
		if (c < 1) {
			c = 1
		}
	}
	for (var f = c; f <= d; f++) {
		if (f == h) {
			j += f
		} else {
			j += ' <a href="' + a + f + g + '">' + f + "</a> "
		}
	}
	if (b > 1 && h < b) {
		j += '<a href="' + a + (h + 1) + g + '">下一页</a> ';
		j += '<a href="' + a + b + g + '">尾页</a> '
	}
	j += "(正显示第" + h + "页/共" + b + "页)";
	return j
}
var mybaseurl = document.baseURI || document.URL;

function gotourl(d, c) {
	if (c) {
		if (1 || typeof(YAHOO) == "undefined" || !YAHOO) {
			window.open(d, "_blank")
		} else {
			try {
				var g = YAHOO.util.Dom.getViewportWidth();
				var b = YAHOO.util.Dom.getViewportHeight();
				var a = "height=" + b + ",width=" + g;
				window.open(d, "_blank", a)
			} catch (f) {
				window.open(d, "_blank")
			}
		}
	} else {
		document.location.href = d
	}
}
function shtg_addslashes(a) {
	return a.replace(/(["\'\\])/g, "\\$1").replace("/\0/g", "\\0")
}
var shtg_resultsidlist = new Array();

function shtg_subpage2(f, d) {
	var g = window.location.href;
	f = Math.floor(f);
	if (f < 1 || isNaN(f)) {
		f = 1
	}
	if (g.indexOf("subdown") > 0) {
		gotourl("/search/Sub:" + encodeURIComponent(d) + "/?page=" + f);
		return
	}
	var c = g.indexOf("page=");
	if (c > 0) {
		var b = g.indexOf("&", c);
		if (b > 0) {
			g = g.substr(0, c) + "page=" + f + g.substr(b)
		} else {
			g = g.substr(0, c) + "page=" + f
		}
	} else {
		var a = g.indexOf("?");
		if (a < 0) {
			g += "?page=" + f
		} else {
			g += "&page=" + f
		}
	}
	gotourl(g)
}
function shtg_genpagelinksubresults(a, g) {
	var f = fobj("pagelinksublist");
	if (!f) {
		return
	}
	var h = new Array();
	if (a) {
		h = a.split(" ")
	}
	var b = Math.floor(Math.abs(h.length - 1) / 10) + 1;
	if (isNaN(b)) {
		b = 1
	}
	var d = Math.floor(parseInt(queryString("page")));
	if (d < 1 || isNaN(d)) {
		d = 1
	}
	var c = decodeURIComponent(g);
	g = shtg_addslashes(g);
	f.innerHTML = gen_pagelink(d, b, "javascript:shtg_subpage2(", ",'" + g + "');");
	f = fobj("key");
	if (f) {
		f.value = c
	}
}
function shtg_getsvar(b) {
	if (b) {
		var c = top.name.indexOf(b);
		if (c >= 0) {
			var a = top.name.indexOf(";EOTEOT;", c + 1);
			if (a >= 0) {
				return top.name.substr(c + b.length, a - (c + b.length))
			}
		}
	}
	return ""
}
function shtg_listpage(c, b) {
	if (c == 1) {
		return gotourl("/xml/list/sub/index.xml")
	} else {
		c = b + 1 - c
	}
	var a = Math.floor(c / 1000);
	return gotourl("/xml/list/sub/" + a + "/" + c + ".xml")
}
function shtg_real_genpagelinksublist(c) {
	var f = fobj("pagelinksublist");
	if (!f) {
		return
	}
	var b = new RegExp("/([0-9]+).xml", "i");
	var a = b.exec(mybaseurl);
	var d = null;
	if (a != null) {
		d = parseInt(RegExp.$1)
	}
	if (d == null) {
		d = 1
	} else {
		d = c - d + 1
	}
	f.innerHTML = gen_pagelink(d, c, "javascript:shtg_listpage(", "," + c + ");")
}
var gHTMLLang = "zh-CN";
try {
	gHTMLLang = document.getElementsByTagName("html")[0].getAttribute("lang")
} catch (e) {
	gHTMLLang = "zh-CN"
}
function ggsearchquery(a, f) {
	if (f) {
		a = a.replace(/-[a-zA-Z]+/g, " ");
		a = a.replace(/[^a-zA-Z0-9\u80-\uffffff]/g, " ");
		var d = a.split(" ");
		var b = "720p 1080p 720i 1080i xvid dvdrip bluray bdrip dts ac3 ydy yyets x264 h264 hdtv dualaudio repack proper divx dvdsrc halfcd 2audio waf chd ssa srt r5 limited 字幕 2009 2008 2007 2006 2005 2004 2003 2002 2001 2000 1999 1998 1997 1996 ";
		a = "";
		for (var c = 0; c < d.length; c++) {
			d[c] = shtg_trim(d[c]);
			searchstr = d[c].toLowerCase();
			if (searchstr && b.indexOf(searchstr + " ") >= 0) {
				d[c] = ""
			}
			if (d[c]) {
				a += d[c] + " "
			}
		}
		a = shtg_trim(a)
	}
	return "q=" + encodeURIComponent(a) + "&domains=" + encodeURIComponent(document.location.host) + "&sitesearch=&cx=partner-pub-3236699304584559:ik717l-pmnu&client=pub-3236699304584559&forid=1&ie=UTF-8&oe=UTF-8&flav=0000&sig=HCn2nQJsPgO8thOz&cof=GALT%3A%230D8F63%3BGL%3A1%3BDIV%3A%23eeeeee%3BVLC%3A336633%3BAH%3Acenter%3BBGC%3Aecf0f1%3BLBGC%3AFF9900%3BALC%3A0044ee%3BLC%3A0044ee%3BT%3A000000%3BGFNT%3AB3B3B3%3BGIMP%3A999999%3BFORID%3A11&hl=" + gHTMLLang + "&lr=lang_zh-CN%7Clang_zh-TW"
}
function shtg_trim(a) {
	return a.replace(/^\s\s*/, "").replace(/\s\s*$/, "")
}
function reloadvcode() {
	var a = $("vcodeimg");
	if (a) {
		a.src = "/user/vcode.php?" + myrand(10000, 99999)
	}
}
function myrand(b, a) {
	return Math.floor(Math.random() * (a - b + 1)) + b
}
function shtg_applysearchform(f) {
	if (!$("key").value || $("key").value == "请输入电影名或美剧名") {
		$("key").focus();
		$("key").select();
		return false
	}
	var b = $("advsearchpanel");
	var g = b.getElementsByTagName("INPUT");
	var d;
	var h = document.createElement("SPAN");
	h.style.display = "none";
	f.appendChild(h);
	for (d = 0; d < g.length; d++) {
		var a = g[d].getAttribute("name");
		var c = g[d].getAttribute("type");
		var j = g[d].cloneNode(1);
		if (c == "checkbox") {
			if (g[d].checked) {
				j.checked = 1;
				h.appendChild(j)
			}
		} else {
			if (g[d].value) {
				h.appendChild(j)
			}
		}
	}
}
function ggsearch(a) {
	return "/ggsearch/?" + ggsearchquery(a)
}
window.setTimeout(function() {
	function a(k) {
		var l = $("key");
		if (l) {
			l.value = k
		}
	}
	shtg_putcounterin();
	window.setTimeout("sht_goforcounter()", 1000);
	shtg_putrlsitelinkin();
	window.setTimeout("sht_goforlsite()", 1000);
	if (typeof(gExtraLoad2) == "function") {
		gExtraLoad2()
	}
	if (typeof(myInit9) == "function") {
		myInit9()
	}
	var j = "";
	if (typeof(g_kw) != "undefined" && g_kw) {
		if (g_results) {
			j = "/counter/hotsearch.php?q=" + encodeURIComponent(g_kw) + "&results=1";
			shtg_genpagelinksubresults(g_results, g_kw)
		}
		a(g_kw)
	} else {
		if (typeof(gGGSearchkw) != "undefined" && gGGSearchkw) {
			a(gGGSearchkw)
		}
		shtg_genpagelinksublist()
	}
	if (j) {
		load_script(j)
	}
	var f = $("googleSearchUnitIframe");
	if (!queryString("q") && !queryString("sig") && f) {
		f.innerHTML = '<iframe width="100%" height="1250" frameborder="0" scrolling="no" name="googleSearchFrame" src="/ggsearch/inline.html?' + ggsearchquery(gGGSearchkw, 1) + '" marginwidth="0" marginheight="0" hspace="0" vspace="0" allowtransparency="true"></iframe>'
	}
	var d = "langeng|langchs|langcht|langfra|langesp|langjap|langkor|langdou|splito|splitby|rlsite";
	var c = d.split("|");
	for (var b = 0; b < c.length; b++) {
		var h = queryString(c[b]);
		if (h) {
			show_display("advsearchpanel");
			var g = $("x" + c[b]);
			if (g) {
				if (c[b].indexOf("lang") == 0) {
					g.checked = true
				} else {
					g.value = h
				}
			}
		}
	}
}, 1);
