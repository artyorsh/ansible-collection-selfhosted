# selfhosted.rss

Installs [miniflux](https://miniflux.app) - a minimalist and opinionated feed reader
and [rss-bridge](https://rss-bridge.org) - a PHP project capable of generating RSS and Atom feeds for websites that don't have one.

Also installs a PostgreSQL database that is [required](https://miniflux.app/docs/database.html) by Miniflux to work.

## Role Variables

- `rss_miniflux_version`
  - Default: `latest`
  - Description: The version of Miniflux to install. See [docker tags](https://hub.docker.com/r/linuxserver/miniflux/tags).
  - Type: str
  - Required: no
- `rss_miniflux_webui_port`
  - Default: `8082`
  - Description: The port on which Miniflux will be accessible.
  - Type: int
  - Required: no
- `rss_miniflux_install_dir`
  - Default: `/opt/docker/miniflux`
  - Description: The directory where Miniflux will be installed.
  - Type: str
  - Required: no
- `rss_miniflux_env`
  - Default: See [rss_miniflux_env_default](./vars/main.yml)
  - Description: Docker container environment variables for Miniflux. See [docs](https://miniflux.app/docs/configuration.html#options).
  - Type: dict
  - Required: no
- `rss_miniflux_postgres_version`
  - Default: `15`
  - Description: The version of PostgreSQL to use with Miniflux. See [docker tags](https://hub.docker.com/_/postgres/tags).
  - Type: str
  - Required: no
- `rss_miniflux_postgres_env`
  - Default: See [rss_miniflux_postgres_env_default](./vars/main.yml)
  - Description: Docker container environment variables for PostgreSQL.
  - Type: dict
  - Required: no
- `rss_rssbridge_version`
  - Default: `latest`
  - Description: The version of RSS Bridge to install. See [docker tags](https://hub.docker.com/r/rssbridge/rss-bridge/tags).
  - Type: str
  - Required: no
- `rss_rssbridge_webui_port`
  - Default: `8083`
  - Description: The port on which RSS Bridge will be accessible.
  - Type: int
  - Required: no
- `rss_rssbridge_install_dir`
  - Default: `/opt/docker/rssbridge`
  - Description: The directory where RSS Bridge will be installed.
  - Type: str
  - Required: no
- `rss_rssbridge_env`
  - Default: See [rss_rssbridge_env_default](./vars/main.yml)
  - Description: Docker container environment variables for RSS Bridge.
  - Type: dict
  - Required: no
- `rss_rssbridge_bridges`
  - Default: `[]`
  - Description: List of bridges to be used by RSS Bridge. See [docs](https://github.com/RSS-Bridge/rss-bridge/tree/master/bridges).
  - Type: list
  - Required: no

## Dependencies

- [community.docker](https://docs.ansible.com/ansible/latest/collections/community/docker/index.html)

## Example Playbook

```yaml
- hosts: localhost

  roles:
    - artyorsh.selfhosted.rss
```

## Polling frequency, bridges

```yaml
- hosts: localhost

  vars:
    rss_miniflux_env:
      DATABASE_URL: "postgres://miniflux:changeme@miniflux-db/miniflux?sslmode=disable"
      POLLING_FREQUENCY: "720"
      FORCE_REFRESH_INTERVAL: "1"

    rss_miniflux_postgres_env:
      POSTGRES_USER: "miniflux"
      POSTGRES_PASSWORD: "changeme"

  roles:
    - artyorsh.selfhosted.rss