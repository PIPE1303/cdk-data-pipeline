import os, json, gzip, io, urllib.request, datetime
from typing import Any, Dict

BUCKET = os.environ["DATA_BUCKET_NAME"]
API_URL = os.environ.get("API_URL", "https://randomuser.me/api/?results=100")

def fetch_json(url: str) -> Dict[str, Any]:
    with urllib.request.urlopen(url) as resp:
        return json.loads(resp.read().decode("utf-8"))

def handler(event, context):
    payload = fetch_json(API_URL)
    records = payload.get("results", [])

    buf = io.BytesIO()
    with gzip.GzipFile(fileobj=buf, mode="wb") as gz:
        for rec in records:
            line = json.dumps(rec, separators=(",", ":")).encode("utf-8")
            gz.write(line + b"\n")

    import boto3
    s3 = boto3.client("s3")
    today = datetime.date.today().isoformat()
    key = f"raw/randomuser/ingestion_date={today}/batch.jsonl.gz"
    s3.put_object(Bucket=BUCKET, Key=key, Body=buf.getvalue())

    return {"written": len(records), "s3_key": key}
