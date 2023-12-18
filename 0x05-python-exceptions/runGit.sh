#!/bin/bash

# Prompt for a commit message
read -p "Enter your commit message: " commit_message

# Add all changes and commit
git add .
git commit -m "$commit_message"

# Push to the origin
git push origin master

# Print a success message
echo "Changes pushed to Git successfully!"

