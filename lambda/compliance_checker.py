import json

def lambda_handler(event, context):
    """
    Simulated IAM Role & Policy Compliance Checker
    Detects overly permissive IAM policies (Action: *, Resource: *)
    """
    print("Event received:", json.dumps(event))

    # Example IAM Policy Simulation
    simulated_policies = [
        {"Role": "DevOpsRole", "Policy": {"Action": "*", "Resource": "*"}},
        {"Role": "ReadOnlyRole", "Policy": {"Action": ["s3:GetObject"], "Resource": "*"}}
    ]

    non_compliant = []

    for policy in simulated_policies:
        actions = policy["Policy"]["Action"]
        resources = policy["Policy"]["Resource"]
        if actions == "*" or resources == "*":
            non_compliant.append(policy["Role"])

    if non_compliant:
        message = {
            "Status": "Non-Compliant",
            "Roles": non_compliant
        }
    else:
        message = {"Status": "Compliant"}

    print("Compliance check result:", message)

    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }
