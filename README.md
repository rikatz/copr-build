# COPR Build

RPM spec files and automation for building packages on [Fedora COPR](https://copr.fedorainfracloud.org/).

## Packages

- **rtk** — [rtk-ai/rtk](https://github.com/rtk-ai/rtk), a CLI proxy that reduces LLM token consumption by 60-90%.

## Automation

A scheduled GitHub Action checks for new upstream releases every 6 hours. When a new version is found, it bumps the spec and pushes to `main`. A second action triggers the COPR build via webhook on every push to `main`.

## Setup

### GitHub Secrets

| Secret | Description |
|--------|-------------|
| `PUSH_TOKEN` | Fine-grained PAT with Contents read/write on this repo |
| `COPR_WEBHOOK_URL` | COPR webhook URL from project Settings > Integrations |
