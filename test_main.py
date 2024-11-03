import pandas as pd
from main import generate_summary_stats, get_true_accuracy


def test_summary_stats():
    stats = generate_summary_stats(
        "https://github.com/fivethirtyeight/data/raw/refs/heads/master/historical-ncaa-forecasts/historical-538-ncaa-tournament-model-results.csv"
    )
    assert stats.loc["mean"]["favorite_probability"] == 0.721383


def test_accuracy():
    ncaa_data = pd.read_csv(
        "https://github.com/fivethirtyeight/data/raw/refs/heads/master/historical-ncaa-forecasts/historical-538-ncaa-tournament-model-results.csv"
    )
    acc_data = get_true_accuracy(ncaa_data)
    assert acc_data.loc[0, "actual_win_percents"] == 0.6031746031746031
