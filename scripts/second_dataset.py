from __future__ import annotations

from pathlib import Path

from src.data import MarketDataClient
from src.config.logging import setup_logging


def main() -> int:
    setup_logging()

    output_path = Path("data/raw/us500_5m_second.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    client = MarketDataClient()

    df = client.get_candles(
        instrument="SPX500_USD",
        granularity="M5",
        count=500,
    )

    df.to_csv(output_path, index=False)

    print(f"Saved {len(df)} candles to {output_path}")
    print(df.head())

    return 0


if __name__ == "__main__":
    raise SystemExit(main())