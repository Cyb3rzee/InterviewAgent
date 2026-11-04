import json
from pathlib import Path

class ProfileRetriever:
    def __init__(self, profile_path: str = "candidate/profile.json"):
        self.profile_path = Path(profile_path)
        self.profile_data = self._load_profile()

    def _load_profile(self) -> dict:
        if not self.profile_path.exists():
            return {}
        with open(self.profile_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_context(self, question: str) -> str:
        experiences = self.profile_data.get("experiences", [])
        matched = []
        q_lower = question.lower()

        for exp in experiences:
            if (exp.get("category", "").lower() in q_lower or
                exp.get("title", "").lower() in q_lower or
                any(t in q_lower for t in exp.get("technologies", [])) or
                "vulnerability" in q_lower or "security" in q_lower or "api" in q_lower or "testing" in q_lower):
                matched.append(exp)

        if not matched:
            matched = experiences

        formatted_context = "VERIFIED CANDIDATE BACKGROUND:\n"
        for item in matched:
            formatted_context += f"- Title: {item.get('title')}\n"
            formatted_context += f"  Category: {item.get('category')}\n"
            formatted_context += f"  Skills/Tech: {', '.join(item.get('technologies', []))}\n"
            formatted_context += f"  Details: {item.get('verified_details')}\n\n"
        
        return formatted_context
