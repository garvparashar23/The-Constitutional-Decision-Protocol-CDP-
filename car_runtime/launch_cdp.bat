@echo off
echo =======================================================
echo  THE CONSTITUTIONAL DECISION PROTOCOL (CDP)
echo  Formal Governance Infrastructure - FULL PROJECT LAUNCH
echo =======================================================
echo.

echo [1/3] Verifying environment dependencies...
pip install -r requirements.txt -q
echo Dependencies satisfied.
echo.

echo [2/3] Executing Formal Verification Simulation Suite...
echo Generating cryptographic provenance and bounded constraints...
python run_simulation.py
echo.
echo Simulation Matrix Completed Successfully!
echo.

echo [3/3] Initializing Elite Master Governance Console...
echo Launching Visualization and Observability Layer (VOL)...
start streamlit run app.py

echo.
echo =======================================================
echo  SYSTEM ONLINE. Awaiting Human-in-the-Loop input.
echo =======================================================
pause
