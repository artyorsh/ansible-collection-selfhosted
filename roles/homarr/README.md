# selfhosted.homarr

Installs [Homarr](https://homarr.dev) - A simple, yet powerful dashboard for your server.

> [!NOTE]
> This role is not actively maintained as it is not in use since I moved to a much more simplified approach - bookmarks.
> Bugs may be present due to incompatibility with the latest versions of Homarr image.

## Role Variables

- `homarr_version`
  - Default: `latest`
  - Description: The version of Homarr to install. See [tags](https://hub.docker.com/r/jesec/homarr/tags).
  - Type: str
  - Required: no
- `homarr_install_dir`
  - Default: `/opt/docker/homarr`
  - Description: The directory where Homarr will be installed.
  - Type: str
  - Required: no
- `homarr_docker_settings`
  - Default: See [homarr_docker_settings_default](./vars/main.yml)
  - Description: Docker container settings.
  - Type: dict
  - Required: no

## Dependencies

- [community.docker](https://docs.ansible.com/ansible/latest/collections/community/docker/index.html)

## Example Playbook

```yaml
- hosts: localhost

  roles:
    - artyorsh.selfhosted.homarr
``` 