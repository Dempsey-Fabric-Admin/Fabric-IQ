# Dempsey Fabric IQ

This repository is the source for the Dempsey Fabric IQ Codex marketplace
plugin. The plugin provides read-only business analytics over the configured
Fabric IQ app for Business Central Finance, with planned workflows for Warehouse
Operations and Retail Operations.

## Install from GitHub

Add the GitHub repository as a Codex marketplace and install the plugin:

```powershell
codex plugin marketplace add Dempsey-Fabric-Admin/Fabric-IQ --ref main
codex plugin add dempsey-fabric-iq@dempsey-chatgpt
```

Start a new Codex chat after installation so the updated skills are loaded.

To refresh the Git marketplace after a new release:

```powershell
codex plugin marketplace upgrade dempsey-chatgpt
codex plugin add dempsey-fabric-iq@dempsey-chatgpt
```

## Development

The Git-managed marketplace source is under `src/chatgpt`. Validate it before
committing or publishing an update:

```powershell
python src/chatgpt/scripts/validate_plugins.py
```

Develop from a local clone. Push approved commits to Azure DevOps `develop` and
GitHub `main`, then upgrade the Git marketplace installation.
