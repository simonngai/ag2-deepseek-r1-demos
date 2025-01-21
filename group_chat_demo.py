import autogen
from model_list import (
    config_list_openai_4o_mini,
    config_list_deepseek_reasoner,
)

user_proxy = autogen.UserProxyAgent(
    "user_proxy",
    human_input_mode="NEVER",
    code_execution_config={"work_dir": "coding", "use_docker": False},
)

supervisor = autogen.AssistantAgent(
    "supervisor",
    llm_config={
        "config_list": config_list_deepseek_reasoner,
    },
)


assistant = autogen.AssistantAgent(
    "assistant",
    llm_config={
        "config_list": config_list_deepseek_reasoner,
    },
)


groupchat = autogen.GroupChat(
    agents=[user_proxy, supervisor, assistant],
    messages=["A group chat"],
    max_round=5,
)

manager = autogen.GroupChatManager(
    groupchat=groupchat,
    llm_config={
        # Error is expected using deepseek_reasoner as manager
        # "config_list": config_list_deepseek_reasoner,
        #############
        # raise self._make_status_error_from_response(err.response) from None
        # openai.BadRequestError: Error code: 400 -
        # {'error': {'message': 'The last message of deepseek-reasoner must be a user message,
        # or an assistant message with prefix mode on (refer to https://api-docs.deepseek.com/guides/chat_prefix_completion).',
        # 'type': 'invalid_request_error', 'param': None, 'code': 'invalid_request_error'}}
        #############
        
        
        # Another expected using openai_4o_mini as manager
        "config_list": config_list_openai_4o_mini,
        #############
        # Error code: 400 - {'error': {'message': 'deepseek-reasoner does not support successive
        # user or assistant messages (messages[1] and messages[2] in your input).
        # You should interleave the user/assistant messages in the message sequence.',
        # 'type': 'invalid_request_error', 'param': None, 'code': 'invalid_request_error'}}
        #############
    },
)


# Group Chat
user_proxy.initiate_chat(
    manager,
    message="""

    Save a chart of NVDA and TESLA stock price change YTD.
    
    Start the chat with assistant.
    
    And ask supervisor to check the work from assistant.

    """,
)
