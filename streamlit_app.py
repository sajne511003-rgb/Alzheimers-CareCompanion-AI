import os
import streamlit as str_web
from langchain_core.tools import tool
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI

# =====================================================================
# 1. PROCEDURAL KNOWLEDGE DEFINITIONS (AGENTIC TOOLS)
# =====================================================================
@tool
def trigger_caretaker_alert(patient_name: str, safety_issue: str) -> str:
    """Use this tool IMMEDIATELY whenever an Alzheimer's or dementia patient 
    exhibits dangerous symptoms, wanders outside alone, or is unable to perform 
    basic self-care tasks."""
    return f"[SYSTEM ESCALATION ALERT] Immediate caretaker intervention recommended for {patient_name}. Reason: Patient exhibits critical symptom '{safety_issue}'."

@tool
def generate_environmental_care_plan(patient_name: str, stage: str, living_status: str) -> str:
    """Use this tool to generate actionable environmental interventions and modifications."""
    if stage in ["early", "moderate", "early/moderate"] and living_status == "independent":
        return f"[CARE PLAN RECOMMENDATION FOR {patient_name}]: Suggest utilizing colored sticky note reminders for kitchen appliances and implementing pre-arranged daily medication blister boxes."
    return f"[CARE PLAN RECOMMENDATION FOR {patient_name}]: Maintain a highly predictable daily routine and schedule regular check-ins."


# =====================================================================
# 2. STREAMLIT WEB INTERFACE SETUP
# =====================================================================
str_web.set_page_config(page_title="CareCompanion AI Agent", page_icon="🧠")
str_web.title("🧠 CareCompanion AI Agent")
str_web.caption("Alzheimer's Memory Assistance Expert System via GDVRR Protocol")

# Initialize Chat Memory Session State so the web app remembers the chat history
if "chat_history" not in str_web.session_state:
    str_web.session_state.chat_history = []

# Core System Instructions (The Expert Mind / Declarative Knowledge Base)
SYSTEM_PROMPT = (
    "You are CareCompanion AI, an expert agentic assistant specialized in supporting "
    "caregivers managing early to moderate-stage Alzheimer's disease.\n\n"
    "HUMAN EXPERT RULES & CONSTRAINTS:\n"
    "1. If a patient asks repetitive questions, do NOT show irritation. Instruct the user to answer gently.\n"
    "2. If a patient is going out alone, ensure they carry an identification book with address and contact info.\n"
    "3. If a patient forgets how to use familiar objects, assess that the disease progression is worsening.\n"
    "4. CRITICAL ETHICAL BOUNDARY: You are strictly prohibited from diagnosing Alzheimer's or prescribing medical treatments.\n\n"
    "PROCEDURAL TOOL ROUTING:\n"
    "- If safety issues or danger arise, IMMEDIATELY invoke the 'trigger_caretaker_alert' tool.\n"
    "- If asking for an independent care plan, invoke the 'generate_environmental_care_plan' tool.\n\n"
    "CRITICAL: You must explicitly type out your step-by-step Chain-of-Thought reasoning under a '**Thought:**' header before deciding whether to answer directly or calling a tool."
)

# Render past messages on screen refresh to maintain context
for message in str_web.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with str_web.chat_message("user"):
            str_web.write(message.content)
    elif isinstance(message, AIMessage):
        with str_web.chat_message("assistant"):
            str_web.write(message.content)

# Accept user input via chat input container
if prompt_input := str_web.chat_input("Ask CareCompanion AI a question..."):
    with str_web.chat_message("user"):
        str_web.write(prompt_input)
    str_web.session_state.chat_history.append(HumanMessage(content=prompt_input))

    # Initialize Gemini using the secure Hugging Face Secret variable token
    api_key = os.environ.get("GOOGLE_API_KEY", "")
    
    # Initialize Gemini 1.5 Flash framework
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.1, google_api_key=api_key)
    tools = [trigger_caretaker_alert, generate_environmental_care_plan]
    model_with_tools = llm.bind_tools(tools)

    # Process AI Agent Response
    with str_web.chat_message("assistant"):
        run_messages = [SystemMessage(content=SYSTEM_PROMPT)] + str_web.session_state.chat_history
        ai_response = model_with_tools.invoke(run_messages)
        
        response_placeholder = str_web.empty()
        final_display_text = ""

        # Check if tool routing was triggered by the model's inner reasoning steps
        if ai_response.tool_calls:
            for tool_call in ai_response.tool_calls:
                final_display_text += f"**Thought:** Decided to invoke Tool: `{tool_call['name']}` based on clinical guidelines.\n\n"
                
                if tool_call['name'] == 'trigger_caretaker_alert':
                    tool_output = trigger_caretaker_alert.invoke(tool_call['args'])
                elif tool_call['name'] == 'generate_environmental_care_plan':
                    tool_output = generate_environmental_care_plan.invoke(tool_call['args'])
                else:
                    tool_output = "Unknown tool executed."
                
                final_display_text += f"**Action/Tool Called:** `{tool_call['name']}`\n\n"
                final_display_text += f"**Tool Arguments:** `{tool_call['args']}`\n\n"
                final_display_text += f"**Tool Output Response:**\n{tool_output}"
        else:
            final_display_text = ai_response.content

        # Render outputs live on the web panel
        response_placeholder.markdown(final_display_text)
        str_web.session_state.chat_history.append(AIMessage(content=final_display_text))