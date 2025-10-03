# selfhosted.weblate

Installs [weblate](https://docs.weblate.org/en/latest/admin/install/docker.html) - Web-based continuous localization software.

> [!NOTE]
> The role is tested to run on a bridge network.
> Running on host network (which is the default) may cause issues.

## Role Variables

- `weblate_version`
  - Default: `latest`
  - Description: The version of weblate to install. See [tags](https://hub.docker.com/r/weblate/weblate/tags).
  - Type: str
  - Required: no
- `weblate_webui_port`
  - Default: `8080`
  - Description: The port on which weblate's web UI will be accessible.
  - Type: int
  - Required: no
- `weblate_install_dir`
  - Default: `/opt/docker/weblate`
  - Description: The directory where weblate will be installed.
  - Type: str
  - Required: no
- `weblate_env`
  - Default: See [weblate_env_default](./vars/main.yml)
  - Description: Docker container environment variables. See [docs](https://docs.weblate.org/en/latest/admin/install/docker.html#generic-settings).
  - Type: dict
  - Required: no
- `weblate_docker_settings`
  - Default: See [weblate_docker_settings_default](./vars/main.yml)
  - Description: Docker container settings.
  - Type: dict
  - Required: no
- `weblate_redis_image`
  - Default: `redis:8-alpine`
  - Description: Docker image for Redis.
  - Type: str
  - Required: no
- `weblate_postgres_image`
  - Default: `postgres:17-alpine`
  - Description: Docker image for PostgreSQL.
  - Type: str
  - Required: no

## Dependencies

- [community.docker](https://docs.ansible.com/ansible/latest/collections/community/docker/index.html)

## Example Playbook

```yaml
- hosts: localhost

  vars:
    weblate_docker_settings:
      network: "weblate"
      weblate_port: 8080
    weblate_env:
      WEBLATE_GITHUB_HOST: "api.github.com"
      WEBLATE_GITHUB_USERNAME: "octocat"

  roles:
    - artyorsh.selfhosted.weblate
```
