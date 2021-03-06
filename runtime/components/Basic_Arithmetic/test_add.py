import pandas as pd
from .add import main


def test_numeric():
    assert main(a=17.3, b=16.7)["sum"] == 34.0


def test_series_numeric():
    assert main(
        a=pd.Series(
            {
                "2019-08-01T15:20:12": 1.2,
                "2019-08-01T15:44:12": 0.0,
                "2019-08-03T16:20:15": 0.3,
                "2019-08-05T12:00:34": 0.5,
            }
        ),
        b=-6,
    )["sum"].equals(
        pd.Series(
            {
                "2019-08-01T15:20:12": -4.8,
                "2019-08-01T15:44:12": -6.0,
                "2019-08-03T16:20:15": -5.7,
                "2019-08-05T12:00:34": -5.5,
            }
        )
    )


def test_series_series():
    assert main(
        a=pd.Series(
            {
                "2019-08-01T15:20:12": 1.2,
                "2019-08-01T15:44:12": 0.0,
                "2019-08-03T16:20:15": 0.3,
                "2019-08-05T12:00:34": 0.5,
            }
        ),
        b=pd.Series(
            {
                "2019-08-01T15:20:12": 1.1,
                "2019-08-01T15:44:12": 1.2,
                "2019-08-03T16:20:15": 1.3,
                "2019-08-05T12:00:34": 1.4,
            }
        ),
    )["sum"].equals(
        pd.Series(
            {
                "2019-08-01T15:20:12": 2.3,
                "2019-08-01T15:44:12": 1.2,
                "2019-08-03T16:20:15": 1.6,
                "2019-08-05T12:00:34": 1.9,
            }
        )
    )


def test_series_empty():
    assert main(a=pd.Series(dtype=float), b=-6)["sum"].empty


def test_df_df():
    assert main(
        a=pd.DataFrame(
            {
                "a": {
                    "2019-08-01T15:20:12": 1.2,
                    "2019-08-01T15:44:12": 7.2,
                    "2019-08-03T16:20:15": 0.3,
                    "2019-08-05T12:00:34": 0.5,
                },
                "b": {
                    "2019-08-01T15:20:12": 7.2,
                    "2019-08-01T15:44:12": 7.0,
                    "2019-08-03T16:20:15": 7.3,
                    "2019-08-05T12:00:34": 7.5,
                },
            }
        ),
        b=pd.DataFrame(
            {
                "a": {
                    "2019-08-01T15:20:12": 1.2,
                    "2019-08-01T15:44:12": 7.2,
                    "2019-08-03T16:20:15": 0.3,
                    "2019-08-05T12:00:34": 0.5,
                },
                "b": {
                    "2019-08-01T15:20:12": 7.2,
                    "2019-08-01T15:44:12": 7.0,
                    "2019-08-03T16:20:15": 7.3,
                    "2019-08-05T12:00:34": 7.5,
                },
            }
        ),
    )["sum"].equals(
        pd.DataFrame(
            {
                "a": {
                    "2019-08-01T15:20:12": 2.4,
                    "2019-08-01T15:44:12": 14.4,
                    "2019-08-03T16:20:15": 0.6,
                    "2019-08-05T12:00:34": 1.0,
                },
                "b": {
                    "2019-08-01T15:20:12": 14.4,
                    "2019-08-01T15:44:12": 14.0,
                    "2019-08-03T16:20:15": 14.6,
                    "2019-08-05T12:00:34": 15.0,
                },
            }
        )
    )

    def test_df_empty():
        assert main(a=pd.DataFrame(dtype=float), b=-6)["sum"].empty

