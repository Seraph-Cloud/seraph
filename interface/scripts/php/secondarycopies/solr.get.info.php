<?php
$url = 'http://localhost:8983/solr/library/select?q=jesus+christ&wt=json&hl=on&hl.fl=*&fl=id,name&group=true&group.field=content&hl=on&hl.fl=*&hl.encoder=html&hl.fragmenter=regex&hl.regex.slop=1.0&hl.fl=text_*&hl.usePhraseHighlighter=true&hl.bs.type=WHOLE&hl.defaultSummary=true&hl.offsetSource=POSTINGS&hl.fragsize=125000&hl.maxAnalyzedChars=25000&hl.highlightMultiTerm=true&hl.tag.pre=<b>&hl.tag.post=</b>&results=50';
$contents = file_get_contents($url);
$data = json_decode($contents, true);
$docs = $data['response']['content']['id'];
var_dump($data);
$file = "json.txt";
fwrite($file, $docs);
fclose($file);
?>


