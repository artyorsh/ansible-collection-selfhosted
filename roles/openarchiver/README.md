# selfhosted.openarchiver

Installs [openarchiver](https://openarchiver.com) - an Open Source Email Archiving & eDiscovery tool.

## Role Variables

- `openarchiver_version`
  - Default: `latest`
  - Description: The version of openarchiver to install. See [tags](https://github.com/gitroomhq/openarchiver-app/pkgs/container/openarchiver-app).
  - Type: str
  - Required: no
- `openarchiver_port`
  - Default: `3000`
  - Description: The port on which openarchiver's web UI will be accessible.
  - Type: int
  - Required: no
- `openarchiver_install_dir`
  - Default: `/opt/docker/openarchiver`
  - Description: The directory where openarchiver will be installed.
  - Type: str
  - Required: no
- `openarchiver_storage_dir`
  - Default: `{{ openarchiver_install_dir }}/storage`
  - Description: The directory where openarchiver will store mail.
  - Type: str
  - Required: no
- `openarchiver_env`
  - Default: See [openarchiver_env_default](./vars/main.yml)
  - Description: Docker container environment variables. See [docs](https://github.com/LogicLabs-OU/OpenArchiver/blob/main/.env.example)
  - Type: dict
  - Required: no
- `openarchiver_db_env`
  - Default: See [openarchiver_db_env_default](./vars/main.yml)
  - Description: Postgres environment variables. See [docs](https://github.com/LogicLabs-OU/OpenArchiver/blob/main/.env.example)
  - Type: dict
  - Required: no
- `openarchiver_docker_settings`
  - Default: See [openarchiver_docker_settings_default](./vars/main.yml)
  - Description: Docker container settings.
  - Type: dict
  - Required: no
- `openarchiver_db_postgres_version`
  - Default: `17-alpine`
  - Description: The version of PostgreSQL to use for the database.
  - Type: str
  - Required: no
- `openarchiver_valkey_version`
  - Default: `7.2`
  - Description: The version of Valkey to use.
  - Type: str
  - Required: no

## Dependencies

- [community.docker](https://docs.ansible.com/ansible/latest/collections/community/docker/index.html)

## Example Playbook

```yaml
- hosts: localhost

  vars:
    openarchiver_env:
      REDIS_PASSWORD: "supersecret"
      MEILI_MASTER_KEY: "supersecret"
      JWT_SECRET: "supersecret"
      STORAGE_ENCRYPTION_KEY: "supersecret" # openssl rand -hex 32
      ENCRYPTION_KEY: "supersecret" # openssl rand -hex 32
  roles:
    - artyorsh.selfhosted.openarchiver
```
