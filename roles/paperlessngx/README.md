# selfhosted.paperlessngx

Installs [paperless-ngx](https://docs.paperless-ngx.com) - a community-supported open-source document management system that transforms your physical documents into a searchable online archive.

[!NOTE]
 > The role is tested to run on a bridge network.
 > Running on host network (which is the default) may cause issues with Redis.

## Role Variables

- `paperlessngx_version`
  - Default: `latest`
  - Description: The version of paperless-ngx to install. See [docker tags](https://hub.docker.com/r/paperlessngx/paperless-ngx/tags).
  - Type: str
  - Required: no
- `paperlessngx_redis_version`
  - Default: `7.2.4-alpine`
  - Description: The version of redis to install. Redis is required for processing scheduled tasks. See [docs](https://docs.paperless-ngx.com/configuration/#redis-broker).
  - Type: str
  - Required: no
- `paperlessngx_port`
  - Default: `9898`
  - Description: The port on which paperless-ngx will be accessible.
  - Type: int
  - Required: no
- `paperlessngx_docker_settings`
  - Default: See [paperlessngx_docker_settings_default](./vars/main.yml)
  - Description: Docker container settings.
  - Type: dict
  - Required: no
- `paperlessngx_install_dir`
  - Default: `/opt/docker/paperlessngx`
  - Description: The directory where paperless-ngx will be installed.
  - Type: str
  - Required: no
- `paperlessngx_consume_dir`
  - Default: `{{ paperlessngx_install_dir }}/consume`
  - Description: The directory where paperless-ngx will consume documents. See [docs](https://docs.paperless-ngx.com/usage/#the-consumption-directory).
  - Type: str
  - Required: no
- `paperlessngx_media_dir`
  - Default: `{{ paperlessngx_install_dir }}/media`
  - Description: The directory where paperless-ngx will store media files.
  - Type: str
  - Required: no
- `paperlessngx_env`
  - Default: See [paperlessngx_env_default](./vars/main.yml)
  - Description: Docker container environment variables. See [docs](https://docs.paperless-ngx.com/configuration/).
  - Type: dict
  - Required: no

## Dependencies

- [community.docker](https://docs.ansible.com/ansible/latest/collections/community/docker/index.html)

## Example Playbook

```yaml
- hosts: localhost

  vars:
    paperlessngx_consume_dir: "/path/to/documents/inbox"
    paperlessngx_media_dir: "/path/to/documents"
    paperlessngx_docker_settings:
      network: "my-bridge-network"

  roles:
    - artyorsh.selfhosted.paperlessngx
```