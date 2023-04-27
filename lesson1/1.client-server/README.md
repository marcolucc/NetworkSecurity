# Client server communication

## Setting overview
We have two docker containers: the server A and the client B.
B is sending packets to A, using the command `curl --data "$PAYLOAD" $SERVER_HOST:$SERVER_PORT`.


## Curl command
The `curl` command is a popular tool used for transferring data from or to a server, using a variety of protocols such as HTTP, HTTPS, FTP, and more.

In this case, the `curl` command is used to send an HTTP POST request to the server with the `--data` option, which specifies the data to send in the request. The data is set to the value of the `PAYLOAD` variable, which is a simple string "Hello, world!" in this example.

When the script runs, it continuously sends HTTP POST requests to the specified server address with the specified payload data. The server can then capture and process these requests as necessary. 

### Structure of the packet sent
The `curl` command is sending an HTTP POST request with the specified payload data. 
The structure of an HTTP POST request is as follows:

```
POST /path/to/resource HTTP/1.1
Host: example.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 13

Hello, world!
```

Let's break down each part of the request:

- `POST`: This is the HTTP method being used, which indicates that the request is sending data to the server.
- `/path/to/resource`: This is the path to the resource on the server that the request is being sent to.
- `HTTP/1.1`: This is the version of the HTTP protocol being used.
- `Host: example.com`: This is the hostname of the server that the request is being sent to.
- `Content-Type: application/x-www-form-urlencoded`: This is the type of data being sent in the request body. In this case, it's `application/x-www-form-urlencoded`, which is a standard way of encoding form data in an HTTP request.
- `Content-Length: 13`: This is the length of the request body in bytes. In this case, it's 13 bytes, which is the length of the "Hello, world!" string.
- `Hello, world!`: This is the actual data being sent in the request body. It's the value of the `PAYLOAD` variable in the `send_packets.sh` script.

