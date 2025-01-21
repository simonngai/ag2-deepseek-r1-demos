import autogen
from model_list import (
    config_list_deepseek_reasoner,
)

assistant = autogen.AssistantAgent(
    "assistant",
    llm_config={
        "config_list": config_list_deepseek_reasoner,
    },
)
user_proxy = autogen.UserProxyAgent(
    "user_proxy",
    human_input_mode="NEVER",
    code_execution_config={"work_dir": "coding", "use_docker": False},
)
user_proxy.initiate_chat(
    assistant, message="Save a chart of NVDA and TESLA stock price change YTD."
)
