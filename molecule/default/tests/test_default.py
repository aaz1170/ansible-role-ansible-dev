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


def test_venv_is_created(host):
    venv = host.file('/home/vagrant/.venv-ansible/bin/activate')
    assert venv.exists
    assert venv.user == 'vagrant'
    assert venv.group == 'vagrant'


def test_ansible_is_installed_in_venv(host):
    packages = host.pip_package.get_packages(pip_path='/home/vagrant/.venv-ansible/bin/pip')
    assert packages["ansible"]
    assert packages["molecule"]
    
