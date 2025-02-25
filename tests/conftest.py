import os
import random
import signal
import socket
import subprocess
import sys
import time

from subprocess import Popen, PIPE
from threading import Thread

import pytest

from requests import Session
from burdock.restclient.rest_client import RestClient

# Add the utils directory to the path
root_url = subprocess.check_output("git rev-parse --show-toplevel".split(" ")).decode("utf-8").strip()
sys.path.append(os.path.join(root_url, "utils"))

from service_utils import run_app  # NOQA


@pytest.fixture(scope="session")
def client():
    port = int(os.environ.get("BURDOCK_SERVICE_PORT", 5000))

    class Credentials():
        def signed_session(self, session=None):
            return session if session is not None else Session()

    base_url = "http://localhost:{}/api/".format(port)
    client = RestClient(Credentials(), base_url)
    return client
