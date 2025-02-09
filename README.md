# Armaan-Transfer-CLI-System

A lightning-fast CLI tool for secure peer-to-peer file transfers between computers on the same network. This is a side project I am working on besides my main project of a recycling app. I am open to feedbacks about my code and any further discussions that come with it. Feel free to improve my existing system. Looking forward to connecting with like minded folks! 

## Features
- 🚀 Fast peer-to-peer file transfer
- 🔒 Direct computer-to-computer transfer
- 📊 Real-time progress tracking
- ✨ Simple command-line interface

## Installation

I published a python package:
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
