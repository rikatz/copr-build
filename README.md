# COPR Build

RPM spec files and automation for building packages on [Fedora COPR](https://copr.fedorainfracloud.org/).

## Packages

- **rtk** — [rtk-ai/rtk](https://github.com/rtk-ai/rtk), a CLI proxy that reduces LLM token consumption by 60-90%.
- **herdr** — [herdrdev/herdr](https://github.com/herdrdev/herdr), a multiplexer for coding agents

## Automation

A scheduled GitHub Action checks for new upstream releases every 6 hours. When a new version is found, it bumps the spec and pushes to `main`. A second action triggers the COPR build via webhook on every push to `main`.


