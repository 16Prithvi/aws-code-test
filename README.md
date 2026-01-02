# 🚀 AI-Powered Code Review Automation System

An end-to-end, serverless, and automated code review pipeline seamlessly integrated into GitHub Actions. This project leverages **AWS components** and **Generative AI (Amazon Bedrock)** to provide intelligent, contextual, and secure code analysis for every pull request.


---

## 📖 Overview

In modern DevSecOps workflows, manual code reviews can be a bottleneck. This project solves that by automating the initial pass of code review using AI.  

Whenever a developer pushes code or opens a Pull Request (PR), the system automatically:
1.  **Captures the Diff**: GitHub Actions extracts the changes.
2.  **Analyzes with AI**: A secured AWS Lambda function invokes Amazon Bedrock to review the code against security, performance, and quality standards.
3.  **Generates a Report**: A comprehensive PDF report is generated and stored in S3.
4.  **Notifies the Developer**: The PR is commented on with a direct link to the review report.

This ensures that every line of code is reviewed for **OWASP Top 10 vulnerabilities**, **clean code principles**, and **optimization opportunities** before it even reaches a human reviewer.

---

## 🏗 Architecture

The system is built on a **fully serverless, event-driven architecture** ensuring scalability and low maintenance.

<img width="850" height="450" alt="architecture-diagram" src="https://github.com/user-attachments/assets/fd36f10a-ed35-4dce-a8ab-a628967dee12" />

### Key Components:
-   **GitHub Actions**: Orchestrates the CI/CD workflow, capturing git diffs and triggering the analysis.
-   **AWS Lambda**: The compute engine that processes the diff and interacts with the AI model.
-   **Amazon Bedrock**: The generative AI engine (using Claude or Titan models) providing deep code analysis.
-   **Amazon S3**: Secure storage for the generated PDF reports.
-   **AWS IAM**: Granular permission management to ensure least-privilege access between services.

---

## 🧠 AI Review Logic

The core intelligence lies in how the AI model processes context. We don't just send raw code; we send a structured prompt combining **System Persona** (Senior Security Engineer) and **User Context** (Git Diff).

<img width="850" height="450" alt="ai-logic-flow" src="https://github.com/user-attachments/assets/fc7cbffc-b08d-4a51-9884-cfb5c39fad18" />

The AI evaluates:
-   **Security**: Hardcoded credentials, injection risks, insecure dependencies.
-   **Performance**: O(n^2) loops, memory leaks, inefficient queries.
-   **Maintainability**: SOLID principles, function complexity, naming conventions.

---

## 📸 Workflow & Demo

### 1.GitHub Actions Workflow Execution
This image illustrates the CI/CD pipeline in motion. The GitHub Actions workflow, "stable AI code review workflow," has executed successfully. It tracks every step from checking out the repository and configuring AWS credentials to invoking the Lambda function and extracting the final PDF URL. It serves as proof of a robust, automated integration between GitHub and AWS.

<img width="850" height="450" alt="pull-req" src="https://github.com/user-attachments/assets/5d6400c1-51a4-499b-b40a-8f0cf97913e8" />

### 2.Persistent Storage in Amazon S3
This screenshot captures the Amazon S3 console, showing the reports/ directory within your dedicated bucket. It lists the generated PDF code review artifacts, each tagged with a unique identifier. This highlights the project’s ability to store historical audits securely, ensuring that every code review is archived as a persistent, downloadable resource for the development team.
Within seconds, the AI posts a comment on your PR with a secure link to the detailed report.

<img width="850" height="450" alt="github-pr-comment" src="https://github.com/user-attachments/assets/5cd3c0ce-3ca0-456f-91a5-4b26560062bc" />

### 3.Pull Request Status Integration
The final piece of the puzzle: a GitHub Pull Request showing a successful automated check. The "AI Code Review" job is marked with a green checkmark, indicating that the code has been audited and the report is ready. This demonstrates how the tool provides immediate feedback within the developer's native workflow, helping catch security flaws and logical errors before any code is merged

<img width="850" height="450" alt="s3-bucket-report" src="https://github.com/user-attachments/assets/e8683d8b-2b53-4eda-945c-43d0ae7437d4" />

---

## 🛠 Tech Stack

-   **Cloud Provider**: AWS (Lambda, S3, IAM, Bedrock)
-   **CI/CD**: GitHub Actions
-   **AI Model**: Amazon Bedrock (Claude 3 / Titan)
-   **Language**: Python (Boto3, PDF generation)
-   **Infrastructure**: Serverless

## 🚀 Getting Started

### Prerequisites
-   AWS Account with Bedrock access enabled.
-   GitHub Repository.

### Installation
1.  **Clone the Repo**
    ```bash
    git clone https://github.com/your-username/ai-code-reviewer.git
    ```
2.  **Deploy AWS Infrastructure**
    -   Create S3 Bucket.
    -   Deploy Lambda Function (upload code from `src/`).
    -   Configure IAM Roles.
3.  **Configure GitHub Secrets**
    -   `AWS_ACCESS_KEY_ID`
    -   `AWS_SECRET_ACCESS_KEY`
    -   `AWS_REGION`
    -   `S3_BUCKET_NAME`

---

*This project demonstrates the power of combining cloud-native serverless infrastructure with modern AI capabilities to enhance developer's productivity.*
