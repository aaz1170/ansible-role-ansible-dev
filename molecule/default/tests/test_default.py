import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

def test_dependency_docker_is_appliyed(host):
    assert host.package("docker-ce").is_installed
    assert host.service("docker").is_running

def test_packages_are_installed(host):
    packageList = [
        "python3-pip",
        "python3-venv",
        "libssl-dev",
        "python3-docker"
    ]
    for item in packageList:
        assert host.package(item).is_installed

def test_ansible_is_pinned_for_apt(host):
    cmd = host.run('sudo apt install ansible')
    assert "E: Package 'ansible' has no installation candidate" in cmd.stderr
    assert cmd.rc == 100
