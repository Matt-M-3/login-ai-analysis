import requests

OLLAMA_MODEL = "gemma3:27b"
LOG_FILE = "fake_auth_log.log"
OLLAMA_API_URL = "http://localhost:11434/api/generate"

def read_log_file(filepath):
    with open(filepath, "r") as f:
        return f.read()

def query_ollama(prompt, model=OLLAMA_MODEL):
    response = requests.post(OLLAMA_API_URL, json={
        "model": model,
        "prompt": prompt,
        "stream": False
    })
    if response.status_code == 200:
        return response.json()["response"]
    else:
        print("Error from Ollama:", response.text)
        return None

def main():
    log_data = read_log_file(LOG_FILE)

    prompt = f"""
You are a security analyst. The following is a Linux authentication log. Please identify any unusual or potentially suspicious login activity, such as failed privileged logins, logins from unusual IPs, or anomalous usage patterns.

Log:
{log_data}

Respond with a list of suspicious entries and a short explanation for each.
"""

    analysis = query_ollama(prompt)
    print("\n--- Analysis ---\n")
    print(analysis)

if __name__ == "__main__":
    main()
