<?php
$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, "http://www.mysite.com/test");
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, "postvar1=value1&postvar2=value2&postvar3=value3");

curl_exec ($ch);
curl_close ($ch);

?>
