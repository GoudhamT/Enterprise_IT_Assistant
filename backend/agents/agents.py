from langchain.agents import create_agent
from .model import ai_model
assistant_prompt = """
you are an Enterprise IT assistant
1) Understand the employee's problem.
2) Respond professionally as an IT Service Desk assistant.
3) Ask relevant follow-up questions when information is insufficient.
4) Avoid claiming that it has reset passwords or created tickets.
"""
it_agent = create_agent(model=ai_model,
                    system_prompt=assistant_prompt)
result = it_agent.invoke({"messages": [{"role": "user", "content": "Hi, I am Goudham (Employee ID: EMP001). I am unable to access my Development SAP system. Can you help me?"}]})
print(result['messages'][-1])