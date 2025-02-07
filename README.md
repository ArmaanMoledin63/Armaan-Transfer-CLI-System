# Armaan-Transfer-CLI-System

A lightning-fast CLI tool for secure peer-to-peer file transfers between computers on the same network.

## Features
- 🚀 Fast peer-to-peer file transfer
- 🔒 Direct computer-to-computer transfer
- 📊 Real-time progress tracking
- ✨ Simple command-line interface

## Installation
```bash
pip install armaan-transfer
```

## Quick Start

1. On receiving computer:
```bash
armaan-transfer --mode receive
```

2. On sending computer:
```bash
armaan-transfer --mode send --file path/to/file --host IP_ADDRESS
```

## Examples
```bash
# Receive files
armaan-transfer --mode receive

# Send a file
armaan-transfer --mode send --file document.txt --host 192.168.1.100
```

## Common Issues
- Ensure receiver is running first
- Check firewall settings
- Verify IP address

## Author
Created by Armaan Moledina
