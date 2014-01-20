window = {};

window.onload = function(){
  onloadNewkcxx('newkcxx');
  onloadHotkcxx('highkcxx');
  onloadYears();
  onloadKcfl('2');
  setTimeout("document.getElementById('retMsg').innerHTML=document.getElementById('warn').value","5000");
}

function onloadYears(){
  Ajax.doPost("xlClanderAction.do","type=years",function(){
    var data=this.responseText;
    document.getElementById("xl_years").innerHTML=data;
    onloadXL(1);
  })
}

/**
 * 加载校历
 * @return
 */
function onloadXL(v){
  var year=document.getElementById("year").value;
  var month=document.getElementById("month").value;
  var url="";
  if(v==1){
    url="type=getxl&year="+year+"&month="+month+"&init=init";
  }else{
    url="type=getxl&year="+year+"&month="+month;
  }
  Ajax.doPost("xlClanderAction.do",url,function(){
    var data=this.responseText;
    document.getElementById("xlshow").innerHTML=data.split("*_*")[0];
    document.getElementById("xqshow").innerHTML=data.split("*_*")[1];
  })
}

/**
 * 加载学期
 * @return
 */
function onloadXQ(){
  var url="type=getxq";
  Ajax.doPost("xlClanderAction.do",url,function(){
    var data=this.responseText;
    if(data!=null&&data!=''){
    }
  })
}

/**
 * 加载最新和资源最丰富课程
 * @param type
 * @return
 */
function onloadNewkcxx(type){
  var url="type="+type;
  Ajax.doPost("xlClanderAction.do",url,function(){
    var data=eval(this.responseText);
    var html="<table width='310px' cellpadding='0' cellspacing='0'>";
    var value="";
    var textAlign="left";
    if("morekcxx"==type){
      value="个资源";
      textAlign="right";
    }
    html=html+""
    for(var i=0;i<data.length;i++){
      html=html+"<tr height='26px'>" +
        "<td align="+textAlign+" style=\"color:#666666;border-bottom:1px solid #EAEAEA;padding-left:7px\">"
        +"<span style='cursor:pointer;' onclick=\"gotoKcinfo('"+data[i].kcbh+"','"+type+"')\">"+data[i].kcmc+"</span></td>"+
        "</tr>";
    }
    html=html+"</table>";
    document.getElementById("newMore").innerHTML=html;
  })
}

/**
 * 加载最热门和讨论在热烈课程
 * @param type
 * @return
 */
function onloadHotkcxx(type){
  var url="type="+type;
  Ajax.doPost("xlClanderAction.do",url,function(){
    var data=eval(this.responseText);
    var html="<table width='310px' cellpadding='0' cellspacing='0'>";
    var textAlign="left";
    if("hotkcxx"==type){
      textAlign="right";
    }
    for(var i=0;i<data.length;i++){
      html=html+"<tr height='26px'>" +
      "<td align="+textAlign+" style=\"color:#666666;border-bottom:1px solid #EAEAEA;padding-left:7px\">"
      +"<span style='cursor:pointer;' onclick=\"gotoKcinfo('"+data[i].kcbh+"','"+type+"')\">"+data[i].kcmc+"</span></td>"+
      "</tr>";
    }
    html=html+"</table>";
    document.getElementById("hotHigh").innerHTML=html;
  })
}

/**
 * 跳转到课程详情页面
 * @param kcdm
 * @param kcmc
 * @param type
 * @return
 */
function gotoKcinfo(kcdm,type){
  //setMaxDigits(130);   
  //var passkey = new RSAKeyPair("10001","",document.getElementById("module").value);  
  var kcdm=str_encode(kcdm);
  Ajax.doPost("xlClanderAction.do","kcdm="+kcdm+"&type=click",function(){
    var data=this.responseText;
    if(data=='ok'){
      document.getElementById("kcdm").value=kcdm;
      document.getElementById("type").value=type;
      document.getElementById("fm").action="./kc/kcinfo.jsp";
      document.getElementById("fm").submit();
    }else{
      alert("error");
    }
  })
}

/**
 * 跳转到课程列表页面
 * @param id
 * @param type
 * @param mc
 * @return
 */
function gotoKcList(id,type,mc,key){
  document.getElementById("type").value=type;
  document.getElementById("typeid").value=id;
  document.getElementById("mc").value=mc;
  document.getElementById("key").value=key;
  document.getElementById("fm").submit();
}

/**
 * 跳转到专业列表页面
 * @param id
 * @param type
 * @param mc
 * @return
 */
function gotoZyList(mlid,mc,key){
  document.getElementById("mlid").value=mlid;
  document.getElementById("type").value="";
  document.getElementById("mlmc").value=mc;
  document.getElementById("key").value=key;
  //document.getElementById("fm").action="./kc/zylist.jsp";
  document.getElementById("fm").action="./kc/gbzylist.jsp";
  document.getElementById("fm").submit();
}

/**
 * 首页检索课程信息
 * @return
 */
function kcSearch(){
  if(navigator.appName=="Microsoft Internet Explorer"){//IE浏览器
    if(event.keyCode==13){
      var kcmc=document.getElementById("kcsearchtext").value;
      gotoKcList(kcmc,"search","");
    }
  }else if(navigator.appName=="Netscape"){//firefox浏览器
    if(e.keyCode==13){
      var kcmc=document.getElementById("kcsearchtext").value;
      gotoKcList(kcmc,"search","");
    }
  }
}

function clickSearch(){
  var kcmc=document.getElementById("kcsearchtext").value;
  gotoKcList(kcmc,"search","");
}

/**
 * 加载课程分类数据
 * @param key
 * @return
 */
function onloadKcfl(key,page){
  document.getElementById("key").value=key;
  var url="type=kclb&fl="+key;
  Ajax.doPost("xlClanderAction.do",url,function(){
    var data=eval(this.responseText);
    var lblistdiv="<table width='100%' cellspacing='0' style='color:#666666;border-top:1px #EAEAEA solid;border-right:1px #EAEAEA solid'><tr>";
    var start=0;
    var end=28;
    var halfsize=4;
    var height="29"
    if(key==1){
      height="34"
      start=(page-1)*24;
      end=parseInt(page)*24;
      document.getElementById("page").value=page;
      var len=data.length;
      document.getElementById("count").value=len%24==0?parseInt(len/24):parseInt(len/24)+1;
    }
    for(var i=start;i<end;i++){
      if(i%halfsize==0){
        lblistdiv=lblistdiv+"</tr><tr>";
      }
      if(i<data.length){
        if(key==2){
          lblistdiv=lblistdiv+"<td width='185px' height='"+height+"px' valign='middle' style='font-size:10pt;" +
          "border-bottom:1px #EAEAEA solid;border-left:1px #EAEAEA solid;cursor:pointer' onclick=\"gotoZyList('"+data[i].dm+"','"+data[i].mc+"','"+key+"')\">"+ data[i].mc + "</td>";
        }else{
          lblistdiv=lblistdiv+"<td width='185px' height='"+height+"px' valign='middle' style='font-size:10pt;" +
          "border-bottom:1px #EAEAEA solid;border-left:1px #EAEAEA solid;cursor:pointer' onclick=\"gotoKcList('"+data[i].dm+"','"+key+"','"+data[i].mc+"','1')\">"+ data[i].mc + "</td>";
        }
      }else{
        lblistdiv=lblistdiv+"<td width='185px' height='"+height+"px' valign='middle' style='font-size:10pt;" +
            "border-bottom:1px #EAEAEA solid;border-left:1px #EAEAEA solid;'>&nbsp;</td>";
      }
    }
    lblistdiv=lblistdiv+"</tr></table>";
    document.getElementById("lblistDiv").innerHTML=lblistdiv;
  })
}

//院系分页
function pageSearch(key){
  var page=document.getElementById("page").value;
  if(key=="0"){
    if(page>1){
      onloadKcfl("1",parseInt(page)-1);
      document.getElementById("page").value=parseInt(page)-1;
    }
  }else{
    var count=document.getElementById("count").value;
    if(page<count){
      onloadKcfl("1",parseInt(page)+1);
      document.getElementById("page").value=parseInt(page)+1;
    }
  }
  document.getElementById("page").value=page;
}

/**
* 导航栏的跳转
* @param obj
* @return
*/
function toolClick(obj,key){
  switch(obj.id){
      case "mxdx":gotoKcList("","4","","4");break;
      case "kclb":document.getElementById("fenye").style.display="none";onloadKcfl("3",1);break;
      case "xkml":document.getElementById("fenye").style.display="none";onloadKcfl("2",1);break;
      case "kkyx":document.getElementById("fenye").style.display="block";onloadKcfl("1",1);break;
  }
  var divs=document.getElementsByTagName("div");
  for(var i=0;i<divs.length;i++){
    if(obj.id==divs[i].id){
      obj.className="toolLinkEd";
    }else if(divs[i].className=="toolLinkEd"){
      divs[i].className="toolLink";
    }
  }
}

function newMoreClick(obj){
  if(obj.id=="more"){
    document.getElementById("new").className="newMoreKC";
    onloadNewkcxx('morekcxx');
  }else{
    document.getElementById("more").className="newMoreKC";
    onloadNewkcxx('newkcxx');
  }
  document.getElementById(obj.id).className="newMoreKCED";
}

function hotHighClick(obj){
  if(obj.id=="hot"){
    document.getElementById("high").className="newMoreKC";
    onloadHotkcxx('hotkcxx');
  }else{
    document.getElementById("hot").className="newMoreKC";
    onloadHotkcxx('highkcxx');
  }
  document.getElementById(obj.id).className="newMoreKCED";
}

function doSubmit(key) {
  var account = document.getElementById("loginId").value;
  if( account == "" ) {
    showMessage("\u9700\u5f55\u5165\u7528\u6237\u540d\uff01");
    return;
  }
  var password = document.getElementById("upassword").value;
  if( password == "") {
    showMessage("\u9700\u5f55\u5165\u5bc6\u7801\uff01");
    return;
  }
  checkrand(key);
}

function gologin(e){
  if(navigator.appName=="Microsoft Internet Explorer"){//IE浏览器
    if(event.keyCode==13){
      document.getElementById("login_").click();
    }
  }else if(navigator.appName=="Netscape"){//firefox浏览器
    if(e.keyCode==13){
      document.getElementById("login_").click();
    }
  }
}

