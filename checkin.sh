#!/bin/bash

# Add all files to staging
git add .

# Create a new commit with the given message
commit_message="$1"
git commit -m "$commit_message"

# Push changes to origin
git push origin
