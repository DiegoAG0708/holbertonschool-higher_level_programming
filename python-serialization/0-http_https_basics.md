# HTTP vs HTTPS Basics

## Differences between HTTP and HTTPS
- **HTTP**: No encryption, data is sent in plain text, vulnerable to eavesdropping.
- **HTTPS**: Secure, uses SSL/TLS encryption, protects confidentiality and integrity.
- HTTPS is required for sensitive sites (banking, email, e-commerce).

## Structure of HTTP Request/Response
**Request Example:**
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html


**Response Example:**
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1256

<html> ... </html>