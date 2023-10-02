$params = @{
    key = 'd35AFvCPEXATL7kNnjz6CD6r20KR9qh5q1L9nZ6bk5k='
    }
$response = Invoke-WebRequest -Uri 'http://127.0.0.1:8000/get-system-log' -Body $params -Method Get
$test = $response.RawContent
Write-Host $test