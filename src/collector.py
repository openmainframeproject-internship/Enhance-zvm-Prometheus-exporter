import json
from zvmconnector.connector import ZVMConnector
from prometheus_client.core import GaugeMetricFamily

# collect the infomation from sdk server
class ZVMCollector(ZVMConnector):
    def __init__(self, ip_addr: str=None, port: int=None, timeout: int=3600,
                 connection_type: str=None, ssl_enabled: bool=False, verify: bool=False,
                 token_path: bool=None):
        super().__init__(ip_addr=ip_addr, port=port, timeout=timeout,
                        connection_type=connection_type, ssl_enabled=ssl_enabled,
                        verify=verify, token_path=token_path)

    def collect(self):
        pass