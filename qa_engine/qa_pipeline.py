import yaml
import json

def load_prompt_template(path="qa_engine/prompt_templates.yaml"):
    with open(path, "r") as f:
        data = yaml.safe_load(f)
    return data["prompts"]["default_qa"]

def fill_prompt(question, context):
    template = load_prompt_template()
    return template.format(question=question, context=context)

# Example
if __name__ == "__main__":
    sample_question = "What is the date of the last assessment?"
    sample_context = "The patient underwent an assessment on March 12, 2024. It was the final evaluation."
    prompt = fill_prompt(sample_question, sample_context)
    print("🧠 Prompt to be sent to LLM:")
    print(prompt)
