#!/bin/bash
# Git Bisect Automation Script
# Automates finding the commit that introduced a bug

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}=== Git Bisect Automation ===${NC}"

# Check if we're in a git repo
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo -e "${RED}Error: Not in a git repository${NC}"
    exit 1
fi

# Get current branch
BRANCH=$(git branch --show-current)
echo -e "Current branch: ${GREEN}$BRANCH${NC}"

# Check for uncommitted changes
if [ -n "$(git status --porcelain)" ]; then
    echo -e "${YELLOW}Warning: You have uncommitted changes${NC}"
    echo "Stashing changes..."
    git stash
    STASHED=1
fi

# Get good commit (known working)
echo -e "\n${YELLOW}Step 1: Find a known good commit${NC}"
echo "Enter a commit hash or tag that's known to work:"
read GOOD_COMMIT

# Verify good commit exists
if ! git rev-parse --verify "$GOOD_COMMIT" > /dev/null 2>&1; then
    echo -e "${RED}Error: Invalid commit: $GOOD_COMMIT${NC}"
    exit 1
fi

echo -e "Good commit: ${GREEN}$GOOD_COMMIT${NC}"

# Get bad commit (known broken)
echo -e "\n${YELLOW}Step 2: Find a known bad commit${NC}"
echo "Enter a commit hash that's known to be broken (default: HEAD):"
read BAD_COMMIT

if [ -z "$BAD_COMMIT" ]; then
    BAD_COMMIT="HEAD"
fi

# Verify bad commit exists
if ! git rev-parse --verify "$BAD_COMMIT" > /dev/null 2>&1; then
    echo -e "${RED}Error: Invalid commit: $BAD_COMMIT${NC}"
    exit 1
fi

echo -e "Bad commit: ${GREEN}$BAD_COMMIT${NC}"

# Ask for test command
echo -e "\n${YELLOW}Step 3: Enter test command${NC}"
echo "What command tests for the bug? (e.g., npm test, pytest, etc.):"
read TEST_CMD

# Start bisect
echo -e "\n${YELLOW}Starting bisect...${NC}"
echo "Good: $GOOD_COMMIT"
echo "Bad: $BAD_COMMIT"
echo "Test: $TEST_CMD"

git bisect start
git bisect bad "$BAD_COMMIT"
git bisect good "$GOOD_COMMIT"

# Run bisect
echo -e "\n${YELLOW}Running bisect...${NC}"
if git bisect run bash -c "$TEST_CMD"; then
    echo -e "\n${GREEN}=== Bisect Complete ===${NC}"
    RESULT=$(git bisect log | tail -3 | head -1)
    echo "First bad commit: $RESULT"
else
    echo -e "\n${RED}Bisect failed - test command may have non-zero exit${NC}"
fi

# Cleanup
git bisect reset

# Restore stashed changes if any
if [ "$STASHED" = 1 ]; then
    echo -e "\n${YELLOW}Restoring stashed changes...${NC}"
    git stash pop
fi

echo -e "\n${GREEN}Done!${NC}"
