<?php
//commit the changes
$curl = curl_init();
curl_setopt_array($curl, array(
  CURLOPT_URL => 'http://localhost:8983/solr/library/update?commit=true'
));

curl_exec($curl);
?>
