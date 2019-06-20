import os
import pandas as pd
from collections import Counter
from textwrap import dedent


def main():
    basepath = os.path.dirname(__file__)
    src_path = os.path.join(basepath, 'data.csv')
    out_path = os.path.join(basepath, 'output.txt')

    data = read_csv_data(src_path)
    res = parse_csv_data(data)
    out_str = format_output(res)
    write_output(out_path, out_str)


def read_csv_data(src):
    with open(src, "r") as f:
        return pd.read_csv(f)


def parse_csv_data(data):
    return Counter(data["Candidate"])


def format_output(data):
    total_votes = sum(data.values())
    winner_name = data.most_common()[0][0]

    header = f"""\
        Election Results
        -------------------------
        Total Votes: {total_votes:,}
        -------------------------
    """

    tally_str = ""
    for candidate, votes in data.most_common():
        percent = (votes / total_votes) * 100
        tally_str += f"{candidate}: {percent:.3f}% ({votes:,})\n"

    footer = f"""\
        -------------------------
        Winner: {winner_name}
        -------------------------
    """

    return dedent(header) + tally_str + dedent(footer)


def write_output(file_path, content):
    print(content)
    with open(file_path, "w") as f:
        f.write(content)


main()
