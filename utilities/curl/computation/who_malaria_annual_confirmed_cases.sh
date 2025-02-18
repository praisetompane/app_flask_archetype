curl  -X POST --location 'http://localhost:8080/app_flask_quickstart/api/computation/' \
--header 'Content-Type: application/json' \
--data '
    {
        "etl_name": "Malaria Annual Confirmed Cases"
    }
'
