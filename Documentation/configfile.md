## Decription
The exporter can support multi Feilong SDK servers via a configuration file. To specify which configuration file to load, use `--config-from` flag. The configuration controls each servers' authentication, address/port, access and so on.

The file is written in [INI-like format](https://docs.python.org/3/library/configparser.html#supported-ini-file-structure).

## Configuration Format
The file consists of servers and parameters. A server begins with the name of the server in square brackets and continues untils the next module begins. Servers contain parameters of the form `name = value` or `name : value`. Comments are prefixed by specific characters (`#` and `;` by default).

For example:
```ini
[feilong-server1]
ip_addr = 127.0.0.1
port = 8909
token_path = yourtokenfile
timeout = 3600  # optional, int
verify = true   # optional, boolean
ssl_enable = true   # optional, boolean
```