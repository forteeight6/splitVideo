from os import walk, path
import re

def Browse():
    for root, _, files in walk("cache"):
        for file in files:
            local = path.join(root, file)
            yield local

def BrowsePrefix(prefix):
    for root, _, files in walk("cache"):
        for file in files:
            local = path.join(root, file)
            ver = re.search(f"^{prefix}", file)
            if ver:
                return local
                
def BrowseSuffix(suffix):
    for root, _, files in walk("cache"):
        for file in files:
            local = path.join(root, file)
            ver = re.search(f"{suffix}$", file)
            if ver:
                return local

def BrowsePrefixSuffix(prefix, suffix):
    for root, _, files in walk("cache"):
        for file in files:
            local = path.join(root, file)
            ver = re.search(f"^{prefix}.*{suffix}$", file)
            if ver:
                return local


