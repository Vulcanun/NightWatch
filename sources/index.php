<?php

	$data= $_SERVER['REQUEST_METHOD'] . ";" . $_SERVER['REMOTE_ADDR'] . ";";
	file_put_contents('../logs/accessTry.log', $data, "FILE_APPEND");

?>