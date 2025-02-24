# selfhosted.nginx

Installs [nginx-proxy-manager](https://github.com/NginxProxyManager/nginx-proxy-manager) - a Docker container for managing Nginx proxy hosts with a simple, powerful interface.

[!NOTE]
> The role is tested to run on a bridge network.
> Running on host network (which is the default) may cause issues with binding.

## Role Variables

- `nginx_version`
  - Default: `latest`
  - Description: The version of nginx-proxy-manager to install. See [tags](https://hub.docker.com/r/jc21/nginx-proxy-manager/tags).
  - Type: str
  - Required: no
- `nginx_port_http`
  - Default: `80`
  - Description: The port on which nginx-proxy-manager will be accessible.
  - Type: int
  - Required: no
- `nginx_port_https`
  - Default: `443`
  - Description: The port on which nginx-proxy-manager will be accessible.
  - Type: int
  - Required: no
- `nginx_port_admin`
  - Default: `81`
  - Description: The port on which nginx-proxy-manager's admin interface will be accessible.
  - Type: int
  - Required: no
- `nginx_install_dir`
  - Default: `/opt/docker/nginx`
  - Description: The directory where nginx-proxy-manager will be installed.
  - Type: str
  - Required: no
- `nginx_env`
  - Default: See [nginx_env_default](./vars/main.yml)
  - Description: Docker container environment variables. See [docs](https://nginxproxymanager.com/advanced-config/#advanced-configuration).
  - Type: dict
  - Required: no
- `nginx_docker_settings`
  - Default: See [nginx_docker_settings_default](./vars/main.yml)
  - Description: Docker container settings.
  - Type: dict
  - Required: no

## Dependencies

- [community.docker](https://docs.ansible.com/ansible/latest/collections/community/docker/index.html)

## Example Playbook

```yaml
- hosts: localhost

  vars:
    nginx_docker_settings:
      network: "my-docker-network"
      puid: "1000" # id -u
      pgid: "1000" # id -g

  roles:
    - artyorsh.selfhosted.nginx
``` 

## Disable IPv6

```yaml
- hosts: localhost

  vars:
    nginx_docker_settings:
      network: "my-docker-network"
      puid: "1000" # id -u
      pgid: "1000" # id -g
    nginx_env:
      disable_ipv6: "true"

  roles:
    - artyorsh.selfhosted.nginx
```