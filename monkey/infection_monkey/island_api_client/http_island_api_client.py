import functools
import logging

import requests

from common import OperatingSystem
from common.common_consts.timeouts import LONG_REQUEST_TIMEOUT, MEDIUM_REQUEST_TIMEOUT

from . import (
    IIslandAPIClient,
    IslandAPIConnectionError,
    IslandAPIError,
    IslandAPIRequestError,
    IslandAPIRequestFailedError,
    IslandAPITimeoutError,
)

logger = logging.getLogger(__name__)


def handle_island_errors(fn):
    @functools.wraps(fn)
    def decorated(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except requests.exceptions.ConnectionError as err:
            raise IslandAPIConnectionError(err)
        except requests.exceptions.HTTPError as err:
            if 400 <= err.response.status_code < 500:
                raise IslandAPIRequestError(err)
            elif 500 <= err.response.status_code < 600:
                raise IslandAPIRequestFailedError(err)
            else:
                raise IslandAPIError(err)
        except TimeoutError as err:
            raise IslandAPITimeoutError(err)
        except Exception as err:
            raise IslandAPIError(err)

    return decorated


class HTTPIslandAPIClient(IIslandAPIClient):
    """
    A client for the Island's HTTP API
    """

    @handle_island_errors
    def __init__(self, island_server: str):
        response = requests.get(  # noqa: DUO123
            f"https://{island_server}/api?action=is-up",
            verify=False,
            timeout=MEDIUM_REQUEST_TIMEOUT,
        )
        response.raise_for_status()

        self._island_server = island_server
        self._api_url = f"https://{self._island_server}/api"

    @handle_island_errors
    def send_log(self, log_contents: str):
        response = requests.post(  # noqa: DUO123
            f"{self._api_url}/log",
            json=log_contents,
            verify=False,
            timeout=MEDIUM_REQUEST_TIMEOUT,
        )
        response.raise_for_status()

    @handle_island_errors
    def get_pba_file(self, filename: str):
        response = requests.get(  # noqa: DUO123
            f"{self._api_url}/pba/download/{filename}",
            verify=False,
            timeout=LONG_REQUEST_TIMEOUT,
        )
        response.raise_for_status()

        return response.content

    @handle_island_errors
    def get_agent_binary(self, operating_system: OperatingSystem):
        os_name = operating_system.value
        response = requests.get(  # noqa: DUO123
            f"{self._api_url}/agent-binaries/{os_name}",
            verify=False,
            timeout=MEDIUM_REQUEST_TIMEOUT,
        )
        response.raise_for_status()

        return response.content
