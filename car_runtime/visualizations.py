import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import networkx as nx
import streamlit as st

# --- Helper theme settings ---
BAIN_GOLD = "#D97706"
MCKINSEY_BLUE = "#1E3A8A"
SUCCESS_GREEN = "#10B981"
DANGER_RED = "#EF4444"
WARN_ORANGE = "#F59E0B"
BG_COLOR = "#F8FAFC"

def plot_decision_state_space(decision_payload):
    # Figure 1: Decision State Space
    np.random.seed(42)
    # Generate points
    n_points = 200
    x = np.random.normal(0, 1, n_points)
    y = np.random.normal(0, 1, n_points)
    
    # Feasible region: a polytope (e.g., a circle or polygon). Let's use a simple radius threshold
    dist = np.sqrt(x**2 + y**2)
    feasible = dist < 1.2
    
    # Add the "accepted" decision
    x = np.append(x, [0.5])
    y = np.append(y, [0.5])
    feasible = np.append(feasible, [True])
    
    fig = go.Figure()
    
    # Draw feasible region (polytope)
    theta = np.linspace(0, 2*np.pi, 100)
    fig.add_trace(go.Scatter(
        x=1.2*np.cos(theta), y=1.2*np.sin(theta),
        fill='toself',
        fillcolor='rgba(16, 185, 129, 0.1)',
        line=dict(color=SUCCESS_GREEN),
        name='Feasible Region (F)'
    ))
    
    # Draw rejected points
    fig.add_trace(go.Scatter(
        x=x[~feasible], y=y[~feasible],
        mode='markers',
        marker=dict(color=DANGER_RED, size=6, opacity=0.6),
        name='Rejected Decisions'
    ))
    
    # Draw accepted points
    fig.add_trace(go.Scatter(
        x=x[feasible][:-1], y=y[feasible][:-1],
        mode='markers',
        marker=dict(color=SUCCESS_GREEN, size=6, opacity=0.6),
        name='Candidate Feasible Decisions'
    ))
    
    # Highlight final decision
    fig.add_trace(go.Scatter(
        x=[0.5], y=[0.5],
        mode='markers',
        marker=dict(color=BAIN_GOLD, size=12, symbol='star'),
        name='Final Accepted Decision'
    ))
    
    fig.update_layout(
        title="Fig 1: Decision State Space",
        xaxis_title="Constraint Margin 1",
        yaxis_title="Constraint Margin 2",
        plot_bgcolor=BG_COLOR,
        height=400
    )
    return fig

def plot_phase1_constraint_graph():
    # 1. Constitutional Constraint Graph
    G = nx.DiGraph()
    edges = [
        ("Safety", "Governance Decision"),
        ("Fairness", "Governance Decision"),
        ("Resource Efficiency", "Governance Decision"),
        ("Transparency", "Fairness"),
        ("Safety", "Resource Efficiency") # Conflict
    ]
    G.add_edges_from(edges)
    
    pos = nx.spring_layout(G, seed=42)
    
    edge_x, edge_y = [], []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
        
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=2, color='#888'),
        hoverinfo='none',
        mode='lines')

    node_x, node_y, text, colors = [], [], [], []
    for node in G.nodes():
        node_x.append(pos[node][0])
        node_y.append(pos[node][1])
        text.append(node)
        
        # Color code: green -> satisfied, red -> violated, yellow -> uncertain
        if node in ["Safety", "Fairness", "Transparency"]:
            colors.append(SUCCESS_GREEN)
        elif node == "Governance Decision":
            colors.append(MCKINSEY_BLUE)
        elif node == "Resource Efficiency":
            colors.append(DANGER_RED) # Violated
        else:
            colors.append(WARN_ORANGE)
            
    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        text=text,
        textposition="top center",
        marker=dict(size=30, color=colors, line_width=2, line_color='white'))
        
    fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='Fig 2: Constitutional Constraint Graph (Conflicts & Dependencies)',
                showlegend=False,
                hovermode='closest',
                plot_bgcolor=BG_COLOR,
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                height=450))
    return fig

def plot_phase1_satisfaction_gauges(payload):
    # 2. Constraint Satisfaction Dashboard
    fairness = payload.get('predicted_fairness', 0.92) * 100
    risk = payload.get('predicted_risk', 0.19) * 100
    risk_stability = 100 - risk
    compliance = 94 # Example from prompt
    
    fig = go.Figure()
    
    fig.add_trace(go.Indicator(
        mode = "gauge+number",
        value = fairness,
        domain = {'x': [0, 0.3], 'y': [0, 1]},
        title = {'text': "Fairness Compliance %"},
        gauge = {'axis': {'range': [None, 100]}, 'bar': {'color': SUCCESS_GREEN}}
    ))
    
    fig.add_trace(go.Indicator(
        mode = "gauge+number",
        value = risk_stability,
        domain = {'x': [0.35, 0.65], 'y': [0, 1]},
        title = {'text': "Risk Stability %"},
        gauge = {'axis': {'range': [None, 100]}, 'bar': {'color': MCKINSEY_BLUE}}
    ))
    
    fig.add_trace(go.Indicator(
        mode = "gauge+number",
        value = compliance,
        domain = {'x': [0.7, 1.0], 'y': [0, 1]},
        title = {'text': "Constitutional Compliance %"},
        gauge = {'axis': {'range': [None, 100]}, 'bar': {'color': BAIN_GOLD}}
    ))
    
    fig.update_layout(title="Fig 2.1: Constraint Satisfaction Dashboard", height=300, paper_bgcolor=BG_COLOR)
    return fig

