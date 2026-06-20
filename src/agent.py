"""Agent Initialization"""

from llama_index.core.agent import ReActAgent
from llama_index.core.tools import QueryEngineTool, ToolMetadata

from src import llm
from src.engine.hackerrank import hackerrank_engine
from src.prompts import CONTEXT, TOOL_DESCRIPTION, TOOL_NAME

tools = []

tools.append(
    QueryEngineTool(
        hackerrank_engine,
        metadata=ToolMetadata(
            description=TOOL_DESCRIPTION,
            name=TOOL_NAME,
        ),
    )
)


def get_agent():
    """Returns ReActAgent"""
    # return ReActAgent.from_tools(tools=tools, llm=llm, context=CONTEXT, verbose=True)
    return ReActAgent.from_tools(tools, llm=llm, context=CONTEXT, verbose=True)
