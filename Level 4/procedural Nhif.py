def calculate_claim_procedural(amount):
    return amount * 0.90

patient_data = {"name": "Alice Wanjiku", "policy_no": "NHIF-5544"}
bill_amount = 8000

final_claim = calculate_claim_procedural(bill_amount)
print(f"Processed claim for {patient_data['name']}: {final_claim}")