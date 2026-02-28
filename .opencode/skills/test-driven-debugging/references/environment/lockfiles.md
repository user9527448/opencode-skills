# Environment-Specific Deterministic Setup

Guide for freezing environments across different programming languages and package managers.

---

## Why Lockfiles Matter

Deterministic debugging requires:
- Same dependencies locally and in CI
- Consistent behavior across machines
- Reproducible failures

Different languages have different tools - choose your environment:

| Language | Package Manager | Lockfile | Command |
|----------|----------------|----------|---------|
| **JavaScript/Node.js** | npm | `package-lock.json` | `--frozen-lockfile` |
| **JavaScript/Node.js** | yarn | `yarn.lock` | `--frozen-lockfile` |
| **JavaScript/Node.js** | pnpm | `pnpm-lock.yaml` | `--frozen-lockfile` |
| **Python** | pip + pip-tools | `requirements.txt` + hash | `--require-hashes` |
| **Python** | pipenv | `Pipfile.lock` | `--deploy` |
| **Python** | poetry | `poetry.lock` | `--no-update` |
| **Java** | Maven | `pom.xml` + `.m2` | `-o` (offline) |
| **Java** | Gradle | `gradle.lockfile` | `--offline` |
| **Go** | go mod | `go.sum` | `-mod=readonly` |
| **Rust** | Cargo | `Cargo.lock` | `--locked` |
| **Ruby** | Bundler | `Gemfile.lock` | `--deployment` |
| **PHP** | Composer | `composer.lock` | `--no-dev` |
| **.NET** | NuGet | `packages.lock.json` | `--locked` |
| **Docker** | - | Dockerfile + build args | BuildKit |

---

## JavaScript / Node.js

### npm

```bash
# Install exact versions from lockfile
npm ci --ignore-scripts

# Or with frozen lockfile (fails if lockfile outdated)
npm install --frozen-lockfile

# Verify installed versions match lockfile
npm ls

# Save exact version
npm install --save-exact

# Capture environment
node --version > env.txt
npm --version >> env.txt
npm ls --depth=0 >> env.txt
```

### yarn

```bash
# Install from lockfile (fails if outdated)
yarn install --frozen-lockfile

# Or with strict mode
yarn install --immutable

# Verify
yarn install --check-files
```

### pnpm

```bash
# Frozen install
pnpm install --frozen-lockfile

# Strict install
pnpm install --strict-lockfile
```

---

## Python

### pip + pip-tools

```bash
# Generate locked requirements
pip-compile requirements.in --output-file requirements.txt

# Verify hashes (prevents tampering)
pip install --require-hashes -r requirements.txt

# Capture environment
python3 --version > env.txt
pip freeze >> env.txt
```

### pipenv

```bash
# Install from Pipfile.lock
pipenv install --deploy

# Verify lockfile is up to date
pipenv lock --check

# Capture environment
pipenv --venv > env.txt
pipenv graph >> env.txt
```

### poetry

```bash
# Install without updating lockfile
poetry install --no-root
poetry lock --no-update  # Create/update lockfile

# Verify
poetry check

# Export for other tools
poetry export -f requirements.txt --output requirements.txt

# Capture environment
poetry show --tree >> env.txt
```

---

## Java

### Maven

```bash
# Offline mode (use cached dependencies)
mvn install -o

# Use specific settings
mvn install -s settings.xml

# Verify dependencies
mvn dependency:tree

# Capture environment
mvn --version > env.txt
mvn dependency:tree >> env.txt
```

### Gradle

```bash
# Offline mode
./gradlew build --offline

# Use lockfile
./gradlew dependencies --configuration compileClasspath

# Capture environment
./gradlew --version > env.txt
./gradlew dependencies >> env.txt
```

---

## Go

```bash
# Ensure reproducible builds
go mod download
go build -mod=readonly

# Verify modules
go mod verify

# Capture environment
go version > env.txt
go list -m all >> env.txt
```

---

## Rust

