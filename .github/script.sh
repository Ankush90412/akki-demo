#!/bin/bash

# GitHub API endpoint for comparing branches
API_URL="https://api.github.com/repos/Ankush90412/akki-demo/compare"

# GitHub personal access token with appropriate permissions
TOKEN="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"

# Source and target branches
SOURCE_BRANCH="dev"
TARGET_BRANCH="stage"

# Function to check if there are differences between branches
check_branch_difference() {
    local response
    response=$(curl -s -H "Authorization: token $TOKEN" "$API_URL/$SOURCE_BRANCH...$TARGET_BRANCH")
    # Check if there are any differences between branches
    if [[ $(echo "$response" | jq '.status') == "\"identical\"" ]]; then
        echo "No differences found between $SOURCE_BRANCH and $TARGET_BRANCH."
    else
        echo "Differences found between $SOURCE_BRANCH and $TARGET_BRANCH:"
        # Print the differences
        echo "$response" | jq '.files'
        # Exit with non-zero status to indicate differences found
        exit 1
    fi
}

# Main function
main() {
    echo "Checking for differences between $SOURCE_BRANCH and $TARGET_BRANCH..."
    check_branch_difference
}

main
