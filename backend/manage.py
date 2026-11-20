#!/usr/bin/env python
"""Django command-line utility for administrative tasks."""

import os
import sys
from pathlib import Path

if __name__ == "__main__":
    backend_root = Path(__file__).resolve().parent
    sys.path.insert(0, str(backend_root))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
