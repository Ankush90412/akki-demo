#!/bin/bash

# Define the source and target branches
SOURCE_BRANCH="stage"
TARGET_BRANCH="dev"

# Fetch the latest changes from remote
git fetch origin $TARGET_BRANCH:$TARGET_BRANCH

# Compare the changes between the source and target branches
git diff --name-status $TARGET_BRANCH..$SOURCE_BRANCH

# Optionally, you can also show the diff content using:
# git diff $TARGET_BRANCH..$SOURCE_BRANCH