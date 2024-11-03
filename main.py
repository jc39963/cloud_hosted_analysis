import pandas as pd

ncaa_data = pd.read_csv(
    "https://github.com/fivethirtyeight/data/raw/refs/heads/master/historical-ncaa-forecasts/historical-538-ncaa-tournament-model-results.csv"
)


def generate_summary_stats(filename):
    ncaa_data = pd.read_csv(filename)
    return ncaa_data["favorite_probability"].describe()


def get_true_accuracy(ncaa_data):
    bins = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    labels = [
        "50.0 - 59.9%",
        "60.0 - 69.9%",
        "70.0 - 79.9%",
        "80.0 - 89.9%",
        "90.0 - 99.9%",
    ]
    ncaa_data["probability_bin"] = pd.cut(
        ncaa_data["favorite_probability"], bins=bins, labels=labels, right=False
    )
    accuracy_data = (
        ncaa_data.groupby("probability_bin")
        .agg(
            total_games=("favorite_win_flag", "size"),
            won_games=("favorite_win_flag", "sum"),
        )
        .reset_index()
    )
    accuracy_data["actual_win_percents"] = (
        accuracy_data["won_games"] / accuracy_data["total_games"]
    )
    return accuracy_data


if __name__ == "__main__":
    filename = "https://github.com/fivethirtyeight/data/raw/refs/heads/master/historical-ncaa-forecasts/historical-538-ncaa-tournament-model-results.csv"
    ncaa_data = pd.read_csv(filename)
    generate_summary_stats(filename)
    get_true_accuracy(ncaa_data)
