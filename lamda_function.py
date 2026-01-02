import json
import boto3
from fpdf import FPDF
import uuid
import os

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
s3 = boto3.client("s3")

BUCKET_NAME = "ai-code-review-reports-yourname"  # change this

def generate_pdf(content, filename):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=11)

    for line in content.split("\n"):
        pdf.multi_cell(0, 8, line)

    pdf.output(filename)

def lambda_handler(event, context):
    try:
        files = event.get("files", [])
        if not files:
            return {"statusCode": 400, "body": "No files provided"}

        code = "\n".join(files)

        prompt = f"""
You are a senior software engineer.
Review the following code and provide:
1. Project Summary
2. Issues (with severity)
3. Recommendations

Code:
{code}
"""

        response = bedrock.invoke_model(
            modelId="amazon.titan-text-express-v1",
            body=json.dumps({
                "inputText": prompt,
                "textGenerationConfig": {
                    "maxTokenCount": 800,
                    "temperature": 0.2
                }
            })
        )

        ai_text = json.loads(response["body"].read())["results"][0]["outputText"]

        file_id = str(uuid.uuid4())
        pdf_path = f"/tmp/code-review-{file_id}.pdf"

        generate_pdf(ai_text, pdf_path)

        s3_key = f"reports/code-review-{file_id}.pdf"
        s3.upload_file(pdf_path, BUCKET_NAME, s3_key)

        pdf_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{s3_key}"

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "PDF generated successfully",
                "pdf_url": pdf_url
            })
        }

    except Exception as e:
        return {"statusCode": 500, "body": str(e)}
