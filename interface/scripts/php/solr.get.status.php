<?php
$url = 'http://localhost:8983/solr/library/select?q=*:*';
$contents = file_get_contents($url);
$data = json_decode($contents, true);
var_dump($data)
?>
