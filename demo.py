"""
Sphinx 2.4.0-2.4.1 bug
"""

print(__name__)
from typing import Optional

def pony(c,
         a,  # type: str
         b=None  # type: Optional[str]
         ):
    # type: (...) -> str
    return a + (b or "")
