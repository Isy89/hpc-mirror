# hpc-sync

A lightweight, reproducible CLI tool to mirror project folders between your local machine and an HPC cluster using `rsync`.

Designed for **consistency across projects**: install once, configure per project.

---

## ✨ Features

* Simple CLI powered by Click
* Project-level configuration (`hpc-sync.yml`)
* Safe mirroring with `--dry-run`
* Push (local → HPC) and pull (HPC → local)
* `.hpcignore` support (like `.gitignore`)
* One tool for all projects

---

## 📦 Installation

Clone or unzip the package, then install:

```bash
pip install -e .
```

This installs the `hpc-sync` command globally (in your environment).

---

## 🚀 Quick Start

Inside your project:

```bash
hpc-sync init
```

This creates:

```text
hpc-sync.yml
.hpcignore
```

Edit `hpc-sync.yml`:

```yaml
hpc_host: username@hpc.cluster.edu
remote_dir: /path/on/hpc/project-name
local_dir: .
exclude_file: .hpcignore
delete_remote: true
```

---

## 🔁 Usage

### Preview sync (safe)

```bash
hpc-sync push --dry-run
```

### Push local → HPC

```bash
hpc-sync push
```

### Pull HPC → local

```bash
hpc-sync pull
```

### Show configuration

```bash
hpc-sync show
```

---

## 📁 `.hpcignore`

Works like `.gitignore`. Example:

```gitignore
.git/
.venv/
__pycache__/
*.pyc

# Large or temporary data
results/
logs/
scratch/
```

---

## 🧠 Recommended Workflow

Follow this pattern for reproducibility:

| Type          | Location |
| ------------- | -------- |
| Source code   | synced   |
| Config files  | synced   |
| Small inputs  | synced   |
| Large outputs | HPC only |
| Scratch data  | HPC only |

---

## ⚠️ Important Notes

* Uses `rsync --delete` by default → remote files not present locally are removed
* Always test with `--dry-run` before syncing
* Requires SSH access to your HPC system

---

## 🔧 Requirements

* Python ≥ 3.9
* `rsync`
* SSH access to HPC

---

## 🔮 Future Extensions

Potential improvements:

* Multiple HPC profiles
* Bandwidth limiting
* Slurm job submission integration
* Pre/post sync hooks

---
