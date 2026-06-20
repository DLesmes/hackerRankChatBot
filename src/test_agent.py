import pytest
from unittest.mock import MagicMock, patch

from llama_index.core.agent import ReActAgent
from llama_index.core.tools import QueryEngineTool

from src.engine.hackerrank import hackerrank_engine
from src.prompts import CONTEXT
from src.agent import get_agent, tools, llm

@pytest.fixture
def mock_react_agent():
    """Fixture to create a mock ReActAgent instance"""
    return MagicMock(spec=ReActAgent)

@patch("llama_index.core.agent.ReActAgent.from_tools")
def test_agent_instance(mock_from_tools, mock_react_agent):
    """Test that get_agent returns a properly configured ReActAgent instance"""
    mock_from_tools.return_value = mock_react_agent

    agent = get_agent()

    assert isinstance(agent, ReActAgent), "agent should be an instance of ReActAgent"

    mock_from_tools.assert_called_once_with(
        tools=tools,
        llm=llm,
        context=CONTEXT,
        verbose=True
    )

    assert agent == mock_react_agent, "get_agent should return the mocked instance"

def test_tools_initialization():
    # pylint: disable=import-outside-toplevel
    from src.agent import tools as agent_tools

    assert len(agent_tools) == 1, "There should be exactly 1 tools in the list."

    assert isinstance(
        agent_tools[0], QueryEngineTool
    ), "The second tool should be a QueryEngineTool."
    assert agent_tools[0].query_engine == hackerrank_engine
