import click
import json
import shutil

from azure.keyvault.secrets import SecretClient
from azure.identity import AzureCliCredential

def az_check():
    if not shutil.which("az"):
        print("Az not available")
        return False
    return True

def get_client(name):
    uri = f"https://{name}.vault.azure.net"

    credential = AzureCliCredential()
    client = SecretClient(vault_url=uri, credential=credential)
    return client

@click.group()
def cli():
    pass

@click.argument('name')
@click.argument('file')
@click.command(name='import')
def command_import(name, file):
    if not az_check():
        return

    with open(file, "r", encoding="utf-8") as fs:
        data = json.load(fs)

    client = get_client(name)
    for key, val in data.items():
        client.set_secret(key, val)
    
    print(f"Imported secrets from {file}")
    


@click.argument('name')
@click.argument('file')
@click.command(name='export')
def command_export(name, file):
    if not az_check():
        return

    client = get_client(name)

    secret_properties = client.list_properties_of_secrets()
    secret_data = dict()
    for secret_property in secret_properties:
        secret = client.get_secret(secret_property.name)
        secret_data.update({secret_property.name: secret.value})

    with open(file, "w", encoding="utf-8") as fs:
        json.dump(secret_data, fs, indent=4)

    print(f"Exported secrets to {file}")

cli.add_command(command_export)
cli.add_command(command_import)
cli()