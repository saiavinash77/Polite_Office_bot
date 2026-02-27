# 👔 The Polite Office Bot

## 🚨 The Problem
Workplace conflict is expensive. Employees send angry emails, causing HR issues and slowing down productivity.

## 💡 The Solution
**The Polite Office Bot** is an AI Agent powered by **Elasticsearch** and **Elastic Agent Builder**. It intercepts "raw" thoughts and converts them into "professional corporate speak."

## 🛠️ How it Works
1. **User Input:** The user types a frustrated message (e.g., "I hate this").
2. **Elasticsearch Retrieval:** The Agent searches a custom index (`polite-index`) containing 200+ mappings of angry-to-polite phrases.
3. **AI Synthesis:** The LLM uses the retrieved context to generate a perfectly professional email.

## 💻 Tech Stack
- **Database:** Elasticsearch (Vector/Keyword Search)
- **AI:** Elastic Agent Builder
- **Data:** Custom JSON dataset with 200+ corporate scenarios.

## 🚀 How to Run
This project is hosted on Elastic Cloud.
1. Upload `corporate_data.json` to Elastic.
2. Create an Agent with the instructions in `agent_instructions.txt`.
3. Connect the Agent to the index.
4. Ask it to fix your emails!
