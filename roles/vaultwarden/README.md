# selfhosted.vaultwarden

Installs [vaultwarden](https://github.com/dani-garcia/vaultwarden) - an unofficial Bitwarden compatible server written in Rust.

## Role Variables

- `vaultwarden_version`
  - Default: `latest-alpine`
  - Description: The version of vaultwarden to install. See [docker tags](https://hub.docker.com/r/vaultwarden/server/tags).
  - Type: str
  - Required: no
- `vaultwarden_install_dir`
  - Default: `/opt/docker/vaultwarden`
  - Description: The directory where vaultwarden will be installed.
  - Type: str
  - Required: no
- `vaultwarden_env`
  - Default: See [vaultwarden_env_default](./vars/main.yml)
  - Description: Docker container environment variables. See [docs](https://github.com/dani-garcia/vaultwarden/wiki/Configuration-overview).
  - Type: dict
  - Required: no
- `vaultwarden_docker_settings`
  - Default: See [vaultwarden_docker_settings_default](./vars/main.yml)
  - Description: Docker container settings.
  - Type: dict
  - Required: no

## Dependencies

- [community.docker](https://docs.ansible.com/ansible/latest/collections/community/docker/index.html)

## Example playbook

```yaml
- hosts: localhost

  vars:
    vaultwarden_docker_settings:
      network: "my-bridge-net"

  roles:
    - artyorsh.selfhosted.vaultwarden
```