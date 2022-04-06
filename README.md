Its a API beta for check When will be it happen the some one satellite over country.
-----------------------

## DATASOURCES

- celestrak public site.
- reference document [TLE](https://gportal.jaxa.jp/gpr/assets/mng_upload/GCOM-C/TLE_en.pdf)
- using library [orbit predictor satellogic](https://github.com/satellogic/orbit-predictor)


## API

```
POST /api/v1/reload by token
GET /api/v1/sats by return list satettlites available
POST /api/v1/orbit by param country=ARG sat=ISS1

Example POST orbit will happend visible over country

HTTP/1.1 200 OK
Content-Length: 109
Content-Type: application/json
Date: We....
Server: ...

{
    "message": "It's visisble on ARG  Result:.... 1512 over ARG on 2022-04-07 03:41:...."
}


```

## CONFIG json

```
Inject json configuration

{
"app":{
    "port":8080,
    "provider_active_satellites":"https://www.celestrak.com/NORAD/elements/gp.php?GROUP=active&FORMAT=tle",
    "file_resource":"pathfile",
    "cmdb3937aafaa8971c0":"hash"
    }
}

```
## Building app

```
make build

docker run -p 8080:8080 -v $(pwd)/config/testing.json:/home/uapi/app/config/testing.json apiorbit:1.0.0

```