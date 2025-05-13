# Ollama + Python Log Analysis
This readme will contain information for the purpose of analyzing login type data utilizing a Python script. 

## Dependencies
1. Ollama: somewhat obviously, you must have Ollama installed and running. 
2. LLM: again, somewhat obviously, you must have an available LLM. You can pull a new model with something like `ollama pull gemma3:27b`. Make sure you select a model that is appropriate for your hardware. 
3. Python: we'll be using a Python script, so having it installed is kind of a must.

## Setup
Depending on your current setup, a few changes might be needed to be made to the Python script itself. Open it with any editor, such as vim, nano, of VS Code, and take a look at the following lines:

- OLLAMA_MODEL: make sure the model you want to use is listed here. You can obtain a list of your current installed models using `ollama list`. 
- LOG_FILE: this is the location of the log file you wish to analyze.
- OLLAMA_API_URL: this is the default location OLLAMA's API will be listening. In most cases, this probably won't need to be altered.
- Prompt: if, for any reason, there is a desire to alter the prompt being sent to the LLM, take a look at lines 27 and 32. Alter these as needed. 

## Running the Script
Evaluating the logs is as easy as executing the following:
```bash
python3 analyze_log_with_ollama.py
```
Depending on your hardware, this may take a few moments. Eventually, you might see something like the following:
```txt
--- Analysis ---

Here's a list of suspicious entries from the provided logs, along with explanations:

*   **Multiple Failed Login Attempts for Root:** Several "Failed password for root" entries (like `11:16:00`, `11:21:00`) are highly suspicious. Root is the administrator account, and repeated failed attempts suggest a brute-force attack or someone trying to gain unauthorized access.
*   **Failed Logins for Various Users:** Numerous failed login attempts for users like `diana`, `sysadmin`, `bob`, `eve`, `backupuser` indicate potential probing or attacks targeting specific accounts.
*   **Mix of Successful and Failed Logins from the Same IPs:** Some IPs (particularly those in the `203.0.113.x` range) show both successful *and* failed login attempts for *different* users. This could indicate an attacker who successfully compromised one account and is now trying to leverage that access to guess other credentials or attempt privilege escalation.
*   **Internal and External IPs:** The logs show login attempts from both internal IPs (e.g., `10.0.0.x`, `192.168.1.x`) and external IPs (`203.0.113.x`). While internal access is normal, the sheer volume of attempts from external sources is concerning.
* **Successful logins after failed attempts:** The combination of failed attempts immediately followed by successful logins to the same IP address or user is highly suspicious. This could indicate a successful brute-force attack or credential stuffing.



**Overall:** The logs suggest an ongoing attempt to compromise the system, potentially through brute-force attacks, credential stuffing, or exploiting known vulnerabilities. The combination of failed and successful logins from the same sources makes this particularly concerning. It's important to investigate these entries further, review security configurations, and consider implementing stronger authentication measures.
```