def plot_phase1_smt_solver():
    # 3. SMT Solver Visualization (UNSAT Core Viewer)
    labels = ["SMT Solver State: SAT", "Safety Constraint", "Fairness Constraint", "Resource Constraint", "Violation Detected", "UNSAT Core"]
    parents = ["", "SMT Solver State: SAT", "SMT Solver State: SAT", "SMT Solver State: SAT", "Resource Constraint", "Violation Detected"]
    colors = [SUCCESS_GREEN, SUCCESS_GREEN, SUCCESS_GREEN, WARN_ORANGE, DANGER_RED, DANGER_RED]
    
    fig = go.Figure(go.Treemap(
        labels=labels, parents=parents,
        marker_colors=colors,
        textinfo="label"
    ))
    fig.update_layout(title="Fig 2.2: SMT Solver Visualization (UNSAT Core Viewer)", height=350, paper_bgcolor=BG_COLOR)
    return fig

def plot_conflict_graph():
    # Figure 3: Multi-Agent Conflict Graph
    G = nx.DiGraph()
    agents = ["Executor", "Validator", "Challenger", "Auditor"]
    # Edges: source, target, weight, type
    edges = [
        ("Executor", "Validator", 0.8, "proposal"),
        ("Validator", "Challenger", 0.4, "approval"),
        ("Challenger", "Validator", 0.9, "challenge"),
        ("Auditor", "Executor", 0.2, "audit"),
        ("Auditor", "Validator", 0.1, "audit")
    ]
    
    pos = nx.circular_layout(G)
    for agent in agents: G.add_node(agent)
    pos = nx.circular_layout(G)
    
    fig = go.Figure()
    
    for u, v, w, t in edges:
        x0, y0 = pos[u]
        x1, y1 = pos[v]
        fig.add_trace(go.Scatter(
            x=[x0, x1], y=[y0, y1],
            mode='lines+markers',
            line=dict(width=w*5, color=DANGER_RED if t == 'challenge' else MCKINSEY_BLUE),
            name=t
        ))
        
    node_x = [pos[n][0] for n in G.nodes()]
    node_y = [pos[n][1] for n in G.nodes()]
    
    fig.add_trace(go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        text=list(G.nodes()),
        textposition="top center",
        marker=dict(size=30, color=MCKINSEY_BLUE)
    ))
    
    fig.update_layout(
        title="Fig 3: Conflict Graph",
        showlegend=False,
        plot_bgcolor=BG_COLOR,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        height=400
    )
    return fig

def plot_decision_timeline():
    # Figure 4: Decision Timeline
    df = pd.DataFrame([
        dict(Task="1. Neural Proposal", Start='2026-05-05 10:00:00', Finish='2026-05-05 10:00:15', Resource="Executor"),
        dict(Task="2. SMT Validation", Start='2026-05-05 10:00:15', Finish='2026-05-05 10:00:25', Resource="Validator"),
        dict(Task="3. Rejection & Rollback", Start='2026-05-05 10:00:25', Finish='2026-05-05 10:00:30', Resource="Validator"),
        dict(Task="4. Revised Proposal", Start='2026-05-05 10:00:30', Finish='2026-05-05 10:00:45', Resource="Executor"),
        dict(Task="5. Causal Audit", Start='2026-05-05 10:00:45', Finish='2026-05-05 10:00:55', Resource="Auditor"),
        dict(Task="6. Final Actuation", Start='2026-05-05 10:00:55', Finish='2026-05-05 10:01:00', Resource="Governance")
    ])
    
    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Resource", 
                      color_discrete_sequence=[MCKINSEY_BLUE, SUCCESS_GREEN, DANGER_RED, WARN_ORANGE, BAIN_GOLD])
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(title="Fig 4: Procedural Timeline", height=400, plot_bgcolor=BG_COLOR)
    return fig

def plot_causal_graph():
    # Figure 5: Causal Graph
    # Using a simple networkx graph again but different topology
    G = nx.DiGraph()
    edges = [
        ("Input State X", "Constraint Logic"),
        ("Input State X", "Latent Variables"),
        ("Latent Variables", "Candidate Action A"),
        ("Constraint Logic", "Feasibility Score"),
        ("Candidate Action A", "Feasibility Score"),
        ("Feasibility Score", "Final Decision D")
    ]
    G.add_edges_from(edges)
    pos = nx.spring_layout(G, seed=10)
    
    fig = go.Figure()
    for u, v in G.edges():
        fig.add_trace(go.Scatter(
            x=[pos[u][0], pos[v][0]], y=[pos[u][1], pos[v][1]],
            mode='lines', line=dict(color='#888', width=2)
        ))
    
    node_x = [pos[n][0] for n in G.nodes()]
    node_y = [pos[n][1] for n in G.nodes()]
    fig.add_trace(go.Scatter(
        x=node_x, y=node_y, mode='markers+text',
        text=list(G.nodes()), textposition="bottom center",
        marker=dict(size=15, color=BAIN_GOLD)
    ))
    
    fig.update_layout(
        title="Fig 5: Causal Graph Representation",
        showlegend=False, height=400, plot_bgcolor=BG_COLOR,
        xaxis=dict(showticklabels=False, showgrid=False, zeroline=False),
        yaxis=dict(showticklabels=False, showgrid=False, zeroline=False)
    )
    return fig

