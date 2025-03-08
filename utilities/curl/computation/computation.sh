curl  -X POST --location 'http://localhost:8080/app_flask_archetype/api/computation/' \
--header 'Content-Type: application/json' \
--data '
    {
        "input": "input"
    }
'