```bash
# Install exact versions from lockfile
cargo build --locked

# Verify lockfile
cargo check --locked

# Capture environment
rustc --version > env.txt
cargo tree >> env.txt
```

---

## Ruby

### Bundler

```bash
# Frozen install
bundle install --deployment

# Or with frozen lockfile
bundle install --frozen

# Verify
bundle check

# Capture environment
ruby --version > env.txt
bundle exec gem list >> env.txt
```

---

## PHP

### Composer

```bash
# Install from lockfile (no dev if not needed)
composer install --no-dev
composer validate --strict

# Capture environment
php --version > env.txt
composer show --tree >> env.txt
```

---

## .NET

### NuGet

```bash
# Restore with lock
dotnet restore --locked

# Verify
dotnet restore --verbosity minimal

# Capture environment
dotnet --version > env.txt
dotnet list package >> env.txt
```

---

## Docker

### Dockerfile Best Practices

```dockerfile
# Use specific versions
FROM node:18.17.0-alpine3.18

# Pin dependency versions
RUN npm ci --ignore-scripts

# Use build arguments for reproducibility
ARG VERSION=1.2.3
ENV APP_VERSION=${VERSION}

# Copy lockfile first (layer caching)
COPY package-lock.json ./
RUN npm ci

# Then copy source
COPY . .
```

### BuildKit for reproducibility

```bash
# Enable BuildKit
DOCKER_BUILDKIT=1 docker build .

# Use cache mounts for package managers
docker build --build-arg BUILDKIT_INLINE_CACHE=1 .
```

---

## Capturing Full Environment

For complex debugging, capture everything:

```bash
# Create debug package
mkdir debug-env && cd debug-env

# System info
uname -a > system.txt
cat /etc/os-release >> system.txt

# Language versions
node --version  # or python --version, etc.
npm --version

# Dependencies
npm ls --depth=0 > deps.txt

# Environment variables (sanitized)
env | grep -v 'PASSWORD\|TOKEN\|SECRET' > env.txt

# Git info
git log -3 --oneline > git.txt
git diff >> git.txt

# Test configuration
cat package.json | grep -A5 '"scripts"' > test-config.txt

cd ..
tar -czvf debug-env.tar.gz debug-env/
```

---

## CI Environment Matching

To match CI environment locally:

### GitHub Actions

```yaml
# In your workflow file
jobs:
  build:
    runs-on: ubuntu-latest  # Use same OS
    steps:
      - uses: actions/checkout@v4
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '18'  # Match CI
          cache: 'npm'
      - run: npm ci  # Uses lockfile
```

### GitLab CI

```yaml
# .gitlab-ci.yml
image: node:18.17.0

cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - node_modules/

test:
  script:
    - npm ci
    - npm test
```

---

## Quick Reference by Language

| Language | Freeze Command | Verify Command |
|----------|---------------|----------------|
| Node.js (npm) | `npm ci` | `npm ls` |
| Node.js (yarn) | `yarn install --frozen-lockfile` | `yarn check` |
| Python (pip) | `pip install --require-hashes -r requirements.txt` | `pip hash` |
| Python (poetry) | `poetry install --no-root` | `poetry check` |
| Java (Maven) | `mvn install -o` | `mvn dependency:tree` |
| Go | `go mod download` | `go mod verify` |
| Rust | `cargo build --locked` | `cargo check --locked` |
| Ruby | `bundle install --frozen` | `bundle check` |

---

## Troubleshooting

### "Lockfile not found"

```bash
# Generate lockfile
npm install   # npm
yarn install  # yarn
poetry lock    # poetry
```

### "Lockfile out of date"

```bash
# Update lockfile (cautiously)
npm install   # npm will update package-lock.json
yarn install  # yarn will update yarn.lock
poetry lock    # poetry will update poetry.lock
```

### "Works locally but fails in CI"

1. Check Node/version: `node --version` (local vs CI)
2. Check npm version: `npm --version`
3. Clear cache: `npm cache clean --force`
4. Delete node_modules and reinstall: `rm -rf node_modules && npm ci`
