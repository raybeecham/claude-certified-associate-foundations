# Security Policy

## Reporting a security issue

Do not open a public issue for a vulnerability that could expose credentials, private data, workflow permissions, or repository publishing controls.

Report privately through GitHub's security advisory feature when available. Include:

- affected file or component;
- impact;
- reproduction steps;
- proposed mitigation; and
- whether any secret or sensitive data was exposed.

## Repository threat model

This repository is primarily static Markdown and a zero-dependency local Python study tool. Relevant risks include:

- malicious pull requests altering links or study answers;
- supply-chain changes to documentation dependencies;
- executable examples containing unsafe commands;
- accidental inclusion of secrets or private study notes;
- prompt templates that grant overly broad tool access; and
- publication workflows receiving excessive permissions.

The CI workflows use minimal permissions. Do not add third-party actions without reviewing their source, version pinning, and permission requirements.
