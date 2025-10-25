# 🧠 AWS Lambda – Retrieve HTML from S3

This project demonstrates how to use **AWS Lambda** to retrieve an HTML file stored in **Amazon S3**, process it if required, and return the content as an HTTP response or for further integration.

---

---

## 🚀 Features

- AWS Lambda function written in **Python**
- Retrieves **HTML files from S3**
- Example **test event JSON** for simulating function triggers
- HTML folder for reference structure or output testing
- Simple, modular folder organization

---

## ⚙️ How It Works

1. Upload your HTML file to an S3 bucket.  
2. Deploy the `lambda_function.py` from the `lamda` folder to AWS Lambda.  
3. Configure an IAM Role with **S3 Read permissions**.  
4. Use `test_events.json` to simulate Lambda events locally or through the AWS Console.  
5. Lambda fetches the specified HTML file from S3 and returns its content.

---

## 🧩 Example Event (test_events.json)

```json
{
  "bucket_name": "your-bucket-name",
  "file_key": "index.html"
}

```
## 🪄 Technologies Used
AWS Lambda

Amazon S3

Python (boto3)

HTML

```

```
## Future enhacements:

Add support for multiple file types (e.g., JSON, text)

Integrate with API Gateway to return HTML as HTTP response

Add error handling and logging to CloudWatch
