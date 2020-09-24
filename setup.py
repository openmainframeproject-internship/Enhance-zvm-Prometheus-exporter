from setuptools import setup, find_packages

setup(
    name = 'zvm_feilong_exporter',
    version = '0.0.1',
    author = 'Kai',
    author_email = 'kaiakx@yandex.com',
    description = 'Prometheus Exporter for z/VM Metrics, based on Feilong',
    long_description = 'Prometheus Exporter for z/VM Metrics, based on Feilong(zVMCloudConnector)',
    url = 'https://github.com/openmainframeproject-internship/Enhance-zvm-Prometheus-exporter/',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
    ],
        package_dir = {'': 'src'},
        packages = find_packages(where='src'),
        python_requires = '>=3.5, <4',
        entry_points = {
            'console_scripts': [
                'zvm_feilong_exporter = zvm_feilong_exporter.main:main'
            ]
        },
        install_requires = [
            'zVMCloudConnector',
            'prometheus_client',
            'flask',
        ],
)