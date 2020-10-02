import argparse
import logging
import sys
from zvm_feilong_exporter.exporter import start_exporter

def main():
    argparser = argparse.ArgumentParser(description="zVM Exporter for Prometheus. Metrics are exported to localhost.")
    argparser.add_argument(
        "-c", "--config",
        help="Load configuration from an existing file")
    # argparser.add_argument(
    #     "-f", "--logfile",
    #     help="Output log file. If not provided, logs will not be output to "
    #             "file.")
    argparser.add_argument(
        "-p", "--port",
        help="Port on which to expose metrics. (defaults to 8009)",
        type=int,
        default='8009')
    argparser.add_argument(
        "--server",
        help="Address to the zVM SDK server. (port defaults to 8909)",
        required=True)
    argparser.add_argument(
        "--timeout",
        help="Wait timeout if request no response.",
        type=int,
        default=3600)
    argparser.add_argument(
        "--token",
        help="The path of token file.",
        required=True)
    argparser.add_argument(
        "--connection_type", 
        help="The connection can be 'socket' or 'rest'.",
        choices=['rest', 'sock'],
        default='rest'
    )
    argparser.add_argument(
        "--verify",
        help="Either a boolean, in which case it controls whether we verify the server's TLS certificate, or a string, in which case it must be a path to a CA bundle to use. Default to False.",
        action="store_true")
    argparser.add_argument(
        "--ssl_enabled",
        help="Whether SSL enabled or not. If enabled, use HTTPS instead of HTTP. The httpd server should enable SSL to support this.",
        action="store_true"
    )
    argparser.add_argument(
        "--cache",
        help="Enable cache for metrics, it will be refreshed after a specified number of seconds.",
        type=int,
        default=0
    )

    args = argparser.parse_args()
    ip, port = args.server.split(':')
    configfile = args.config
    if ip == None:
        logging.ERROR("Bad server address")

    start_exporter(prometheus_port=args.port, ip_addr=ip, 
                    port=int(port), timeout=args.timeout, token_path=args.token,
                    verify=args.verify, ssl_enabled=args.ssl_enabled, cache_duration=args.cache)


if __name__ == "__main__":
    sys.exit(main())