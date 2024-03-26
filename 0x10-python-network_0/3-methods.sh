#!/bin/bash
# displays all HTTP methods the server accepts.
curl -Is "$1" | grep "Allow:" | cut -d " " -f 2-
