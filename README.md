---
page_type: sample
description: "This is a minimal sample app that demonstrates how to run a Python Flask application on Azure App Service on Linux."
languages:
- python
products:
- azure
- azure-app-service
---

# Python Flask sample for Azure App Service (Linux)

This is a minimal sample app that demonstrates how to run a Python Flask application on Azure App Service on Linux.

For more information, please see the [Python on App Service quickstart](https://docs.microsoft.com/azure/app-service/containers/quickstart-python).

## Notes
* Please note this function will not work properly without an Azure identity assigned. This can be done in the Azure Portal in the [Settings, Identity pane of the App Service](https://docs.microsoft.com/en-us/azure/app-service/overview-managed-identity?tabs=dotnet), or with az CLI.
* Please note this function will not work properly without the HashiCorp Vault address and namespace in the app config. This can be done in the Azure Portal in the Settings, Configuration pane of the App Service, or with az CLI. Create an application setting named `VAULT_ADDR` with the address of your Vault instance, and an application setting named `VAULT_NAMESPACE` with the namespace you are using.
* This function attempts to read a secret from a kv v2 mount located at secret/foo, and renders the value of the key named `key`.