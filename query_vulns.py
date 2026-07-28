#!/usr/bin/env python3
"""Query helper for vulnerability-database.json.

Usage:
  ./query_vulns.py --category "Injection (Core)"
  ./query_vulns.py --cwe CWE-89
  ./query_vulns.py --severity Critical
  ./query_vulns.py --search "header"
  ./query_vulns.py --list-categories
  ./query_vulns.py --id 39
"""
import json
import argparse
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vulnerability-database.json")


def load():
    with open(DB_PATH) as f:
        return json.load(f)


def show(entry):
    print(f"\n[{entry['id']}] {entry['name']}  ({entry['category']})")
    print(f"  CWE:        {entry['cwe']}")
    print(f"  Severity:   {entry['severity_range']}")
    print(f"  Desc:       {entry['description']}")
    print(f"  Detect:     {entry['detection_method']}")
    print(f"  Payload:    {entry['example_payload']}")
    print(f"  Fix:        {entry['remediation']}")
    print(f"  Reference:  {entry['real_world_reference']}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--category", help="filter by exact category name")
    p.add_argument("--cwe", help="filter by CWE id, e.g. CWE-89")
    p.add_argument("--severity", help="substring match on severity_range, e.g. Critical")
    p.add_argument("--search", help="case-insensitive substring search across name/description")
    p.add_argument("--id", type=int, help="show a single entry by id")
    p.add_argument("--list-categories", action="store_true", help="list all categories with counts")
    args = p.parse_args()

    data = load()
    vulns = data["vulnerabilities"]

    if args.list_categories:
        counts = {}
        for v in vulns:
            counts[v["category"]] = counts.get(v["category"], 0) + 1
        for cat, n in sorted(counts.items()):
            print(f"{n:3d}  {cat}")
        print(f"\nTotal: {len(vulns)} entries across {len(counts)} categories")
        return

    if args.id is not None:
        match = [v for v in vulns if v["id"] == args.id]
        for v in match:
            show(v)
        return

    results = vulns
    if args.category:
        results = [v for v in results if v["category"].lower() == args.category.lower()]
    if args.cwe:
        results = [v for v in results if v["cwe"].lower() == args.cwe.lower()]
    if args.severity:
        results = [v for v in results if args.severity.lower() in v["severity_range"].lower()]
    if args.search:
        s = args.search.lower()
        results = [v for v in results if s in v["name"].lower() or s in v["description"].lower()]

    if not any([args.category, args.cwe, args.severity, args.search]):
        print(f"No filter given. Database has {len(vulns)} total entries. Use --help for options.")
        return

    print(f"{len(results)} match(es):")
    for v in results:
        show(v)


if __name__ == "__main__":
    main()
