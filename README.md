# Ansible Collection - Selfhosted

[![Ansible Galaxy](https://img.shields.io/badge/collection-artyorsh.selfhosted-blue)](https://galaxy.ansible.com/artyorsh/selfhosted)
[![Test](https://github.com/artyorsh/ansible-collection-selfhosted/actions/workflows/test.yml/badge.svg?event=push)](https://github.com/artyorsh/ansible-collection-selfhosted/actions/workflows/test.yml)

An opinionated collection of selfhosted apps, managed with Ansible.

## Roles

- [adguardhome](./roles/adguardhome/README.md)
- [authelia](./roles/authelia/README.md)
- [changedetection](./roles/changedetection/README.md)
- [cloudflare](./roles/cloudflare/README.md)
- [docker](./roles/docker/README.md)
- [duplicati](./roles/duplicati/README.md)
- [filebrowser](./roles/filebrowser/README.md)
- [forgejo](./roles/forgejo/README.md)
- [glances](./roles/glances/README.md)
- [homebox](./roles/homebox/README.md)
- [homarr](./roles/homarr/README.md)
- [nginx](./roles/nginx/README.md)
- [olivetin](./roles/olivetin/README.md)
- [paperless_ai](./roles/paperless_ai/README.md)
- [paperlessngx](./roles/paperlessngx/README.md)
- [postiz](./roles/postiz/README.md)
- [rss](./roles/rss/README.md)
- [vaultwarden](./roles/vaultwarden/README.md)
- [wallos](./roles/wallos/README.md)
- [watchtower](./roles/watchtower/README.md)
- [wg-easy](./roles/wgeasy/README.md)

## Installation

```
ansible-galaxy collection install artyorsh.selfhosted
```

## Example Playbook

See more examples in roles' README files.

```yaml
- hosts: localhost

  roles:
    - artyorsh.selfhosted.docker
    - artyorsh.selfhosted.duplicati
    - artyorsh.selfhosted.watchtower
```

## More collections

- [artyorsh.smarthome](https://github.com/artyorsh/ansible-collection-smarthome)

## License

MIT