# QA/Data Ops - Automated Unit Testing for Manufacturing Line

## Introduction

In an event-driven architecture, data contracts play a crucial role in ensuring compatibility and communication between different components or services. The goal is to validate that data exchanges adhere to the defined contracts, allowing seamless integration and preventing breaking changes. In this assignment, you will focus on automated unit testing for a Manufacturing Line API, which is a mock API that simulates the initiation of the production line in a manufacturing environment.

## Assignment – Overview

In this assignment, you will build and run a Docker container hosting a Manufacturing Line API. You will use cURL to interact with the API and initiate the production line. Additionally, you will design and execute unit tests to ensure contract compliance using a scripting language or framework of your choice. Finally, you will showcase how these tests can be integrated into an overall framework for automation and continuous testing.


## Mock API - Manufacturing Line API

The Manufacturing Line API is a mock API that allows the initiation of the production line in a manufacturing environment. It exposes a single endpoint, `/api/v1/production-line/start`, which accepts a JSON payload with the `productId` and `quantity` fields. The API validates the payload against the defined contract and starts the production line accordingly.

## Assignment Tasks

1. Build & Run the Docker Container:
   - Clone the provided repository containing `app.py`, `requirements.txt`, and `Dockerfile`.
   - Build the Docker image:
     ```
     docker build -t manufacturing-line-api .
     ```
   - Run the Docker container:
     ```
     docker run -p 8080:8080 manufacturing-line-api
     ```

2. Using the Mock API:
   - Test the Mock API using cURL:
     ```
     curl -X POST -H "Content-Type: application/json" -d '{"productId": "ABC123", "quantity": 100}' localhost:8080/api/v1/production-line/start
     ```

3. Test Strategy Slide:
   - Create a slide that explains the scenario, tests, and the chosen framework.
   - Include an overview of the Manufacturing Line API, the API contract, and the importance of automated unit testing.
   - Describe the selected framework for unit testing and how it enables efficient contract validation.

4. Unit Testing with Chosen Framework:
   - Using a scripting language or framework of your choice (e.g., Python with pytest), design and execute unit tests to validate the contract compliance of the Manufacturing Line API.
   - Focus on scenarios such as valid and invalid payloads, edge cases, and data type validation.
   - Demonstrate the ability to test the API endpoints and assert the expected responses based on the contract.
   - The file testcases.md gives a couple of examples, you are free to use those or create your own.

5. Automation Integration:
   - Showcase how the unit tests can be integrated into an overall testing framework for automation purposes.
   - Explain how the unit tests can be seamlessly incorporated into a continuous integration and delivery (CI/CD) pipeline.
   - Discuss strategies for running the tests in parallel, generating test reports, and integrating them with other quality assurance and data operations processes.