function checkrand(key) {
  var randValue = document.getElementById("randnumber").value;
    if(randValue == ""){
        showMessage("\u9700\u5f55\u5165\u9a8c\u8bc1\u7801\uff01");
        return;
    }
    setMaxDigits(130);   
    var passkey = new RSAKeyPair("10001","",key);  
    document.getElementById("_upassword").value = encryptedString(passkey, document.getElementById("upassword").value);
    document.getElementById("_loginId").value = encryptedString(passkey, document.getElementById("loginId").value);
  var xmlHttp;  
  if (window.ActiveXObject) {
    xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
  } else {
    if (window.XMLHttpRequest) {
      xmlHttp = new XMLHttpRequest();
    }
  }
  xmlHttp.onreadystatechange = function () {          //得到响应结果
    if (xmlHttp.readyState == 4) {
      if (xmlHttp.status == 200) {
        if(xmlHttp.responseText=="true"){
          document.forms[1].submit();
        }else if(xmlHttp.responseText == "false"){
          showMessage("\u9a8c\u8bc1\u7801\u9519\u8bef\uff01");
          refreshImg();
        }
      }
    }
  };
  url ="imageensureAction.do?randString="+randValue;
  xmlHttp.open("GET", url, true);     //调用listservlet   等待响应
  xmlHttp.send(null);
}

function showMessage(errStr){
  alert(errStr);
}

function onloadEvent() {
  var flag = request("flag");
  if (flag == "1") {
      showMessage("\u7528\u6237\u540d\u6216\u5bc6\u7801\u9519\u8bef\uff01");
  } else if (flag == "2") {
      showMessage("\u670d\u52a1\u5668\u5f02\u5e38\uff01");
  }
}

function refreshImg(){
  document.getElementById("randpic").src="imageensureAction.do?dateTime="+(new Date());
}

function goToHUB(){
  window.open("http://hub.hust.edu.cn/auth/maintenceAccSec/retrievePassword.jsp");
}
// RSA, a suite of routines for performing RSA public-key computations in
// JavaScript.
//
//
// Copyright 1998-2005 David Shapiro.
//
// You may use, re-use, abuse, copy, and modify this code to your liking, but
// please keep this header.
//
// Thanks!
// 
// Dave Shapiro
// dave@ohdave.com 


function twoDigit(n)
{
	return (n < 10 ? "0" : "") + String(n);
}

function encryptedString(key, s)
	// Altered by Rob Saunders (rob@robsaunders.net). New routine pads the
	// string after it has been converted to an array. This fixes an
	// incompatibility with Flash MX's ActionScript.
{
	var a = new Array();
	var sl = s.length;
	var i = 0;
	while (i < sl) {
		a[i] = s.charCodeAt(i);
		i++;
	}

	while (a.length % key.chunkSize != 0) {
		a[i++] = 0;
	}

	var al = a.length;
	var result = "";
	var j, k, block;
	for (i = 0; i < al; i += key.chunkSize) {
		block = new BigInt();
		j = 0;
		for (k = i; k < i + key.chunkSize; ++j) {
			block.digits[j] = a[k++];
			block.digits[j] += a[k++] << 8;
		}
		var crypt = key.barrett.powMod(block, key.e);
		var text = key.radix == 16 ? biToHex(crypt) : biToString(crypt, key.radix);
		result += text + " ";
	}
	return result.substring(0, result.length - 1); // Remove last space.
}

function decryptedString(key, s)
{
	var blocks = s.split(" ");
	var result = "";
	var i, j, block;
	for (i = 0; i < blocks.length; ++i) {
		var bi;
		if (key.radix == 16) {
			bi = biFromHex(blocks[i]);
		}
		else {
			bi = biFromString(blocks[i], key.radix);
		}
		block = key.barrett.powMod(bi, key.d);
		for (j = 0; j <= biHighIndex(block); ++j) {
			result += String.fromCharCode(block.digits[j] & 255,
			                              block.digits[j] >> 8);
		}
	}
	// Remove trailing null, if any.
	if (result.charCodeAt(result.length - 1) == 0) {
		result = result.substring(0, result.length - 1);
	}
	return result;
}/*
 * A JavaScript implementation of the RSA Data Security, Inc. MD5 Message
 * Digest Algorithm, as defined in RFC 1321.
 * Version 2.1 Copyright (C) Paul Johnston 1999 - 2002.
 * Other contributors: Greg Holt, Andrew Kepert, Ydnar, Lostinet
 * Distributed under the BSD License
 * See http://pajhome.org.uk/crypt/md5 for more info.
 */

/*
 * Configurable variables. You may need to tweak these to be compatible with
 * the server-side, but the defaults work in most cases.
 */
var hexcase = 0;  /* hex output format. 0 - lowercase; 1 - uppercase        */
var b64pad  = ""; /* base-64 pad character. "=" for strict RFC compliance   */
var chrsz   = 8;  /* bits per input character. 8 - ASCII; 16 - Unicode      */

/*
 * These are the functions you'll usually want to call
 * They take string arguments and return either hex or base-64 encoded strings
 */
function hex_md5(s){ return binl2hex(core_md5(str2binl(s), s.length * chrsz));}
function b64_md5(s){ return binl2b64(core_md5(str2binl(s), s.length * chrsz));}
function str_md5(s){ return binl2str(core_md5(str2binl(s), s.length * chrsz));}
function hex_hmac_md5(key, data) { return binl2hex(core_hmac_md5(key, data)); }
function b64_hmac_md5(key, data) { return binl2b64(core_hmac_md5(key, data)); }
function str_hmac_md5(key, data) { return binl2str(core_hmac_md5(key, data)); }

/*
 * Perform a simple self-test to see if the VM is working
 */
function md5_vm_test()
{
  return hex_md5("abc") == "900150983cd24fb0d6963f7d28e17f72";
}

/*
 * Calculate the MD5 of an array of little-endian words, and a bit length
 */
function core_md5(x, len)
{
  /* append padding */
  x[len >> 5] |= 0x80 << ((len) % 32);
  x[(((len + 64) >>> 9) << 4) + 14] = len;

  var a =  1732584193;
  var b = -271733879;
  var c = -1732584194;
  var d =  271733878;

  for(var i = 0; i < x.length; i += 16)
  {
    var olda = a;
    var oldb = b;
    var oldc = c;
    var oldd = d;

    a = md5_ff(a, b, c, d, x[i+ 0], 7 , -680876936);
    d = md5_ff(d, a, b, c, x[i+ 1], 12, -389564586);
    c = md5_ff(c, d, a, b, x[i+ 2], 17,  606105819);
    b = md5_ff(b, c, d, a, x[i+ 3], 22, -1044525330);
    a = md5_ff(a, b, c, d, x[i+ 4], 7 , -176418897);
    d = md5_ff(d, a, b, c, x[i+ 5], 12,  1200080426);
    c = md5_ff(c, d, a, b, x[i+ 6], 17, -1473231341);
    b = md5_ff(b, c, d, a, x[i+ 7], 22, -45705983);
    a = md5_ff(a, b, c, d, x[i+ 8], 7 ,  1770035416);
    d = md5_ff(d, a, b, c, x[i+ 9], 12, -1958414417);
    c = md5_ff(c, d, a, b, x[i+10], 17, -42063);
    b = md5_ff(b, c, d, a, x[i+11], 22, -1990404162);
    a = md5_ff(a, b, c, d, x[i+12], 7 ,  1804603682);
    d = md5_ff(d, a, b, c, x[i+13], 12, -40341101);
    c = md5_ff(c, d, a, b, x[i+14], 17, -1502002290);
    b = md5_ff(b, c, d, a, x[i+15], 22,  1236535329);

    a = md5_gg(a, b, c, d, x[i+ 1], 5 , -165796510);
    d = md5_gg(d, a, b, c, x[i+ 6], 9 , -1069501632);
    c = md5_gg(c, d, a, b, x[i+11], 14,  643717713);
    b = md5_gg(b, c, d, a, x[i+ 0], 20, -373897302);
    a = md5_gg(a, b, c, d, x[i+ 5], 5 , -701558691);
    d = md5_gg(d, a, b, c, x[i+10], 9 ,  38016083);
    c = md5_gg(c, d, a, b, x[i+15], 14, -660478335);
    b = md5_gg(b, c, d, a, x[i+ 4], 20, -405537848);
    a = md5_gg(a, b, c, d, x[i+ 9], 5 ,  568446438);
    d = md5_gg(d, a, b, c, x[i+14], 9 , -1019803690);
    c = md5_gg(c, d, a, b, x[i+ 3], 14, -187363961);
    b = md5_gg(b, c, d, a, x[i+ 8], 20,  1163531501);
    a = md5_gg(a, b, c, d, x[i+13], 5 , -1444681467);
    d = md5_gg(d, a, b, c, x[i+ 2], 9 , -51403784);
    c = md5_gg(c, d, a, b, x[i+ 7], 14,  1735328473);
    b = md5_gg(b, c, d, a, x[i+12], 20, -1926607734);

    a = md5_hh(a, b, c, d, x[i+ 5], 4 , -378558);
    d = md5_hh(d, a, b, c, x[i+ 8], 11, -2022574463);
    c = md5_hh(c, d, a, b, x[i+11], 16,  1839030562);
    b = md5_hh(b, c, d, a, x[i+14], 23, -35309556);
    a = md5_hh(a, b, c, d, x[i+ 1], 4 , -1530992060);
    d = md5_hh(d, a, b, c, x[i+ 4], 11,  1272893353);
    c = md5_hh(c, d, a, b, x[i+ 7], 16, -155497632);
    b = md5_hh(b, c, d, a, x[i+10], 23, -1094730640);
    a = md5_hh(a, b, c, d, x[i+13], 4 ,  681279174);
    d = md5_hh(d, a, b, c, x[i+ 0], 11, -358537222);
    c = md5_hh(c, d, a, b, x[i+ 3], 16, -722521979);
    b = md5_hh(b, c, d, a, x[i+ 6], 23,  76029189);
    a = md5_hh(a, b, c, d, x[i+ 9], 4 , -640364487);
    d = md5_hh(d, a, b, c, x[i+12], 11, -421815835);
    c = md5_hh(c, d, a, b, x[i+15], 16,  530742520);
    b = md5_hh(b, c, d, a, x[i+ 2], 23, -995338651);

    a = md5_ii(a, b, c, d, x[i+ 0], 6 , -198630844);
    d = md5_ii(d, a, b, c, x[i+ 7], 10,  1126891415);
    c = md5_ii(c, d, a, b, x[i+14], 15, -1416354905);
    b = md5_ii(b, c, d, a, x[i+ 5], 21, -57434055);
    a = md5_ii(a, b, c, d, x[i+12], 6 ,  1700485571);
    d = md5_ii(d, a, b, c, x[i+ 3], 10, -1894986606);
    c = md5_ii(c, d, a, b, x[i+10], 15, -1051523);
    b = md5_ii(b, c, d, a, x[i+ 1], 21, -2054922799);
    a = md5_ii(a, b, c, d, x[i+ 8], 6 ,  1873313359);
    d = md5_ii(d, a, b, c, x[i+15], 10, -30611744);
    c = md5_ii(c, d, a, b, x[i+ 6], 15, -1560198380);
    b = md5_ii(b, c, d, a, x[i+13], 21,  1309151649);
    a = md5_ii(a, b, c, d, x[i+ 4], 6 , -145523070);
    d = md5_ii(d, a, b, c, x[i+11], 10, -1120210379);
    c = md5_ii(c, d, a, b, x[i+ 2], 15,  718787259);
    b = md5_ii(b, c, d, a, x[i+ 9], 21, -343485551);

    a = safe_add(a, olda);
    b = safe_add(b, oldb);
    c = safe_add(c, oldc);
    d = safe_add(d, oldd);
  }
  return Array(a, b, c, d);

}

