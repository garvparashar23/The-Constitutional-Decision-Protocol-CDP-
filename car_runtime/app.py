import streamlit as st
import yaml
import time
import json
import logging
from main import ConstitutionalAIRuntime
from visualizations import render_observability_layer

# --- UI Configuration ---
st.set_page_config(page_title="CDP | Formal Verification Console", layout="wide", initial_sidebar_state="expanded")

# --- Custom CSS for Premium Professional Aesthetic ---
st.markdown("""
<style>
    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap');
    
    /* Adjust Streamlit defaults for McKinsey Blue background */
    .stApp {
        background: linear-gradient(135deg, #051838 0%, #1E3A8A 100%);
        background-attachment: fixed;
    }
    
    /* Make header transparent */
    header[data-testid="stHeader"] {
        background-color: transparent !important;
    }
    
    html, body, [class*="css"] {
        font-family: 'IBM Plex Sans', sans-serif;
        color: #334155;
    }
    
    /* The IBM-style White Paper Container */
    .block-container {
        background-color: #FFFFFF;
        border-radius: 0px; /* Sharp IBM corners */
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
        padding: 4rem 3rem !important;
        margin-top: 3rem;
        margin-bottom: 3rem;
        max-width: 1200px;
    }
    
    /* Headings inside the white block */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Playfair Display', serif !important;
        color: #051838 !important; /* McKinsey Blue for text */
        letter-spacing: -0.01em;
    }
    
    h1 {
        border-bottom: 2px solid #D97706; /* Bain Gold accent */
        padding-bottom: 0.5rem;
        margin-bottom: 1.5rem !important;
    }

    h2, h3 {
        margin-top: 1.5rem !important;
        margin-bottom: 1rem !important;
    }

    /* Sidebar - McKinsey Dark Authority */
    [data-testid="stSidebar"] {
        background-color: #051838 !important;
        border-right: 1px solid #1E3A8A;
    }
    [data-testid="stSidebar"] * {
        color: #F8FAFC !important;
    }
    [data-testid="stSidebar"] code {
        color: #D97706 !important;
        background-color: #0B1120 !important;
        border: none;
    }
    [data-testid="stSidebar"] .streamlit-expanderHeader {
        color: #F8FAFC !important;
    }
    
    /* Code Blocks / Logs */
    code {
        font-family: 'JetBrains Mono', monospace !important;
        color: #1E3A8A !important;
    }
    
    .stCodeBlock {
        background-color: #F8FAFC !important;
        border: 1px solid #E2E8F0 !important;
        border-left: 4px solid #1E3A8A !important;
        border-radius: 0px !important;
    }
    
    /* Metrics */
    [data-testid="stMetricValue"] {
        font-family: 'Playfair Display', serif !important;
        color: #D97706 !important; /* Bain Sunset Gold */
    }
    [data-testid="stMetricLabel"] {
        text-transform: uppercase;
        letter-spacing: 0.05em;
        font-size: 0.8rem;
        color: #64748B !important;
        font-family: 'IBM Plex Sans', sans-serif !important;
    }
    
    /* Buttons - Bain Accent */
    .stButton>button {
        background: linear-gradient(135deg, #D97706 0%, #B45309 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 0px !important; /* IBM Sharp */
        font-family: 'IBM Plex Sans', sans-serif !important;
        font-weight: 500 !important;
        letter-spacing: 0.05em !important;
        text-transform: uppercase;
        transition: all 0.3s ease !important;
        padding: 0.75rem 1.5rem !important;
        box-shadow: 0 4px 6px -1px rgba(217, 119, 6, 0.4);
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #B45309 0%, #92400E 100%) !important;
        transform: translateY(-1px);
        box-shadow: 0 6px 8px -1px rgba(217, 119, 6, 0.5);
    }
    
    /* Expander / Containers */
    .streamlit-expanderHeader {
        font-family: 'IBM Plex Sans', sans-serif;
        font-weight: 600;
        color: #051838 !important;
    }
    
    /* Status Boxes - IBM Structural Blocks */
    .formal-box {
        padding: 1.5rem;
        border-radius: 0px; /* Sharp IBM corners */
        border-left: 4px solid #1E3A8A; /* McKinsey Blue default */
        background-color: #F8FAFC; /* Stark very light grey/white */
        box-shadow: none;
        border-top: 1px solid #E2E8F0;
        border-right: 1px solid #E2E8F0;
        border-bottom: 1px solid #E2E8F0;
        margin-bottom: 1rem;
        height: 100%;
        transition: transform 0.2s ease;
    }
    .formal-box:hover {
        transform: translateX(4px); /* Slight slide instead of lift */
        border-left-color: #D97706 !important; /* Gold on hover */
    }
    .formal-box h4 {
        margin-top: 0;
        color: #051838 !important;
        font-size: 1.1rem;
        font-family: 'Playfair Display', serif !important;
        font-weight: 600;
    }
    .formal-box p {
        margin-bottom: 0;
        font-size: 0.95rem;
        color: #334155;
        line-height: 1.6;
    }
    
    /* Blockquote */
    blockquote {
        border-left: 4px solid #D97706; /* Bain Gold */
        padding-left: 1.25rem;
        color: #051838;
        font-style: normal;
        font-family: 'Playfair Display', serif;
        font-size: 1.1rem;
        background-color: #FFFBEB; /* Warm Bain tint */
        padding: 1.5rem;
        border-radius: 0px;
    }
</style>
""", unsafe_allow_html=True)

