# Coding Tracker

This script tracks your progress on competitive programming platforms like CodeWars, LeetCode, and Codeforces. It fetches your stats from their respective APIs and saves them to a CSV file named `coding_progress.csv`.

## Dependencies

The script requires the `requests` library. You can install it using pip:

```bash
pip install requests
```

## Usage

To use the script, you need to provide your usernames for the platforms you want to track using command-line arguments:

```bash
python tracker.py --codewars YOUR_CODEWARS_USERNAME --leetcode YOUR_LEETCODE_USERNAME --codeforces YOUR_CODEFORCES_HANDLE
```

You can provide usernames for one or more platforms. The script will fetch the data for the provided usernames and save it to `coding_progress.csv`.