/*
 * These functions implement the four basic operations the algorithm uses.
 */
function md5_cmn(q, a, b, x, s, t)
{
  return safe_add(bit_rol(safe_add(safe_add(a, q), safe_add(x, t)), s),b);
}
function md5_ff(a, b, c, d, x, s, t)
{
  return md5_cmn((b & c) | ((~b) & d), a, b, x, s, t);
}
function md5_gg(a, b, c, d, x, s, t)
{
  return md5_cmn((b & d) | (c & (~d)), a, b, x, s, t);
}
function md5_hh(a, b, c, d, x, s, t)
{
  return md5_cmn(b ^ c ^ d, a, b, x, s, t);
}
function md5_ii(a, b, c, d, x, s, t)
{
  return md5_cmn(c ^ (b | (~d)), a, b, x, s, t);
}

/*
 * Calculate the HMAC-MD5, of a key and some data
 */
function core_hmac_md5(key, data)
{
  var bkey = str2binl(key);
  if(bkey.length > 16) bkey = core_md5(bkey, key.length * chrsz);

  var ipad = Array(16), opad = Array(16);
  for(var i = 0; i < 16; i++)
  {
    ipad[i] = bkey[i] ^ 0x36363636;
    opad[i] = bkey[i] ^ 0x5C5C5C5C;
  }

  var hash = core_md5(ipad.concat(str2binl(data)), 512 + data.length * chrsz);
  return core_md5(opad.concat(hash), 512 + 128);
}

/*
 * Add integers, wrapping at 2^32. This uses 16-bit operations internally
 * to work around bugs in some JS interpreters.
 */
function safe_add(x, y)
{
  var lsw = (x & 0xFFFF) + (y & 0xFFFF);
  var msw = (x >> 16) + (y >> 16) + (lsw >> 16);
  return (msw << 16) | (lsw & 0xFFFF);
}

/*
 * Bitwise rotate a 32-bit number to the left.
 */
function bit_rol(num, cnt)
{
  return (num << cnt) | (num >>> (32 - cnt));
}

/*
 * Convert a string to an array of little-endian words
 * If chrsz is ASCII, characters >255 have their hi-byte silently ignored.
 */
function str2binl(str)
{
  var bin = Array();
  var mask = (1 << chrsz) - 1;
  for(var i = 0; i < str.length * chrsz; i += chrsz)
    bin[i>>5] |= (str.charCodeAt(i / chrsz) & mask) << (i%32);
  return bin;
}

/*
 * Convert an array of little-endian words to a string
 */
function binl2str(bin)
{
  var str = "";
  var mask = (1 << chrsz) - 1;
  for(var i = 0; i < bin.length * 32; i += chrsz)
    str += String.fromCharCode((bin[i>>5] >>> (i % 32)) & mask);
  return str;
}

/*
 * Convert an array of little-endian words to a hex string.
 */
function binl2hex(binarray)
{
  var hex_tab = hexcase ? "0123456789ABCDEF" : "0123456789abcdef";
  var str = "";
  for(var i = 0; i < binarray.length * 4; i++)
  {
    str += hex_tab.charAt((binarray[i>>2] >> ((i%4)*8+4)) & 0xF) +
           hex_tab.charAt((binarray[i>>2] >> ((i%4)*8  )) & 0xF);
  }
  return str;
}

/*
 * Convert an array of little-endian words to a base-64 string
 */
function binl2b64(binarray)
{
  var tab = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
  var str = "";
  for(var i = 0; i < binarray.length * 4; i += 3)
  {
    var triplet = (((binarray[i   >> 2] >> 8 * ( i   %4)) & 0xFF) << 16)
                | (((binarray[i+1 >> 2] >> 8 * ((i+1)%4)) & 0xFF) << 8 )
                |  ((binarray[i+2 >> 2] >> 8 * ((i+2)%4)) & 0xFF);
    for(var j = 0; j < 4; j++)
    {
      if(i * 8 + j * 6 > binarray.length * 32) str += b64pad;
      else str += tab.charAt((triplet >> 6*(3-j)) & 0x3F);
    }
  }
  return str;
}// RSA, a suite of routines for performing RSA public-key computations in
// JavaScript.
//
//
// Copyright 1998-2005 David Shapiro.
//
// You may use, re-use, abuse, copy, and modify this code to your liking, but
// please keep this header.
//
// Thanks!
// 
// Dave Shapiro
// dave@ohdave.com 

function RSAKeyPair(encryptionExponent, decryptionExponent, modulus) {
	this.e = biFromHex(encryptionExponent);
	this.d = biFromHex(decryptionExponent);
	this.m = biFromHex(modulus);
	// We can do two bytes per digit, so
	// chunkSize = 2 * (number of digits in modulus - 1).
	// Since biHighIndex returns the high index, not the number of digits, 1 has
	// already been subtracted.
	this.chunkSize = 2 * biHighIndex(this.m);
	this.radix = 16;
	this.barrett = new BarrettMu(this.m);
}

function twoDigit(n)
{
	return (n < 10 ? "0" : "") + String(n);
}

function encryptedString(key, s)
	// Altered by Rob Saunders (rob@robsaunders.net). New routine pads the
	// string after it has been converted to an array. This fixes an
	// incompatibility with Flash MX's ActionScript.
{
	var a = new Array();
	var sl = s.length;
	var i = 0;
	while (i < sl) {
		a[i] = s.charCodeAt(i);
		i++;
	}

	while (a.length % key.chunkSize != 0) {
		a[i++] = 0;
	}

	var al = a.length;
	var result = "";
	var j, k, block;
	for (i = 0; i < al; i += key.chunkSize) {
		block = new BigInt();
		j = 0;
		for (k = i; k < i + key.chunkSize; ++j) {
			block.digits[j] = a[k++];
			block.digits[j] += a[k++] << 8;
		}
		var crypt = key.barrett.powMod(block, key.e);
		var text = key.radix == 16 ? biToHex(crypt) : biToString(crypt, key.radix);
		result += text + " ";
	}
	return result.substring(0, result.length - 1); // Remove last space.
}

function decryptedString(key, s)
{
	var blocks = s.split(" ");
	var result = "";
	var i, j, block;
	for (i = 0; i < blocks.length; ++i) {
		var bi;
		if (key.radix == 16) {
			bi = biFromHex(blocks[i]);
		}
		else {
			bi = biFromString(blocks[i], key.radix);
		}
		block = key.barrett.powMod(bi, key.d);
		for (j = 0; j <= biHighIndex(block); ++j) {
			result += String.fromCharCode(block.digits[j] & 255,
			                              block.digits[j] >> 8);
		}
	}
	// Remove trailing null, if any.
	if (result.charCodeAt(result.length - 1) == 0) {
		result = result.substring(0, result.length - 1);
	}
	return result;
}// BigInt, a suite of routines for performing multiple-precision arithmetic in
// JavaScript.
//
// Copyright 1998-2005 David Shapiro.
//
// You may use, re-use, abuse,
// copy, and modify this code to your liking, but please keep this header.
// Thanks!
//
// Dave Shapiro
// dave@ohdave.com

// IMPORTANT THING: Be sure to set maxDigits according to your precision
// needs. Use the setMaxDigits() function to do this. See comments below.
//
// Tweaked by Ian Bunning
// Alterations:
// Fix bug in function biFromHex(s) to allow
// parsing of strings of length != 0 (mod 4)

// Changes made by Dave Shapiro as of 12/30/2004:
//
// The BigInt() constructor doesn't take a string anymore. If you want to
// create a BigInt from a string, use biFromDecimal() for base-10
// representations, biFromHex() for base-16 representations, or
// biFromString() for base-2-to-36 representations.
//
// biFromArray() has been removed. Use biCopy() instead, passing a BigInt
// instead of an array.
//
// The BigInt() constructor now only constructs a zeroed-out array.
// Alternatively, if you pass <true>, it won't construct any array. See the
// biCopy() method for an example of this.
//
// Be sure to set maxDigits depending on your precision needs. The default
// zeroed-out array ZERO_ARRAY is constructed inside the setMaxDigits()
// function. So use this function to set the variable. DON'T JUST SET THE
// VALUE. USE THE FUNCTION.
//
// ZERO_ARRAY exists to hopefully speed up construction of BigInts(). By
// precalculating the zero array, we can just use slice(0) to make copies of
// it. Presumably this calls faster native code, as opposed to setting the
// elements one at a time. I have not done any timing tests to verify this
// claim.

// Max number = 10^16 - 2 = 9999999999999998;
//               2^53     = 9007199254740992;

var biRadixBase = 2;
var biRadixBits = 16;
var bitsPerDigit = biRadixBits;
var biRadix = 1 << 16; // = 2^16 = 65536
var biHalfRadix = biRadix >>> 1;
var biRadixSquared = biRadix * biRadix;
var maxDigitVal = biRadix - 1;
var maxInteger = 9999999999999998; 

// maxDigits:
// Change this to accommodate your largest number size. Use setMaxDigits()
// to change it!
//
// In general, if you're working with numbers of size N bits, you'll need 2*N
// bits of storage. Each digit holds 16 bits. So, a 1024-bit key will need
//
// 1024 * 2 / 16 = 128 digits of storage.
//

var maxDigits;
var ZERO_ARRAY;
var bigZero, bigOne;

function setMaxDigits(value)
{
	maxDigits = value;
	ZERO_ARRAY = new Array(maxDigits);
	for (var iza = 0; iza < ZERO_ARRAY.length; iza++) ZERO_ARRAY[iza] = 0;
	bigZero = new BigInt();
	bigOne = new BigInt();
	bigOne.digits[0] = 1;
}

setMaxDigits(20);

// The maximum number of digits in base 10 you can convert to an
// integer without JavaScript throwing up on you.
var dpl10 = 15;
// lr10 = 10 ^ dpl10
var lr10 = biFromNumber(1000000000000000);


function biFromDecimal(s)
{
	var isNeg = s.charAt(0) == '-';
	var i = isNeg ? 1 : 0;
	var result;
	// Skip leading zeros.
	while (i < s.length && s.charAt(i) == '0') ++i;
	if (i == s.length) {
		result = new BigInt();
	}
	else {
		var digitCount = s.length - i;
		var fgl = digitCount % dpl10;
		if (fgl == 0) fgl = dpl10;
		result = biFromNumber(Number(s.substr(i, fgl)));
		i += fgl;
		while (i < s.length) {
			result = biAdd(biMultiply(result, lr10),
			               biFromNumber(Number(s.substr(i, dpl10))));
			i += dpl10;
		}
		result.isNeg = isNeg;
	}
	return result;
}