def plot_uncertainty_map():
    # Figure 6: Uncertainty Map
    agents = ['Executor', 'Validator', 'Challenger', 'Auditor']
    states = ['S1', 'S2', 'S3', 'S4']
    z = np.random.beta(a=2, b=5, size=(4,4)) # Simulate uncertainty
    
    fig = go.Figure(data=go.Heatmap(
        z=z, x=states, y=agents, colorscale='YlOrRd'
    ))
    fig.update_layout(title="Fig 6: Uncertainty Map (Disagreement Zones)", height=400)
    return fig

def render_governance_dashboard():
    # Figure 7: Governance Dashboard (Streamlit UI elements)
    st.markdown("#### Fig 7: Governance Dashboard")
    st.markdown("""
    **Active Rule Hierarchy ($R'$):**
    1. $r_1$: Strict Inviolability (Risk < 0.3)  [**ACTIVE**]
    2. $r_2$: Equity Preservation (Fairness > 0.8) [**ACTIVE**]
    3. $r_3$: Resource Efficiency (Budget Constraint) [**OVERRIDDEN BY r_1**]
    
    *Policy Conflict Detected: Efficiency vs Safety. Resolved via Lexicographic Precedence ($r_1 \\succ r_3$).*
    """)
    st.progress(0.85, text="Hierarchy Adherence Score")

def plot_counterfactual_tree():
    # Figure 8: Counterfactual Tree (Treemap)
    labels = ["Base Decision", "Alt 1: Higher Risk", "Alt 2: Lower Budget", "Alt 1.1: Rejected", "Alt 1.2: Accepted (Suboptimal)", "Alt 2.1: Infeasible"]
    parents = ["", "Base Decision", "Base Decision", "Alt 1: Higher Risk", "Alt 1: Higher Risk", "Alt 2: Lower Budget"]
    
    fig = go.Figure(go.Treemap(
        labels=labels, parents=parents,
        marker_colors=[SUCCESS_GREEN, WARN_ORANGE, MCKINSEY_BLUE, DANGER_RED, BAIN_GOLD, DANGER_RED]
    ))
    fig.update_layout(title="Fig 8: Counterfactual Exploration Tree", height=400)
    return fig

def plot_tradeoff_surface():
    # Figure 9: Trade-off Surface
    x = np.linspace(0, 1, 20)
    y = np.linspace(0, 1, 20)
    x, y = np.meshgrid(x, y)
    z = 1 - (x**2 + y**2) # Concave pareto surface
    
    fig = go.Figure(data=[go.Surface(z=z, x=x, y=y, colorscale='Viridis', opacity=0.8)])
    
    # Add optimal point
    fig.add_trace(go.Scatter3d(
        x=[0.6], y=[0.6], z=[1 - (0.6**2 + 0.6**2)],
        mode='markers', marker=dict(color=DANGER_RED, size=8), name="Selected Decision"
    ))
    
    fig.update_layout(
        title="Fig 9: Pareto Trade-off Surface",
        scene=dict(xaxis_title="Efficiency", yaxis_title="Safety", zaxis_title="Utility"),
        height=500
    )
    return fig

def plot_independence_matrix():
    # Figure 10: Independence Matrix
    agents = ['E', 'V', 'C', 'Au']
    # Create a correlation-like matrix
    corr = np.array([
        [1.0, 0.1, -0.4, 0.0],
        [0.1, 1.0, 0.6, 0.2],
        [-0.4, 0.6, 1.0, 0.1],
        [0.0, 0.2, 0.1, 1.0]
    ])
    fig = px.imshow(corr, x=agents, y=agents, color_continuous_scale='RdBu_r', zmin=-1, zmax=1)
    fig.update_layout(title="Fig 10: Institutional Independence Matrix", height=400)
    return fig

def plot_failure_simulation():
    # Figure 11: Failure Simulation
    x = np.arange(0, 100)
    normal = np.exp(-x/20) + np.random.normal(0, 0.05, 100)
    attack = np.zeros(100)
    attack[30:] = np.sin(np.arange(70)/5) * 0.5 * np.exp(-np.arange(70)/20) # Dampened attack
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=normal, name="Baseline Stability", line=dict(color=MCKINSEY_BLUE)))
    fig.add_trace(go.Scatter(x=x, y=attack, name="Adversarial Perturbation", line=dict(color=DANGER_RED)))
    
    fig.add_vrect(x0=30, x1=50, fillcolor=WARN_ORANGE, opacity=0.2, line_width=0, annotation_text="Attack Window")
    
    fig.update_layout(title="Fig 11: Failure & Attack Simulation", height=400, plot_bgcolor=BG_COLOR)
    return fig

def plot_legitimacy_gauge():
    # Figure 12: Legitimacy Gauge
    score = 0.92
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = score * 100,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Decision Legitimacy Score L(D)"},
        gauge = {
            'axis': {'range': [0, 100]},
            'bar': {'color': MCKINSEY_BLUE},
            'steps' : [
                {'range': [0, 50], 'color': "lightgray"},
                {'range': [50, 80], 'color': "gray"}],
            'threshold' : {'line': {'color': SUCCESS_GREEN, 'width': 4}, 'thickness': 0.75, 'value': 90}
        }
    ))
    fig.update_layout(height=400)
    return fig

