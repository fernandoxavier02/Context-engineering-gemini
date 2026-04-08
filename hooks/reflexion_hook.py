import sys
import json
import re

def main():
    try:
        input_data = sys.stdin.read()
        if not input_data: return
        data = json.loads(input_data)
        prompt = data.get("prompt", "").strip()
        
        # Auto-detect need for reflection based on complexity or length
        if len(prompt) > 200 and not "/reflect" in prompt:
            sys.stdout.write(json.dumps({
                "decision": "allow",
                "systemMessage": "## 🧠 Reflexion Suggested\nEste pedido é complexo. Considere usar o comando `/reflect` para analisar criticamente sua estratégia antes de agir."
            }))
        else:
            sys.stdout.write(json.dumps({"decision": "allow"}))
            
        sys.stdout.flush()
    except Exception:
        sys.stdout.write(json.dumps({"decision": "allow"}))

if __name__ == "__main__":
    main()
