import sys
import json
import re

# 🧠 Reflexion Hook: Smart Heuristics
# Avoids noise by only suggesting reflection for truly complex/risky tasks.

COMPLEXITY_KEYWORDS = [
    r"\brefactor", r"\bmigrate", r"\bcomplex", r"\barchitecture", 
    r"\brewrite", r"\bbug", r"\bissue", r"\bfix", r"\berror",
    r"\bdoesn't work", r"\bfail", r"\bsecurity", r"\bperformance",
    r"\boptimization", r"\broot cause", r"\bbreaking change"
]

IMPLEMENTATION_PATTERNS = [
    r"\b(fix|corrig|arrum|consert|resolv)\b",
    r"\b(implement|criar|crie|adicion|add|desenvolv)\b",
    r"\b(alter|modific|mud|atualiz|updat)\b",
    r"\b(refator|refactor|reescrev|rewrite)\b"
]

def is_complex_request(prompt):
    p = prompt.lower()
    # 1. Length check (higher threshold)
    if len(p) < 100: return False
    
    # 2. Keyword detection
    has_keyword = any(re.search(kw, p) for kw in COMPLEXITY_KEYWORDS)
    
    # 3. Implementation intent
    has_intent = any(re.search(pat, p) for pat in IMPLEMENTATION_PATTERNS)
    
    # Trigger if it's both an implementation intent and has complexity keywords
    # or if it's exceptionally long (> 500 chars)
    return (has_intent and has_keyword) or len(p) > 500

def main():
    try:
        input_data = sys.stdin.read()
        if not input_data: return
        data = json.loads(input_data)
        prompt = data.get("prompt", "").strip()
        
        if is_complex_request(prompt) and not "/reflect" in prompt:
            sys.stdout.write(json.dumps({
                "decision": "allow",
                "systemMessage": "## 🧠 Reflexion Suggested\nEsta tarefa parece complexa ou envolve alterações de código críticas. Considere usar o comando `/reflect` para analisar criticamente sua estratégia e identificar possíveis falhas antes de agir."
            }))
        else:
            sys.stdout.write(json.dumps({"decision": "allow"}))
            
        sys.stdout.flush()
    except Exception:
        sys.stdout.write(json.dumps({"decision": "allow"}))

if __name__ == "__main__":
    main()
