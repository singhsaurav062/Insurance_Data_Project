import pdfplumber
import re
import json

MANDATORY_FIELDS = [
    "policy_number",
    "policyholder",
    "date_of_loss",
    "location",
    "description",
    "claim_type",
    "estimated_damage"
]

def extract_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.lower()

def extract_fields(text):
    fields = {}

    patterns = {
        "policy_number": r"policy number\s*([a-z0-9\-]+)",
        "policyholder": r"name of insured\s*([a-z\s]+)",
        "date_of_loss": r"date of loss.*?(\d+/\d+/\d+)",
        "location": r"location of loss\s*(.*)",
        "description": r"description of accident\s*(.*)",
        "estimated_damage": r"estimate amount\s*\$?(\d+)",
    }

    for k, p in patterns.items():
        m = re.search(p, text)
        fields[k] = m.group(1).strip() if m else None

    # Simple claim type inference
    fields["claim_type"] = "injury" if "injured" in text else "vehicle"

    return fields

def find_missing(fields):
    return [f for f in MANDATORY_FIELDS if not fields.get(f)]

def route(fields, missing, text):
    if any(w in text for w in ["fraud", "staged", "inconsistent"]):
        return "Investigation Flag", "Suspicious wording detected"

    if fields["claim_type"] == "injury":
        return "Specialist Queue", "Injury claim"

    if missing:
        return "Manual Review", "Mandatory fields missing"

    try:
        if int(fields["estimated_damage"]) < 25000:
            return "Fast-track", "Low value claim"
    except:
        pass

    return "Manual Review", "Default routing"

def process(pdf):
    text = extract_text(pdf)
    fields = extract_fields(text)
    missing = find_missing(fields)
    route_to, reason = route(fields, missing, text)

    return {
        "extractedFields": fields,
        "missingFields": missing,
        "recommendedRoute": route_to,
        "reasoning": reason
    }

if __name__ == "__main__":
    result = process("sample_fnol.pdf")
    print(json.dumps(result, indent=2))