function biCopy(bi)
{
	var result = new BigInt(true);
	result.digits = bi.digits.slice(0);
	result.isNeg = bi.isNeg;
	return result;
}

function biFromNumber(i)
{
	var result = new BigInt();
	result.isNeg = i < 0;
	i = Math.abs(i);
	var j = 0;
	while (i > 0) {
		result.digits[j++] = i & maxDigitVal;
		i >>= biRadixBits;
	}
	return result;
}

function reverseStr(s)
{
	var result = "";
	for (var i = s.length - 1; i > -1; --i) {
		result += s.charAt(i);
	}
	return result;
}

var hexatrigesimalToChar = new Array(
 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z'
);

function biToString(x, radix)
	// 2 <= radix <= 36
{
	var b = new BigInt();
	b.digits[0] = radix;
	var qr = biDivideModulo(x, b);
	var result = hexatrigesimalToChar[qr[1].digits[0]];
	while (biCompare(qr[0], bigZero) == 1) {
		qr = biDivideModulo(qr[0], b);
		digit = qr[1].digits[0];
		result += hexatrigesimalToChar[qr[1].digits[0]];
	}
	return (x.isNeg ? "-" : "") + reverseStr(result);
}

function biToDecimal(x)
{
	var b = new BigInt();
	b.digits[0] = 10;
	var qr = biDivideModulo(x, b);
	var result = String(qr[1].digits[0]);
	while (biCompare(qr[0], bigZero) == 1) {
		qr = biDivideModulo(qr[0], b);
		result += String(qr[1].digits[0]);
	}
	return (x.isNeg ? "-" : "") + reverseStr(result);
}

var hexToChar = new Array('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                          'a', 'b', 'c', 'd', 'e', 'f');

function digitToHex(n)
{
	var mask = 0xf;
	var result = "";
	for (i = 0; i < 4; ++i) {
		result += hexToChar[n & mask];
		n >>>= 4;
	}
	return reverseStr(result);
}

function biToHex(x)
{
	var result = "";
	var n = biHighIndex(x);
	for (var i = biHighIndex(x); i > -1; --i) {
		result += digitToHex(x.digits[i]);
	}
	return result;
}

function charToHex(c)
{
	var ZERO = 48;
	var NINE = ZERO + 9;
	var littleA = 97;
	var littleZ = littleA + 25;
	var bigA = 65;
	var bigZ = 65 + 25;
	var result;

	if (c >= ZERO && c <= NINE) {
		result = c - ZERO;
	} else if (c >= bigA && c <= bigZ) {
		result = 10 + c - bigA;
	} else if (c >= littleA && c <= littleZ) {
		result = 10 + c - littleA;
	} else {
		result = 0;
	}
	return result;
}

function hexToDigit(s)
{
	var result = 0;
	var sl = Math.min(s.length, 4);
	for (var i = 0; i < sl; ++i) {
		result <<= 4;
		result |= charToHex(s.charCodeAt(i))
	}
	return result;
}

function biFromHex(s)
{
	var result = new BigInt();
	var sl = s.length;
	for (var i = sl, j = 0; i > 0; i -= 4, ++j) {
		result.digits[j] = hexToDigit(s.substr(Math.max(i - 4, 0), Math.min(i, 4)));
	}
	return result;
}

function biFromString(s, radix)
{
	var isNeg = s.charAt(0) == '-';
	var istop = isNeg ? 1 : 0;
	var result = new BigInt();
	var place = new BigInt();
	place.digits[0] = 1; // radix^0
	for (var i = s.length - 1; i >= istop; i--) {
		var c = s.charCodeAt(i);
		var digit = charToHex(c);
		var biDigit = biMultiplyDigit(place, digit);
		result = biAdd(result, biDigit);
		place = biMultiplyDigit(place, radix);
	}
	result.isNeg = isNeg;
	return result;
}

function biDump(b)
{
	return (b.isNeg ? "-" : "") + b.digits.join(" ");
}

function biAdd(x, y)
{
	var result;

	if (x.isNeg != y.isNeg) {
		y.isNeg = !y.isNeg;
		result = biSubtract(x, y);
		y.isNeg = !y.isNeg;
	}
	else {
		result = new BigInt();
		var c = 0;
		var n;
		for (var i = 0; i < x.digits.length; ++i) {
			n = x.digits[i] + y.digits[i] + c;
			result.digits[i] = n & 0xffff;
			c = Number(n >= biRadix);
		}
		result.isNeg = x.isNeg;
	}
	return result;
}

function biSubtract(x, y)
{
	var result;
	if (x.isNeg != y.isNeg) {
		y.isNeg = !y.isNeg;
		result = biAdd(x, y);
		y.isNeg = !y.isNeg;
	} else {
		result = new BigInt();
		var n, c;
		c = 0;
		for (var i = 0; i < x.digits.length; ++i) {
			n = x.digits[i] - y.digits[i] + c;
			result.digits[i] = n & 0xffff;
			// Stupid non-conforming modulus operation.
			if (result.digits[i] < 0) result.digits[i] += biRadix;
			c = 0 - Number(n < 0);
		}
		// Fix up the negative sign, if any.
		if (c == -1) {
			c = 0;
			for (var i = 0; i < x.digits.length; ++i) {
				n = 0 - result.digits[i] + c;
				result.digits[i] = n & 0xffff;
				// Stupid non-conforming modulus operation.
				if (result.digits[i] < 0) result.digits[i] += biRadix;
				c = 0 - Number(n < 0);
			}
			// Result is opposite sign of arguments.
			result.isNeg = !x.isNeg;
		} else {
			// Result is same sign.
			result.isNeg = x.isNeg;
		}
	}
	return result;
}

function biHighIndex(x)
{
	var result = x.digits.length - 1;
	while (result > 0 && x.digits[result] == 0) --result;
	return result;
}

function biNumBits(x)
{
	var n = biHighIndex(x);
	var d = x.digits[n];
	var m = (n + 1) * bitsPerDigit;
	var result;
	for (result = m; result > m - bitsPerDigit; --result) {
		if ((d & 0x8000) != 0) break;
		d <<= 1;
	}
	return result;
}

function biMultiply(x, y)
{
	var result = new BigInt();
	var c;
	var n = biHighIndex(x);
	var t = biHighIndex(y);
	var u, uv, k;

	for (var i = 0; i <= t; ++i) {
		c = 0;
		k = i;
		for (j = 0; j <= n; ++j, ++k) {
			uv = result.digits[k] + x.digits[j] * y.digits[i] + c;
			result.digits[k] = uv & maxDigitVal;
			c = uv >>> biRadixBits;
		}
		result.digits[i + n + 1] = c;
	}
	// Someone give me a logical xor, please.
	result.isNeg = x.isNeg != y.isNeg;
	return result;
}

function biMultiplyDigit(x, y)
{
	var n, c, uv;

	result = new BigInt();
	n = biHighIndex(x);
	c = 0;
	for (var j = 0; j <= n; ++j) {
		uv = result.digits[j] + x.digits[j] * y + c;
		result.digits[j] = uv & maxDigitVal;
		c = uv >>> biRadixBits;
	}
	result.digits[1 + n] = c;
	return result;
}

function arrayCopy(src, srcStart, dest, destStart, n)
{
	var m = Math.min(srcStart + n, src.length);
	for (var i = srcStart, j = destStart; i < m; ++i, ++j) {
		dest[j] = src[i];
	}
}

var highBitMasks = new Array(0x0000, 0x8000, 0xC000, 0xE000, 0xF000, 0xF800,
                             0xFC00, 0xFE00, 0xFF00, 0xFF80, 0xFFC0, 0xFFE0,
                             0xFFF0, 0xFFF8, 0xFFFC, 0xFFFE, 0xFFFF);

function biShiftLeft(x, n)
{
	var digitCount = Math.floor(n / bitsPerDigit);
	var result = new BigInt();
	arrayCopy(x.digits, 0, result.digits, digitCount,
	          result.digits.length - digitCount);
	var bits = n % bitsPerDigit;
	var rightBits = bitsPerDigit - bits;
	for (var i = result.digits.length - 1, i1 = i - 1; i > 0; --i, --i1) {
		result.digits[i] = ((result.digits[i] << bits) & maxDigitVal) |
		                   ((result.digits[i1] & highBitMasks[bits]) >>>
		                    (rightBits));
	}
	result.digits[0] = ((result.digits[i] << bits) & maxDigitVal);
	result.isNeg = x.isNeg;
	return result;
}

var lowBitMasks = new Array(0x0000, 0x0001, 0x0003, 0x0007, 0x000F, 0x001F,
                            0x003F, 0x007F, 0x00FF, 0x01FF, 0x03FF, 0x07FF,
                            0x0FFF, 0x1FFF, 0x3FFF, 0x7FFF, 0xFFFF);

function biShiftRight(x, n)
{
	var digitCount = Math.floor(n / bitsPerDigit);
	var result = new BigInt();
	arrayCopy(x.digits, digitCount, result.digits, 0,
	          x.digits.length - digitCount);
	var bits = n % bitsPerDigit;
	var leftBits = bitsPerDigit - bits;
	for (var i = 0, i1 = i + 1; i < result.digits.length - 1; ++i, ++i1) {
		result.digits[i] = (result.digits[i] >>> bits) |
		                   ((result.digits[i1] & lowBitMasks[bits]) << leftBits);
	}
	result.digits[result.digits.length - 1] >>>= bits;
	result.isNeg = x.isNeg;
	return result;
}

function biMultiplyByRadixPower(x, n)
{
	var result = new BigInt();
	arrayCopy(x.digits, 0, result.digits, n, result.digits.length - n);
	return result;
}

function biDivideByRadixPower(x, n)
{
	var result = new BigInt();
	arrayCopy(x.digits, n, result.digits, 0, result.digits.length - n);
	return result;
}

function biModuloByRadixPower(x, n)
{
	var result = new BigInt();
	arrayCopy(x.digits, 0, result.digits, 0, n);
	return result;
}

function biCompare(x, y)
{
	if (x.isNeg != y.isNeg) {
		return 1 - 2 * Number(x.isNeg);
	}
	for (var i = x.digits.length - 1; i >= 0; --i) {
		if (x.digits[i] != y.digits[i]) {
			if (x.isNeg) {
				return 1 - 2 * Number(x.digits[i] > y.digits[i]);
			} else {
				return 1 - 2 * Number(x.digits[i] < y.digits[i]);
			}
		}
	}
	return 0;
}


	q = new BigInt();
	r = x;

	// Normalize Y.
	var t = Math.ceil(tb / bitsPerDigit) - 1;
	var lambda = 0;
	while (y.digits[t] < biHalfRadix) {
		y = biShiftLeft(y, 1);
		++lambda;
		++tb;
		t = Math.ceil(tb / bitsPerDigit) - 1;
	}
	// Shift r over to keep the quotient constant. We'll shift the
	// remainder back at the end.
	r = biShiftLeft(r, lambda);
	nb += lambda; // Update the bit count for x.
	var n = Math.ceil(nb / bitsPerDigit) - 1;

	var b = biMultiplyByRadixPower(y, n - t);
	while (biCompare(r, b) != -1) {
		++q.digits[n - t];
		r = biSubtract(r, b);
	}
	for (var i = n; i > t; --i) {
    var ri = (i >= r.digits.length) ? 0 : r.digits[i];
    var ri1 = (i - 1 >= r.digits.length) ? 0 : r.digits[i - 1];
    var ri2 = (i - 2 >= r.digits.length) ? 0 : r.digits[i - 2];
    var yt = (t >= y.digits.length) ? 0 : y.digits[t];
    var yt1 = (t - 1 >= y.digits.length) ? 0 : y.digits[t - 1];
		if (ri == yt) {
			q.digits[i - t - 1] = maxDigitVal;
		} else {
			q.digits[i - t - 1] = Math.floor((ri * biRadix + ri1) / yt);
		}

		var c1 = q.digits[i - t - 1] * ((yt * biRadix) + yt1);
		var c2 = (ri * biRadixSquared) + ((ri1 * biRadix) + ri2);
		while (c1 > c2) {
			--q.digits[i - t - 1];
			c1 = q.digits[i - t - 1] * ((yt * biRadix) | yt1);
			c2 = (ri * biRadix * biRadix) + ((ri1 * biRadix) + ri2);
		}

		b = biMultiplyByRadixPower(y, i - t - 1);
		r = biSubtract(r, biMultiplyDigit(b, q.digits[i - t - 1]));
		if (r.isNeg) {
			r = biAdd(r, b);
			--q.digits[i - t - 1];
		}
	}
	r = biShiftRight(r, lambda);
	// Fiddle with the signs and stuff to make sure that 0 <= r < y.
	q.isNeg = x.isNeg != origYIsNeg;
	if (x.isNeg) {
		if (origYIsNeg) {
			q = biAdd(q, bigOne);
		} else {
			q = biSubtract(q, bigOne);
		}
		y = biShiftRight(y, lambda);
		r = biSubtract(y, r);
	}
	// Check for the unbelievably stupid degenerate case of r == -0.
	if (r.digits[0] == 0 && biHighIndex(r) == 0) r.isNeg = false;

	return new Array(q, r);
}



