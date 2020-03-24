Role Name
=========

This role prepares a Debian/Ubuntu host to develop Ansible roles with molecule.

It installes the required Debian Packages, but not Ansible. The
ansible Package is instead blocked for apt. The role creates virtual
Python environments for each listed developer. Inside these virtual
environments, ansible and molecule are installed as pip packages.

Requirements
------------

In order to provision test instances with molecule, you need one of the
supported drivers (see
https://molecule.readthedocs.io/en/latest/configuration.html#driver).
You may need to install Docker, Vagrant, Virtualbox or something alike.

Role Variables
--------------

This role requires two variables to be defined:
- a list of developers (i.e. _usernames_). These have to exist on the target host,
- a dictionary with the ansible and molecule pip version.

<p></p>

    developers:
      - janedoe
    pip_versions:
      ansible: "2.8.0"
      molecule: "2.20"

If the development host needs to use a proxy, you can optionally configure it for pip:

<p></p>

    proxy_env:
      HTTP_PROXY: "http://<HostnameOrIp>:<PortIfNeeded>/"
      HTTPS_PROXY: "https://<HostnameOrIp>:<PortIfNeeded>/"

Setting this variable also causes the role to copy a _pip.config_ file into
the venv. It configures pip to ignore TLS cert errors when accessing the pip
repositories (see _files/pip.config_)

Dependencies
------------

This role has no dependecies. But using other roles (like _docker_) may be
useful.

Example Playbook
----------------

    - hosts: ansible-dev-hosts
      tasks:
        - include_role: 
            name: aaz1170.ansible-dev

License
-------

BSD

Author Information
------------------

This role was created in 2020 by aaz1170
