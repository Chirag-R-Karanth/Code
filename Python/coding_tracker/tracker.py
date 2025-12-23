import argparse
import csv
import datetime
import json

import requests

OUTPUT_FILE = "coding_progress.csv"


# ---------- HELPERS ----------
def fetch_codewars(user):
    try:
        url = f"https://www.codewars.com/users/{user}.json"
        r = requests.get(url, timeout=10).json()

        return {
            "platform": "Codewars",
            "rank": r.get("ranks", {}).get("overall", {}).get("name", "unranked"),
            "honor": r.get("honor", 0),
            "completed_challenges": r.get("codeChallenges", {}).get(
                "totalCompleted", 0
            ),
        }

    except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
        print(f"Error fetching Codewars data for {user}: {e}")
        return None


def fetch_github(user):
    try:
        url = f"https://api.github.com/users/{user}"
        resp = requests.get(url, timeout=10)

        # ✅ Correct error check
        if resp.status_code != 200:
            raise ValueError(f"GitHub API error {resp.status_code}")

        r = resp.json()

        created_at = datetime.datetime.strptime(
            r["created_at"], "%Y-%m-%dT%H:%M:%SZ"
        ).date()

        account_age_days = (datetime.date.today() - created_at).days

        return {
            "platform": "GitHub",
            "public_repos": r.get("public_repos", 0),
            "followers": r.get("followers", 0),
            "following": r.get("following", 0),
            "account_age_days": account_age_days,
        }

    except Exception as e:
        print(f"Error fetching GitHub data for {user}: {e}")
        return None


def fetch_leetcode(user):
    try:
        url = f"https://leetcode-stats-api.herokuapp.com/Chirag-R-Karanth/{user}"
        r = requests.get(url, timeout=10).json()
        return {
            "platform": "LeetCode",
            "total_solved": r.get("totalSolved", 0),
            "easy_solved": r.get("easySolved", 0),
            "medium_solved": r.get("mediumSolved", 0),
            "hard_solved": r.get("hardSolved", 0),
            "ranking": r.get("ranking"),
        }
    except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
        print(f"Error fetching LeetCode data for {user}: {e}")
        return None


# ---------- MAIN ----------
def main():
    parser = argparse.ArgumentParser(
        description="Track coding progress from various platforms."
    )
    parser.add_argument("--codewars")
    parser.add_argument("--leetcode")
    parser.add_argument("--github", help="GitHub username")

    # parser.add_argument("--codeforces")
    args = parser.parse_args()

    today = datetime.date.today().isoformat()
    results = []

    if args.codewars:
        results.append(fetch_codewars(args.codewars))
    if args.leetcode:
        results.append(fetch_leetcode(args.leetcode))
    if args.github:
        results.append(fetch_github(args.github))
    # if args.codeforces:
    #   results.append(fetch_codeforces(args.codeforces))

    results = [r for r in results if r]
    if not results:
        print("No data fetched. Exiting.")
        return

    combined = {"date": today}
    for r in results:
        platform = r.pop("platform").lower()
        for k, v in r.items():
            combined[f"{platform}_{k}"] = v

    rows = []
    try:
        with open(OUTPUT_FILE, "r", newline="") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            fieldnames = sorted(set(reader.fieldnames) | set(combined.keys()))
    except FileNotFoundError:
        fieldnames = sorted(combined.keys())
    else:
        updated = False
        for i, row in enumerate(rows):
            if row["date"] == today:
                rows[i] = {**row, **combined}
                updated = True
                break
        if not updated:
            rows.append(combined)

    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, restval="")
        writer.writeheader()
        writer.writerows(rows)

    print("✅ Data saved to", OUTPUT_FILE)


if __name__ == "__main__":
    main()
