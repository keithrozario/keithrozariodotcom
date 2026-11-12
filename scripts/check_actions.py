#!/usr/bin/env python3
"""CLI script to display the status and date of the latest GitHub Action runs."""

import argparse
import os
from github import Auth, Github

DEFAULT_REPO = "keithrozario/keithrozariodotcom"
STATUS_ICONS = {
    "success": "✅",
    "failure": "❌",
    "cancelled": "⚪",
    "skipped": "⏭️",
}


def format_run(run) -> str:
    icon = STATUS_ICONS.get(run.conclusion, "⏳" if run.status != "completed" else "ℹ️")
    status_str = f"{run.status} ({run.conclusion})" if run.conclusion else run.status
    local_date = run.created_at.astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
    return f"{icon} [{local_date}] {run.name} — \"{run.display_title}\" | Status: {status_str}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Check the latest GitHub Action runs.")
    parser.add_argument("-n", "--limit", type=int, default=3, help="Number of latest runs to display (default: 3)")
    parser.add_argument("-r", "--repo", default=DEFAULT_REPO, help=f"GitHub repository (default: {DEFAULT_REPO})")
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    gh = Github(auth=Auth.Token(token)) if token else Github()
    runs = list(gh.get_repo(args.repo).get_workflow_runs()[: args.limit])

    print(f"Latest {len(runs)} GitHub Action runs for {args.repo}:\n")
    print("\n".join([format_run(run) for run in runs]))


if __name__ == "__main__":
    main()
