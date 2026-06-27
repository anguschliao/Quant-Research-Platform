from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.execution.oanda import OandaClient


def main() -> int:
    client = OandaClient()

    data = client.get_candles(
        instrument="SPX500_USD",  # change if your OANDA instrument name differs
        granularity="M5",
        count=500,
    )

    rows = []

    for candle in data["candles"]:
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
    df["time"] = pd.to_datetime(df["time"])
    df = df.sort_values("time").reset_index(drop=True)

    output_dir = Path("data/raw")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / "us500_5m.csv"
    df.to_csv(output_path, index=False)

    print(f"Saved {len(df)} candles to {output_path}")
    print(df.head())

    return 0


if __name__ == "__main__":
    raise SystemExit(main())