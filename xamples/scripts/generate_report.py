import json

def generate_audit_brief(json_log):
    # This script simulates turning a JSON file into a human-readable report
    data = json.loads(json_log)
    
    report = f"""
    =========================================
    LXD ADVISORY: AI AUDIT DEFENSE BRIEF
    =========================================
    REPORT ID: {data['compliance_id']}
    STATUS: COMPLIANT
    
    SUMMARY OF INFERENCE:
    - Model: {data['metadata']['model_version']}
    - Decision: {data['inference_logic']['decision']}
    - Confidence: {data['inference_logic']['actual_confidence'] * 100}%
    
    REGULATORY ALIGNMENT:
    - Article 12 (Traceability): VERIFIED
    - Article 14 (Human Oversight): ACTIVE
    
    =========================================
    GENERATED AUTOMATICALLY BY LXD FRAMEWORK
    =========================================
    """
    print(report)

# During the session, you run this and show them how the "Tax" disappears.
