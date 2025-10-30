# helpers/retry_helper.py
import time
from requests.exceptions import ReadTimeout, ConnectionError

def retry_nba_call(fn, *args, retries=3, backoff=2, **kwargs):
    """
    Call fn(*args, **kwargs), retrying on ReadTimeout or ConnectionError.
    backoff is the base wait time in seconds (doubles each retry).
    """
    for attempt in range(1, retries + 1):
        try:
            return fn(*args, **kwargs)
        except (ReadTimeout, ConnectionError) as e:
            if attempt == retries:
                raise
            wait = backoff * (2 ** (attempt - 1))
            print(f"⚠ NBA API error ({e}), retry {attempt}/{retries} in {wait}s…")
            time.sleep(60)
