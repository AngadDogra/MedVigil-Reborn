from gradio_client import Client

client = Client("buddiezweb/Medical")
result = client.predict(
		message="The patient has cancer symptpms",
		system_message="You are advising medical information, give cures and suggestions, if serious suggest to go to doctor",
		max_tokens=512,
		temperature=0.7,
		top_p=0.95,
		api_name="/chat"
)
print(result)