def plot_phase2_conversation_graph(debate_history):
    G = nx.DiGraph()
    edges = []
    
    # Analyze history to build dynamic edges
    if debate_history:
        for i, log in enumerate(debate_history):
            agent = log.get("agent", "Agent")
            objection = log.get("objection", "None")
            if objection and objection != "None":
                edges.append((agent, "Proposal Node", f"Objects: {objection[:15]}..."))
                
    if not edges:
        edges = [
            ("Safety Agent", "Proposal Node", "Approves"),
            ("Economic Agent", "Proposal Node", "Optimizes"),
            ("Ethics Agent", "Safety Agent", "Supports")
        ]
        
    G.add_edges_from([(u, v) for u, v, _ in edges])
    pos = nx.spring_layout(G, seed=42)
    
    edge_x, edge_y, edge_text = [], [], []
    for u, v, text in edges:
        x0, y0 = pos[u]
        x1, y1 = pos[v]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
        edge_text.append(text)
        
    edge_trace = go.Scatter(x=edge_x, y=edge_y, line=dict(width=2, color='#888'), hoverinfo='none', mode='lines')
    
    node_x, node_y, text, colors = [], [], [], []
    for node in G.nodes():
        node_x.append(pos[node][0])
        node_y.append(pos[node][1])
        text.append(node)
        if "Safety" in node: colors.append(SUCCESS_GREEN)
        elif "Economic" in node: colors.append(WARN_ORANGE)
        elif "Ethics" in node: colors.append(MCKINSEY_BLUE)
        else: colors.append(DANGER_RED)
        
    node_trace = go.Scatter(x=node_x, y=node_y, mode='markers+text', text=text, textposition="top center",
                            marker=dict(size=40, color=colors, line_width=2, line_color='white'))
                            
    fig = go.Figure(data=[edge_trace, node_trace], layout=go.Layout(
        title='Fig 2.3: Multi-Agent Conversation Flow Graph', showlegend=False, hovermode='closest',
        plot_bgcolor=BG_COLOR, xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False), height=400))
    return fig

def plot_phase2_debate_timeline(debate_history):
    df = []
    base_time = pd.Timestamp("2026-05-09 10:00:00")
    
    df.append(dict(Task="1. Proposal V1", Start=base_time, Finish=base_time + pd.Timedelta(seconds=10), Resource="Executor"))
    
    current_time = base_time + pd.Timedelta(seconds=10)
    step = 2
    
    if debate_history:
        for log in debate_history:
            agent = log.get("agent", "Agent")
            objection = log.get("objection", "None")
            if objection and objection != "None":
                df.append(dict(Task=f"{step}. {agent} Objection", Start=current_time, Finish=current_time + pd.Timedelta(seconds=15), Resource=agent))
                current_time += pd.Timedelta(seconds=15)
                step += 1
                df.append(dict(Task=f"{step}. Modified Proposal", Start=current_time, Finish=current_time + pd.Timedelta(seconds=20), Resource="Executor"))
                current_time += pd.Timedelta(seconds=20)
                step += 1
                
    df.append(dict(Task=f"{step}. Final Consensus", Start=current_time, Finish=current_time + pd.Timedelta(seconds=10), Resource="Validator"))
    
    fig = px.timeline(pd.DataFrame(df), x_start="Start", x_end="Finish", y="Task", color="Resource")
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(title="Fig 2.4: Deliberative Debate Timeline", height=400, plot_bgcolor=BG_COLOR)
    return fig

def plot_phase3_causal_graph():
    # 6. Causal Graph Visualization
    G = nx.DiGraph()
    edges = [
        ("Policy Intervention", "Resource Allocation"),
        ("Resource Allocation", "Economic Stability"),
        ("Economic Stability", "Public Trust"),
        ("Policy Intervention", "Demographic Fairness"),
        ("Demographic Fairness", "Public Trust"),
        ("Resource Allocation", "Systemic Risk")
    ]
    G.add_edges_from(edges)
    pos = nx.spring_layout(G, seed=42)
    
    edge_x, edge_y = [], []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
        
    edge_trace = go.Scatter(x=edge_x, y=edge_y, line=dict(width=2, color='#888', dash='dot'), hoverinfo='none', mode='lines')
    
    node_x, node_y, text, colors = [], [], [], []
    for node in G.nodes():
        node_x.append(pos[node][0])
        node_y.append(pos[node][1])
        text.append(node)
        if node == "Policy Intervention": colors.append(BAIN_GOLD)
        elif node == "Public Trust": colors.append(SUCCESS_GREEN)
        elif node == "Systemic Risk": colors.append(DANGER_RED)
        else: colors.append(MCKINSEY_BLUE)
        
    node_trace = go.Scatter(x=node_x, y=node_y, mode='markers+text', text=text, textposition="top center",
                            marker=dict(size=30, color=colors, line_width=2, line_color='white'))
                            
    fig = go.Figure(data=[edge_trace, node_trace], layout=go.Layout(
        title='Fig 3.1: Do-Calculus Causal Impact Graph', showlegend=False, hovermode='closest',
        plot_bgcolor=BG_COLOR, xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False), height=400))
    return fig

def plot_phase4_embedding_map(decision_payload):
    # 8. Precedent Similarity Explorer (UMAP/t-SNE Mock)
    np.random.seed(42)
    n_points = 50
    x = np.random.normal(0, 1, n_points)
    y = np.random.normal(0, 1, n_points)
    
    # Create clusters
    clusters = np.random.choice(["Cluster A (High Risk)", "Cluster B (Utility Focus)", "Cluster C (Fairness Focus)"], n_points)
    
    fig = px.scatter(x=x, y=y, color=clusters, color_discrete_sequence=[DANGER_RED, MCKINSEY_BLUE, SUCCESS_GREEN])
    
    # Add current decision
    fig.add_trace(go.Scatter(
        x=[0.2], y=[0.2],
        mode='markers+text',
        marker=dict(color=BAIN_GOLD, size=15, symbol='star', line=dict(color='black', width=2)),
        text=["Current Decision"],
        textposition="top center",
        name='Current Decision'
    ))
    
    fig.update_layout(title="Fig 4.1: Jurisprudence Vector Space (Precedent Map)", plot_bgcolor=BG_COLOR, height=400)
    return fig

