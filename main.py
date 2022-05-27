import csv

if __name__ == "__main__":
    calls_dict_sum = dict()

    with open('phoneCalls.csv', 'r') as fin:
        reader = csv.reader(fin, delimiter=",")
        headers = next(reader)

        for row in reader:
            from_subsr = int(row[0])
            if from_subsr not in calls_dict_sum:
                calls_dict_sum[from_subsr] = 0
            calls_dict_sum[from_subsr] += 1

    najczesciej_call = max(calls_dict_sum.items(), key=lambda x: x[1])

    print(najczesciej_call)
    