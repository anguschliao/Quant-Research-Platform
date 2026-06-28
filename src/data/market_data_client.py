from __future__ import annotations

from typing import Any

import pandas as pd

from src.execution.oanda import OandaClient


class MarketDataClient:
    """Provides standardized market data for the rest of the platform."""

    def __init__(self, client: OandaClient | None = None) -> None:
        self.client = client or OandaClient()

    def get_candles(
        self,
        instrument: str,
        granularity: str = "M5",
        count: int = 500,
        price: str = "M",
    ) -> pd.DataFrame:
        """Retrieve candle data and return a standardized DataFrame."""

        response = self.client.get_candles(
            instrument=instrument,
            granularity=granularity,
            count=count,
            price=price,
        )

        rows: list[dict[str, Any]] = []

        for candle in response["candles"]:
            if not candle["complete"]:
                continue

            mid = candle["mid"]

            rows.append(
                {
                    "time": candle["time"],
                    "open": float(mid["o"]),
                    "high": float(mid["h"]),
                    "low": float(mid["l"]),
                    "close": float(mid["c"]),
                    "volume": int(candle["volume"]),
                }
            )

        df = pd.DataFrame(rows)

        if df.empty:
            return df

        df["time"] = pd.to_datetime(df["time"], utc=True)

        return df.sort_values("time").reset_index(drop=True)