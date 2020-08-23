import os
import hvac
import requests
from flask import Flask

app = Flask(__name__)
identity_endpoint = os.environ["IDENTITY_ENDPOINT"]
identity_header = os.environ["IDENTITY_HEADER"]
vault_address = os.environ["VAULT_ADDR"]
vault_namespace = os.environ["VAULT_NAMESPACE"]
RESOURCE_URL = "https://management.azure.com/"


def get_bearer_token(resource_uri):
    token_auth_uri = f"{identity_endpoint}?resource={resource_uri}& \
                       api-version=2019-08-01"
    head_msi = {'X-IDENTITY-HEADER': identity_header}

    resp = requests.get(token_auth_uri, headers=head_msi)
    access_token = resp.json()['access_token']

    return access_token


def run_example():
    jwt = get_bearer_token(RESOURCE_URL)

    client = hvac.Client(
        url=vault_address,
        namespace=vault_namespace,
    )

    client.auth_kubernetes(  # intentional hvac misuse \
                             # since python hvac jwt method incomplete
        mount_point='jwt',
        role='appsvc',
        jwt=jwt,
    )

    vault_read_response = client.secrets.kv.v2.read_secret_version(
                          mount_point='secret', path='foo')
    return vault_read_response['data']['data']['key']


@app.route('/')
def hello_world():
    try:
        return run_example()
    except Exception as err:
        return str(err)


@app.route('/ping')
def ping():
    return "Hello world"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
