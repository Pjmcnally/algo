import csv
import os
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
        return list(csv.reader(f))


def parse_csv_data(data):
    last_month_profit = 0
    start_profit = None
    res = {
        "month_count": 0,
        "profit_total": 0,
        "change_avg": 0,
        "max_increase": {
            "month": "",
            "change": 0
        },
        "max_decrease": {
            "month": "",
            "change": 0
        }
    }

    for row in data:
        if row == ['Date', 'Profit/Losses']:
            continue
        else:
            month = row[0]
            profit = int(row[1])
            change = profit - last_month_profit

            res["month_count"] += 1
            res["profit_total"] += profit

            if start_profit is None:
                start_profit = profit

            if change > res["max_increase"]["change"]:
                res["max_increase"]["change"] = change
                res["max_increase"]["month"] = month
            elif change < res["max_decrease"]["change"]:
                res["max_decrease"]["change"] = change
                res["max_decrease"]["month"] = month

            last_month_profit = profit

    end_profit = profit
    res["change_avg"] = (end_profit - start_profit) / (res["month_count"] - 1)

    return res


def format_output(data):
    template = f"""\
        Financial Analysis
        ----------------------------
        Total Months: {data["month_count"]}
        Total: ${data["profit_total"]:,}
        Average Change: ${data["change_avg"]:,.2f}
        Greatest Increase in Profits: {data["max_increase"]["month"]} (${data["max_increase"]["change"]:,})
        Greatest Decrease in Profits: {data["max_decrease"]["month"]} (${data["max_decrease"]["change"]:,})
    """  # noqa: E501

    return dedent(template)


def write_output(file_path, content):
    print(content)
    with open(file_path, "w") as f:
        f.write(content)


main()
