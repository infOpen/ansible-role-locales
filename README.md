locales
=======

[![Build Status](https://travis-ci.org/infOpen/ansible-role-locales.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-locales)

Install locales package.

Requirements
------------

This role requires Ansible 1.4 or higher, and platform requirements are listed
in the metadata file.

Role Variables
--------------

Default role variables


    locales_to_configure :
      - "fr_FR.UTF-8 UTF-8"

    locales_default_lang : "fr_FR.UTF-8"

    locales_default_timezone : "Europe/Paris"

    locales_config_file_owner : "root"
    locales_config_file_group : "root"
    locales_config_file_mode  : "0644"

    locales_gen_file_owner : "root"
    locales_gen_file_group : "root"
    locales_gen_file_mode  : "0644"


# Default Debian vars

    locales_packages :
      - locales
      - language-pack-fr

    locales_config_file_dest : "/etc/default/locale"
    locales_gen_file_dest    : "/etc/locale.gen"


    locales_update_command : "/usr/sbin/update-locale"


Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
        - { role: achaussier.locales }

License
-------

MIT

Author Information
------------------

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
