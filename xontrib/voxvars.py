"""
Loads a dotenv when a vox environment is activated.

Supported syntax is based on the original JS dotenv module.
"""

import xontrib.voxapi as voxapi
from pathlib import Path

__all__ = ()


def parse_stream(fobj):
    for line in fobj:
        if '=' not in line:
            continue
        key, value = line.split('=', 1)
        key = key.strip()
        value = value.strip()

        if value.startswith("'") and value.endswith("'"):
            # Just a simple string
            value = value[1:-1]
        elif value.startswith('"') and value.endswith('"'):
            # Allows \n to mean newline
            value = value[1:-1].replace(r"\n", "\n")

        yield key, value


def get_venv_root(env):
    vox = voxapi.Vox()
    return Path(vox[env].env)


@events.vox_on_activate
def activate_handler(name, **_):
    try:
        root = get_venv_root(name)
    except KeyError:
        return

    envpath = root / 'dotenv'

    if envpath.is_file():
        with envpath.open('rt') as f:
            for key, value in parse_stream(f):
                __xonsh__.env[key] = value


@events.vox_on_deactivate
def deactivate_handler(name, **_):
    # FIXME: What's the right undo algorithm and where do we source that information?
    ...


def cmd(args, stdin=None):
    ...


aliases['voxvars'] = cmd
