#global vars

from kernel.hooks.llm import useLLMRequestQueue

global_llm_req_queue, global_llm_req_queue_get_message, global_llm_req_queue_add_message, global_llm_req_queue_is_empty = useLLMRequestQueue()
