from prefect import flow, task
import os
from gradio_client import Client

PROMPT_FILE = "prompt.txt"
RESPONSE_FILE = "response.txt"

@task
def test_llm():
    """Uses the Gradio client to generate a response based on user input."""
    # Initialize the Gradio client
    client = Client("buddiezweb/Medical")

    # Read user input from prompt.txt
    if os.path.exists(PROMPT_FILE):
        with open(PROMPT_FILE, "r") as file:
            prompt = file.read().strip()
    else:
        return "❌ No prompt file found!"

    print(f"📄 Read prompt: {prompt}")  # Debugging output

    if not prompt:
        return "❌ Prompt file is empty!"

    # Call the Gradio API
    try:
        result = client.predict(
            message=prompt,
            system_message="You are advising medical information, give detailed cures and suggestions, if serious suggest to go to doctor.",
            max_tokens=512,
            temperature=0.7,
            top_p=0.95,
            api_name="/chat"
        )
        response = result  # Assuming the result is the response text
    except Exception as e:
        response = f"❌ Error during API call: {str(e)}"

    # Save output
    with open(RESPONSE_FILE, "w") as file:
        file.write(response)

    print(f"📝 Model Response: {response}")  # Debugging output

@flow(name="MedVigil Processing Flow")
def main_flow():
    """Main Prefect flow: process user input with MedVigil."""
    test_llm()

if __name__ == "__main__":
    main_flow()