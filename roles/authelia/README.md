# selfhosted.authelia

Installs [Authelia](https://www.authelia.com) service - an open-source authentication and authorization server.

> [!NOTE]
> This role is not actively maintained as it is currently not in use (since November 2024).
> Bugs may be present due to incompatibility with the latest versions of Authelia image.

## Role Variables

- `authelia_version`
  - Default: `latest`
  - Description: The version of Authelia to install. See [tags](https://hub.docker.com/r/authelia/authelia/tags).
  - Type: str
  - Required: no
- `authelia_port`
  - Default: `9091`
  - Description: The port on which Authelia will be accessible.
  - Type: int
  - Required: no
- `authelia_install_dir`
  - Default: `/opt/docker/authelia`
  - Description: The directory where Authelia will be installed.
  - Type: str
  - Required: no
- `authelia_env`
  - Default: See [authelia_env_default](./vars/main.yml)
  - Description: Docker container environment variables. See [docs](https://www.authelia.com/configuration/methods/environment/#environment-variables).
  - Type: dict
  - Required: no
- `authelia_config`
  - Default: See [authelia_default_config](./vars/main.yml)
  - Description: Authelia configuration. See [docs](https://www.authelia.com/integration/prologue/get-started/#configuration).
  - Type: dict
  - Required: no
- `authelia_users`
  - Default: See [authelia_users](./defaults/main.yml)
  - Description: Authelia users create for the [file authentication backend](https://www.authelia.com/configuration/first-factor/introduction/). 
  - Type: dict
  - Required: no
- `authelia_docker_settings`
  - Default: See [authelia_docker_settings_default](./vars/main.yml)
  - Description: Docker container settings.
  - Type: dict
  - Required: no

## Dependencies

- [community.docker](https://docs.ansible.com/ansible/latest/collections/community/docker/index.html)

## Example Playbook

```yaml
- hosts: localhost

  vars:
    domain: "example.com"
    authelia_users:
      users:
        admin:
          displayname: "Admin"
          email: "admin@{{ domain }}"
          # supersecret, salt=supersecret
          # https://argon2.online
          password: "$argon2id$v=19$m=1024,t=1,p=8$c3VwZXJzZWNyZXQ$3DK6bsCIIa3MWorb4zatsQ"
          groups: ["admins"]

    authelia_config:
      access_control:
        default_policy: "one_factor"
        rules:
          - { domain: "auth.{{ domain }}", policy: "bypass" }

      identity_validation:
        reset_password:
          # https://www.authelia.com/configuration/identity-validation/reset-password/#jwt_secret
          jwt_secret: "supersecret"

      totp:
        issuer: "{{ domain }}"

      session:
        # https://www.authelia.com/configuration/session/introduction/#secret
        secret: "supersecret"
        cookies:
          - { domain: "{{ domain }}", authelia_url: "https://auth.{{ domain }}" }

      storage:
        # https://www.authelia.com/configuration/storage/introduction/#encryption_key
        encryption_key: "supersecret"

      authentication_backend:
        password_reset:
          disable: true

  roles:
    - artyorsh.selfhosted.authelia
``` 