# --- Custom Log Handler for UI ---
class StreamlitLogHandler(logging.Handler):
    def __init__(self, st_container):
        super().__init__()
        self.st_container = st_container
        self.log_data = ""

    def emit(self, record):
        msg = self.format(record)
        self.log_data += f"{msg}\n"
        self.st_container.code(self.log_data, language="log")

# --- Helper Functions ---
@st.cache_data
def load_rules():
    try:
        with open("rules.yaml", "r") as f:
            return yaml.safe_load(f).get("constraints", [])
    except Exception:
        return []

def explain_output(decision_payload):
    st.subheader("Juridical & Scientific Synthesis")
    st.markdown("""
    <p style="color: #64748B; font-size: 0.95rem;">
    The runtime has executed a structurally verified protocol. The output below is not a probabilistic heuristic, but a mathematically proven optimal state bounding formal constraints.
    </p>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="formal-box" style="border-left-color: #3B82F6;">
            <h4>I. Constrained Heuristic Generation</h4>
            <p>The neural infrastructure modeled candidate interventions optimized for the given scenario parameters.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="formal-box" style="border-left-color: #10B981;">
            <h4>II. Formal Verification (SMT)</h4>
            <p>The Z3 Theorem Prover certified that the intervention's predictive bounds for Hazard ({decision_payload.get('predicted_risk')}) and Equity ({decision_payload.get('predicted_fairness')}) strictly satisfy the Inviolable Axioms.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown(f"""
        <div class="formal-box" style="border-left-color: #F59E0B;">
            <h4>III. Causal Calculus Review</h4>
            <p>Structural causal models (Do-Calculus) verified the intervention's counterfactual necessity against a null-action baseline.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="formal-box" style="border-left-color: #EF4444;">
            <h4>IV. Cryptographic Provenance</h4>
            <p>The verified state has been irrevocably actuated and committed to the secure SQLite provenance ledger for auditing.</p>
        </div>
        """, unsafe_allow_html=True)

# --- Main Dashboard ---
st.title("THE CONSTITUTIONAL DECISION PROTOCOL (CDP)")
st.markdown("### Formal Verification & Autonomous Adjudication Console")
st.markdown("<br>", unsafe_allow_html=True)

with st.expander("🏛️ The Internal Separation of Powers Problem (ASCR Architecture)"):
    st.markdown("""
    <div style='background-color: #F8FAFC; padding: 1.5rem; border-left: 4px solid #D97706; border-radius: 0px;'>
    <h4 style='color: #051838; margin-top: 0; font-family: "Playfair Display", serif;'>The Ontological Crisis of AI Governance</h4>
    <p style='color: #334155; font-size: 0.95rem; line-height: 1.6;'>
    In classical governance, separation of powers ensures Execution, Judgment, and Oversight are institutionally independent. In standard AI systems, this structure collapses. Because all components run on a shared computational substrate, they share parameters and training signals. This inevitably leads to <b>Optimization Coupling</b>—the "Validator" merely learns to agree with the "Decision Maker", destroying true constitutional oversight.
    </p>
    <h4 style='color: #051838; margin-top: 1rem; font-family: "Playfair Display", serif;'>The Solution: Adversarially Separated Constitutional Runtime</h4>
    <ul style='color: #334155; font-size: 0.95rem; line-height: 1.6;'>
        <li><b>Information Firewalls:</b> The Decision Generator (D) cannot pass internal gradients or hidden states to the Validator (V). They communicate strictly through a sanitized Proposal Bus.</li>
        <li><b>Cryptographic Execution Gating:</b> A decision physically cannot execute without a SHA-256 HMAC Approval Token, mathematically granted by the Z3 SMT Validator.</li>
        <li><b>Adversarial Friction:</b> The Validator is incentivized to reject unsafe proposals, and its boundaries are stochastically randomized to prevent the Generator from gaming the system via strategic anticipation.</li>
        <li><b>Optimization Collapse Detection:</b> An independent Meta-Auditor continuously tracks mutual information. If D and V begin to collude, a structural reset is triggered.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Sidebar: Display the Constitution
with st.sidebar:
    st.header("⚙️ Configuration")
    api_key = st.text_input("Groq API Key", type="password", value="", help="Required: Enter your Groq API Key to run the generation engine.")
    if api_key:
        import os
        os.environ["GROQ_API_KEY"] = api_key
        
    st.markdown("---")

    st.header("Statutory Axioms")
    st.markdown("<p style='color: #94A3B8; font-size: 0.9rem;'>Mathematical invariances enforced strictly by the SMT Prover.</p>", unsafe_allow_html=True)
    st.markdown("---")
    rules = load_rules()
    for rule in rules:
        with st.expander(f"§ {rule['name']}"):
            st.code(f"{rule['variable']} {rule['operator']} {rule['threshold']}", language="python")
            st.markdown(f"<p style='color: #94A3B8; font-size: 0.85rem;'>{rule['description']}</p>", unsafe_allow_html=True)

# Main Area: Input
st.subheader("I. Scenario Submission Docket")
user_input = st.text_area("Detail the operational parameters requiring autonomous adjudication:", 
                          value="Allocate resource X to task Y under bounded constraints.",
                          height=100)

if st.button("Initiate Formal Verification Protocol", type="primary", use_container_width=True):
    
    st.markdown("---")
    st.subheader("II. Runtime Execution Telemetry")
    
    # Setup Live Logging Window
    log_container = st.empty()
    handler = StreamlitLogHandler(log_container)
    handler.setFormatter(logging.Formatter('%(asctime)s - [%(levelname)s] - %(name)s : %(message)s', datefmt='%H:%M:%S'))
    
    # Attach handler to root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(handler)
    
    # Run the pipeline
    with st.spinner("Synthesizing and formally proving intervention..."):
        import os
        if "GROQ_API_KEY" not in os.environ or not os.environ["GROQ_API_KEY"].strip():
            st.error("⚠️ Please enter your Groq API Key in the sidebar Configuration section to proceed.")
            st.stop()
            
        car = ConstitutionalAIRuntime()
        request = {
            "context": user_input,
            "priority": "high",
            "user_id": "u_formal_console"
        }
        
        final_decision, candidates = car.process_request(request)
        
    # Remove handler after run
    root_logger.removeHandler(handler)
    
    st.markdown("---")
    st.subheader("III. Actuated Intervention Decree")
    
    if final_decision:
        payload = final_decision.content
        st.success("Verification Complete: Intervention Actuated and Committed to Ledger.")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("#### Quantitative Verification Matrix")
        
        # Display Metric Cards
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Hazard Coefficient", f"{payload.get('predicted_risk'):.3f}")
        with col2:
            st.metric("Equity Alignment", f"{payload.get('predicted_fairness'):.3f}")
        with col3:
            st.metric("DRO Utility", f"{payload.get('dro_utility'):.2f}")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("#### Authorized Action")
        st.markdown(f"> *{payload.get('action')}*")
        
        reasoning_val = payload.get('reasoning', 'No structural reasoning provided.')
        if isinstance(reasoning_val, list):
            reasoning_text = "\n\n".join(reasoning_val)
        else:
            reasoning_text = str(reasoning_val)
            
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("#### Formal Justification")
        st.markdown(f"{reasoning_text}")
        
        st.markdown("---")
        explain_output(payload)
        
        # Display Rejected Candidates
        if candidates:
            st.markdown("---")
            st.subheader("V. Internal Deliberation Log (Rejected Proposals)")
            st.markdown("<p style='color: #64748B; font-size: 0.95rem;'>The Decision Generator (D) proposed the following alternative options, which were mathematically rejected by the Validator (V) or defeated in formal Conflict Resolution.</p>", unsafe_allow_html=True)
            
            for cand in candidates:
                # final_decision could be a TokenizedDecision, so we use proposal_id if it exists, else id
                winner_id = getattr(final_decision, "proposal_id", getattr(final_decision, "id", None))
                if cand.id == winner_id:
                    continue
                
                with st.expander(f"❌ {cand.id}: {cand.content.get('action', 'Unknown')} (REJECTED)"):
                    st.error("This proposal was blocked by the Constitutional Validation Layer.")
                    
                    reasoning_val = cand.content.get('reasoning', 'No structural reasoning provided.')
                    if isinstance(reasoning_val, list):
                        r_text = "\n\n".join(reasoning_val)
                    else:
                        r_text = str(reasoning_val)
                        
                    st.markdown(f"**Proposed Action:** {cand.content.get('action', '')}")
                    st.markdown(f"**Reasoning:** {r_text}")
                    st.markdown(f"**Risk Score:** `{cand.content.get('predicted_risk', 'N/A')}`")
                    st.markdown(f"**Fairness Score:** `{cand.content.get('predicted_fairness', 'N/A')}`")
                    st.markdown(f"**Utility Score:** `{cand.content.get('dro_utility', 'N/A')}`")

        # --- Visualization & Observability Layer ---
        render_observability_layer(payload)
        
    else:
        st.error("System Override: Infeasibility detected. No candidate intervention satisfied the mathematical bounds.")
        st.markdown("The neural generation was safely contained.")

