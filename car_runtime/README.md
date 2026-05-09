# The Constitutional Decision Protocol (CDP)

A computationally rigorous, integrated multi-agent system designed to enforce structural, procedural, and mathematical limits on autonomous algorithmic decision-making. 

This repository contains the full executable prototype, mapping advanced formal verification methods and game-theoretic constraints directly into a Python pipeline.

## 🚀 Quickstart: How to Run the Project

The entire system is already built and configured for you. To implement and run the project locally, follow these steps:

### 1. Prerequisites
Ensure you have the required dependencies installed. Open your terminal in the `car_runtime` folder and run:
```bash
pip install -r requirements.txt
```
*(This installs `z3-solver` for formal logic, `networkx` and `dowhy` for causal inference, and `groq` for the LLM).*

### 2. Execute the Main Pipeline
Run the orchestrator script:
```bash
python main.py
```

### 3. Understanding the Output
When you run the system, you will see a console trace of the **11-Layer Pipeline**. Watch specifically for:
*   **Layer 3 (LLM Generation)**: The system contacts Groq (`llama-3.1-8b-instant`) to generate candidate decisions based on your prompt.
*   **Layer 6 (Adjudication)**: The system runs the LLM's outputs through the **Z3 SMT solver**. You will see it either `PASS` or `FAIL` based on whether the LLM obeyed the math.
*   **Layer 10 (Audit)**: The successful decisions are permanently saved to `provenance_ledger.db` (a local SQLite database created in your folder).

---

## 🧠 Customizing the System (How to Use It)

### 1. Change the Constitutional Rules
The system obeys strict mathematical boundaries. You can change these boundaries without touching the Python code!
*   Open **`rules.yaml`**.
*   You will see rules like `predicted_risk < 0.1`. 
*   Change `0.1` to `0.5`, save the file, and run `main.py` again to see how the system adapts.

### 2. Change the LLM Prompt
*   Open **`main.py`**.
*   Scroll to the bottom where `sample_request` is defined.
*   Change the `"context"` to whatever scenario you want the AI to solve (e.g., `"Decide on autonomous vehicle braking trajectory"`).

---

## 🏛️ Architecture Breakdown (Where everything is located)

If you are presenting this code for research (e.g., NeurIPS), here is where all the advanced theoretical methods are actually implemented in the code:

*   **Formal Logic & SMT Solving**: `layers/l2_constraints.py` (Compiles YAML into Z3).
*   **Mechanism Design & Game Theory**: `layers/l6_adjudication.py` (Uses VCG payment calculations and Nash Equilibrium staking for validators).
*   **Distributed Consensus**: `layers/l6_adjudication.py` (Uses Python `asyncio` to simulate independent BFT agent voting).
*   **Causal Inference & Do-Calculus**: `layers/l8_appeal.py` (Uses Microsoft `dowhy` and `networkx` to run counterfactuals).
*   **Information Flow Control & Privacy**: `layers/l1_input.py` (Injects Differential Privacy noise and checks security labels).
*   **Robust Optimization**: `layers/l3_generation.py` (Applies a Min-Max DRO penalty to LLM outputs).
*   **Formal Argumentation Theory**: `layers/l7_conflict.py` (Uses Dung's Abstract Argumentation to resolve objective conflicts).
*   **Control Theory**: `main.py` (Implements a Lyapunov stability feedback loop to prevent system divergence).

---

## 📊 Database Audit
The system utilizes **Event Sourcing**. Every time a decision passes all checks, it is written to the SQLite database.
To view your historical decisions:
1. Open the `provenance_ledger.db` file using any SQLite viewer (like DBeaver or a VSCode extension).
2. Query the `events` table to see the full cryptographically secure history of the system.
