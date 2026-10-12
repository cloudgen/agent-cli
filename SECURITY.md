# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.1.0 (current) | Yes |
| 1.0.0 | Yes |
| Older releases | Best-effort; prefer upgrading to current |

## Reporting a Vulnerability

Please **do not** open a public issue for security-sensitive reports when a private channel is available.

**Maintainer contact (email):** `wongcf22@gmail.com`

- Source of contact: product **author-email** SSOT in [`LICENSE.md`](./LICENSE.md) (Copyright line).
- Prefer email for vulnerability details, reproduction steps, and impact.
- You should receive an acknowledgment when the report is received and actionable.
- Do not include exploit weaponization guides in public channels.

## Security Design Principles (CIAO)

This project follows **[CIAO](https://github.com/cloudgen/ciao)** / **CIAO-Lite** defensive design. Security-relevant intent:

| Letter | Principle | Security application |
|--------|-----------|----------------------|
| **C** | **Caution** | Assume missing tools. Fail closed on an unknown verb, a missing grant, and a pip failure. |
| **I** | **Intentional** | The only elevated command is `agent-cli backup`. The sudoers argument list is `backup` and nothing else. |
| **A** | **Anti-fragile** | A missed cache tier is silent and the next tier is used. A signed-in session skips `sync-auth`. |
| **O** | **Over-protect** | Empty argv does not install this package and does not download peer `grok`. `setup` does not run a vendor shell installer. |

Full principles: [CIAO Defensive Programming](https://github.com/cloudgen/ciao) · agent contract: [CIAO-Lite](https://github.com/cloudgen/ciao-lite).

This section describes **design posture**. It is **not** a claim of third-party certification.

## Scope notes

- AgentCli is a **local** interactive CLI plus a pip package. Peer `grok` auth files stay under `~/.grok`. The deposit is `/var/agent-cli`.
- `setup` may download the peer binary from the vendor channel, then the public fallback. This package does not publish a shell installer for itself.
- Do not commit tokens, private keys, or `auth.json` contents.
- Related product docs: [`README.md`](./README.md), [`LICENSE.md`](./LICENSE.md).