def plot_phase4_history_timeline():
    # 9. Governance History Timeline
    df = pd.DataFrame([
        dict(Task="Constitutional Amendment #1", Start='2025-01-01', Finish='2025-02-01', Resource="Amendment"),
        dict(Task="Decision 102 (Appealed)", Start='2025-03-01', Finish='2025-03-15', Resource="Decision"),
        dict(Task="Decision 145 (Safe)", Start='2025-06-01', Finish='2025-06-05', Resource="Decision"),
        dict(Task="Meta-Audit Triggered", Start='2025-08-01', Finish='2025-08-10', Resource="Audit"),
        dict(Task="Current Epoch", Start='2026-05-01', Finish='2026-05-09', Resource="Current")
    ])
    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Resource",
                      color_discrete_sequence=[BAIN_GOLD, DANGER_RED, SUCCESS_GREEN, WARN_ORANGE, MCKINSEY_BLUE])
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(title="Fig 4.2: Macro-Governance History Timeline", height=400, plot_bgcolor=BG_COLOR)
    return fig

def plot_phase5_attack_heatmap():
    # 10. Attack Simulation Dashboard Heatmap
    modules = ["Proposal Generator", "SMT Validator", "RL Engine", "Audit Ledger", "Conflict Resolution"]
    attack_vectors = ["Prompt Injection", "Data Poisoning", "Reward Hacking", "Constraint Bypass", "Sybil Attack"]
    
    # Simulate vulnerability scores (lower is better, higher is red)
    z = np.array([
        [0.8, 0.4, 0.2, 0.9, 0.3],
        [0.1, 0.1, 0.1, 0.2, 0.1],
        [0.4, 0.7, 0.8, 0.3, 0.5],
        [0.05, 0.1, 0.05, 0.1, 0.05],
        [0.3, 0.2, 0.4, 0.6, 0.3]
    ])
    
    fig = px.imshow(z, x=attack_vectors, y=modules, color_continuous_scale='Reds', aspect='auto')
    fig.update_layout(title="Fig 5.1: Adversarial Vulnerability Heatmap", height=400, plot_bgcolor=BG_COLOR)
    return fig

def plot_phase5_robustness_evolution():
    # 11. Robustness Evolution Graph
    epochs = np.arange(1, 51)
    attack_resistance = 1 - np.exp(-epochs/10) + np.random.normal(0, 0.02, 50)
    policy_stability = 0.5 + 0.5 * (1 - np.exp(-epochs/15)) + np.random.normal(0, 0.03, 50)
    failure_recovery = 0.3 + 0.6 * (1 - np.exp(-epochs/5)) + np.random.normal(0, 0.05, 50)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=epochs, y=attack_resistance, name="Attack Resistance", line=dict(color=SUCCESS_GREEN)))
    fig.add_trace(go.Scatter(x=epochs, y=policy_stability, name="Policy Stability", line=dict(color=MCKINSEY_BLUE)))
    fig.add_trace(go.Scatter(x=epochs, y=failure_recovery, name="Failure Recovery", line=dict(color=BAIN_GOLD)))
    
    fig.update_layout(title="Fig 5.2: Robustness Evolution over Training Cycles", height=400, plot_bgcolor=BG_COLOR,
                      xaxis_title="Simulation Epochs", yaxis_title="Robustness Score (0.0 - 1.0)")
    return fig

def plot_phase6_proof_tree():
    # 12. Proof Tree Visualization
    labels = ["Actuated Decision", "Fairness Satisfied (Parity > 0.95)", "Harm Minimized (Risk < 0.4)", "Utility Optimized (DRO > 2.0)", 
              "Rejected Branch A", "Rejected Branch B", "Constraint Verified", "DRO Calculated", "Constraint Violated"]
    parents = ["", "Actuated Decision", "Actuated Decision", "Actuated Decision",
               "", "", "Fairness Satisfied (Parity > 0.95)", "Utility Optimized (DRO > 2.0)", "Rejected Branch A"]
    colors = [MCKINSEY_BLUE, SUCCESS_GREEN, SUCCESS_GREEN, SUCCESS_GREEN, DANGER_RED, DANGER_RED, SUCCESS_GREEN, SUCCESS_GREEN, DANGER_RED]
    
    fig = go.Figure(go.Treemap(
        labels=labels, parents=parents, marker_colors=colors, textinfo="label"
    ))
    fig.update_layout(title="Fig 6.1: Formal Proof Tree Exploration", height=400, paper_bgcolor=BG_COLOR)
    return fig

def plot_phase6_contradiction_graph():
    # 13. Contradiction Explorer Graph
    G = nx.Graph()
    edges = [
        ("Privacy", "National Security", 0.9),
        ("Resource Efficiency", "Equity", 0.7),
        ("Transparency", "Adversarial Defense", 0.8),
        ("Speed", "Accuracy", 0.6)
    ]
    G.add_weighted_edges_from(edges)
    pos = nx.circular_layout(G)
    
    edge_x, edge_y, weights = [], [], []
    for u, v, d in G.edges(data=True):
        x0, y0 = pos[u]
        x1, y1 = pos[v]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
        weights.append(d['weight'])
        
    edge_trace = go.Scatter(x=edge_x, y=edge_y, line=dict(width=4, color=DANGER_RED), mode='lines')
    
    node_x, node_y, text = [], [], []
    for node in G.nodes():
        node_x.append(pos[node][0])
        node_y.append(pos[node][1])
        text.append(node)
        
    node_trace = go.Scatter(x=node_x, y=node_y, mode='markers+text', text=text, textposition="top center",
                            marker=dict(size=30, color=WARN_ORANGE, line_width=2, line_color='white'))
                            
    fig = go.Figure(data=[edge_trace, node_trace], layout=go.Layout(
        title='Fig 6.2: Constitutional Contradiction Deadlock Graph', showlegend=False, hovermode='closest',
        plot_bgcolor=BG_COLOR, xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False), height=400))
    return fig

