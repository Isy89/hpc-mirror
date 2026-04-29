from pathlib import Path
import click
import yaml

def load_config(path: Path) -> dict:
    if not path.exists():
        raise click.ClickException(f"Config file not found: {path}")
    with path.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f) or {}

    required = ["hpc_host", "remote_dir"]
    missing = [key for key in required if key not in config]

    if missing:
        raise click.ClickException(
            f"Missing required config keys: {', '.join(missing)}"
        )

    return config
