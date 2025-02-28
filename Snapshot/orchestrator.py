import getSnapshots as gs
import getSnapShotExport as ge
import os

# Base URL for API requests
url_base = "https://api.staging.landing.ai/v1/projects"
# API key for authentication
api_key = "land_sk_ZF74SGID25P4saw8z2iizbB8SgEidk1FMIBzPP4MrNRSKyMn0a"  # Org: landing
# Project ID
project_id = 27689531707438
# URL
url = f"{url_base}/{project_id}/dataset/snapshots"

listSnapShots = gs.listSnapShots(api_key, url)
print(listSnapShots)
lastSnapShot = gs.display_snapshot(listSnapShots)

snapshot_version = listSnapShots["version"]
print(snapshot_version)

url = f"{url_base}/{project_id}/dataset/snapshots/{snapshot_version}/export"
print(url)
export = ge.SnapShotExport(api_key, url)
print(export)

# output_filename = f"C:/Users/user/Desktop/API-s-/Snapshot/project_{project_id}_version_{snapshot_version}_downloaded_file.tar.bz2"
output_filename = os.path.join(
    "Snapshot", f"project_{project_id}_version_{snapshot_version}_downloaded_file.tar.bz2"
)
url = export["downloadUrl"]
print(url)
ge.download_file_from_url(url=url, local_filename=output_filename)
