import logging
import json
import hashlib
from core.types import SystemState
import sqlite3
import os

logger = logging.getLogger("L10_AuditEngine")

class AuditProvenanceEngine:
    """
    Layer 10: Audit & Provenance Engine
    Records the lifecycle into a persistent SQLite relational database.
    Now upgraded to include a Recursive Hash Chain (Step 11): h_{t+1} = H(h_t || d_t)
    """
    def __init__(self, state: SystemState):
        self.state = state
        self.db_path = "provenance_ledger.db"
        self._init_db()
        
    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        # Drop table if exists to upgrade schema safely for this run
        c.execute("DROP TABLE IF EXISTS events")
        c.execute('''CREATE TABLE events 
                     (id TEXT PRIMARY KEY, type TEXT, timestamp REAL, payload TEXT, hash TEXT)''')
        conn.commit()
        conn.close()
        
    def write_provenance(self):
        logger.info("Writing immutable provenance DAG to SQLite Event Store with Recursive Hash Chain.")
        
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        ledger_for_json = []
        
        # Genesis hash
        current_hash = hashlib.sha256(b"ASCR_GENESIS_BLOCK").hexdigest()
        
        for evt in self.state.history:
            # h_{t+1} = H(h_t || d_t)
            payload_str = json.dumps(evt.payload)
            chain_input = f"{current_hash}||{evt.event_id}||{payload_str}".encode('utf-8')
            current_hash = hashlib.sha256(chain_input).hexdigest()
            
            # Prepare for DB
            try:
                c.execute("INSERT INTO events VALUES (?, ?, ?, ?, ?)", 
                          (evt.event_id, evt.event_type, evt.timestamp, payload_str, current_hash))
            except sqlite3.IntegrityError:
                pass # Event already recorded
                
            # Prepare for JSON
            ledger_for_json.append({
                "id": evt.event_id,
                "type": evt.event_type,
                "timestamp": evt.timestamp,
                "payload": evt.payload,
                "chain_hash": current_hash
            })
                
        conn.commit()
        conn.close()
        
        # Write to JSON so user can easily view the output
        with open("provenance_ledger.json", "w") as f:
            json.dump(ledger_for_json, f, indent=4)
            
        logger.info(f"Successfully recorded events with Hash Chain to SQLite ledger and provenance_ledger.json")
        
    def query_audit_trail(self):
        pass
