from pathlib import Path
from os import getenv


_conf_folder = f"/configurations/{getenv('EP_APP')}-s3"
is_deploy = Path(_conf_folder).exists()

_params_keys = ["accesskey", "secretkey", "endpoint_url", "bucket_name"]

def _get_key_value(key):
    if (is_deploy):
        return Path(f'{_conf_folder}/{key}').read_text()
    else:
        envvar_name = f'MINIO_{key.upper()}'
        return getenv(envvar_name, '')

params = { k: _get_key_value(k) for k in _params_keys }