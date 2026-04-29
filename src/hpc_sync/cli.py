from pathlib import Path
import shlex
import click
import yaml

from .config import load_config
from .rsync import build_rsync_command, run_rsync

@click.group()
def cli():
    """Mirror project folders between local machine and HPC."""
    pass

@cli.command()
@click.option("--config", default="hpc-sync.yml", show_default=True)
@click.option("--dry-run", is_flag=True)
def push(config: str, dry_run: bool):
    """Sync local project → HPC."""
    cfg = load_config(Path(config))
    cmd = build_rsync_command(cfg, dry_run=dry_run, pull=False)

    click.echo("Running:")
    click.echo(shlex.join(cmd))
    run_rsync(cmd)

@cli.command()
@click.option("--config", default="hpc-sync.yml", show_default=True)
@click.option("--dry-run", is_flag=True)
def pull(config: str, dry_run: bool):
    """Sync HPC → local project."""
    cfg = load_config(Path(config))
    cmd = build_rsync_command(cfg, dry_run=dry_run, pull=True)

    click.echo("Running:")
    click.echo(shlex.join(cmd))
    run_rsync(cmd)

@cli.command()
@click.option("--config", default="hpc-sync.yml", show_default=True)
def show(config: str):
    """Show loaded configuration."""
    cfg = load_config(Path(config))
    click.echo(yaml.dump(cfg, sort_keys=False))

@cli.command()
def init():
    """Create default hpc-sync.yml and .hpcignore."""
    config_path = Path("hpc-sync.yml")
    ignore_path = Path(".hpcignore")

    if not config_path.exists():
        config_path.write_text(
            """hpc_host: username@hpc.cluster.edu
remote_dir: /path/on/hpc/project-name
local_dir: .
exclude_file: .hpcignore
delete_remote: true
""",
            encoding="utf-8",
        )
        click.echo("Created hpc-sync.yml")

    if not ignore_path.exists():
        ignore_path.write_text(
            """.git/
.venv/
venv/
__pycache__/
*.pyc
.DS_Store
results/
logs/
scratch/
""",
            encoding="utf-8",
        )
        click.echo("Created .hpcignore")