function biMultiplyMod(x, y, m)
{
	return biModulo(biMultiply(x, y), m);
}

function biModulo(x, y)
{
	return biDivideModulo(x, y)[1];
}

function biPow(x, y)
{
	var result = bigOne;
	var a = x;
	while (true) {
		if ((y & 1) != 0) result = biMultiply(result, a);
		y >>= 1;
		if (y == 0) break;
		a = biMultiply(a, a);
	}
	return result;
}

function biPowMod(x, y, m)
{
	var result = bigOne;
	var a = x;
	var k = y;
	while (true) {
		if ((k.digits[0] & 1) != 0) result = biMultiplyMod(result, a, m);
		k = biShiftRight(k, 1);
		if (k.digits[0] == 0 && biHighIndex(k) == 0) break;
		a = biMultiplyMod(a, a, m);
	}
	return result;
}
// BarrettMu, a class for performing Barrett modular reduction computations in
// JavaScript.
//
// Requires BigInt.js.
//
// Copyright 2004-2005 David Shapiro.
//
// You may use, re-use, abuse, copy, and modify this code to your liking, but
// please keep this header.
//
// Thanks!
// 
// Dave Shapiro
// dave@ohdave.com 


function BarrettMu_modulo(x)
{
	var q1 = biDivideByRadixPower(x, this.k - 1);
	var q2 = biMultiply(q1, this.mu);
	var q3 = biDivideByRadixPower(q2, this.k + 1);
	var r1 = biModuloByRadixPower(x, this.k + 1);
	var r2term = biMultiply(q3, this.modulus);
	var r2 = biModuloByRadixPower(r2term, this.k + 1);
	var r = biSubtract(r1, r2);
	if (r.isNeg) {
		r = biAdd(r, this.bkplus1);
	}
	var rgtem = biCompare(r, this.modulus) >= 0;
	while (rgtem) {
		r = biSubtract(r, this.modulus);
		rgtem = biCompare(r, this.modulus) >= 0;
	}
	return r;
}

function BarrettMu_multiplyMod(x, y)
{
	/*
	x = this.modulo(x);
	y = this.modulo(y);
	*/
	var xy = biMultiply(x, y);
	return this.modulo(xy);
}

function BarrettMu_powMod(x, y)
{
	var result = new BigInt();
	result.digits[0] = 1;
	var a = x;
	var k = y;
	while (true) {
		if ((k.digits[0] & 1) != 0) result = this.multiplyMod(result, a);
		k = biShiftRight(k, 1);
		if (k.digits[0] == 0 && biHighIndex(k) == 0) break;
		a = this.multiplyMod(a, a);
	}
	return result;
}
function utf16to8(str) {
    var out, i, len, c;

    out = "";
    len = str.length;
    for(i = 0; i < len; i++) {
        c = str.charCodeAt(i);
        if ((c >= 0x0001) && (c <= 0x007F)) {
            out += str.charAt(i);
        } else if (c > 0x07FF) {
            out += String.fromCharCode(0xE0 | ((c >> 12) & 0x0F));
            out += String.fromCharCode(0x80 | ((c >>  6) & 0x3F));
            out += String.fromCharCode(0x80 | ((c >>  0) & 0x3F));
        } else {
            out += String.fromCharCode(0xC0 | ((c >>  6) & 0x1F));
            out += String.fromCharCode(0x80 | ((c >>  0) & 0x3F));
        }
    }
    return out;
}
function utf8to16(str) {
    var out, i, len, c;
    var char2, char3;

    out = "";
    len = str.length;
    i = 0;
    while(i < len) {
        c = str.charCodeAt(i++);
        switch(c >> 4)
        {
          case 0: case 1: case 2: case 3: case 4: case 5: case 6: case 7:
            // 0xxxxxxx
            out += str.charAt(i-1);
            break;
          case 12: case 13:
            // 110x xxxx   10xx xxxx
            char2 = str.charCodeAt(i++);
            out += String.fromCharCode(((c & 0x1F) << 6) | (char2 & 0x3F));
            break;
          case 14:
            // 1110 xxxx  10xx xxxx  10xx xxxx
            char2 = str.charCodeAt(i++);
            char3 = str.charCodeAt(i++);
            out += String.fromCharCode(((c & 0x0F) << 12) |
                                           ((char2 & 0x3F) << 6) |
                                           ((char3 & 0x3F) << 0));
            break;
        }
    }

    return out;
}

var base64EncodeChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
var base64DecodeChars = new Array(
    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 62, -1, -1, -1, 63,
    52, 53, 54, 55, 56, 57, 58, 59, 60, 61, -1, -1, -1, -1, -1, -1,
    -1,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14,
    15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1, -1, -1, -1, -1,
    -1, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, -1, -1, -1, -1, -1);

function base64encode(str) {
    var out, i, len;
    var c1, c2, c3;

    len = str.length;
    i = 0;
    out = "";
    while(i < len) {
        c1 = str.charCodeAt(i++) & 0xff;
        if(i == len)
        {
            out += base64EncodeChars.charAt(c1 >> 2);
            out += base64EncodeChars.charAt((c1 & 0x3) << 4);
            out += "==";
            break;
        }
        c2 = str.charCodeAt(i++);
        if(i == len)
        {
            out += base64EncodeChars.charAt(c1 >> 2);
            out += base64EncodeChars.charAt(((c1 & 0x3)<< 4) | ((c2 & 0xF0) >> 4));
            out += base64EncodeChars.charAt((c2 & 0xF) << 2);
            out += "=";
            break;
        }
        c3 = str.charCodeAt(i++);
        out += base64EncodeChars.charAt(c1 >> 2);
        out += base64EncodeChars.charAt(((c1 & 0x3)<< 4) | ((c2 & 0xF0) >> 4));
        out += base64EncodeChars.charAt(((c2 & 0xF) << 2) | ((c3 & 0xC0) >>6));
        out += base64EncodeChars.charAt(c3 & 0x3F);
    }
    return out;
}

function base64decode(str) {
    var c1, c2, c3, c4;
    var i, len, out;

    len = str.length;
    i = 0;
    out = "";
    while(i < len) {
        /* c1 */
        do {
            c1 = base64DecodeChars[str.charCodeAt(i++) & 0xff];
        } while(i < len && c1 == -1);
        if(c1 == -1)
            break;

        /* c2 */
        do {
            c2 = base64DecodeChars[str.charCodeAt(i++) & 0xff];
        } while(i < len && c2 == -1);
        if(c2 == -1)
            break;

        out += String.fromCharCode((c1 << 2) | ((c2 & 0x30) >> 4));

        /* c3 */
        do {
            c3 = str.charCodeAt(i++) & 0xff;
            if(c3 == 61)
                return out;
            c3 = base64DecodeChars[c3];
        } while(i < len && c3 == -1);
        if(c3 == -1)
            break;

        out += String.fromCharCode(((c2 & 0XF) << 4) | ((c3 & 0x3C) >> 2));

        /* c4 */
        do {
            c4 = str.charCodeAt(i++) & 0xff;
            if(c4 == 61)
                return out;
            c4 = base64DecodeChars[c4];
        } while(i < len && c4 == -1);
        if(c4 == -1)
            break;
        out += String.fromCharCode(((c3 & 0x03) << 6) | c4);
    }
    return out;
}
//js_base64 加密
function str_encode(str){
    return base64encode(utf16to8(str));
}
//js_base64 解密
function str_decode(str){
        return utf8to16(base64decode(str));
}/**
 * pStyle：
 * 		begin-end：开始日期到结束日期
 * 		begin-end-ym：开始日期到结束日期，不含日
 * 		begin-end-time：开始日期时间到结束日期时间
 * 		begin-end-default：开始时间到结束时间
 * 		default：日期
 * 		default-ym：日期，不含日
 * 		default-time：日期时间
 * 		time：时间
 * theID：第一个输入框的ID，必须有
 * secID：第二个输入框的ID，可为null
 * size：输入框的长度样式值，需带单位，可不提供
 */
