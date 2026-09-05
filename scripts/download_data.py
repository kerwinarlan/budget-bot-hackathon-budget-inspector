import hashlib
import json
import os
import sys
from datetime import datetime, timezone
import requests

DATA_SOURCES = [
    {
        "fiscal_year": 2025,
        "filename": "GAA-2025.xlsx",
        "url": "https://www.dbm.gov.ph/wp-content/uploads/GAA/GAA2025/GAA-2025.xlsx",
        "source_page": "https://www.dbm.gov.ph/index.php/2025/general-appropriations-act-gaa-fy-2025",
        "document_type": "GAA_EXCEL",
        "dest_dir": "raw/2025"
    },
    {
        "fiscal_year": 2026,
        "filename": "FY2026-GAA-Byobject.xlsx",
        "url": "https://www.dbm.gov.ph/wp-content/uploads/GAA/GAA2026/FY2026-GAA-Byobject.xlsx",
        "source_page": "https://www.dbm.gov.ph/index.php/2026/general-appropriations-act-gaa-fy-2026",
        "document_type": "GAA_EXCEL",
        "dest_dir": "raw/2026"
    }
]

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

manifest_entries = []

for src in DATA_SOURCES:
    os.makedirs(src["dest_dir"], exist_ok=True)
    dest_path = os.path.join(src["dest_dir"], src["filename"])
    
    need_download = True
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 10_000_000:
        print(f"File {dest_path} already exists ({os.path.getsize(dest_path)} bytes). Verifying integrity...")
        # Check if zipfile/openpyxl can open it
        import openpyxl
        try:
            wb = openpyxl.load_workbook(dest_path, read_only=True)
            sheet_names = wb.sheetnames
            wb.close()
            print(f"File {dest_path} is a valid Excel workbook with sheets: {sheet_names}")
            need_download = False
        except Exception as e:
            print(f"File {dest_path} is incomplete or invalid ({e}), re-downloading...")
            need_download = True

    if need_download:
        print(f"Downloading {src['url']} -> {dest_path}...")
        response = requests.get(src["url"], headers=headers, stream=True, timeout=120)
        response.raise_for_status()
        
        sha256 = hashlib.sha256()
        total_bytes = 0
        with open(dest_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1048576):
                if chunk:
                    f.write(chunk)
                    sha256.update(chunk)
                    total_bytes += len(chunk)
                    print(f"  Downloaded {total_bytes / (1024*1024):.1f} MB...")
        print(f"Downloaded finished: {dest_path}")

    # Compute hash and size
    sha256 = hashlib.sha256()
    with open(dest_path, "rb") as f:
        while chunk := f.read(1048576):
            sha256.update(chunk)
    hash_hex = sha256.hexdigest()
    file_size = os.path.getsize(dest_path)

    entry = {
        "fiscal_year": src["fiscal_year"],
        "filename": src["filename"],
        "filepath": dest_path,
        "source_url": src["url"],
        "source_page": src["source_page"],
        "retrieval_timestamp": datetime.now(timezone.utc).isoformat(),
        "file_size_bytes": file_size,
        "sha256": hash_hex,
        "document_type": src["document_type"]
    }
    manifest_entries.append(entry)

os.makedirs("data/manifests", exist_ok=True)
manifest_path = "data/manifests/manifest.json"
with open(manifest_path, "w") as f:
    json.dump({"manifest_version": "1.0", "sources": manifest_entries}, f, indent=2)

print(f"Saved manifest to {manifest_path}")
