from dotenv import load_dotenv
import os
from services.utils.mongo_dataframe_converter import ConvertToDF
from services.data_processing.process_data import DataProcessing
from services.load_data.from_mongo import AtlasClient
# Load environment variables from .env file


class Manager:
    @staticmethod
    def manager():
        load_dotenv()
        user = os.getenv("USER")
        conn = os.getenv("CONN")
        password = os.getenv("PASSWORD")
        db_name = os.getenv("DB_NAME")
        collection = os.getenv("COLLECTION")
        atlas_client = AtlasClient (conn, db_name)
        atlas_client.ping()
        convert_to_df = ConvertToDF.convert(atlas_client.find(collection))
        data_processing = DataProcessing(convert_to_df)
        result = data_processing.all_tweets()
        return result