# curl -X POST "https://api.intelligence.io.solutions/api/r2r/v3/health"\
#      -H "Content-Type: application/json" \
#      -H "Authorization: Bearer io-v2-eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJvd25lciI6IjAzNzRhMjJjLTVmZTctNDBhNS04OGU4LTEwMjk3MGViMjEyNiIsImV4cCI6NDkwNTc2MTYyM30.F2HzmnMxRaHpRh2kfPRSgp7JHqtVb5BUmZD4kz1TxY28Usvyh18shHpNpvmncoE8S-IvZH3qlEEScNtO9j-5Dw" \


curl -X GET https://api.intelligence.io.solutions/api/r2r/v3/collections?offset=0&limit=10&name=Sample \
  -H "Authorization: Bearer io-v2-eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJvd25lciI6IjAzNzRhMjJjLTVmZTctNDBhNS04OGU4LTEwMjk3MGViMjEyNiIsImV4cCI6NDkwNTc2MTYyM30.F2HzmnMxRaHpRh2kfPRSgp7JHqtVb5BUmZD4kz1TxY28Usvyh18shHpNpvmncoE8S-IvZH3qlEEScNtO9j-5Dw"