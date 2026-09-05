import hashlib
import json
import os
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

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def acquire_data(force: bool = False) -> str:
    manifest_entries = []

    for src in DATA_SOURCES:
        os.makedirs(src["dest_dir"], exist_ok=True)
        dest_path = os.path.join(src["dest_dir"], src["filename"])
        
        need_download = force or not os.path.exists(dest_path)
        if not need_download and os.path.getsize(dest_path) > 10_000_000:
            import openpyxl
            try:
                wb = openpyxl.load_workbook(dest_path, read_only=True)
                _ = wb.sheetnames
                wb.close()
                print(f"[Acquire] Verified valid existing file: {dest_path}")
            except Exception:
                print(f"[Acquire] File {dest_path} corrupted/invalid, re-downloading...")
                need_download = True

        if need_download:
            print(f"[Acquire] Downloading {src['url']} -> {dest_path}...")
            response = requests.get(src["url"], headers=HEADERS, stream=True, timeout=120)
            response.raise_for_status()
            
            sha256 = hashlib.sha256()
            total_bytes = 0
            with open(dest_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=1048576):
                    if chunk:
                        f.write(chunk)
                        sha256.update(chunk)
                        total_bytes += len(chunk)
            print(f"[Acquire] Download complete: {dest_path} ({total_bytes} bytes)")

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

    print(f"[Acquire] Manifest saved to {manifest_path}")
    return manifest_path

if __name__ == "__main__":
    acquire_data()