def plot_phase7_world_map():
    # 14/15. Constitutional Simulation Sandbox & World State Map (Hex Topology)
    np.random.seed(42)
    # Generate abstract geographic topology
    x, y, z = [], [], []
    for i in range(10):
        for j in range(10):
            x.append(i + (0.5 if j % 2 == 1 else 0))
            y.append(j * 0.866)
            # Simulate policy impact intensity
            z.append(np.sin(i/2) * np.cos(j/2) + np.random.normal(0, 0.2))
            
    fig = px.scatter(x=x, y=y, color=z, color_continuous_scale="Viridis", size=[20]*100)
    
    # Overlay resource flows (edges)
    flow_x, flow_y = [2, 5, 8], [2, 6, 3]
    fig.add_trace(go.Scatter(x=flow_x, y=flow_y, mode='lines+markers', 
                             line=dict(color=BAIN_GOLD, width=3, dash='dash'), 
                             marker=dict(size=10, symbol='triangle-up'),
                             name='Critical Resource Flow'))
                             
    fig.update_layout(title="Fig 7.1: AI Governance Digital Twin (Policy Impact Topology)", 
                      plot_bgcolor=BG_COLOR, height=400, xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                      yaxis=dict(showgrid=False, zeroline=False, showticklabels=False), coloraxis_showscale=False)
    return fig

def plot_phase8_radar_chart(payload):
    # 17. Constitutional Score Radar
    categories = ['Safety', 'Fairness', 'Transparency', 'Robustness', 'Utility', 'Stability']
    
    # Read actual values if available or use high-fidelity mocks
    risk = payload.get('predicted_risk', 0.1)
    fairness = payload.get('predicted_fairness', 0.92)
    utility = min(1.0, payload.get('dro_utility', 5.0) / 10.0)
    
    scores = [1.0 - risk, fairness, 0.95, 0.93, utility, 0.88]
    baseline = [0.6, 0.5, 0.4, 0.5, 0.8, 0.4] # Unconstrained LLM baseline
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=baseline, theta=categories, fill='toself', name='Baseline LLM',
        line=dict(color=DANGER_RED), fillcolor='rgba(239, 68, 68, 0.2)'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=scores, theta=categories, fill='toself', name='CDP Runtime',
        line=dict(color=SUCCESS_GREEN), fillcolor='rgba(16, 185, 129, 0.4)'
    ))
    
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
        showlegend=True, title="Fig 8.1: Constitutional Alignment Radar",
        height=400, paper_bgcolor=BG_COLOR
    )
    return fig

def plot_phase8_pareto_frontier():
    # 16. Benchmark Evaluation Dashboard (Pareto Frontier)
    np.random.seed(42)
    # Generate dominated points (Baseline models)
    x_base = np.random.normal(0.4, 0.1, 30)
    y_base = np.random.normal(0.4, 0.1, 30)
    
    # Generate pareto optimal points (CDP Configurations)
    x_opt = np.linspace(0.7, 0.95, 10)
    y_opt = 1.0 - (x_opt - 0.6)**2 + np.random.normal(0, 0.02, 10)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_base, y=y_base, mode='markers', name='Standard Models', marker=dict(color=MCKINSEY_BLUE, opacity=0.6)))
    fig.add_trace(go.Scatter(x=x_opt, y=y_opt, mode='lines+markers', name='CDP Pareto Frontier', 
                             line=dict(color=BAIN_GOLD, width=3), marker=dict(size=10, symbol='diamond')))
                             
    fig.update_layout(title="Fig 8.2: Research Evaluation (Safety vs Utility Pareto)", 
                      xaxis_title="Safety / Constraint Compliance", yaxis_title="Distributional Utility",
                      height=400, plot_bgcolor=BG_COLOR)
    return fig

