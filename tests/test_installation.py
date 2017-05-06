"""
Role tests
"""

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_packages(host):
    """
    Check if packages are installed
    """

    packages = []

    if host.system_info.distribution == 'debian':
        packages = [
            'locales',
        ]
    elif host.system_info.distribution == 'ubuntu':
        packages = [
            'locales',
            'language-pack-fr',
        ]

    for package in packages:
        assert host.package(package).is_installed