function HTMLTime_InputCalendar(pStyle, theID, secID, size) {
	var json = {};
	if(Object.prototype.toString.call(pStyle) == "[object Object]"){
		json = pStyle;
	}else{
		json.pStyle = pStyle;
		json.theID = theID;
		json.secID = secID;
		json.size = size;
	}
	
	if(!HTMLTime_InputCalendar.link) {
		var scripts = document.getElementsByTagName("script");
		for(var k = 0; k < scripts.length; k++) {
			if(scripts[k].src && scripts[k].src.indexOf("js/Ref_PopCalendar.js") > -1) {
				var link = document.createElement("link");
				link.setAttribute("rel", "stylesheet");
				link.setAttribute("type", "text/css");
				link.setAttribute("href", scripts[k].src.replace("js/Ref_PopCalendar.js", "css/Ref_Calendar.css"));
				document.getElementsByTagName("head")[0].appendChild(link);
				HTMLTime_InputCalendar.link = true;
				break;
			}
		}
	}
	
	if(!HTMLTime_InputCalendar.bind) {
		HTMLTime_InputCalendar.bind = true;
		
		if(document.all) {
			window.attachEvent("onload", _window_onload);
		} else {
			window.addEventListener("load", _window_onload, false);
		}
	}
	
	function _window_onload() {
		if(document.all) {
			document.body.attachEvent("onclick", _remove_calendar_);
		} else {
			document.addEventListener("click", _remove_calendar_, false);
		}
	}
	
	function _remove_calendar_(e) {
		e = window.event || e;
		//HTMLTime_InputCalendar.stopPropagation(e);
		e.stopPropagation ? e.stopPropagation() : e.cancelBubble = true;
		e = e.srcElement || e.target;
		
		var flag = true;
		if(e.className == "calendar-input"||e.className=="calendar-input-readOnly") {
			flag = false;
		}
		
		if(flag) {
			while(e) {
				if(e.id && e.id == "kingo-mask-div") {
					flag = false;
					break;
				}
				e = e.parentNode;
			}
		}
		
		if(flag) {
			HTMLTime_InputCalendar.removeCalendar();
		}
	}
	
	if(!HTMLTime_InputCalendar.TheCalendarStyle) {
		HTMLTime_InputCalendar.TheCalendarStyle = {};
	}
	
	if(json.theID) {
		HTMLTime_InputCalendar.TheCalendarStyle[json.theID] = json.pStyle; // 传递全局变量
	}
	
	if(json.secID) {
		HTMLTime_InputCalendar.TheCalendarStyle[json.secID] = json.pStyle; // 传递全局变量
	}
	
	var s = HTMLTime_InputCalendar.createCalendarInputHtml(json);
	document.write(s.join(""));
}

HTMLTime_InputCalendar.createCalendarInputHtml = (function(){
	var html = ["<input type='text' class='",
				"",
				"' name='",
				"",
				"' id='",
				"",
				"' style='width:",
				"",
				";' maxlength='",
				"",
				"'",
				"",
				" onclick=HTMLTime_InputCalendar.popCalendar('",
				"",
				"') onblur=HTMLTime_InputCalendar.inputOnblur(this,event)",
				" onpaste=HTMLTime_InputCalendar.inputOnpaste(this,event)",
				" onkeyup=HTMLTime_InputCalendar.inputOnkeyup(this,event)",
				" onkeypress=HTMLTime_InputCalendar.inputOnkeypress(this,event)>"];
				
	var createInputHtml = function(id, size, maxLength, readOnly){
		html[1] = readOnly===true?"calendar-input-readOnly":"calendar-input";
		html[3] = html[5] = html[13] =  id;
		html[7] = size;
		html[9] = maxLength;
		html[11] = readOnly===true?" readOnly='true' ":"";
		return html;
	}
	
	return function(json){
		if (json.pStyle == 'begin-end' || json.pStyle == 'begin-end-ym') {
			json.size = json.size || 65;
			json.maxLength = (json.pStyle == 'begin-end' ? 10 : 7);
		} else if (json.pStyle == 'begin-end-time') {
			json.size = json.size || 120;
			json.maxLength = 19;
		} else if (json.pStyle == 'begin-end-default') {
			json.size = json.size || 55;
			json.maxLength = 8;
		} else if (json.pStyle == 'default') {
			json.size = json.size || "65px";//65;
			json.maxLength = 10;
		} else if (json.pStyle == 'default-time') {
			json.size = json.size || "100px";//120;
			json.maxLength = 19;
		} else if (json.pStyle == 'time') {
			json.size = json.size || 35;
			json.maxLength = 8;
		} else if (json.pStyle == 'default-ym') {
		    json.size = json.size || "45px";
			json.maxLength = 7;
		}
		
		json.size = parseInt(json.size,10)+18;
		
		if(json.pStyle.substr(0,9)=="begin-end"){
			return createInputHtml(json.theID,json.size,json.maxLength,json.readOnly).concat(["&nbsp;",json.separator||"&ndash;","&nbsp;"]).concat(createInputHtml(json.secID,json.size,json.maxLength,json.readOnly));
		}else{
			return createInputHtml(json.theID,json.size,json.maxLength,json.readOnly);
		}
	}
})();

HTMLTime_InputCalendar.popCalendar = function(theID){
	
	if (!document.getElementById(theID)) {
		alert('传入的参数有误!对象ID(' + theID + ')不存在.');
		return;
	} else {
		var o = document.getElementById(theID);
		if(o.readOnly==true){
			return;
		}
		
		var x = 0, temp = y = o.offsetHeight;
		while(o) {
			x += o.offsetLeft || 0;
			y += o.offsetTop || 0;
			o = o.offsetParent;
		}
		
		var width = window.innerWidth || document.body.clientWidth;
		if(width - x < 167) {
			x = width - 167 - 5;
		}
		
		var height = window.innerHeight || document.body.clientHeight;
		if(height - y < 228) {
			y = y - 228-temp;
		}
		
		//特殊情况input标签上下高度不够228
		if(y<0){
			y = height - 228;
			var offsetWidth_x = document.getElementById(theID).offsetWidth;
			x = x + offsetWidth_x + 2;
			if(width - x <167){
				x = x - 167 - offsetWidth_x - 2;
			}
		}
		
		this.showMask(x, y, theID);
	}
}

HTMLTime_InputCalendar.showMask = function(x_, y_, ids) {
	
	if(document.getElementById('kingo-mask-div')) {
		this.removeCalendar();
	}
	
	var maskDiv = document.createElement("div");
	maskDiv.id = "kingo-mask-div";
	maskDiv.style.top = y_ + "px";
	maskDiv.style.left = x_ + "px";
	if(document.all) {
		var maskIframe = document.createElement("iframe");
		maskIframe.id = "kingo-mask-iframe";
		maskIframe.name = "kingo-mask-iframe";
		maskIframe.style.top = y_ + "px";
		maskIframe.style.left = x_ + "px";
		document.body.appendChild(maskIframe);
		maskIframe = null;
	}
	
	var nowDate = new Date();
	var y,m,d,h,mi;
	var idsObj = document.getElementById(ids);
	var dateStr = idsObj.style.color=="red"?[]:idsObj.value.split(/[-\s:]/);
	var cStyle = HTMLTime_InputCalendar.TheCalendarStyle[ids];
	if(cStyle == 'time' || cStyle == 'begin-end-default') {
		dateStr[0] = nowDate.getFullYear();
		dateStr[1] = nowDate.getMonth()+1;
		dateStr[2] = nowDate.getDate();
	}
	y = dateStr[0]||nowDate.getFullYear();
	m = dateStr[1]||nowDate.getMonth()+1;
	d = dateStr[2]||nowDate.getDate();
	h = dateStr[3]||nowDate.getHours();
	mi = dateStr[4]||nowDate.getMinutes();
	
	maskDiv.innerHTML += this.GetTableStr(y, parseInt(m,10), parseInt(d,10), parseInt(h,10), parseInt(mi,10), ids);
	document.body.appendChild(maskDiv);
}

HTMLTime_InputCalendar.removeCalendar = function() {
	function $(sid) {
		return document.getElementById(sid);
	}
	
	if($("kingo-mask-div")) {
		document.body.removeChild($("kingo-mask-div"));
	}
	
	if(window.frames["kingo-mask-iframe"]) {
		document.body.removeChild($("kingo-mask-iframe"));
	}
}

HTMLTime_InputCalendar.retCalendarValue = function(retStr, theID) {
	if (!retStr) {
		var nowDate = new Date();
		var y,m,d,h,mi;
		y = this.appendZero(nowDate.getFullYear());
		m = this.appendZero(nowDate.getMonth()+1);
		d = this.appendZero(nowDate.getDate());
		h = this.appendZero(nowDate.getHours());
		mi = this.appendZero(nowDate.getMinutes());
		s = this.appendZero(nowDate.getSeconds());
		retStr = y+"-"+m+"-"+d+" "+h+":"+mi+":"+s;
	}
	document.getElementById(theID).value = this.retStrByPstyle(theID,retStr);
	
	try{funAfterChooseCalendar(theID);}catch(e){}
	try{calendarEvent()}catch(e){}
}

HTMLTime_InputCalendar.retStrByPstyle = function(theID,retStr){
	var cStyle = HTMLTime_InputCalendar.TheCalendarStyle[theID];
	retStr = retStr.substring(0, 16); // 不要秒了
	if(cStyle == 'time' || cStyle == 'begin-end-default') {
		retStr = retStr.substr(11);
	} else if (cStyle.indexOf('-time') == -1) {
		retStr = retStr.substring(0, 10);
		if(cStyle.indexOf('-ym') != -1) {
			retStr = retStr.substring(0, 7);
		}
	}
	return retStr;
}

HTMLTime_InputCalendar.GetDateStr = function(y, m) {
	var DayArray = [];
	for ( var i = 0; i < 42; i++){
		DayArray[i] = "&nbsp;";
	}
	
	for ( var i = 0; i < new Date(y, m, 0).getDate(); i++){
		DayArray[i + new Date(y, m - 1, 1).getDay()] = i + 1;
	}
	return DayArray;
}