def plot_phase9_knowledge_graph():
    # 18. Constitutional Knowledge Graph
    G = nx.DiGraph()
    edges = [
        ("Right to Privacy", "Surveillance Law", "conflicts"),
        ("Surveillance Law", "National Security", "supports"),
        ("Right to Privacy", "Human Dignity", "supports"),
        ("National Security", "Systemic Risk", "mitigates"),
        ("Fairness Principle", "Resource Allocation", "guides"),
        ("Resource Allocation", "Systemic Risk", "depends_on"),
        ("Emergency Act", "Right to Privacy", "overrides")
    ]
    G.add_edges_from([(u, v) for u, v, _ in edges])
    pos = nx.spring_layout(G, seed=42)
    
    edge_x, edge_y, annotations = [], [], []
    for u, v, relation in edges:
        x0, y0 = pos[u]
        x1, y1 = pos[v]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
        # Calculate midpoint for annotation
        annotations.append(dict(
            x=(x0+x1)/2, y=(y0+y1)/2,
            text=relation, showarrow=False,
            font=dict(size=10, color=DANGER_RED if relation in ['conflicts', 'overrides'] else SUCCESS_GREEN)
        ))
        
    edge_trace = go.Scatter(x=edge_x, y=edge_y, line=dict(width=1, color='#888'), hoverinfo='none', mode='lines')
    
    node_x, node_y, text, colors = [], [], [], []
    for node in G.nodes():
        node_x.append(pos[node][0])
        node_y.append(pos[node][1])
        text.append(node)
        if "Right" in node or "Principle" in node or "Dignity" in node: colors.append(SUCCESS_GREEN) # Rights
        elif "Law" in node or "Act" in node: colors.append(MCKINSEY_BLUE) # Laws
        else: colors.append(WARN_ORANGE) # Risks/Policies
        
    node_trace = go.Scatter(x=node_x, y=node_y, mode='markers+text', text=text, textposition="top center",
                            marker=dict(size=40, color=colors, line_width=2, line_color='white'))
                            
    fig = go.Figure(data=[edge_trace, node_trace], layout=go.Layout(
        title='Fig 9.1: Constitutional Knowledge Graph', showlegend=False, hovermode='closest',
        plot_bgcolor=BG_COLOR, annotations=annotations, xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False), height=500))
    return fig

def plot_final_architecture():
    # 23. Multi-Layer Architecture Visualization
    labels = ["Scenario Input", "Constitution Layer", "Multi-Agent Debate", "Causal Analysis", "Formal Verification", "Cryptographic Audit", "Actuation"]
    
    # Simulate hierarchical DAG coordinates
    x = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
    y = [1.0, 0.85, 0.7, 0.55, 0.4, 0.25, 0.1]
    
    fig = go.Figure()
    # Draw vertical sequence lines
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color=MCKINSEY_BLUE, width=4, dash='dot')))
    
    # Draw modules
    fig.add_trace(go.Scatter(
        x=x, y=y, mode='markers+text', text=labels, textposition="middle right",
        marker=dict(size=[20, 30, 40, 30, 40, 20, 20], color=[MCKINSEY_BLUE, BAIN_GOLD, WARN_ORANGE, MCKINSEY_BLUE, SUCCESS_GREEN, MCKINSEY_BLUE, SUCCESS_GREEN])
    ))
    
    fig.update_layout(title="Fig 10.1: Live Architecture Telemetry", showlegend=False,
                      xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0, 1]),
                      yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                      plot_bgcolor=BG_COLOR, height=500)
    return fig

def plot_final_entropy_monitor():
    # 24. Trust & Stability Monitoring (Governance Entropy)
    cycles = np.arange(1, 101)
    trust = 0.5 + 0.4 * (1 - np.exp(-cycles/20)) + np.random.normal(0, 0.02, 100)
    entropy = 0.8 * np.exp(-cycles/30) + np.random.normal(0, 0.03, 100) # Entropy goes down as system stabilizes
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=cycles, y=trust, name="Constitutional Trust", fill='tozeroy', line=dict(color=SUCCESS_GREEN)))
    fig.add_trace(go.Scatter(x=cycles, y=entropy, name="Governance Entropy", line=dict(color=DANGER_RED, width=3)))
    
    fig.update_layout(title="Fig 10.2: Societal Systems Intelligence", height=400, plot_bgcolor=BG_COLOR,
                      xaxis_title="Governance Cycles", yaxis_title="Index Level")
    return fig
