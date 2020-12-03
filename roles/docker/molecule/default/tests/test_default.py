import os
import pytest

import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('pkg', [
    'docker'
])
def test_packages(host, pkg):
    """ Verifies that fixture packages are installed. """
    package = host.package(pkg)

    assert package is_installed


@pytest.mark.parametrize('svc', [
    'docker'
])
def test_services(host, svc):
    """ Test that fixture services are running. """
    service = host.service(svc)

    assert service.is_running
    assert service.is_enabled
