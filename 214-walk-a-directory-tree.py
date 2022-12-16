from collections import Counter
import os
from pathlib import Path

def count_extensions(origin='.', top=10):
    cnt = Counter()
    for root, dirs, files in os.walk(origin):
        for file in files:
            cnt[Path(file).suffix] += 1
    return cnt.most_common(top)

ret = count_extensions()
print(ret)

# [('.py', 1659), ('.pyc', 711), ('.html', 337), ('', 109), ('.txt', 35),
# ('.json', 16), ('.csv', 14), ('.sample', 11), ('.exe', 10), ('.png', 9)]