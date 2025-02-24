# selfhosted.wgeasy

Installs [wg-easy](https://github.com/wg-easy/wg-easy/pkgs/container/wg-easy) - the easiest way to run WireGuard VPN + Web-based Admin UI.

[!NOTE]
 > The role is tested to run on a bridge network.
 > Running on host network (which is the default) may cause issues.

## Role Variables

- `wgeasy_version`
  - Default: `latest`
  - Description: The version of wg-easy to install. See [tags](https://github.com/wg-easy/wg-easy/pkgs/container/wg-easy).
  - Type: str
  - Required: no
- `wgeasy_webui_port`
  - Default: `51821`
  - Description: The port on which wg-easy's web UI will be accessible.
  - Type: int
  - Required: no
- `wgeasy_install_dir`
  - Default: `/opt/docker/wgeasy`
  - Description: The directory where wg-easy will be installed.
  - Type: str
  - Required: no
- `wgeasy_env`
  - Default: See [wgeasy_env_default](./vars/main.yml)
  - Description: Docker container environment variables. See [docs](https://github.com/wg-easy/wg-easy?tab=readme-ov-file#options).
  - Type: dict
  - Required: no
- `wgeasy_docker_settings`
  - Default: See [wgeasy_docker_settings_default](./vars/main.yml)
  - Description: Docker container settings.
  - Type: dict
  - Required: no

## Dependencies

- [community.docker](https://docs.ansible.com/ansible/latest/collections/community/docker/index.html)

## Example Playbook

```yaml
- hosts: localhost

  roles:
    - artyorsh.selfhosted.wgeasy
``` 

## Ping peers from the host

```yaml
- hosts: localhost

  vars:
    wgeasy_docker_settings:
      network: "my-bridge-network"
    wgeasy_env:
      # https://github.com/wg-easy/wg-easy/issues/427#issuecomment-1644527712
      WG_POST_UP: "iptables -t nat -A POSTROUTING -s 10.8.0.0/24 -o eth0 -j MASQUERADE; iptables -t nat -A POSTROUTING -o wg+ -j MASQUERADE"

  roles:
    - artyorsh.selfhosted.wgeasy
```