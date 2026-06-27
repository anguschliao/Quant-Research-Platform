from __future__ import annotations

from requests.exceptions import HTTPError, RequestException

from src.execution import OandaClient


def main() -> int:
    try:
        client = OandaClient()
        response = client.get_account_summary()

        account = response["account"]

        print("Connected to OANDA")
        print(f"Account ID : {account['id']}")
        print(f"Currency   : {account['currency']}")
        print(f"Balance    : {account['balance']}")
        print(f"Open Trades: {account['openTradeCount']}")

        return 0

    except HTTPError as error:
        print("OANDA rejected the request.")
        print(error)
        return 1

    except RequestException as error:
        print("Could not connect to OANDA.")
        print(error)
        return 1

    except KeyError as error:
        print("Connected, but response format was unexpected.")
        print(error)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())