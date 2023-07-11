# Test Cases

## Description

Send a valid request payload to the /production-line/start endpoint and verify that the production line starts successfully.

Steps:
* Create a test case with a valid request payload.
* Send the request to the API.
* Assert that the API returns a response with a status code of 200, indicating a successful start of the production line.
* Test: Invalid request payload returns appropriate error response

## Description

Send a request with an invalid or missing field to the /production-line/start endpoint and verify that the API returns the appropriate error response.

Steps:
* Create a test case with an invalid request payload (e.g., missing productId or quantity).
* Send the request to the API.
* Assert that the API returns a response with a status code of 400, indicating a validation error.
* Test: Verify request payload data types and constraints

## Description

Send a request with different data types and constraints to the /production-line/start endpoint and verify that the API enforces them correctly.

Steps:
* Create test cases with various valid and invalid request payloads, including different data types and constraint violations.
* Send each request to the API.
* Assert that the API returns the expected response, either with a status code of 200 for valid payloads or 400 for invalid payloads.
* Test: Edge case testing for quantity field

## Description

Test the edge cases and boundary conditions for the quantity field in the request payload of the /production-line/start endpoint.

Steps:
* Create test cases with the minimum and maximum allowed values for the quantity field.
* Send each request to the API.
* Assert that the API correctly handles the edge cases and returns the expected response.
* Test: Verify response structure and format

## Description

Send a valid request to the /production-line/start endpoint and verify that the API response adheres to the defined response structure in the Swagger specification.

Steps:
* Send a valid request to start the production line.
* Receive the response from the API.
* Assert that the response structure and format match the expectations defined in the Swagger specification.
