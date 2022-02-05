<?php
$ch = curl_init();
$query = "JESUS CHRIST!!!";
$encode = urlencode($query);
curl_setopt($ch, CURLOPT_URL, "http://10.1.1.37:8983/solr/library/select?q=".$encode."&wt=php&indent=true&start=0q=god&wt=json&indent=true&fl=id,name,content&group=true&group.field=content&hl=on&hl.fl=*&hl.encoder=html&hl.fragmenter=regex&hl.regex.slop=1.0&hl.fl=text_*&hl.usePhraseHighlighter=true&hl.bs.type=WHOLE&hl.defaultSummary=true&hl.offsetSource=POSTINGS&hl.fragsize=125000&hl.maxAnalyzedChars=25000&hl.highlightMultiTerm=true&hl.tag.pre=<b>&hl.tag.post=</b>&results=50");
curl_setopt($ch, CURLOPT_HEADER, false);
curl_setopt ($ch, CURLOPT_RETURNTRANSFER, true);
$re = curl_exec($ch); curl_close($ch);
$arr; eval("\$arr = " . $re . ";");
echo "Found " . $arr['response']['numFound'] . " results\n";
foreach($arr['response']['docs'] as $item) {
    echo "title is : " . $item['name']. "\n"; }
 ?>
