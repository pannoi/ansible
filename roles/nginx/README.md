Role Name
=========

Role installs nginx and starts service + copying config from templates

Requirements
------------

missing...

Role Variables
--------------

```yaml
nginx_yum_repo_enabled: true
nginx_service_state: started
nginx_service_enabled: true
nginx_package_name: nginx
nginx_service_name: nginx
nginx_config_template: nginx.conf
nginx_conf_path: /etc/nginx/conf.d
```

Dependencies
------------

missing...

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

@pannoi
