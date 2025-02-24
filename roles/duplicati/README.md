# selfhosted.duplicati

Installs [Duplicati](https://duplicati.com) - a central backup management & monitoring system.
This role installs the [linuxserver/duplicati](https://docs.linuxserver.io/images/docker-duplicati) image.

## Role Variables

- `duplicati_version`
  - Default: `latest`
  - Description: The version of Duplicati to install. See [tags](https://hub.docker.com/r/linuxserver/duplicati/tags).
  - Type: str
  - Required: no
- `duplicati_port`
  - Default: `8200`
  - Description: The port on which Duplicati will be accessible.
  - Type: int
  - Required: no
- `duplicati_install_dir`
  - Default: `/opt/docker/duplicati`
  - Description: The directory where Duplicati will be installed.
  - Type: str
  - Required: no
- `duplicati_source_dir`
  - Default: `{{ duplicati_install_dir }}/source`
  - Description: Path to source for files to backup.
  - Type: str
  - Required: no
- `duplicati_backups_dir`
  - Default: `{{ duplicati_install_dir }}/backups`
  - Description: Path to store local backups.
- `duplicati_env`
  - Default: See [duplicati_env_default](./vars/main.yml)
  - Description: Docker container environment variables. See [docs](https://docs.linuxserver.io/images/docker-duplicati/#environment-variables-e).
  - Type: dict
  - Required: no
- `duplicati_docker_settings`
  - Default: See [duplicati_docker_settings_default](./vars/main.yml)
  - Description: Docker container settings.
  - Type: dict
  - Required: no

## Dependencies

- [community.docker](https://docs.ansible.com/ansible/latest/collections/community/docker/index.html)

## Example Playbook

```yaml
- hosts: localhost

  vars:
    duplicati_source_dir: "/path/to/source/files"
    duplicati_backups_dir: "/path/to/backups"
    duplicati_env:
      # https://docs.duplicati.com/detailed-descriptions/using-duplicati-from-docker#managing-secrets-in-docker
      SETTINGS_ENCRYPTION_KEY: "supersecret"

  roles:
    - artyorsh.selfhosted.duplicati
``` 