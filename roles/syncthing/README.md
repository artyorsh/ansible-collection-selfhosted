# selfhosted.syncthing

Installs [syncthing](https://github.com/syncthing/syncthing) - a continuous file synchronization program.

## Role Variables

- `syncthing_version`
  - Default: `latest`
  - Description: The version of syncthing to install. See [tags](https://hub.docker.com/r/syncthing/syncthing/tags).
  - Type: str
  - Required: no
- `syncthing_port_webui`
  - Default: `8384`
  - Description: The port on which syncthing Web UI will be accessible.
  - Type: int
  - Required: no
- `syncthing_port_listen`
  - Default: `22000`
  - Description: The port on which syncthing will listen.
  - Type: int
  - Required: no
- `syncthing_install_dir`
  - Default: `/opt/docker/syncthing`
  - Description: The directory where syncthing will be installed.
  - Type: str
  - Required: no
- `syncthing_sync_dir`
  - Default: `/opt/docker/syncthing/sync`
  - Description: The directory available for syncing (/data1).
  - Type: str
  - Required: no
- `syncthing_env`
  - Default: See [syncthing_env_default](./vars/main.yml)
  - Description: Docker container environment variables. See [docs](https://syncthing.org/configuration).
  - Type: dict
  - Required: no
- `syncthing_docker_settings`
  - Default: See [syncthing_docker_settings_default](./vars/main.yml)
  - Description: Docker container settings.
  - Type: dict
  - Required: no

## Dependencies

- [community.docker](https://docs.ansible.com/ansible/latest/collections/community/docker/index.html)

## Example Playbook

```yaml
- hosts: localhost

  vars:
    syncthing_sync_dir: "/mnt/data"

  roles:
    - artyorsh.selfhosted.syncthing
```
