import os
import pytest

import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('pkg', [
    'nginx'
])
def test_packages(host, pkg):
    """ Test that fixture packages are intsalled. """
    package = host.package(pkg)

    assert package.is_installed


@pytest.mark.parametrize('svc', [
    'nginx'
])
def test_services(host, svc):
    """ Test that fixture services are running. """
    service = host.service(svc)

    assert service.is_running
    assert service.is_enabled


@pytest.mark.parametrize('cfg', [
    '/etc/nginx/conf.d/nginx.conf'
])
def test_configs(host, cfg):
    """ Test that configration file exists. """
    config = host.file(cfg)

    assert config.exists
