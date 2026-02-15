import json

class SenseUpAI:
    def __init__(self):
        self.config = {
            "ui_level": 1,
            "theme": "default",
            "buttons_count": 1,
            "focus_interest": None,
            "sensory_filter": "off"
        }

    def analyze_parent_input(self, text):
        text = text.lower()
        
        interests = ["car", "train", "animal", "water", "blue", "red"]
        for interest in interests:
            if interest in text:
                self.config["focus_interest"] = interest
        
        sensory_keywords = ["sensitive", "bright", "light", "noise", "overload"]
        if any(word in text for word in sensory_keywords):
            self.config["theme"] = "pastel_soft_blue"
            self.config["sensory_filter"] = "high"
        
        if "non-verbal" in text or "beginner" in text:
            self.config["ui_level"] = 1
            self.config["buttons_count"] = 1
        elif "some words" in text or "intermediate" in text:
            self.config["ui_level"] = 2
            self.config["buttons_count"] = 3

    def get_json_config(self):
        return json.dumps(self.config, indent=4)

if __name__ == "__main__":
    tutor = SenseUpAI()
    parent_feedback = "My child is non-verbal and very sensitive to bright light. He loves blue cars."
    
    tutor.analyze_parent_input(parent_feedback)
    config_output = tutor.get_json_config()
    
    print(config_output)

    with open('ui_config.json', 'w') as f:
        f.write(config_output)
