# locales

[![Build Status](https://travis-ci.org/infOpen/ansible-role-locales.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-locales)

Install locales package.

## Requirements

This role requires Ansible 2.0 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Locally, you can run tests on Docker (default driver) or Vagrant.
Travis run tests using Docker driver only.

Currently, tests are done on:
- Debian Jessie
- Ubuntu Trusty
- Ubuntu Xenial

and use:
- Ansible 2.0.x
- Ansible 2.1.x
- Ansible 2.2.x
- Ansible 2.3.x

### Running tests

#### Using Docker driver

```
$ tox
```

#### Using Vagrant driver

```
$ MOLECULE_DRIVER=vagrant tox
```

## Role Variables

### Default role variables

``` yaml
# Packages management
locales_packages: "{{ _locales_packages }}"
locales_language_packs_packages: "{{ _locales_language_packs_packages | default([]) }}"
locales_repositories_cache_valid_time: 3600

# Files management
locales_config_file_dest: "{{ _locales_config_file_dest }}"
locales_gen_file_dest: "{{ _locales_gen_file_dest }}"
locales_update_command: "{{ _locales_update_command }}"
locales_config_file_owner: 'root'
locales_config_file_group: 'root'
locales_config_file_mode: '0644'

# Locales management
locales_to_configure:
  - name: 'en_US.UTF-8'
    modifier: 'UTF-8'
locales_defaults:
  LANG: 'en_US.UTF-8'
  LANGUAGE: 'en_US.UTF-8'
  LC_CTYPE: '"en_US.UTF-8"'
  LC_NUMERIC: '"en_US.UTF-8"'
  LC_TIME: '"en_US.UTF-8"'
  LC_COLLATE: '"en_US.UTF-8"'
  LC_MONETARY: '"en_US.UTF-8"'
  LC_MESSAGES: '"en_US.UTF-8"'
  LC_PAPER: '"en_US.UTF-8"'
  LC_NAME: '"en_US.UTF-8"'
  LC_ADDRESS: '"en_US.UTF-8"'
  LC_TELEPHONE: '"en_US.UTF-8"'
  LC_MEASUREMENT: '"en_US.UTF-8"'
  LC_IDENTIFICATION: '"en_US.UTF-8"'
  LC_ALL: 'en_US.UTF-8'
```

### Debian family role variables

``` yaml
# Packages
_locales_packages:
  - name: 'locales'

# Configuration files path
_locales_config_file_dest: '/etc/default/locale'
_locales_gen_file_dest: '/etc/locale.gen'

# Locale update command
_locales_update_command: '/usr/sbin/update-locale'
```

### Ubuntu OS role variables

``` yaml
locales_language_packs_packages:
  - name: 'language-pack-en'
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: infOpen.locales }
```

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
