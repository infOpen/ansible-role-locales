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

# Files management
locales_config_file_dest: "{{ _locales_config_file_dest }}"
locales_gen_file_dest: "{{ _locales_gen_file_dest }}"
locales_update_command: "{{ _locales_update_command }}"
locales_config_file_owner: 'root'
locales_config_file_group: 'root'
locales_config_file_mode: '0644'
locales_gen_file_owner: 'root'
locales_gen_file_group: 'root'
locales_gen_file_mode: '0644'

# Locales management
locales_to_configure:
  - 'fr_FR.UTF-8 UTF-8'
locales_default_lang: 'fr_FR.UTF-8'
locales_default_timezone: 'Europe/Paris'
```

### Debian family role variables

``` yaml
# Configuration files path
_locales_config_file_dest: '/etc/default/locale'
_locales_gen_file_dest: '/etc/locale.gen'

# Locale update command
_locales_update_command: '/usr/sbin/update-locale'
```

### Debian OS role variables

``` yaml
_locales_packages:
  - 'locales'
```

### Ubuntu OS role variables

``` yaml
_locales_packages:
  - 'locales'
  - 'language-pack-fr'
```

## Dependencies

None

## Example Playbook

    - hosts: servers
      roles:
         - { role: infOpen.locales }

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro

