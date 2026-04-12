# selfhosted.forgejo

Installs [Forgejo](https://forgejo.org/) - a lightweight git service.
Also installs a MySQL database that is [required](https://forgejo.org/docs/latest/admin/database-preparation/#mysqlmariadb) by Forgejo to work.

## Role Variables

- `forgejo_version`
  - Default: `9-rootless`
  - Description: The version of Forgejo to install. See [tags](https://codeberg.org/forgejo/forgejo/packages).
  - Type: str
  - Required: no
- `forgejo_docker_settings`
  - Default: See [forgejo_docker_settings_default](./vars/main.yml)
  - Description: Docker container settings.
  - Type: dict
  - Required: no
- `forgejo_install_dir`
  - Default: `/opt/docker/forgejo`
  - Description: The directory where Forgejo will be installed.
  - Type: str
  - Required: no
- `forgejo_env`
  - Default: See [forgejo_env_default](./vars/main.yml)
  - Description: Docker container environment variables. See [docs](https://forgejo.org/docs/latest/admin/config-cheat-sheet/#default-configuration-non-appini-configuration)
  - Type: dict
  - Required: no
- `forgejo_repositories_dir`
  - Default: `{{ forgejo_install_dir }}/repositories`
  - Description: The directory where Forgejo will store the repositories.
  - Type: str
  - Required: no
- `forgejo_db_mysql_version`
  - Default: `8`
  - Description: The version of MySQL to use for the database.
  - Type: int
  - Required: no
- `forgejo_db_env`
  - Default: See [forgejo_db_env_default](./vars/main.yml)
  - Description: Docker container environment variables for the database.
  - Type: dict
  - Required: no
  
## Dependencies

- [community.docker](https://docs.ansible.com/ansible/latest/collections/community/docker/index.html)

## Example Playbook

```yaml
- hosts: localhost

  vars:
    forgejo_repositories_dir: "/path/to/repositories"

  roles:
    - artyorsh.selfhosted.forgejo
``` 

## Disable features

```yaml
- hosts: localhost

  vars:
    forgejo_env:
      FORGEJO__actions__ENABLED: "false"
      FORGEJO__attachment__ENABLED: "false"
      FORGEJO__picture__DISABLE_GRAVATAR: "true"
      FORGEJO__repository__DISABLED_REPO_UNITS: "repo.actions"
      FORGEJO__repository__DISABLE_STARS: "true"
      FORGEJO__repository.upload__ENABLED: "false"
      FORGEJO__security__DISABLE_WEBHOOKS: "true"
      FORGEJO__service__DISABLE_REGISTRATION: "true"
      FORGEJO__service__ENABLE_BASIC_AUTHENTICATION: "true"
      FORGEJO__service.explore__DISABLE_USERS_PAGE: "true"
      FORGEJO__service.explore__REQUIRE_SIGNIN_VIEW: "true"
      FORGEJO__ui.notification__EVENT_SOURCE_UPDATE_TIME: "-1"

  roles:
    - artyorsh.selfhosted.forgejo
```
