class SleepChatBot:
    def __init__(self):
        self.data = {}

    def greet(self):
        print("😴 SleepBot: Hi! I'm your AI Sleep Advisor.")
        print("😴 SleepBot: I'll ask you a few questions to understand your sleep routine.\n")

    def ask_sleep_hours(self):
        self.data["sleep_hours"] = float(
            input("SleepBot: How many hours do you sleep daily? \nYou: ")
        )

    def ask_bedtime(self):
        self.data["bedtime"] = int(
            input("SleepBot: What time do you usually go to bed? (24-hour format) \nYou: ")
        )

    def ask_screen_time(self):
        self.data["screen_time"] = float(
            input("SleepBot: How many hours do you use screens before sleeping? \nYou: ")
        )

    def ask_caffeine(self):
        self.data["caffeine"] = int(
            input("SleepBot: How many cups of caffeine do you consume per day? \nYou: ")
        )

    def ask_stress(self):
        self.data["stress"] = int(
            input("SleepBot: On a scale of 1–10, how stressed do you feel daily? \nYou: ")
        )

    def analyze(self):
        print("\n🤖 SleepBot: Analyzing your sleep pattern...\n")

        issues = []
        advice = []

        if self.data["sleep_hours"] < 7:
            issues.append("You are not getting enough sleep.")
            advice.append("Try to sleep at least 7–8 hours every night.")

        if self.data["bedtime"] > 23:
            issues.append("You are sleeping very late.")
            advice.append("Sleeping before 11 PM improves sleep quality.")

        if self.data["screen_time"] > 1:
            issues.append("Too much screen time before bed.")
            advice.append("Avoid screens at least 1 hour before sleeping.")

        if self.data["caffeine"] > 2:
            issues.append("High caffeine intake.")
            advice.append("Reduce caffeine, especially after evening.")

        if self.data["stress"] > 6:
            issues.append("High stress levels.")
            advice.append("Try meditation, deep breathing, or light stretching.")

        if issues:
            print("❌ SleepBot: I found some issues:")
            for i in issues:
                print(" -", i)

            print("\n✅ SleepBot: My recommendations:")
            for a in advice:
                print(" -", a)
        else:
            print("🎉 SleepBot: Your sleep routine looks healthy!")

    def goodbye(self):
        print("\n😴 SleepBot: Thanks for chatting with me.")
        print("😴 SleepBot: Wishing you a peaceful and healthy sleep!")

    def run(self):
        self.greet()
        self.ask_sleep_hours()
        self.ask_bedtime()
        self.ask_screen_time()
        self.ask_caffeine()
        self.ask_stress()
        self.analyze()
        self.goodbye()


# -------- RUN CHATBOT -------- #

bot = SleepChatBot()
bot.run()
