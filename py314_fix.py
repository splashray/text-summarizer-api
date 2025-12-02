"""
Workaround for Python 3.14 + Pydantic compatibility issue
Import this before importing FastAPI
"""
import typing
import sys

# Patch for Python 3.14 compatibility
if sys.version_info >= (3, 14):
    _original_eval_type = typing._eval_type
    
    def _patched_eval_type(value, globalns, localns, *args, **kwargs):
        # Remove unsupported kwargs for Python 3.14
        kwargs.pop('prefer_fwd_module', None)
        return _original_eval_type(value, globalns, localns, *args)
    
    typing._eval_type = _patched_eval_type
