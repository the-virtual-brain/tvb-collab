# keycloak integration
import os
import sys
import warnings
from oauthenticator.generic import GenericOAuthenticator

c.JupyterHub.authenticator_class = GenericOAuthenticator
c.JupyterHub.services = [
    {
        'name': 'access-token-service',
        'admin': True,
        'url': 'http://127.0.0.1:8528' ,
        'command': [sys.executable, '/opt/app-root/configs/service.py'],
    }
   ]


c.GenericOAuthenticator.login_service = 'EBRAINS IAM'
c.GenericOAuthenticator.enable_auth_state = True
c.GenericOAuthenticator.refresh_pre_spawn = True
c.GenericOAuthenticator.token_url= "https://iam.ebrains.eu/auth/realms/hbp/protocol/openid-connect/token" 
c.GenericOAuthenticator.userdata_url= "https://iam.ebrains.eu/auth/realms/hbp/protocol/openid-connect/userinfo" 
c.GenericOAuthenticator.userdata_method= "GET"
c.GenericOAuthenticator.userdata_params= {'state': 'state'}
c.GenericOAuthenticator.username_key= "preferred_username"

if 'JUPYTERHUB_CRYPT_KEY' not in os.environ:
    warnings.warn(
        "Need JUPYTERHUB_CRYPT_KEY env for persistent auth_state.\n"
        "    export JUPYTERHUB_CRYPT_KEY=$(openssl rand -hex 32)"
    )
    c.CryptKeeper.keys = [ os.urandom(32) ]

c.OAuthenticator.client_id= "tvb-pipeline"
c.OAuthenticator.scope = ["openid email roles team offline_access profile group"]
c.OAuthenticator.client_secret= os.environ['KEYCLOAK_CLIENT_SECRET']


if 'APPLICATION_NAME' in os.environ:
    c.KubeSpawner.environment = { 'APPLICATION_NAME': os.environ["APPLICATION_NAME"] }
