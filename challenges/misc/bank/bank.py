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
    template = """\
        Financial Analysis
        ----------------------------
        Total Months: {month_count}
        Total: ${profit_total:,}
        Average Change: ${change_avg:,.2f}
        Greatest Increase in Profits: {max_inc_month} (${max_inc_value:,})
        Greatest Decrease in Profits: {max_dec_month} (${max_dec_value:,})
    """.format(
        month_count=data["month_count"],
        profit_total=data["profit_total"],
        change_avg=data["change_avg"],
        max_inc_month=data["max_increase"]["month"],
        max_inc_value=data["max_increase"]["change"],
        max_dec_month=data["max_decrease"]["month"],
        max_dec_value=data["max_decrease"]["change"],
    )

    return dedent(template)


def write_output(file_path, content):
    print(content)
    with open(file_path, "w") as f:
        f.write(content)


main()
