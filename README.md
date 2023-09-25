# JQuickR API
QR Code Generation API.

**URL :** (https://qrc-gen-api.onrender.com/)

## Table of Contents

- [JQuickR API](#jquickr-api)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Usage](#usage)
    - [Authentication](#authentication)
    - [Endpoints](#endpoints)
    - [Request Body](#request-body)
      - [Request body:](#request-body-1)
      - [Request body:](#request-body-2)
  - [Responses](#responses)
    - [Response Format](#response-format)
    - [Example Response](#example-response)
  - [Errors](#errors)
    - [Error Format](#error-format)
    - [Example Error](#example-error)
  - [Contributing](#contributing)
  - [License](#license)
  - [Creator](#creator)

## Introduction

JQuickR QR Code Generation API is a versatile solution tailored for the swift and effortless creation of QR codes. 

This API features a user-centric endpoint through which consumers can effortlessly produce QR codes. Users provide their desired message via request body, and the API generates a QR code image, securely storing it on a cloud service provider. 

Subsequently, it delivers a URL enabling users to access and disseminate the generated QR code image.

## Features

1. `Message Input`: Users can effortlessly specify the message they wish to embed in the QR code using query parameters.

2. `QR Code Generation` : The API dynamically crafts QR code images based on the user-provided messages.

3. `Cloud Storage` : All generated QR code images are securely preserved on a reliable cloud service provider, ensuring data integrity and accessibility.

4. `URL Provision` : The API returns a URL or location, simplifying user access to and distribution of the created QR code images.

## Usage

How to use API, Including Authentication(if any), How to call the endpoints and also examples

### Authentication

*NO AUTHENTICATION*

### Endpoints

Available endpoints in the API, including their input parameters and expected output.

- POST `/generate`: Generates Qrcode and returns a json containing url to the image

- DELETE `/delete`: Delete Qrcode, after passing the url o the image in the request body, it returns a response on the status

### Request Body

This contains usage examples for the API including examples and request body

1.  **Endpoint:** POST `/generate`

```BASH
curl -X 'POST' \
  'https://qrc-gen-api.onrender.com/generate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "data": "string"
}'
```

#### Request body:
```json
{
  "data":"user message"
}
```
---

2. **Endpoint:** DELETE `/delete`

```bash
curl -X 'DELETE' \
  'https://qrc-gen-api.onrender.com/delete' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "file_url": "https://cdn.uploadfly.cloud/fhRp8N/QRAPI-3115Codeimg.png"
}'
```
#### Request body:
```json
{
  "file_url":"<image_url>"
}
```


## Responses

The format of the responses returned by the API. Including example responses for each endpoint.

### Response Format

The structure of a typical API response.

```json
{
  "field1": "value1",
  "field2": "value2"
}
```

### Example Response

**Endpoint:** POST `/generate`
- **Response:**

```json
{
  "success": true,
  "status": 201,
  "data": {
    "url": "https://cdn.uploadfly.cloud/fhRp8N/QRAPI-7080Codeimg.png",
    "path": "fhRp8N/QRAPI-7080Codeimg.png",
    "type": "text/plain",
    "size": "2.41 kB",
    "name": "QRAPI-7080Codeimg.png"
  }
}
```


**Endpoint:** DELETE `/delete`
- **Response:**

```json
{
  "success": true,
  "status": 200,
  "data": {
    "message": "File deleted successfully"
  }
}
```
## Errors

Explain the possible error responses and their meanings. Include error codes and messages.

### Error Format

When calling the delete url and you miss to add the file url then this error response shows

```json
{
  "success": false,
  "status": 400,
  "error": "File URL is missing in request"
}
```

### Example Error

When calling the delete endpoint and the file url provided is invalid this response shows

```json
{
  "success": false,
  "status": 404,
  "error": "File not found"
}
```

## Contributing

Coming Soon

## License

Specify the license under which your API is distributed.
```
Loading...
```

## Creator

- **Name:** Jamin Onuegbu
- **Email:** jaminonuegbu@gmail.com
- **GitHub:** [JaminCO](https://github.com/JaminCO)
- **LinkedIn:** [Jamin Onuegbu](https://www.linkedin.com/in/jamin-onuegbu-4aa851206/)
- **Twitter:** [@jaminonuegbu](https://twitter.com/jaminonuegbu)

Feel free to reach out if you have any questions or feedback about this project. You can also connect with me on social media for updates and discussions.

---
<!-- <p align="center">
  Created by [Your Name](https://www.yourwebsite.com/)

  [![Twitter](https://img.shields.io/twitter/follow/yourtwitter?label=Follow&style=social)](https://twitter.com/yourtwitter)
  [![GitHub](https://img.shields.io/github/followers/yourgithub?label=Follow&style=social)](https://github.com/yourgithub)
  [![LinkedIn](https://img.shields.io/badge/Connect-blue?style=flat&logo=linkedin&labelColor=blue)](https://www.linkedin.com/in/yourlinkedin)

</p> -->
