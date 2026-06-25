import sys
import os

# add project root path
sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from langgraph.checkpoint.postgres import PostgresSaver
from config.settings import POSTGRES_URL


with PostgresSaver.from_conn_string(POSTGRES_URL) as checkpointer:
    checkpointer.setup()


print("LangGraph PostgreSQL tables created successfully")