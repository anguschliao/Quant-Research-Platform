from __future__ import annotations

from typing import Any

import requests

from src.config.settings import settings


class OandaClient:
    def __init__(self) -> None:
        self.base_url = settings.oanda_api_url.rstrip("/")
        self.account_id = settings.oanda_account_id
        self.api_key = settings.oanda_api_key

        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def get_account_summary(self) -> dict[str, Any]:
        url = f"{self.base_url}/v3/accounts/{self.account_id}/summary"

        response = requests.get(
            url,
            headers=self.headers,
            timeout=15,
        )

        response.raise_for_status()
        return response.json()

    def get_candles(
    self,
    instrument: str,
    granularity: str = "M5",
    count: int = 500,
    price: str = "M",
    ) -> dict[str, Any]:
        
    url = f"{self.base_url}/v3/instruments/{instrument}/candles"

    params = {
        "granularity": granularity,
        "count": count,
        "price": price,
    }

    response = requests.get(
        url,
        headers=self.headers,
        params=params,
        timeout=15,
    )

    response.raise_for_status()
    return response.json()