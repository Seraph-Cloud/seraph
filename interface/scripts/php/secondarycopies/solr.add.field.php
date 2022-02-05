<?php
$new_docs = array();
foreach($docs as $d){
  $id = $d['id'];
  $course = get_course($id);
  $d['course'] = $course;
  unset($d['_version_']);

  $new_docs[] = $d;
}
?>
