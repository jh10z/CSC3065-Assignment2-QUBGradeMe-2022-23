<?php
declare(strict_types=1);
require('functions.inc.php');
use PHPUnit\Framework\TestCase;

final class integration extends TestCase
{
    public function testWithValidRequest(): void
    {
        $expectedOutput = '{"error":false,"modules":"","marks":["10","","","",""],"max_module":"Module 1 - 10","min_module":"Module 1 - 10"}';
        $curl = curl_init("http://40259391.proxy.qpc.hal.davecutting.uk/service/MaxMin?module_1=Module%201&mark_1=10&module_2=Module%202&mark_2=&module_3=Module%203&mark_3=&module_4=Module%204&mark_4=&module_5=Module%205&mark_5=");
        curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);

        $output = curl_exec($curl);
        print(gettype($output));
        $code = curl_getinfo($curl, CURLINFO_HTTP_CODE);

        curl_close($curl);

        $this->assertEquals(
            200,
            $code
        );
        $this->assertEquals(
            $expectedOutput,
            $output
        );
    }

    public function testWithNonNumber(): void
    {
        $expectedOutput = '{"message":"Module 1 is not a number. \n"}';
        $curl = curl_init("http://40259391.proxy.qpc.hal.davecutting.uk/service/MaxMin?module_1=Module%201&mark_1=ee&module_2=Module%202&mark_2=&module_3=Module%203&mark_3=&module_4=Module%204&mark_4=&module_5=Module%205&mark_5=");
        curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);

        $output = curl_exec($curl);
        print(gettype($output));
        $code = curl_getinfo($curl, CURLINFO_HTTP_CODE);

        curl_close($curl);

        $this->assertEquals(
            400,
            $code
        );
        $this->assertEquals(
            $expectedOutput,
            $output
        );
    }

    public function testWithOutOfBoundsUpperEdgeNumber(): void
    {
        $expectedOutput = '{"message":"Module 1 value must be between 0 and 100. \n"}';
        $curl = curl_init("http://40259391.proxy.qpc.hal.davecutting.uk/service/MaxMin?module_1=Module%201&mark_1=101&module_2=Module%202&mark_2=&module_3=Module%203&mark_3=&module_4=Module%204&mark_4=&module_5=Module%205&mark_5=");
        curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);

        $output = curl_exec($curl);
        print(gettype($output));
        $code = curl_getinfo($curl, CURLINFO_HTTP_CODE);

        curl_close($curl);

        $this->assertEquals(
            400,
            $code
        );
        $this->assertEquals(
            $expectedOutput,
            $output
        );
    }

    public function testWithOutOfBoundsLowerEdgeNumber(): void
    {
        $expectedOutput = '{"message":"Module 1 value must be between 0 and 100. \n"}';
        $curl = curl_init("http://40259391.proxy.qpc.hal.davecutting.uk/service/MaxMin?module_1=Module%201&mark_1=-1&module_2=Module%202&mark_2=&module_3=Module%203&mark_3=&module_4=Module%204&mark_4=&module_5=Module%205&mark_5=");
        curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);

        $output = curl_exec($curl);
        print(gettype($output));
        $code = curl_getinfo($curl, CURLINFO_HTTP_CODE);

        curl_close($curl);

        $this->assertEquals(
            400,
            $code
        );
        $this->assertEquals(
            $expectedOutput,
            $output
        );
    }

    public function testWithInBoundsUpperEdgeNumber(): void
    {
        $expectedOutput = '{"error":false,"modules":"","marks":["100","","","",""],"max_module":"Module 1 - 100","min_module":"Module 1 - 100"}';
        $curl = curl_init("http://40259391.proxy.qpc.hal.davecutting.uk/service/MaxMin?module_1=Module%201&mark_1=100&module_2=Module%202&mark_2=&module_3=Module%203&mark_3=&module_4=Module%204&mark_4=&module_5=Module%205&mark_5=");
        curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);

        $output = curl_exec($curl);
        print(gettype($output));
        $code = curl_getinfo($curl, CURLINFO_HTTP_CODE);

        curl_close($curl);

        $this->assertEquals(
            200,
            $code
        );
        $this->assertEquals(
            $expectedOutput,
            $output
        );
    }

    public function testWithInBoundsLowerEdgeNumber(): void
    {
        $expectedOutput = '{"error":false,"modules":"","marks":["0","","","",""],"max_module":"Module 1 - 0","min_module":"Module 1 - 0"}';
        $curl = curl_init("http://40259391.proxy.qpc.hal.davecutting.uk/service/MaxMin?module_1=Module%201&mark_1=0&module_2=Module%202&mark_2=&module_3=Module%203&mark_3=&module_4=Module%204&mark_4=&module_5=Module%205&mark_5=");
        curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);

        $output = curl_exec($curl);
        print(gettype($output));
        $code = curl_getinfo($curl, CURLINFO_HTTP_CODE);

        curl_close($curl);

        $this->assertEquals(
            200,
            $code
        );
        $this->assertEquals(
            $expectedOutput,
            $output
        );
    }

    public function testWithNoValues(): void
    {
        $expectedOutput = '{"message":"Error: To use functionality, please enter at least one mark."}';
        $curl = curl_init("http://40259391.proxy.qpc.hal.davecutting.uk/service/MaxMin?module_1=Module%201&mark_1=&module_2=Module%202&mark_2=&module_3=Module%203&mark_3=&module_4=Module%204&mark_4=&module_5=Module%205&mark_5=");
        curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);

        $output = curl_exec($curl);
        print(gettype($output));
        $code = curl_getinfo($curl, CURLINFO_HTTP_CODE);

        curl_close($curl);

        $this->assertEquals(
            400,
            $code
        );
        $this->assertEquals(
            $expectedOutput,
            $output
        );
    }
}
