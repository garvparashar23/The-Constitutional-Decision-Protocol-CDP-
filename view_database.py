import sqlite3
import json

def view_database():
    print("="*60)
    print(" THE CONSTITUTIONAL DECISION PROTOCOL (CDP) - FINAL AUDIT LOG")
    print("="*60)
    
    try:
        conn = sqlite3.connect("car_runtime/provenance_ledger.db")
        c = conn.cursor()
        
        # Query the database
        c.execute("SELECT id, type, timestamp, payload FROM events")
        rows = c.fetchall()
        
        if not rows:
            print("The database is currently empty.")
            return

        for row in rows:
            event_id, event_type, timestamp, payload_json = row
            payload = json.loads(payload_json)
            
            print(f"\n[EVENT: {event_type.upper()}]")
            print(f"ID: {event_id}")
            
            if "content" in payload:
                print("--- FINAL ACTUATED DECISION ---")
                print(f"Action/Decision: {payload['content'].get('action')}")
                print(f"Predicted Risk:  {payload['content'].get('predicted_risk')}")
                print(f"Predicted Fairness: {payload['content'].get('predicted_fairness')}")
                print(f"Utility Score:   {payload['content'].get('dro_utility')}")
            else:
                print("Payload:", json.dumps(payload, indent=2))
                
        conn.close()
        print("\n" + "="*60)
        
    except sqlite3.OperationalError:
        print("Database not found. Please run 'python main.py' first.")

if __name__ == "__main__":
    view_database()
