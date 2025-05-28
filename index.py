class CryptoBuddy:
    def __init__(self):
        self.rules = {
            "Bitcoin": {  
                "price_trend": "rising",  
                "market_cap": "high",  
                "energy_use": "high",  
                "sustainability_score": 3/10  
            },  
            "Ethereum": {  
                "price_trend": "stable",  
                "market_cap": "high",  
                "energy_use": "medium",  
                "sustainability_score": 6/10  
            },  
            "Cardano": {  
                "price_trend": "rising",  
                "market_cap": "medium",  
                "energy_use": "low",  
                "sustainability_score": 8/10  
            }  
        }
        self.name = "CryptoBuddy"
        self.disclaimer = "\n🤖 Crypto is risky—always do your own research!"

    def respond(self, user_query):
        user_query = user_query.lower().strip()
        response = "I’m not sure about that. Can you ask something else? 🤔"

        if "sustainable" in user_query or "eco" in user_query:
            recommend = max(self.rules, key=lambda x: self.rules[x]["sustainability_score"])
            response = f"Invest in {recommend}! 🌱 It’s eco-friendly and has long-term potential!"
        elif "trending" in user_query or "trend" in user_query or "growth" in user_query:
            # Profitability: rising trend and high market cap
            candidates = [k for k, v in self.rules.items() if v["price_trend"] == "rising" and v["market_cap"] == "high"]
            if candidates:
                recommend = candidates[0]
                response = f"{recommend} is trending up with a strong market cap! 🚀"
            else:
                recommend = max(self.rules, key=lambda x: self.rules[x]["price_trend"] == "rising")
                response = f"Check out {recommend}! 📈 It’s trending upwards!"
        elif "energy" in user_query:
            recommend = min(self.rules, key=lambda x: self.rules[x]["energy_use"])
            response = f"Consider {recommend}! ⚡ It’s energy-efficient!"
        elif "market cap" in user_query:
            recommend = max(self.rules, key=lambda x: self.rules[x]["market_cap"] == "high")
            response = f"Look into {recommend}! 💰 It has a strong market presence!"

        return f"{response}{self.disclaimer}"

# Example usage
if __name__ == "__main__":
    chatbot = CryptoBuddy()
    print("Hey there! I’m CryptoBuddy. Ask me about crypto trends, sustainability, or market advice! (Type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("CryptoBuddy: Goodbye! 👋")
            break
        response = chatbot.respond(user_input)
        print(f"CryptoBuddy: {response}")