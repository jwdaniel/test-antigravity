import os
from pathlib import Path

PROMPTS_DIR = Path(__file__).parent

def load_prompt(prompt_name: str, **kwargs) -> str:
    """
    Load a prompt from a YAML/text file and format it with kwargs.
    """
    prompt_path = PROMPTS_DIR / f"{prompt_name}.yaml"
    if not prompt_path.exists():
        # Fallback to .txt
        prompt_path = PROMPTS_DIR / f"{prompt_name}.txt"
    
    if not prompt_path.exists():
        raise FileNotFoundError(f"Prompt file not found: {prompt_name}")
    
    with open(prompt_path, "r") as f:
        content = f.read()
        
    return content.format(**kwargs)
