# selfhosted.headscale

Installs [Headscale](https://github.com/juanfont/headscale) — an open-source Tailscale control server — as a Docker container.

## Role variables

- `headscale_version`
  - Default: `0.25.0`
  - Description: Image tag for [`headscale/headscale`](https://hub.docker.com/r/headscale/headscale/tags).
- `headscale_install_dir`
  - Default: `/opt/docker/headscale`
- `headscale_port` / `headscale_metrics_port`
  - Defaults: `8080` / `9090` — host ports mapped to the API and `/metrics`.
- `headscale_default_config`
  - Default: See [vars/main.yml](./vars/main.yml) — baseline `config.yaml` for v0.25.x (aligned with upstream `config-example.yaml`).
- `headscale_config`
  - Default: `{}`
  - Description: Recursively merged into `headscale_default_config` (same pattern as [olivetin](../olivetin/README.md) / [authelia](../authelia/README.md)). Use this for `server_url`, nested `dns`, `derp`, etc.
- `headscale_config_replace`
  - Default: `false`
  - Description: When `true`, written `config.yaml` is **only** `headscale_config` (you supply the full document).
- `headscale_env`
  - Default: `{}`
- `headscale_docker_settings`
  - Default: See [headscale_docker_settings_default](./vars/main.yml)
  - Description: Must include `networks` so Headscale shares a Docker network with nginx-proxy-manager (`http://headscale:8080` upstream).

Required after merge: `server_url`, `dns.base_domain`, and at least one Docker network.

## Reverse proxy

Terminate TLS in nginx-proxy-manager: forward `https://hs.<your-domain>` to `http://headscale:8080`, enable WebSockets, and issue a certificate.

## Example host variables

```yaml
headscale_config:
  server_url: "https://hs.example.com"
  dns:
    base_domain: "ts.example.com"
    nameservers:
      global:
        - "100.64.0.1"
headscale_docker_settings:
  networks:
    - name: "docker-network-main"
      ipv4_address: "172.88.0.5"
```

## Dependencies

- `community.docker`

## Example playbook

```yaml
- hosts: vps
  roles:
    - role: "artyorsh.selfhosted.headscale"
      tags: ["headscale"]
```
