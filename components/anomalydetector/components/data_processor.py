import pandas as pd
POLITICIANS_CSV = r"/Users/razcro/PycharmProjects/Tepes.AI/components/anomalydetector/data/politicians.csv"
def process_data(path):
    df = pd.read_csv(path)

    with open("/Users/razcro/PycharmProjects/Tepes.AI/components/anomalydetector/data/politicians_nn.csv", "w+") as f:
        f.write("full_name, total_assets\n")
        for index, row in df.iterrows():
            full_name = row['first_name'] + "-" + row['last_name']
            try:
                investments = int(row['investments'].split(" ")[0])
                if "eur" not in row['investments'].lower():
                    investments //= 5
            except:
                investments = 0
            try:
                assets = int(row['assets'].split(" ")[0])
                if "eur" not in row['assets'].lower():
                    assets //= 5
            except:
                assets = 0
            salary = int(row['salary'].split(" ")[0])
            if "eur" not in row['salary'].lower():
                salary //= 5
            debts = int(row['debts'].split(" ")[0])
            if "eur" not in row['debts'].lower():
                debts //= 5
            value = investments + assets + salary - debts
            print(full_name, value)
            f.write(full_name + ", " + str(value) + ", " + "\n")
    # print(df.to_string())

if __name__ == "__main__":
    process_data(POLITICIANS_CSV)