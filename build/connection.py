import os 
from  pathlib import Path 
from dotenv import load_dotenv
from databricks import sql 

env_path =Path(__file__).parent/".env"
load_dotenv(env_path)


def get_connection():
    return sql.connect(server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"))