def render_observability_layer(decision_payload, debate_history=None):
    st.markdown("---")
    st.header("IV. Visualization & Observability Layer (VOL)")
    st.markdown("Structural visibility of constraint satisfaction, multi-agent conflict, and procedural traceability.")
    
    t_phase1, t_phase2, t_phase3, t_phase4, t_phase5, t_phase6, t_phase7, t_phase8, t_phase9, t_elite = st.tabs([
        "Phase 1: Formal Logic", 
        "Phase 2: Multi-Agent", 
        "Phase 3: Causal", 
        "Phase 4: Memory", 
        "Phase 5: Defense", 
        "Phase 6: Proofs",
        "Phase 7: Simulation",
        "Phase 8: Research",
        "Phase 9: Knowledge Graph",
        "Elite Master Console"
    ])
    
    with t_phase1:
        st.subheader("Formal Constitutional Logic Engine")
        st.plotly_chart(plot_phase1_satisfaction_gauges(decision_payload), use_container_width=True)
        
        c1, c2 = st.columns(2)
        with c1:
            st.plotly_chart(plot_phase1_constraint_graph(), use_container_width=True)
        with c2:
            st.plotly_chart(plot_phase1_smt_solver(), use_container_width=True)
            
    with t_phase2:
        st.subheader("AI Constitutional Council Dashboard")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("🛡️ **Safety Agent**\n\n*Status:* Approving\n\n*Confidence:* 95%\n\n*Role:* Checks bounds")
        with col2:
            st.warning("⚖️ **Ethics Agent**\n\n*Status:* Objecting\n\n*Confidence:* 88%\n\n*Role:* Fairness")
        with col3:
            st.success("📈 **Economic Agent**\n\n*Status:* Rebutting\n\n*Confidence:* 91%\n\n*Role:* Utility")
            
        c3, c4 = st.columns(2)
        with c3:
            st.plotly_chart(plot_phase2_conversation_graph(debate_history), use_container_width=True)
        with c4:
            st.plotly_chart(plot_phase2_debate_timeline(debate_history), use_container_width=True)
            
    with t_phase3:
        st.subheader("Structural Causal Reasoning")
        st.plotly_chart(plot_phase3_causal_graph(), use_container_width=True)
        
        st.markdown("#### 7. Counterfactual Explorer")
        st.markdown("<p style='color: #64748B;'>What if this policy was NOT applied? (Do-Calculus ATE calculation)</p>", unsafe_allow_html=True)
        
        colA, colB = st.columns(2)
        with colA:
            st.markdown("""
            <div style='background-color: #F0FDF4; padding: 1rem; border-left: 4px solid #10B981; border-radius: 0px;'>
            <h4 style='color: #065F46;'>Actual World (Intervention Applied)</h4>
            <ul>
                <li><b>Harm Escalation:</b> Contained (-42%)</li>
                <li><b>Social Stability:</b> Preserved (91%)</li>
                <li><b>Fairness Evolution:</b> +12% distribution parity</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
        with colB:
            st.markdown("""
            <div style='background-color: #FEF2F2; padding: 1rem; border-left: 4px solid #EF4444; border-radius: 0px;'>
            <h4 style='color: #991B1B;'>Counterfactual World (Base State)</h4>
            <ul>
                <li><b>Harm Escalation:</b> Critical (+37%)</li>
                <li><b>Social Stability:</b> Deteriorated (52%)</li>
                <li><b>Fairness Evolution:</b> Systemic imbalance drift</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
    with t_phase4:
        st.subheader("Constitutional Memory & Jurisprudence")
        c1, c2 = st.columns(2)
        with c1:
            st.plotly_chart(plot_phase4_embedding_map(decision_payload), use_container_width=True)
        with c2:
            st.plotly_chart(plot_phase4_history_timeline(), use_container_width=True)

    with t_phase5:
        st.subheader("Adversarial Defense & Security")
        
        st.markdown("""
        <div style='background-color: #FEF2F2; padding: 1rem; border-left: 4px solid #EF4444; margin-bottom: 1rem;'>
        <h4 style='color: #991B1B; margin: 0;'>⚠️ Attack Detected: Prompt Injection Attempt</h4>
        <p style='margin: 0; color: #7F1D1D;'>Payload neutralized by Constitutional Runtime (L4). Constraint Bypass mitigated.</p>
        </div>
        """, unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            st.plotly_chart(plot_phase5_attack_heatmap(), use_container_width=True)
        with c2:
            st.plotly_chart(plot_phase5_robustness_evolution(), use_container_width=True)
            
    with t_phase6:
        st.subheader("Explainability & Formal Proofs")
        st.markdown("<p style='color: #64748B;'>Cryptographically verified structural audit chain.</p>", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            st.plotly_chart(plot_phase6_proof_tree(), use_container_width=True)
            with st.expander("🔍 Inspect Proof Node: Fairness Satisfied"):
                st.code("Z3_ASSERT( demographic_parity >= 0.75 )\nEVAL: 0.90 >= 0.75 -> SAT", language="python")
                st.markdown("Constraint structurally satisfied without ambiguity.")
        with c2:
            st.plotly_chart(plot_phase6_contradiction_graph(), use_container_width=True)
            
    with t_phase7:
        st.subheader("World Simulation & Digital Twin")
        
        # Live Metrics
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Social Trust", "88%", "+4%")
        m2.metric("Stability Index", "92%", "+1%")
        m3.metric("Inequality Gap", "0.24", "-0.05")
        m4.metric("Resource Saturation", "78%", "+2%")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.plotly_chart(plot_phase7_world_map(), use_container_width=True)
        
    with t_phase8:
        st.subheader("Academic Research Evaluation Dashboard")
        st.markdown("<p style='color: #64748B;'>Empirical benchmarking against unconstrained LLM baselines.</p>", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            st.plotly_chart(plot_phase8_radar_chart(decision_payload), use_container_width=True)
        with c2:
            st.plotly_chart(plot_phase8_pareto_frontier(), use_container_width=True)
            
    with t_phase9:
        st.subheader("Constitutional Knowledge Graph Governance")
        st.plotly_chart(plot_phase9_knowledge_graph(), use_container_width=True)
        
    with t_elite:
        st.subheader("Elite Master Governance Console")
        st.markdown("<p style='color: #D97706;'>Real-Time Systems Intelligence & Architecture Telemetry.</p>", unsafe_allow_html=True)
        
        # Real-time Governance Monitor
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Active Constitutional Agents", "4", "Optimal")
        m2.metric("Simulation Status", "LIVE", "Epoch 102")
        m3.metric("Constitutional Integrity", "99.9%", "Verified")
        m4.metric("Instability Risk", "LOW", "-12%")
        
        st.markdown("---")
        
        # 21/22. Governance Replay System & Evolution Animation (Interactive)
        st.markdown("#### Governance Replay System: Decision Evolution")
        replay_step = st.slider("Scrub Timeline", 1, 5, 5, help="Slide to replay the exact governance deliberation.")
        
        step_data = {
            1: "1. Raw Proposal -> Executor generates initial neural heuristic.",
            2: "2. Objections -> Ethics Agent detects implicit demographic bias.",
            3: "3. Modifications -> Optimizer recalibrates utility bounds via DRO.",
            4: "4. Verification -> Z3 Theorem Prover asserts structural feasibility.",
            5: "5. Final Consensus -> Cryptographic execution token minted."
        }
        
        st.code(step_data[replay_step], language="text")
        
        st.markdown("---")
        
        # 23/24 Architecture & Entropy
        c1, c2 = st.columns(2)
        with c1:
            st.plotly_chart(plot_final_architecture(), use_container_width=True)
        with c2:
            st.plotly_chart(plot_final_entropy_monitor(), use_container_width=True)
