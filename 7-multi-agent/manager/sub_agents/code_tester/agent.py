from datetime import datetime
from google.adk.agents import Agent
import subprocess
import tempfile
import os


def run_code_test_tool(input_data: dict) -> dict:
    """
    Installs the given Python package and runs the provided test code.
    Expects input_data with:
    - 'package': name of the package to install (e.g., 'transformers')
    - 'code': a Python code snippet as a string
    """
    package = input_data.get("package")
    code = input_data.get("code")

    print(f"--- Tool: run_code_test_tool called for package: {package} ---")

    if not package or not code:
        return {
            "status": "error",
            "error_message": "Missing 'package' or 'code' in input.",
        }

    try:
        # Install the package
        install_result = subprocess.run(
            ["pip", "install", package],
            capture_output=True,
            text=True,
            timeout=60
        )

        # Save test code to a temporary Python file
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as temp_file:
            temp_file.write(code)
            temp_code_path = temp_file.name

        # Run the test code
        run_result = subprocess.run(
            ["python", temp_code_path],
            capture_output=True,
            text=True,
            timeout=60
        )

        # Clean up the temporary file
        os.remove(temp_code_path)

        return {
            "status": "success" if run_result.returncode == 0 else "failure",
            "package": package,
            "install_output": install_result.stdout,
            "install_error": install_result.stderr,
            "code_output": run_result.stdout,
            "code_error": run_result.stderr,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error during test: {str(e)}"
        }


# Create the code_tester agent
code_tester = Agent(
    name="code_tester",
    model="gemini-2.0-flash",
    description="Installs and tests open-source AI libraries using example code.",
    instruction="""
    You are a code testing agent. Your job is to verify if an AI-related Python package:
    - Can be successfully installed
    - Runs a basic example without errors
    - Produces expected output

    The user will provide the name of a package (e.g., `transformers`) and a small test code snippet.

    Use the run_library_test tool to:
    - Install the package
    - Run the code
    - Return results, including success/failure and output
    """,
    tools=[run_code_test_tool],
)
