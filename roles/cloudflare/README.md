# selfhosted.cloudflare

Installs [cloudflared](https://hub.docker.com/r/cloudflare/cloudflared) - an easy way to make apps accessible remotely without a publicly routable IP address.

> [!NOTE]
> This role is not actively maintained since I moved to [nginx-proxy-manager](../nginx/README.md) and [wg-easy](../wgeasy/README.md).
> Bugs may be present due to incompatibility with the latest versions of cloudflared image.

## Requirements

- [Cloudflare Tunnel Token](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/get-started/create-remote-tunnel)

## Role Variables

- `cloudflare_tunnel_version`
  - Default: `latest`
  - Description: The version of Cloudflare Tunnel to install. See [tags](https://hub.docker.com/r/cloudflare/cloudflared/tags).
  - Type: str
  - Required: no
- `cloudflare_tunnel_uuid_or_name`
  - Default: `""`
  - Description: The UUID or name of the tunnel to use. See [docs](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/get-started/tunnel-useful-terms/#tunnel).
  - Type: str
  - Required: yes
- `cloudflare_tunnel_networks`
  - Default: `[]`
  - Description: A list of docker networks cloudflare tunnel is connected to. If an application is running on a specific bridge network, it won't be accessible to the tunnel unless it's added to the list.
  - Type: list
  - Required: no
- `cloudflare_tunnel_ssh_enabled`
  - Default: `true`
  - Description: Whether to enable SSH on the tunnel. Copies a public key (`{{ cloudflare_certificate_public_key }}`) in `/etc/ssh/ca.pub` and makes it trusted in `/etc/ssh/sshd_config`. See [docs](https://developers.cloudflare.com/cloudflare-one/identity/users/short-lived-certificates#3-generate-a-short-lived-certificate-public-key)
  - Type: bool
  - Required: no
- `cloudflare_env`
  - Default: See [cloudflare_env_default](./vars/main.yml)
  - Description: Cloudflared environment variables. Must contain `TUNNEL_TOKEN` variable.
  - Type: dict
  - Required: yes

## Dependencies

- [community.docker](https://docs.ansible.com/ansible/latest/collections/community/docker/index.html)

## Example Playbook

```yaml
- hosts: localhost

  vars:
    cloudflare_tunnel_uuid_or_name: "my-tunnel-uuid"
    cloudflare_env:
      TUNNEL_TOKEN: "..."

  roles:
    - artyorsh.selfhosted.cloudflare
``` 