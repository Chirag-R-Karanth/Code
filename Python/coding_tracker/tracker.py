import requests
import json
import datetime
import csv
import argparse

# ---------- CONFIG ----------
OUTPUT_FILE = "coding_progress.csv"


# ---------- HELPERS ----------
def fetch_codewars(user):
    try:
        url = f"https://www.codewars.com/api/v1/users/{user}"
        r = requests.get(url).json()
        return {
            "platform": "Codewars",
            "rank": r["ranks"]["overall"]["name"],
            "honor": r["honor"],
            "completed_challenges": r["codeChallenges"]["totalCompleted"],
        }
    except (requests.exceptions.RequestException, KeyError) as e:
        print(f"Error fetching Codewars data for {user}: {e}")
        return None


def fetch_leetcode(user):
    try:
        url = "https://leetcode-stats-api.herokuapp.com/" + user
        r = requests.get(url).json()
        return {
            "platform": "LeetCode",
            "total_solved": r.get("totalSolved", 0),
            "easy_solved": r.get("easySolved", 0),
            "medium_solved": r.get("mediumSolved", 0),
            "hard_solved": r.get("hardSolved", 0),
            "ranking": r.get("ranking", None),
        }
    except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
        print(f"Error fetching LeetCode data for {user}: {e}")
        return None


def fetch_codeforces(user):
    try:
        url = f"https://codeforces.com/api/user.info?handles={user}"
        r = requests.get(url).json()["result"][0]
        return {
            "platform": "Codeforces",
            "rank": r.get("rank", "unrated"),
            "rating": r.get("rating", 0),
            "maxRank": r.get("maxRank", "unrated"),
            "maxRating": r.get("maxRating", 0),
        }
    except (requests.exceptions.RequestException, KeyError) as e:
        print(f"Error fetching Codeforces data for {user}: {e}")
        return None


# ---------- MAIN ----------
def main():
    parser = argparse.ArgumentParser(description="Track coding progress from various platforms.")
    parser.add_argument("--codewars", help="Codewars username")
    parser.add_argument("--leetcode", help="LeetCode username")
    parser.add_argument("--codeforces", help="Codeforces handle")
    args = parser.parse_args()

    today = datetime.date.today().isoformat()
    results = []

    if args.codewars:
        results.append(fetch_codewars(args.codewars))
    if args.leetcode:
        results.append(fetch_leetcode(args.leetcode))
    if args.codeforces:
        results.append(fetch_codeforces(args.codeforces))

    results = [r for r in results if r]  # Filter out None results from failed fetches

    if not results:
        print("No data fetched. Exiting.")
        return

    # Save to CSV
    all_keys = set()
    for r in results:
        all_keys.update(r.keys())

    fieldnames = ["date"] + sorted(list(all_keys))

    # Combine results into a single dictionary
    combined_results = {"date": today}
    for r in results:
        platform = r.pop("platform").lower()
        for key, value in r.items():
            combined_results[f"{platform}_{key}"] = value

    # Save to CSV
    fieldnames = sorted(combined_results.keys())

    try:
        with open(OUTPUT_FILE, 'r+', newline='') as f:
            # Read existing data
            reader = csv.DictReader(f)
            rows = list(reader)
            fieldnames = reader.fieldnames

            # Update today's row if it exists
            updated = False
            for i, row in enumerate(rows):
                if row['date'] == today:
                    rows[i] = {**row, **combined_results}
                    updated = True
                    break

            if not updated:
                rows.append(combined_results)

            # Write back to the file
            f.seek(0)
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore', restval='')
            writer.writeheader()
            writer.writerows(rows)
            f.truncate()

    except FileNotFoundError:
        with open(OUTPUT_FILE, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore', restval='')
            writer.writeheader()
            writer.writerow(combined_results)

    print("Data saved to", OUTPUT_FILE)


if __name__ == "__main__":
    main()
