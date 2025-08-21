from services.load_data.from_mongo import AtlasClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
user = os.getenv("USER")
conn = os.getenv("CONN")
password = os.getenv("PASSWORD")
db_name = os.getenv("DB_NAME")
collection = os.getenv("COLLECTION")

atlas_client = AtlasClient (conn, db_name)
atlas_client.ping()
print(atlas_client.find(collection))
print ('Connected to Atlas instance! We are good to go!')