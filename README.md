# Keyvault2Json

## Run

```
python application.py
```

## Usage

Install script using install.bat/sh then run commands

**Import**

Create a flat json file with `{key: value}` and run

```
$env:AzSubscriptionId = '003f0bfc-4e27-4041-ae3b-9097f04393e9';
$env:AzKeyvaultName = "AZURE-KVT-1"
az account set --subscription $env:AzSubscriptionId
az login
py -3.7 -m keyvault2json import .\keyvault-input.json $env:AzKeyvaultName
```

**Export**

```
$env:AzSubscriptionId = '003f0bfc-4e27-4041-ae3b-9097f04393e9';
$env:AzKeyvaultName = "AZURE-KVT-1"
az account set --subscription $env:AzSubscriptionId
az login
py -3.7 -m keyvault2json export "$($env:AzKeyvaultName).json" $env:AzKeyvaultName
```


## Docker

**build**

```
docker build -t keyvault2json:0.0.1 . 
```

**run**

```
docker run --rm -it keyvault2json:0.0.1 application.py
```

## Testing

```
pytest --doctest-modules --rootdir=tests --cov-config=tests/.coveragerc --cov=keyvault2json tests/
```
