# pre-commit-jinjalint plugin

See explain at https://pre-commit.com/

## How to setup

Install pre-commit on your environment application.

```bash
cd /your/git/application
pip install -U pre-commit
pre-commit install
```

On your git repository put a file called `.pre-commit-config.yaml` with the follow content.

```yaml
repos:
- repo: https://github.com/dgmike/pre-commit-python
  rev: master
  hooks:
  - jinjalint
```

That's it. When you try to commit, pre-commit will validate your jinja files.
