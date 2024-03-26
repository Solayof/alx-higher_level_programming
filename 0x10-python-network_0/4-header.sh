#!/bin/bash
# sends a GET request and sets a header to the URL
curl -sH "X-School-User-Id: 98" "${1}"
