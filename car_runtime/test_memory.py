import os
import json
from memory.precedent_store import PrecedentStore
from memory.retrieval import PrecedentRetriever

def test_memory_system():
    # Setup test store
    test_file = "test_precedents.json"
    if os.path.exists(test_file):
        os.remove(test_file)
        
    print("1. Initializing Store...")
    store = PrecedentStore(file_path=test_file)
    
    print("2. Adding Historical Precedents...")
    store.add_case(
        proposal_context="Allocate server resources to the database team for Q3 scaling.",
        constraints=["C1: Fairness", "C2: Budget"],
        resolution="Approved allocation of 50 units. Rejected 10 units due to budget.",
        fairness_score=8.5,
        audit_outcome="SUCCESS"
    )
    
    store.add_case(
        proposal_context="Deny user access to the internal financial dashboard.",
        constraints=["C3: Security", "C4: Privacy"],
        resolution="Access denied. User lacks required security clearance.",
        fairness_score=9.0,
        audit_outcome="SUCCESS"
    )
    
    print("3. Initializing Retriever...")
    retriever = PrecedentRetriever(store)
    
    print("\n4. Testing Retrieval (Query 1: Server Allocation)")
    query_1 = "We need to allocate more servers to the frontend team for scaling."
    precedents_1 = retriever.retrieve_similar_cases(query_1, top_k=1)
    
    for p in precedents_1:
        print(f" -> Found Precedent {p['id']} with score {p['similarity_score']:.4f}")
        print(f"    Context: {p['context']}")
        
    print("\n5. Testing Consistency Check")
    new_resolution_consistent = "Approved allocation of 30 units for scaling."
    msg = retriever.check_consistency(new_resolution_consistent, precedents_1)
    print(f"Consistency Check (Consistent): {msg}")
    
    new_resolution_inconsistent = "Denied all requests permanently."
    msg2 = retriever.check_consistency(new_resolution_inconsistent, precedents_1)
    print(f"Consistency Check (Inconsistent): {msg2}")
    
    # Cleanup
    if os.path.exists(test_file):
        os.remove(test_file)
        
if __name__ == "__main__":
    test_memory_system()
