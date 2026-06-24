import requests

# 1. Your n8n Local Webhook URL
# (If running on default local port 5678, with the path from your JSON)
webhook_url = "http://localhost:5678/webhook-test/ff1a6e60-8f40-4095-ba49-f026b073a208"

# 2. The data format expected by your "AI Agent" prompt node: {{ $json.body.data }}
payload = {
    "data": "Schedule a project alignment meeting with Ahmed and Adil tomorrow at 3 PM and remind me via WhatsApp."
}

try:
    print("🚀 Triggering n8n AI Chatbot Pipeline...")
    response = requests.post(webhook_url, json=payload)
    
    # Check if the webhook responded successfully
    if response.status_code == 200:
        print("✅ Workflow executed successfully!")
        print("🤖 Response from n8n:", response.json())
    else:
        print(f"❌ Failed to trigger. Status Code: {response.status_code}")
        print("Response text:", response.text)

except requests.exceptions.ConnectionError:
    print("❌ Connection Refused! Make sure your local n8n container is running on port 5678.")