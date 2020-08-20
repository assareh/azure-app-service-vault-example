# Secrets Retrieval in Microsoft Azure App Service from HashiCorp Vault

This is a minimal sample app that demonstrates how to retrieve secrets from HashiCorp Vault from a Python Flask application on Azure App Service on Linux.

The app attempts to read a secret from a kv v2 mount located at secret/foo, and renders the value of the key named `key`.

To run this code, please follow the [Python on App Service quickstart](https://docs.microsoft.com/azure/app-service/containers/quickstart-python).

## Requirements
* An Azure identity must be assigned. This can be done in the Azure Portal in the [Settings, Identity pane of the App Service](https://docs.microsoft.com/en-us/azure/app-service/overview-managed-identity?tabs=dotnet), or with az CLI.
* The app config must contain the HashiCorp Vault address and namespace. This can be done in the Azure Portal in the Settings, Configuration pane of the App Service, or with az CLI. Create an application setting named `VAULT_ADDR` with the address of your Vault instance, and an application setting named `VAULT_NAMESPACE` with the namespace you are using.
