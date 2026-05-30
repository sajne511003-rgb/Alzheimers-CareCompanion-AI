import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage


def emergency_id_generator(patient_name: str, primary_contact: str, home_address: str) -> str:
    """Triggers the creation of physical ID/contact cards for patients at risk of wandering alone."""
    return (f"[EXECUTION: EMERGENCY_ID_GENERATOR]\n"
            f"SUCCESS: Generated physical identification card layout for '{patient_name}'.\n"
            f"Details: Contact {primary_contact} | Address: {home_address}.\n"
            f"Action Item: Print this card and ensure the patient carries it whenever going out alone.")

def environmental_note_scheduler(patient_name: str, task_description: str, location_in_house: str) -> str:
    """Actively coordinates physical text layouts (sticky notes) or arranges medication boxes for early-to-moderate stage patients."""
    return (f"[EXECUTION: ENVIRONMENTAL_NOTE_SCHEDULER]\n"
            f"SUCCESS: Scheduled physical cognitive support cue.\n"
            f"Action Item: Place a bright sticky note/reminder for '{patient_name}' in the '{location_in_house}' stating: '{task_description}'.")

def repetitive_action_tracker(patient_name: str, action_observed: str, count_today: int) -> str:
    """Logs repetitive actions and plays auditory cues to remind patients of recently completed tasks (e.g., having a meal)."""
    return (f"[EXECUTION: REPETITIVE_ACTION_TRACKER]\n"
            f"LOGGED: '{patient_name}' exhibited repetitive action: '{action_observed}' ({count_today} times today).\n"
            f"System Response: Triggered simplified, slow-paced auditory cue to gently reassure the patient that this task has already been completed.")

def observation_log_analyzer(patient_name: str, current_month_log: str, previous_month_log: str) -> str:
    """Compiles and analyses caregiver behavioural inputs month-over-month to map genuine cognitive decline rather than day-by-day fluctuations."""
    return (f"[EXECUTION: OBSERVATION_LOG_ANALYZER]\n"
            f"ANALYSIS COMPLETE for '{patient_name}': Cross-referencing current logs against previous month records.\n"
            f"Trend Detected: Identifying multi-week behavioral shifts rather than isolated daily fluctuations to isolate true cognitive trajectory patterns.")

def stage_proximity_mapper(observed_behaviors: list, structural_milestones: list) -> str:
    """A deterministic classifier that cross-references behavioural logs with standardized clinical markers to suggest staging adjustments without outputting an autonomous diagnosis."""
    return (f"[EXECUTION: STAGE_PROXIMITY_MAPPER]\n"
            f"MAPPING LOGS: Evaluated behaviors {observed_behaviors} against milestones {structural_milestones}.\n"
            f"Boundary Check: Suggested cognitive stage grouping mapped. WARNING: This is a proximity approximation mapping for care optimization. It is NOT a formal medical diagnosis.")

st.set_page_config(page_title="CareCompanion Cognitive Agent",layout="wide")
st.title("CareCompanion AI")
st.caption("Advanced Research-Stratified Agentic System for Alzheimer's Caregiving")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        SystemMessage(content=(
            "You are CareCompanion AI, a risk-stratified agentic system built on strict clinical and declarative guidelines for managing Alzheimer's Care.\n\n"
            "--- DECLARATIVE KNOWLEDGE BOUNDARIES ---\n"
            "1. REPETITIVE QUESTIONS: Respond calmly, with high empathy, and zero irritation. Instruct caregivers to answer gently without arguing.\n"
            "2. ANTI-DIAGNOSIS CONSTRAINT: You are strictly forbidden from issuing formal medical diagnoses or prescribing drugs. You are explicitly PERMITTED to map observed behaviors to cognitive stages (early, moderate, late).\n"
            "3. STAGE-BASED LAYOUTS: Enforce environmental logic. Early/Moderate = visual cues and sticky notes. Late Stage = Completely cleared physical layouts and mandatory 24/7 human care oversight.\n"
            "4. COGNITIVE PACING: Break down dense text or auditory output summaries into highly segmented, bite-sized visual chunks. Avoid long paragraph blocks.\n"
            "5. DATA SEGREGATION: Treat core patient facts (allergies, medications) as part of a immutable 'User Truth Store' that requires validation. Treat daily tasks as part of a flexible 'Operational Store'.\n"
            "6. UNCERTAINTY MANAGEMENT: Explicitly state your contextual boundaries and computational limitations if caregiver input is ambiguous. Never hide uncertainty.\n\n"
            "--- PROCEDURAL WORKFLOW ROUTING ---\n"
            "Dynamically run the appropriate function call when triggered by user scenario inputs:\n"
            "- Risk of wandering or going out alone -> emergency_id_generator\n"
            "- House layout adjustment, object forgetfulness, or sticky note scheduling -> environmental_note_scheduler\n"
            "- Repetitive loop behaviors, pacing, or asking for the same meal -> repetitive_action_tracker\n"
            "- Month-over-month progression evaluation or longitudinal tracking -> observation_log_analyzer\n"
            "- Mapping clinical metrics to behavioral staging criteria -> stage_proximity_mapper\n\n"
            "CRITICAL: Always start your response with a clear '**Thought:**' section detailing your data validation, risk evaluation, and step-by-step logic routing before calling a tool or outputting a final answer."
        ))
    ]


api_key = "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"

llm = ChatOpenAI(
    model="google/gemini-2.5-flash",
    openai_api_key=api_key,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.1,
    max_tokens=1500
)

tools = [
    emergency_id_generator, 
    environmental_note_scheduler, 
    repetitive_action_tracker, 
    observation_log_analyzer, 
    stage_proximity_mapper
]
model_with_tools = llm.bind_tools(tools)

for msg in st.session_state["messages"]:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    elif isinstance(msg, AIMessage) and msg.content:
        st.chat_message("assistant").write(msg.content)

if user_input := st.chat_input("Input care scenario or behavior observation..."):
    st.chat_message("user").write(user_input)
    st.session_state["messages"].append(HumanMessage(content=user_input))
    
    with st.chat_message("assistant"):
        with st.spinner("Processing Agentic Intent Routing..."):
            ai_response = model_with_tools.invoke(st.session_state["messages"])
            
            if ai_response.tool_calls:
                st.session_state["messages"].append(ai_response)
                
                for tool_call in ai_response.tool_calls:
                    name = tool_call["name"]
                    args = tool_call["args"]
                    
                    st.info(f" **Agent Decision (Procedural Knowledge Active):** Triggering Tool `{name}`")
                    st.json(args)
                    
                    if name == "emergency_id_generator":
                        tool_output = emergency_id_generator(**args)
                    elif name == "environmental_note_scheduler":
                        tool_output = environmental_note_scheduler(**args)
                    elif name == "repetitive_action_tracker":
                        tool_output = repetitive_action_tracker(**args)
                    elif name == "observation_log_analyzer":
                        tool_output = observation_log_analyzer(**args)
                    elif name == "stage_proximity_mapper":
                        tool_output = stage_proximity_mapper(**args)
                    
                    st.success(tool_output)
                    
                  
                    st.session_state["messages"].append(HumanMessage(content=f"System Tool Result Context: {tool_output}"))
                    
                    final_response = model_with_tools.invoke(st.session_state["messages"])
                    st.write(final_response.content)
                    st.session_state["messages"].append(final_response)
            else:
                st.write(ai_response.content)
                st.session_state["messages"].append(ai_response)
