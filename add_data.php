<?php
	include("connect.php");
$SQL = "INSERT INTO LoggedInfodb.tbl_Probes(MAC_Address, SSID, Location, Time) VALUES ('".$_GET["MAC"]."','".$_GET["SSID"]."','".$_GET["Location"]."','".$_GET["Time"]."')";

mysql_query($SQL);
?>
