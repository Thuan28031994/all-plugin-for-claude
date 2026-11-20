#!/usr/bin/env python3
"""Synchronize Git submodule gitlinks with upstream default/tracked branches.

Uses GitHub's read-only API plus git update-index. Never downloads, installs,
or executes third-party repository files.
"""
import json
import os
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest_path = ROOT / "sources.json"
lock_path = ROOT / "sources-lock.json"


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, text=True, check=True, capture_output=True)


def get_head(repo, branch):
    path = urllib.parse.quote(branch, safe="/")
    url = f"https://api.github.com/repos/{repo}/git/ref/heads/{path}"
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "claude-sources-sync"}
    if os.environ.get("GH_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["GH_TOKEN"]
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=25) as response:
        data = json.load(response)
    ref = data.get("object", {})
    sha = ref.get("sha", "")
    if ref.get("type") != "commit" or len(sha) != 40 or not all(c in "0123456789abcdef" for c in sha):
        raise ValueError(f"Bad upstream ref: {repo}@{branch}")
    return sha


def main():
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    sources = manifest["sources"]
    if not sources:
        raise ValueError("No git submodule sources configured")
    # Resolve every upstream first; fail atomically if any endpoint fails.
    updates = []
    for item in sources:
        repo = item["repository"]
        branch = item["branch"]
        path = item["path"]
        if not path.startswith("plugins/") or ".." in Path(path).parts:
            raise ValueError(f"Unsafe path: {path}")
        sha = get_head(repo, branch)
        updates.append((item, sha))
        print(f"{repo}@{branch}: {sha}", flush=True)

    # Stage all gitlinks, even if local checkout has not initialized submodules.
    for item, sha in updates:
        git("update-index", "--add", "--cacheinfo", "160000", sha, item["path"])

    lock = {
        "schema_version": 1,
        "sources": {
            item["id"]: {"repository": item["repository"], "branch": item["branch"], "sha": sha}
            for item, sha in updates
        },
    }
    lock_path.write_text(json.dumps(lock, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    git("add", "--", "sources-lock.json")
    print("Staged upstream pointers and lockfile", flush=True)


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, subprocess.CalledProcessError, urllib.error.URLError) as error:
        print(f"Sync failed: {error}", file=sys.stderr)
        sys.exit(1)
