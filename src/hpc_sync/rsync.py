from pathlib import Path
import subprocess

def build_rsync_command(config: dict, dry_run: bool = False, pull: bool = False) -> list[str]:
    local_dir = Path(config.get("local_dir", ".")).resolve()
    hpc_host = config["hpc_host"]
    remote_dir = config["remote_dir"].rstrip("/")
    exclude_file = config.get("exclude_file", ".hpcignore")
    delete = config.get("delete_remote", True)

    cmd = ["rsync", "-avz"]

    if delete:
        cmd.append("--delete")

    if dry_run:
        cmd.append("--dry-run")

    exclude_path = Path(exclude_file)
    if exclude_path.exists():
        cmd.append(f"--exclude-from={exclude_path}")

    if pull:
        source = f"{hpc_host}:{remote_dir}/"
        target = f"{local_dir}/"
    else:
        source = f"{local_dir}/"
        target = f"{hpc_host}:{remote_dir}/"

    cmd.extend([source, target])
    return cmd

def run_rsync(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)
