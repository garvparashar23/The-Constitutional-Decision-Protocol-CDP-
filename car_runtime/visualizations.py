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

def plot_constraint_graph():
    # Figure 2: Constraint Graph
    G = nx.DiGraph()
    constraints = ["C1: Risk < 0.3", "C2: Fairness > 0.8", "C3: Utility > 0.5", "C4: Budget", "C5: Causal Link"]
    G.add_edges_from([
        ("Input", "C1: Risk < 0.3"),
        ("Input", "C2: Fairness > 0.8"),
        ("Input", "C4: Budget"),
        ("C1: Risk < 0.3", "C3: Utility > 0.5"),
        ("C2: Fairness > 0.8", "C3: Utility > 0.5"),
        ("C4: Budget", "C5: Causal Link")
    ])
    
    pos = nx.spring_layout(G, seed=42)
    
    edge_x, edge_y = [], []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
        
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1, color='#888'),
        hoverinfo='none',
        mode='lines')

    node_x, node_y, text, colors = [], [], [], []
    for node in G.nodes():
        node_x.append(pos[node][0])
        node_y.append(pos[node][1])
        text.append(node)
        if node == "Input":
            colors.append(MCKINSEY_BLUE)
        elif "Budget" in node:
            colors.append(WARN_ORANGE) # simulate a conflicting/boundary constraint
        else:
            colors.append(SUCCESS_GREEN) # satisfied
            
    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        text=text,
        textposition="top center",
        marker=dict(size=20, color=colors, line_width=2))
        
    fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='Fig 2: Constraint Graph & UNSAT Core',
                showlegend=False,
                hovermode='closest',
                plot_bgcolor=BG_COLOR,
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                height=400))
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

def render_observability_layer(decision_payload):
    st.markdown("---")
    st.header("IV. Visualization & Observability Layer (VOL)")
    st.markdown("Structural visibility of constraint satisfaction, multi-agent conflict, and procedural traceability.")
    
    t1, t2, t3, t4 = st.tabs(["Geometric & Logical State", "Procedural & Temporal", "Optimization & Independence", "Resilience & Legitimacy"])
    
    with t1:
        c1, c2 = st.columns(2)
        with c1: st.plotly_chart(plot_decision_state_space(decision_payload), use_container_width=True)
        with c2: st.plotly_chart(plot_constraint_graph(), use_container_width=True)
        
        c3, c4 = st.columns(2)
        with c3: st.plotly_chart(plot_conflict_graph(), use_container_width=True)
        with c4: st.plotly_chart(plot_causal_graph(), use_container_width=True)
        
    with t2:
        st.plotly_chart(plot_decision_timeline(), use_container_width=True)
        c1, c2 = st.columns(2)
        with c1: st.plotly_chart(plot_counterfactual_tree(), use_container_width=True)
        with c2: render_governance_dashboard()
        
    with t3:
        c1, c2 = st.columns(2)
        with c1: st.plotly_chart(plot_tradeoff_surface(), use_container_width=True)
        with c2: st.plotly_chart(plot_independence_matrix(), use_container_width=True)
        st.plotly_chart(plot_uncertainty_map(), use_container_width=True)
        
    with t4:
        c1, c2 = st.columns(2)
        with c1: st.plotly_chart(plot_failure_simulation(), use_container_width=True)
        with c2: st.plotly_chart(plot_legitimacy_gauge(), use_container_width=True)
