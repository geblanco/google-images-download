import json
import argparse
from google_images_download import google_images_download

QUERY_TPL = "{term} diagram"

parser = argparse.ArgumentParser()
parser.add_argument("--term", required=True, type=str)
parser.add_argument("--limit", type=int, default=10)
parser.add_argument("--logs", action="store_true")
parser.add_argument("--output_dir", type=str, default="/tmp/test_queries")

args = parser.parse_args()
query = QUERY_TPL.format(term=args.term)

name_map = {query: "1"}

arguments = dict(
    keywords=query,
    limit=args.limit,
    print_paths=False,
    output_directory=args.output_dir,
    silent_mode=False,
    image_directory="long_test",
    print_urls=True,
    extract_metadata=args.logs,
    name_map=name_map,
)

print(f"Querying {json.dumps(arguments, indent=2)}")
downloader = google_images_download.googleimagesdownload()
downloader.download(arguments)
