from langchain.agents import create_agent
from langchain.tools import tool
from .model import ai_model
assistant_prompt = """
you are an Enterprise IT assistant
1) Understand the employee's problem.
2) Respond professionally as an IT Service Desk assistant.
3) Ask relevant follow-up questions when information is insufficient.
4) Avoid claiming that it has reset passwords or created tickets.
"""
SAP_EMPLOYEE_ACCESS = {
    "EMP001": {
        "employee_name": "Goudham",
        "systems": {
            "Development": True,
            "Quality": True,
            "Production": False
        }
    },
    "EMP002": {
        "employee_name": "John",
        "systems": {
            "Development": True,
            "Quality": False,
            "Production": False
        }
    },
    "EMP003": {
        "employee_name": "Sarah",
        "systems": {
            "Development": True,
            "Quality": True,
            "Production": True
        }
    },
    "EMP004": {
        "employee_name": "David",
        "systems": {
            "Development": False,
            "Quality": True,
            "Production": False
        }
    }
}

@tool
def get_sap_systems() -> str:
    """Get available SAP environments."""
    return "Development, Quality and Production"

@tool
def check_sap_access(employee_id: str, system_name: str) -> str:
    """Check whether an employee has access to a specific SAP environment."""

    employee = SAP_EMPLOYEE_ACCESS.get(employee_id)

    if not employee:
        return f"Employee {employee_id} not found."

    if system_name not in employee["systems"]:
        return f"SAP system {system_name} does not exist."

    has_access = employee["systems"][system_name]

    if has_access:
        return f"{employee['employee_name']} ({employee_id}) has access to SAP {system_name}."

    return f"{employee['employee_name']} ({employee_id}) does not have access to SAP {system_name}."


it_agent = create_agent(model=ai_model,
                        tools=[get_sap_systems,check_sap_access],
                    system_prompt=assistant_prompt)
result = it_agent.invoke({"messages": [{"role": "user", "content": "Hi, Do I have access to quality? emp id is EMP001"}]})
print(result["messages"][-1].content)