HTMLTime_InputCalendar.GetTableStr = function(y, m, d, hh, mm, dec) {
	var DateArray = [ "日", "一", "二", "三", "四", "五", "六" ];
	
	var DStr = "<table id='kingoCalendarTable' oncontextmenu='return false' onselectstart='return false' onclick='HTMLTime_InputCalendar.showInnerMask(this,event)' border='0' cellpadding='0' cellspacing='0'>\n"
			+ "<tr><td colspan='7' class='CalTrOut'>"
			+ "<table width='100%' height='100%' border='0' cellpadding='0' cellspacing='0' border='0'><tr align='center'>\n"
			+ "<td width='20px' style='font-size:9pt' onclick='HTMLTime_InputCalendar.JumpToRun(\"b\")' onmouseover='this.style.color=\"#ff9900\"' onmouseout='this.style.color=\"\"'>&lt;</td>\n"
			+ "<td width='70px'>"
			+ this.createInputfield("YearTD",y+" 年","100%",4,"年")
			+ "</td>\n"
			+ "<td width='60px'>"
			+ this.createInputfield("MonthTD",m+" 月","100%",2,"月")
			+ "</td>\n"
			+ "<td width='20px' style='font-size:9pt' onclick='HTMLTime_InputCalendar.JumpToRun(\"n\")' onmouseover='this.style.color=\"#ff9900\"' onmouseout='this.style.color=\"\"'>&gt;</td></tr></table>\n"
			+ "</td></tr>\n"
			+ "<tr><td colspan='7' class='CalTrOut'>"
			+ "<table width='100%' height='100%' border='0' cellpadding='0' cellspacing='0'><tr align='center'>\n"
			+ "<td width='50%'>"
			+ this.createInputfield("HourTD",hh+" 时","100%",2,"时")
			+ "</td>"
			+ "<td width='50%'>"
			+ this.createInputfield("MinuteTD",mm+" 分","100%",2,"分")
			+ "</td></tr></table>\n"
			+ "</td></tr>\n"
			+ "<tr align='center'>\n";
			
	for ( var i = 0; i < 7; i++) {
		DStr += "<td class='CalTrOut'>" + DateArray[i] + "</td>\n";
	}
	DStr += "</tr>\n";
	
	var GetDateStr = this.GetDateStr(y,m);
	for ( var i = 0; i < 6; i++) {
		DStr += "<tr align='center'>\n";
		for ( var j = 0; j < 7; j++) {
			var CS = d == GetDateStr[i * 7+ j] ? "CalTdOver" : "CalTdOut";
			DStr += "<td id='TD' class='"
				 + CS
				 + "' cs='"
				 + CS
				 + "' onmouseover='this.className=\"CalTdOver\"' onmouseout='if(this.getAttribute(\"cs\")!=\"CalTdOver\")this.className=\"CalTdOut\"' onclick='HTMLTime_InputCalendar.AlertDay(\""
				 + dec + "\", event)'>"
				 + GetDateStr[i * 7 + j] + "</td>\n";
		}
		DStr += "</tr>\n";
	}
	
	DStr += "<tr align='center'><td colspan='7' class='CalTrOut'>"
	   	 + "<input type='button' class='calendar-button' value='今天' onclick='HTMLTime_InputCalendar.AlertTaday(\""+dec+"\")'>"
	   	 + "&nbsp;<input type='button' class='calendar-button' value='确定' onclick='HTMLTime_InputCalendar.AlertDay(\""+dec+"\",event)'>"
	     + "</td></tr>\n";
	
	DStr += "</tabe>";
	return DStr;
}

HTMLTime_InputCalendar.AlertTaday = function(decText){
	this.retCalendarValue(null, decText);
	this.removeCalendar();
}

HTMLTime_InputCalendar.appendZero = function(s){
	s = parseInt(s,10);
	return s<10?("0"+s):s;
}
	
HTMLTime_InputCalendar.showInnerMask = function(o, e){
	this.stopPropagation(e);
	var tar = e.target || e.srcElement;
	
	var divObj = document.getElementById("inner-kingo-mask-div");
	if(divObj){
		var pNode = divObj.parentNode;
		pNode.removeChild(divObj);
		HTMLTime_InputCalendar.resetInputField(pNode);
		if(pNode==tar.parentNode||tar.tagName!="INPUT"){
			return;
		}
	}
	
	if(tar.tagName=="INPUT"){
		var html = "";
		var td = tar.parentNode;
		
		var offsetTop=td.offsetHeight,offsetLeft=0,offsetWidth=0,offsetHeight=0;
		if (tar.id == "YearTD") {
			html = this.getYearSwitchHtml(parseInt(tar.value,10));
			offsetLeft+=3;
		}else if (tar.id == "MonthTD") {
			html = this.getMonthSwitchHtml(parseInt(tar.value,10));
			offsetLeft+=3;
		}else if (tar.id == "HourTD"){
			html = this.getHourSwitchHtml(parseInt(tar.value,10));
			offsetTop+=26;
			offsetLeft+=2;
			offsetWidth += 25;
		}else if (tar.id == "MinuteTD"){
			html = this.getMinutesSwitchHtml(parseInt(tar.value,10));
			offsetTop+=26;
			offsetLeft = 1-td.offsetLeft;
			offsetWidth += 83;
			offsetHeight = 47;
		}
		
		var maskDiv = document.createElement("div");
		maskDiv.className = "calendar-mask-div";
		maskDiv.id = "inner-kingo-mask-div";
		maskDiv.style.width  = td.offsetWidth + offsetWidth;
		maskDiv.style.height = 125 + offsetHeight;
		maskDiv.style.top    = td.offsetTop + offsetTop;
		maskDiv.style.left   = td.offsetLeft + offsetLeft;
		maskDiv.innerHTML    = html;
		
		if(document.all) {
			maskDiv.attachEvent("onclick", HTMLTime_InputCalendar.itemOnclick);
		} else {
			var d = maskDiv.addEventListener("click", HTMLTime_InputCalendar.itemOnclick, false);
		}
		td.appendChild(maskDiv);
		
		tar.value = parseInt(tar.value);
		tar.className = "calendarInputFieldOver";
		var txt =tar.createTextRange();
		txt.moveStart('character',tar.value.length);
		txt.collapse(true);
		txt.findText(tar.value);
		txt.select();
	}
}

HTMLTime_InputCalendar.itemOnclick = function(e){
	e = window.event || e;
	HTMLTime_InputCalendar.stopPropagation(e);
	e = e.srcElement || e.target;
	
	if(e.tagName=="SPAN"){
		var temp = e;
		while(e){
			if(e.id=="inner-kingo-mask-div"){
				break;
			}
			e = e.parentNode;
		}
		var pNode = e.parentNode;
		
		if(temp.id=="preYears"){
			var value = parseInt(e.firstChild.innerHTML,10)-5;
			e.innerHTML = HTMLTime_InputCalendar.getYearSwitchHtml(value);
		}else if(temp.id=="nextYears"){
			var value = parseInt(e.firstChild.innerHTML,10)+15;
			e.innerHTML = HTMLTime_InputCalendar.getYearSwitchHtml(value);
		}else if(temp.id=="hh"){
			pNode.removeChild(e);
			HTMLTime_InputCalendar.resetInputField(pNode,temp.innerHTML);
		}else if(temp.id=="mi"){
			pNode.removeChild(e);
			HTMLTime_InputCalendar.resetInputField(pNode,temp.innerHTML);
		}else{
			pNode.removeChild(e);
			HTMLTime_InputCalendar.resetInputField(pNode,temp.innerHTML);
			
			var month = document.getElementById("MonthTD").value;
			var year = document.getElementById("YearTD").value;
			HTMLTime_InputCalendar.RewriteTableStr(parseInt(year,10),parseInt(month,10));
		}
	}
}

HTMLTime_InputCalendar.resetInputField = function(pNode,value){
	var o = pNode.getElementsByTagName("INPUT")[0];
	value = parseInt(value||o.value||o.getAttribute("temp"),10);
	if(o.id=="YearTD"){
		if(value<=1585||value>=2255){
			value = new Date().getFullYear();
		}
	}
	if(o.id=="MonthTD"&&value==0){
		value = parseInt(o.getAttribute("temp"),10);
	}
	o.value =  value + " " + o.getAttribute("units");
	o.className = "calendarInputFieldOut";
	window.setTimeout(function(){
		o.blur();
	},20);
}

HTMLTime_InputCalendar.getYearSwitchHtml = function(value){
	var html = [];
	for(var i=-5;i<0;i++){
		html.push("<span class='item-out' onmouseover='this.className=\"item-over\"' onmouseout='this.className=\"item-out\"'>"+(value+i)+"</span>");
		html.push("<span class='item-out' onmouseover='this.className=\"item-over\"' onmouseout='this.className=\"item-out\"'>"+(value+i+5)+"</span>");
	}
	html.push("<span id='preYears' class='item-out' onmouseover='this.className=\"item-over\"' onmouseout='this.className=\"item-out\"'>←</span>");
	html.push("<span id='nextYears' class='item-out' onmouseover='this.className=\"item-over\"' onmouseout='this.className=\"item-out\"'>→</span>");
	return html.join("");
}

HTMLTime_InputCalendar.getMonthSwitchHtml = (function(){
	var html;
	return function(){
		if(!html){
			html = [];
			for(var i=1;i<7;i++){
				html.push("<span class='item-out' onmouseover='this.className=\"item-over\"' onmouseout='this.className=\"item-out\"'>"+i+"月</span>");
				html.push("<span class='item-out' onmouseover='this.className=\"item-over\"' onmouseout='this.className=\"item-out\"'>"+(i+6)+"月</span>");
			}
			html = html.join("");
		}
		return html;
	}
})();

HTMLTime_InputCalendar.getHourSwitchHtml = (function(){
	var html;
	return function(){
		if(!html){
			html = [];
			for(var i=0;i<24;i++){
				html.push("<span id='hh' class='item-out' style='width:20px;' onmouseover='this.className=\"item-over\"' onmouseout='this.className=\"item-out\"'>"+i+"</span>");
			}
			html = html.join("");
		}
		return html;
	}
})();

HTMLTime_InputCalendar.getMinutesSwitchHtml = (function(){
	var html;
	return function(){
		if(!html){
			html = [];
			for(var i=0;i<60;i++){
				html.push("<span id='mi' class='item-out' style='width:20px;' onmouseover='this.className=\"item-over\"' onmouseout='this.className=\"item-out\"'>"+i+"</span>");
			}
			html = html.join("");
		}
		return html;
	}
})();

HTMLTime_InputCalendar.RewriteTableStr = function(y, m) {
	var TArray = this.GetDateStr(y, m);
	var len = TArray.length;
	var temps = document.getElementsByTagName('td');
	var tds = []
	
	for ( var j = 0; j < temps.length; j++) {
		if (temps[j].getAttribute("cs"))
			tds.push(temps[j]);
	}
	temps = null;
	var now = new Date();
	for ( var i = 0; i < len; i++) {
		tds[i].innerHTML = TArray[i];
		tds[i].className = "CalTdOut";
		tds[i].cs = "CalTdOut";
		if (now.getYear() == y && now.getMonth() + 1 == m && now.getDate() == TArray[i]) {
			tds[i].className = "CalTdOver";
			tds[i].cs = "CalTdOver";
		}
	}
}

HTMLTime_InputCalendar.JumpToRun = function(action) {
	var yearTd = document.getElementById('YearTD');
	var monthTd = document.getElementById('MonthTD');
	var YearNO = parseInt(yearTd.value,10);
	var MonthNO = parseInt(monthTd.value,10);
	if (action == "b") {
		if (MonthNO == 1) {
			MonthNO = 13;
			YearNO = YearNO - 1;
		}
		MonthNO--;
	}
	if (action == "n") {
		if (MonthNO == 12) {
			MonthNO = 0;
			YearNO = YearNO + 1;
		}
		MonthNO++;
	}
	monthTd.value = MonthNO + " 月";
	yearTd.value = YearNO + " 年";
	this.RewriteTableStr(YearNO, MonthNO);
}

