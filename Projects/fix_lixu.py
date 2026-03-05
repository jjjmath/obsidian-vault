# -*- coding: utf-8 -*-
import os
import re

base_path = r"d:\高中数学math\obsidian-vault\Projects\理序之路"

renames = [
    (r"恒成立有解问题🚀\.md", "恒成立有解问题.md"),
]

count = 0
for root, dirs, files in os.walk(base_path):
    for filename in files:
        if filename.endswith('.md'):
            original = filename
            for pattern, replacement in renames:
                if re.search(pattern, filename):
                    filename = re.sub(pattern, replacement, filename)

            if filename != original:
                old_path = os.path.join(root, original)
                new_path = os.path.join(root, filename)
                try:
                    os.rename(old_path, new_path)
                    print(f"OK: {original} -> {filename}")
                    count += 1
                except Exception as e:
                    print(f"FAIL: {original} - {e}")

print(f"\nDone! Renamed {count} files")
