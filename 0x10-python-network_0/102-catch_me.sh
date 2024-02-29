#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me server that makes it respond "You got me!"
curl -sL -X PUT 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool" -d "user_id=98"
