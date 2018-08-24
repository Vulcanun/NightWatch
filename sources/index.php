<?php
	$data= $_SERVER['REQUEST_METHOD'] . ";" . $_SERVER['REMOTE_ADDR'] . ";";

	if(!is_dir("../logs/")) mkdir($dir);
	file_put_contents('../logs/accessTry.log', $data, "FILE_APPEND");
?>
