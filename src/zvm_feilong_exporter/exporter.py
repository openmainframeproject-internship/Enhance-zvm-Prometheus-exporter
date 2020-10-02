import json
from prometheus_client import start_http_server
from prometheus_client.core import REGISTRY
import logging
import time

from zvm_feilong_exporter.collector import ZVMCollector

# Export them to Prometheus
def start_exporter(prometheus_port: int=8009, ip_addr: str=None, port: int=None, timeout: int=3600,
                 connection_type: str=None, ssl_enabled: bool=False, verify: bool=False,
                 token_path: str=None, cache_duration:int=0):
    try:
        REGISTRY.register(ZVMCollector(ip_addr=ip_addr, port=port, timeout=timeout, 
                            connection_type=connection_type, ssl_enabled=ssl_enabled, 
                            verify=verify, token_path=token_path, cache_duration=cache_duration))     # TODO
        start_http_server(prometheus_port)
        while True:
            time.sleep(1)      
    except AttributeError as e:
        logging.error("Exporter Error:", e)
