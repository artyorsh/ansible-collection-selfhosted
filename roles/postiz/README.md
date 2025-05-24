# selfhosted.postiz

Installs [postiz](https://postiz.com) - an ultimate social media scheduling tool.
Also installs a PostgreSQL database that is [required](https://docs.postiz.com/installation/docker-compose#docker-compose) by postiz to work.

## Role Variables

- `postiz_version`
  - Default: `latest`
  - Description: The version of postiz to install. See [tags](https://github.com/gitroomhq/postiz-app/pkgs/container/postiz-app).
  - Type: str
  - Required: no
- `postiz_webui_port`
  - Default: `5000`
  - Description: The port on which postiz's web UI will be accessible.
  - Type: int
  - Required: no
- `postiz_install_dir`
  - Default: `/opt/docker/postiz`
  - Description: The directory where postiz will be installed.
  - Type: str
  - Required: no
- `postiz_uploads_dir`
  - Default: `{{ postiz_uploads_dir }}/uploads`
  - Description: The directory where postiz will store uploads.
  - Type: str
  - Required: no
- `postiz_env`
  - Default: See [postiz_env_default](./vars/main.yml)
  - Description: Docker container environment variables. See [docs](https://docs.postiz.com/installation/docker-compose#docker-compose)
  - Type: dict
  - Required: no
- `postiz_db_env`
  - Default: See [postiz_db_env_default](./vars/main.yml)
  - Description: Postgres environment variables. See [docs](https://docs.postiz.com/installation/docker-compose#docker-compose)
  - Type: dict
  - Required: no
- `postiz_docker_settings`
  - Default: See [postiz_docker_settings_default](./vars/main.yml)
  - Description: Docker container settings.
  - Type: dict
  - Required: no
- `postiz_db_postgres_version`
  - Default: `17-alpine`
  - Description: The version of PostgreSQL to use for the database.
  - Type: str
  - Required: no
- `postiz_redis_version`
  - Default: `7.2`
  - Description: The version of Redis to use.
  - Type: str
  - Required: no
  
## Dependencies

- [community.docker](https://docs.ansible.com/ansible/latest/collections/community/docker/index.html)

## Example Playbook

```yaml
- hosts: localhost

  vars:
    postiz_env:
      NOT_SECURED: "true"
      JWT_SECRET: "supersecret"
      MAIN_URL: "https://postiz.example.com"
      FRONTEND_URL: "https://postiz.example.com"
      NEXT_PUBLIC_BACKEND_URL: "https://postiz.example.com/api"
      EMAIL_PROVIDER: "nodemailer"
      EMAIL_FROM_NAME: "Postiz Notifications"
      EMAIL_FROM_ADDRESS: "postiz@example.com"
      EMAIL_HOST: "smtp.gmail.com"
      EMAIL_PORT: "465"
      EMAIL_SECURE: "true"
      EMAIL_USER: "postiz@gmail.com"
      EMAIL_PASS: "" # https://support.google.com/mail/answer/185833?hl=en
      OPENAI_API_KEY: "" # https://platform.openai.com/api-keys
      INSTAGRAM_APP_ID: "" # https://github.com/gitroomhq/postiz-docs/blob/main/pages/providers/instagram.mdx
      INSTAGRAM_APP_SECRET: ""

  roles:
    - artyorsh.selfhosted.postiz
```