HTMLTime_InputCalendar.AlertDay = function(decText, e) {
	var event = e || window.event;
	var tar = event.target || event.srcElement;
	
	if(tar.tagName=="INPUT"){
		var tab = document.getElementById("kingoCalendarTable");
		for(var i=0;i<tab.rows.length;i++){
			for(var j=0;j<tab.rows[i].cells.length;j++){
				var cell = tab.rows[i].cells[j];
				if(cell.className=="CalTdOver"){
					tar = cell;
					break;
				}
			}
		}
	}
	
	var y,m,d,h,mi;
	y = this.appendZero(document.getElementById('YearTD').value);
	if(isNaN(parseInt(y,10))||parseInt(y,10)<=1585||parseInt(y,10)>=2255){
		y = new Date().getFullYear();
	}
	
	m = this.appendZero(document.getElementById('MonthTD').value);
	if(isNaN(parseInt(m,10))||parseInt(m,10)==0){
		m = this.appendZero(document.getElementById("MonthTD").getAttribute("temp"));
	}
	
	h = this.appendZero(document.getElementById("HourTD").value);
	if(isNaN(parseInt(h,10))){
		h = this.appendZero(document.getElementById("HourTD").getAttribute("temp"));
	}
	
	mi = this.appendZero(document.getElementById("MinuteTD").value);
	if(isNaN(parseInt(mi,10))){
		mi = this.appendZero(document.getElementById("MinuteTD").getAttribute("temp"));
	}
	
	if (tar.innerHTML.replace(/^\s$/, "") != '&nbsp;') {
		d = this.appendZero(tar.innerHTML||(new Date(y,m,0).getDate()));
		var tempValue = y+"-"+m+"-"+d+" "+h+":"+mi+":00";
		this.retCalendarValue(tempValue, decText);
		this.removeCalendar();
	}
}

HTMLTime_InputCalendar.inputOnkeypress = function(o, e){
	var code = e.keyCode||e.charCode;
	if(!((code>=48&&code<=57)||code==8)){
		HTMLTime_InputCalendar.stopPropagation(e);
	}
}
		
HTMLTime_InputCalendar.inputOnpaste	= function(o, e){
	HTMLTime_InputCalendar.stopPropagation(e);
}

HTMLTime_InputCalendar.stopPropagation = function(e){
	if (e.preventDefault) {
        e.preventDefault();
        e.stopPropagation();
    } else {
    	e.cancelBubble = true;
        e.returnValue = false;
    }
}
		
HTMLTime_InputCalendar.inputOnkeyup = function(o, e){
	var code = e.keyCode||e.charCode;
	
	if((code>=48&&code<=57)||(code>=96&&code<=105)){
		
		var v = o.value.replace(/[-\s:]*/g,"");
		var arr = v.split(/\B/);
		
		var cStyle = HTMLTime_InputCalendar.TheCalendarStyle[o.id];
		if(cStyle == 'time' || cStyle == 'begin-end-default') {
			arr = [0,0,0,0,0,0,0,0].concat(arr);
		}
		
		for(var i=4;i<=12;i++,i++){
			var maxValueOne = i==4?1:i==6?3:i==8?2:5;
			if(arr[i]&&parseInt(arr[i],10)>maxValueOne){
				arr.splice(i,0,0);
			}
			if(arr[i]&&arr[i+1]){
				var temp = 10*parseInt(arr[i],10)+parseInt(arr[i+1]);
				var maxValueTwo = i==4?12:i==6?31:i==8?23:59;
				if(temp>maxValueTwo){
					arr.splice(i,0,0);
				}
			}
		}
		
		v = arr.join("").substr(0,14);
		v = HTMLTime_InputCalendar.retStrByPstyle(o.id,HTMLTime_InputCalendar.formatString(v));
		o.value = v;
	}
	
	HTMLTime_InputCalendar.validateCalendarInput(o);
}

HTMLTime_InputCalendar.validateCalendarInput = function(o){
	if(o.value.length!=o.maxLength){
		o.style.color = "red";
	}else{
		var cStyle = HTMLTime_InputCalendar.TheCalendarStyle[o.id];
		if(cStyle == 'time' || cStyle == 'begin-end-default') {
			o.style.color = "";
		}else{
			var v = o.value.replace(/[-\s:]*/g,"");
			var year = parseInt(v.substr(0,4),10);
			if(year>1585&&year<2255){
				var month  = parseInt(v.substr(4,2),10);
				var maxDay = new Date(year,month,0).getDate();
				var day = parseInt(v.substr(6,2),10);
				if(day<=maxDay&&day!=0&&month!=0){
					o.style.color = "";
				}
			}
		}
	}
}

HTMLTime_InputCalendar.formatString = function(v){
	switch(v.length){
		case 5:
		case 6:
			v = v.substr(0,4)+"-"+v.substr(4);
		break;
		case 7:
		case 8:
			v = v.substr(0,4)+"-"+v.substr(4,2)+"-"+v.substr(6);
		break;
		case 9:
		case 10:
			v = v.substr(0,4)+"-"+v.substr(4,2)+"-"+v.substr(6,2)+" "+v.substr(8);
		break;
		case 11:
		case 12:
			v = v.substr(0,4)+"-"+v.substr(4,2)+"-"+v.substr(6,2)+" "+v.substr(8,2)+":"+v.substr(10);
		break;
		case 13:
		case 14:
			v = v.substr(0,4)+"-"+v.substr(4,2)+"-"+v.substr(6,2)+" "+v.substr(8,2)+":"+v.substr(10,2)+":"+v.substr(12);
		break;
	}
	return v;
}
		
HTMLTime_InputCalendar.inputOnblur = function(o, e){
	if(o.style.color=="red"){
		o.value = "";
		o.style.color="";
	}
}

HTMLTime_InputCalendar.createInputfield = (function(){
	var html = ["<input type='text' class='calendarInputFieldOut' name='",
				"",
				"' id='",
				"",
				"' style='width:",
				"",
				";' maxlength='",
				"",
				"' value='",
				"",
				"' temp='",
				"",
				"' units='",
				"",
				"' ",
				" onpaste=HTMLTime_InputCalendar.inputOnpaste(this,event)",
				" onkeyup=HTMLTime_InputCalendar.inputFieldOnkeyup(this,event)",
				" onfocus='this.select()'",
				" onmouseover='this.style.color=\"blue\"' onmouseout='this.style.color=\"\"' ",
				" onkeypress=HTMLTime_InputCalendar.inputOnkeypress(this,event)>"];
	
	var createInputHtml = function(id,value,size,maxLength,units){
		html[1] = html[3] =  id;
		html[5] = size;
		html[7] = maxLength;
		html[9] = html[11] = value;
		html[13] = units;
		return html;
	}
	
	return function(theID,value, size, maxLength,units){
		return createInputHtml(theID,value,size,maxLength,units).join("");
	}
})();

HTMLTime_InputCalendar.inputFieldOnkeyup = function(o,e){
	this.stopPropagation(e);
	
	var maxValueOne,maxValueTwo;
	if(o.id=="YearTD"){
		return;
	}else if(o.id=="MonthTD"){
		maxValueOne = 1;
		maxValueTwo = 12;
	}else if(o.id=="HourTD"){
		maxValueOne = 2;
		maxValueTwo = 23;
	}else if(o.id=="MinuteTD"){
		maxValueOne = 5;
		maxValueTwo = 59;
	}
	
	var v = (o.value).replace(/[-\s:]*/g,"");
	var arr = v.split(/\B/);
	
	if(maxValueOne&&maxValueTwo){
		if(arr[0]&&parseInt(arr[0],10)>maxValueOne){
			arr.splice(0,0,0);
		}
		if(arr[0]&&arr[1]){
			var temp = 10*parseInt(arr[0],10)+parseInt(arr[1]);
			if(temp>maxValueTwo){
				arr.splice(1,0,0);
			}
		}
	}
	o.value = arr.join("").substr(0,2);
}













function biDivideModulo(x, y)
{
	var nb = biNumBits(x);
	var tb = biNumBits(y);
	var origYIsNeg = y.isNeg;
	var q, r;
	if (nb < tb) {
		// |x| < |y|
		if (x.isNeg) {
			q = biCopy(bigOne);
			q.isNeg = !y.isNeg;
			x.isNeg = false;
			y.isNeg = false;
			r = biSubtract(y, x);
			// Restore signs, 'cause they're references.
			x.isNeg = true;
			y.isNeg = origYIsNeg;
		} else {
			q = new BigInt();
			r = biCopy(x);
		}
		return new Array(q, r);
	}
}


function biDivide(x, y)
{
	return biDivideModulo(x, y)[0];
}


function BigInt(flag)
{
	if (typeof flag == "boolean" && flag == true) {
		this.digits = null;
	}
	else {
		this.digits = ZERO_ARRAY.slice(0);
	}
	this.isNeg = false;
}

function BarrettMu(m)
{
	this.modulus = biCopy(m);
	this.k = biHighIndex(this.modulus) + 1;
	var b2k = new BigInt();
	b2k.digits[2 * this.k] = 1; // b2k = b^(2k)
	this.mu = biDivide(b2k, this.modulus);
	this.bkplus1 = new BigInt();
	this.bkplus1.digits[this.k + 1] = 1; // bkplus1 = b^(k+1)
	this.modulo = BarrettMu_modulo;
	this.multiplyMod = BarrettMu_multiplyMod;
	this.powMod = BarrettMu_powMod;
}

function RSAKeyPair(encryptionExponent, decryptionExponent, modulus)
{
	this.e = biFromHex(encryptionExponent);
	this.d = biFromHex(decryptionExponent);
	this.m = biFromHex(modulus);
	// We can do two bytes per digit, so
	// chunkSize = 2 * (number of digits in modulus - 1).
	// Since biHighIndex returns the high index, not the number of digits, 1 has
	// already been subtracted.
	this.chunkSize = 2 * biHighIndex(this.m);
	this.radix = 16;
	this.barrett = new BarrettMu(this.m);
}


var key = 'a932d703e092635b11ecc0c59e3eb0f0640c1090f844f644fe45524998aaedc8a10e184622c71def5574ef688ed68e5fbf752cb82cbf336e30a23ed107236fe55e21ebebc16f45899a3b0bdc2e630d8786e88e15289320f0c9c309ee416644858d83cf0e6b30ce5ddebd6e398a1ab79f005c72d763f6e803ea288d2f993864cd';
var passkey = new RSAKeyPair("10001","",key);  


console.log(encryptedString(passkey, "LKYs4690102"));
