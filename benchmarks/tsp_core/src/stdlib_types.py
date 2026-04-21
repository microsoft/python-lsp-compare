from pathlib import Path
from collections import defaultdict

path = Path(".")
counts = defaultdict(int)
counts["a"] += 1
