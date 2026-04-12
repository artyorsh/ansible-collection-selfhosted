# selfhosted.homebox

Installs [Homebox](https://homebox.software/en/) - a simple home inventory management software.

## Role Variables

- `homebox_version`
  - Default: `latest`
  - Description: The version of Homebox to install. See [tags](https://github.com/sysadminsmedia/homebox/pkgs/container/homebox).
  - Type: str
  - Required: no
- `homebox_install_dir`
  - Default: `/opt/docker/homebox`
  - Description: The directory where Homebox will be installed.
  - Type: str
  - Required: no
- `homebox_env`
  - Default: See [homebox_env_default](./vars/main.yml)
  - Description: Docker container environment variables. See [docs](https://homebox.software/en/configure-homebox.html#env-variables-configuration).
  - Type: dict
  - Required: no
- `homebox_docker_settings`
  - Default: See [homebox_docker_settings_default](./vars/main.yml)
  - Description: Docker container settings.
  - Type: dict
  - Required: no

## Dependencies

- [community.docker](https://docs.ansible.com/ansible/latest/collections/community/docker/index.html)

## Example Playbook

```yaml
- hosts: localhost

  roles:
    - artyorsh.selfhosted.homebox
``` 