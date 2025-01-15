# SPDX-FileCopyrightText: 2025-present c1au6i0 <claudio.zanettini@gmail.com>
#
# SPDX-License-Identifier: MIT

# Taken from pandas -----
# Let users know if they're missing any of our hard dependencies
_hard_dependencies = ("requests", "rich", "pandas")
_missing_dependencies = []

for _dependency in _hard_dependencies:
    try:
        __import__(_dependency)
    except ImportError as _e:  # pragma: no cover
        _missing_dependencies.append(f"{_dependency}: {_e}")

if _missing_dependencies:  # pragma: no cover
    raise ImportError(
        "Unable to import required dependencies:\n" + "\n".join(_missing_dependencies)
    )
del _hard_dependencies, _dependency, _missing_dependencies


# from pandas._config import (
#    get_option,
#    set_option,
#    reset_option,
#   describe_option,
#    option_context,
#   options,
# )