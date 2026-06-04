# GitHub Secrets Demonstration

A bare minimum project illustrating how to store and access secret tokens in GitHub Actions.

This project uses a GitHub Actions workflow to securely inject a secret token (`MY_SECRET_TOKEN`) into a Python script as an environment variable.

---

## How to Set Up and Run the Demo

### Step 1: Add the Secret to GitHub
1. On GitHub, navigate to the main page of your repository.
2. Under your repository name, click on **Settings** (the gear icon).
3. In the left sidebar, click on **Secrets and variables** -> **Actions**.
4. Click the **New repository secret** button.
5. Configure the secret:
   - **Name**: `MY_SECRET_TOKEN`
   - **Secret**: *Enter any secret text here (e.g., `SuperSecret12345`)*
6. Click **Add secret**.

### Step 2: Trigger the Workflow
You can trigger the workflow in one of two ways:

#### Option A: Manual Trigger (Recommended)
1. Navigate to the **Actions** tab of your repository.
2. In the left sidebar, click on **GitHub Secrets Demonstration**.
3. Click the **Run workflow** dropdown on the right side.
4. Select the branch (e.g., `main`) and click the green **Run workflow** button.
5. Refresh the page after a few seconds, click on the running/completed run, and select the **run-demo** job to inspect the logs.

#### Option B: Push Trigger
- Simply make a commit and push to the `main` branch. This will automatically trigger the workflow.

---

## Project Structure
- [`.github/workflows/demo.yml`](file:///.github/workflows/demo.yml) - The GitHub Actions workflow definition. It maps the GitHub secret to an environment variable `MY_SECRET_TOKEN`.
- [`secrets_demo.py`](file:///secrets_demo.py) - A Python script that retrieves `MY_SECRET_TOKEN` from environment variables, verifies its presence, prints its length, and attempts to print it directly to show how GitHub automatically masks secrets in logs.
