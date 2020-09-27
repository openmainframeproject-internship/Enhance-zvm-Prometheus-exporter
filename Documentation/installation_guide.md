## Requirement
The zvm exporter uses these libraries:
* Feilong/zvmconnector
* Prometheus client_python
* Flask

### Tested on:
OS: Linux 4.19.144-1-MANJARO, 
Python: 3.8, 
Pip: 20.1.1

## Use PIP
`pip install --extra-index-url https://test.pypi.org/simple/ zvm-feilong-exporter` 
(**NOTICE** TestPyPI is unstable)

## Prometheus
Install prometheus first, then add the following lines to the `prometheus.yaml`:
```yaml
  - job_name: 'zvm'
    static_configs
    - targets: ['localhost:8009']
```