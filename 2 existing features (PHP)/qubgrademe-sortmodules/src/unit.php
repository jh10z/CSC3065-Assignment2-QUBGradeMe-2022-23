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

$modules = array($module_1,$module_5);
$marks = array($mark_1,$mark_5);

$sorted_modules=getSortedModules($modules, $marks);
$expect = array(
    "50",
    "10"
);

echo "Test Result: Sorted Order = '" . $sorted_modules[0]["marks"] . ", " . $sorted_modules[1]["marks"] ."' (Expected Min: '" . $expect[0] . " " .$expect[1] . "')\n";

if ($sorted_modules[0]["marks"] == $expect[0] && $sorted_modules[1]["marks"] == $expect[1])
{
    echo "Test Passed\n\n\n\n";
}
else
{
    echo "Test Failed\n\n\n\n";
}

echo "Test 2 - One Value";

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

$modules = array($module_1);
$marks = array($mark_1);

$sorted_modules=getSortedModules($modules, $marks);
$expect = array(
    "10"
);

echo "Test Result: Sorted Order = '" . $sorted_modules[0]["marks"] ."' (Expected Min: '" . $expect[0] . "')\n";

if ($sorted_modules[0]["marks"] == $expect[0])
{
    echo "Test Passed\n\n\n\n";
    exit(0); // exit code 0 - success
}
else
{
    echo "Test Failed\n\n\n\n";
    exit(1); // exit code 1 - failure
}