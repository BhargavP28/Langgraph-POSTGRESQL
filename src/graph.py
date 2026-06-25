import os

from fastapi import FastAPI
from langchain_core.messages import HumanMessage
from langgraph.graph import START, END, StateGraph
from langgraph.checkpoint.postgres import PostgresSaver

from logger.customlogger import CustomLogger
from config.settings import POSTGRES_URL
from src.chatbot import chatbot
from src.models.state import State
from src.summary import summary
from psycopg import connect



logger = CustomLogger().get_logger(__file__)
builder = StateGraph(State)


def should_continue(state: State) -> str:
    messages = state.get("messages")
    if len(messages) > 6:
        return "summary"
    return END


builder.add_node("llmchat", chatbot)
builder.add_node("summary", summary)

builder.add_edge(START, "llmchat")
builder.add_conditional_edges("llmchat", should_continue)
builder.add_edge("summary", END)


try:
   
   conn = connect(POSTGRES_URL, autocommit= True)

   memory = PostgresSaver(conn)

   graph = builder.compile(checkpointer=memory)
   logger.info("Graph compiled successfully with SQLite checkpointer")
except Exception as e:
    logger.exception(f"failed to initialize graph/checkpointer: {e}")
    raise
