<?php
header("Access-Control-Allow-Origin: *");
header("Content-type: application/json");
require('functions.inc.php');

$output = array(
	"error" => false,
  "modules" => "",
	"marks" => 0,
	"max_module" => "",
	"min_module" => ""
);

$error = array(
	"message" => ""
);

$module_1 = $_REQUEST['module_1'];
$module_2 = $_REQUEST['module_2'];
$module_3 = $_REQUEST['module_3'];
$module_4 = $_REQUEST['module_4'];
$module_5 = $_REQUEST['module_5'];
$mark_1 = $_REQUEST['mark_1'];
$mark_2 = $_REQUEST['mark_2'];
$mark_3 = $_REQUEST['mark_3'];
$mark_4 = $_REQUEST['mark_4'];
$mark_5 = $_REQUEST['mark_5'];

$modules = array($module_1,$module_2,$module_3,$module_4,$module_5);
$marks = array($mark_1,$mark_2,$mark_3,$mark_4,$mark_5);

//Type Conversion Error
for ($i = 0; $i < count($marks); $i++) {
	if(!is_numeric($marks[$i]) && !empty($marks[$i])) {
		$error['message'] .= "Module " . ($i + 1) . " is not a number. \n";
		$output['error'] = true;
	}
}

if($output['error'] === true) {
	http_response_code(400);
	echo json_encode($error);
	exit();
}

//Input Validation (0-100)
for ($i = 0; $i < count($marks); $i++) {
	if($marks[$i] < 0 || $marks[$i] > 100) {
		$error['message'] .= "Module " . ($i + 1) . " value must be between 0 and 100. \n";
		$output['error'] = true;
	}
}

if($output['error'] === true) {
	http_response_code(400);
	echo json_encode($error);
	exit();
}

$max_min_modules = getMaxMin($modules, $marks);

//No Marks Provided Error
if(is_null($max_min_modules)) {
	http_response_code(400);
	$error['message'] = "Error: To use functionality, please enter at least one mark.";
	echo json_encode($error);
	exit();
}

$output['marks']=$marks;
$output['max_module']=$max_min_modules[0];
$output['min_module']=$max_min_modules[1];

echo json_encode($output);
exit();
