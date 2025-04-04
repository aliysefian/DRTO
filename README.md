# Appointment Monitor

This Python script monitors available appointment slots on the DoctorEto platform and automatically opens a browser tab for each newly available appointment. It uses the `uv` package manager for dependency management and virtual environment setup.

## Features
- Fetches appointment availability from the DoctorEto API.
- Opens a new browser tab for each available appointment.
- Continuously monitors for new appointments with a configurable delay.
- Uses multi-threading for efficient API calls and browser interactions.

## Prerequisites
- Python 3.8 or higher installed on your system.
- The `uv` package manager installed (see installation instructions below).
- An internet connection to access the DoctorEto API and open browser tabs.

## Installation with `uv`

The script uses the `uv` package manager, a fast and modern alternative to `pip` and `virtualenv`. Follow these steps to set up your environment:

### 1. Install `uv`
You can install `uv` using the official installation script or via `pip`. Choose one of the following methods:

#### Option 1: Using the Installation Script (Recommended)
On macOS/Linux:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh