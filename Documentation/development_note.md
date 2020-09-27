# For Developer
0. `git clone https://github.com/kaiakz/feilong_exporter.git && cd Enhance-zvm-Prometheus-exporter/src`
1. `virtualenv venv`
2. `source venv/bin/activate`
3. `pip install zVMCloudConnector`
4. `pip install prometheus_client`
5. `pip install flask`
6. `python zvm_feilong_exporter/main.py --server 127.0.0.1:8909 --token tests/faketoken.txt` or `venv/bin/python3 main.py --server 127.0.0.1:8909 --token tests/faketoken.txt`

# Publish with TestPyPI
0. `git clone https://github.com/kaiakz/feilong_exporter.git && cd Enhance-zvm-Prometheus-exporter/`
1. `python setup.py sdist bdist_wheel`
2. `pip install zvm_feilong_exporter-*.tar.gz`(test on local)
3. `twine upload --skip-existing --repository-url https://test.pypi.org/legacy/ dist/*` (Upload to TestPyPI)

**TEST ONLY** If you don't have a zvm-sdk server, use the mock server instead. 
# zvm-sdk mocking server
## Usage
1. `cd src`
2. `source venv/bin/activate`
3. `python ./tests/mock_server.py`