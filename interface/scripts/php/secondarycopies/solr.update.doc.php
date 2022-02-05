<?php
$json_doc = json_encode($new_docs); //convert the array to a json string

$curl = curl_init();

curl_setopt_array($curl, array(
    CURLOPT_RETURNTRANSFER => 1, //curl will return something instead of directly outputting
    CURLOPT_HTTPHEADER => array("Content-type:application/json"), //specify content type as json
    CURLOPT_URL => 'http://localhost:8080/solr/library/update/json', //the request url
    CURLOPT_POST => 1, //set the request type to POST
    CURLOPT_POSTFIELDS => $json_doc, //the data that we want to pass in
));

curl_exec($curl); //execute, you can assign a variable to this to check if the request suceeded or not
curl_close($curl);
?>
