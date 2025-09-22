
# Serverless Messaging Pipeline with API Gateway, Lambda, and SQS

## 📘 Overview

This project demonstrates a serverless architecture using AWS services to implement a messaging pipeline. It includes:

- An **API Gateway** that triggers **Lambda Function 1**
- **Lambda Function 1** sends messages to an **Amazon SQS** queue
- **Lambda Function 2** polls the SQS queue to confirm and process messages

This setup is ideal for decoupled, event-driven applications where message processing can be handled asynchronously.

---

## 🏗️ Architecture

The following diagram illustrates the flow of data through the system:

![Architecture Diagram](716c27e9d9.png)

1. **API Gateway** receives HTTP requests.
2. **Lambda Function 1** is triggered and sends a message to **Amazon SQS**.
3. **Lambda Function 2** polls the SQS queue and processes the message.

---

## ⚙️ Setup Instructions

To deploy this architecture:

1. **Create an SQS Queue**
   - Use the AWS Console or CLI to create a standard SQS queue.

2. **Create Lambda Function 1**
   - This function receives input from API Gateway and sends a message to SQS.

3. **Create Lambda Function 2**
   - This function is triggered by SQS and processes incoming messages.

4. **Configure API Gateway**
   - Create a REST API or HTTP API.
   - Set up a POST method to trigger Lambda Function 1.

5. **Set up Event Source Mapping**
   - Link the SQS queue to Lambda Function 2 using event source mapping.

6. **Test the Flow**
   - Send a request to the API Gateway endpoint.
   - Confirm that the message appears in SQS and is processed by Lambda Function 2.

---

## 🚧 Known Limitations

- Lambda Function 1 currently accepts only specific hardcoded values.
- Message validation and error handling are minimal.
- No retry or dead-letter queue (DLQ) is configured for failed messages.

---

## 🚀 Future Improvements

- Update Lambda Function 1 to accept dynamic payloads.
- Add input validation and error handling.
- Implement DLQ for failed message processing.
- Add logging and monitoring via CloudWatch.
- Use Terraform or AWS CDK for infrastructure as code.

---

## 📎 Files

- `716c27e9d9.png`: Architecture diagram
- `README.md`: This documentation file

