# URL Parsing
from urllib.parse import urlparse

url = "https://www.example.com/path/page?query=123"
parsed_url = urlparse(url)
print("Scheme:", parsed_url.scheme)
print("Netloc:", parsed_url.netloc)
print("Path:", parsed_url.path)
print("Query:", parsed_url.query)
