<?php
echo "Test Script Starting\n\n\n\n";
require('functions.inc.php');

echo "Test 1 - Multiple Values\n";

$module_1 = "Module 1";
$module_2 = "Module 2";
$module_3 = "Module 3";
$module_4 = "Module 4";
$module_5 = "Module 5";
$mark_1 = "10";
$mark_2 = "20";
$mark_3 = "30";
$mark_4 = "40";
$mark_5 = "50";

$modules = array($module_1,$module_2,$module_3,$module_4,$module_5);
$marks = array($mark_1,$mark_2,$mark_3,$mark_4,$mark_5);

$max_min_modules = getMaxMin($modules, $marks);
$expect = array(
    "min_module" => "Module 1 - 10",
    "max_module" => "Module 5 - 50"
);

echo "Test Result: Min = '".$max_min_modules[1]."', Max = '".$max_min_modules[0]."' (Expected Min: '" . $expect["min_module"] . "', Expected Max: '" . $expect["max_module"] . "')\n";

if ($max_min_modules[1]==$expect["min_module"] && $max_min_modules[0]==$expect["max_module"])
{
    echo "Test Passed\n\n\n\n";
}
else
{
    echo "Test Failed\n";
}

echo "Test 2 - One Value\n\n\n\n";

$module_1 = "Module 1";
$mark_1 = "10";


$modules = array($module_1);
$marks = array($mark_1);

$max_min_modules = getMaxMin($modules, $marks);
$expect = array(
    "min_module" => "Module 1 - 10",
    "max_module" => "Module 1 - 10"
);

echo "Test Result: Min = '".$max_min_modules[1]."', Max = '".$max_min_modules[0]."' (Expected Min: '" . $expect["min_module"] . "', Expected Max: '" . $expect["max_module"] . "')\n";

if ($max_min_modules[1]==$expect["min_module"] && $max_min_modules[0]==$expect["max_module"])
{
    echo "Test Passed\n";
    exit(0); // exit code 0 - success
}
else
{
    echo "Test Failed\n";
    exit(1); // exit code not zero - error
}
