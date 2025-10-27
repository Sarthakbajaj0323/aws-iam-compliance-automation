# ☁️ AWS IAM Role & Policy Compliance Automation

### 🚀 Overview
A **serverless AWS automation system** that continuously audits IAM roles and policies, detects overly permissive access (like `Action: *`, `Resource: *`), and automatically remediates or alerts via SNS — ensuring compliance and strong cloud governance.

---

### 🧱 Architecture
![Architecture Diagram](architecture/architecture-diagram.png)

---

### 🧩 Core AWS Services Used
- **AWS Config** – Monitors IAM configuration changes  
- **Amazon EventBridge** – Triggers Lambda on drift events  
- **AWS Lambda** – Executes compliance logic  
- **Amazon SNS** – Sends real-time alerts  
- **AWS CloudTrail** – Provides audit logging  

---

### 🧠 How It Works
1. AWS Config tracks IAM role/policy changes.  
2. EventBridge forwards these events to Lambda.  
3. Lambda analyzes roles & policies for `Action: *` or `Resource: *`.  
4. If non-compliant → SNS sends alert to the admin.  
5. Optionally, remediation can be added to auto-remove permissions.

---

### ⚡ Features
- 100% Serverless  
- Real-time Compliance Checks  
- Multi-Account Monitoring Ready  
- Secure & Scalable  
- Zero Manual Intervention  

---

### 📂 Repository Structure
```
aws-iam-compliance-automation/
├── architecture/
│   └── architecture-diagram.png
├── config/
│   └── config-rule-template.json
├── eventbridge/
│   └── rule-template.json
├── lambda/
│   └── compliance_checker.py
└── sns/
    └── sns-notification-sample.json
```

---

### 🧩 Lambda Example Output
```json
{
  "Status": "Non-Compliant",
  "Roles": ["DevOpsRole"]
}
```

---
