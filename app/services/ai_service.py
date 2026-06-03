from groq import Groq
from app.core.config import settings

client = Groq(
    api_key=settings.GROQ_API_KEY
)

def generate_meal_suggestion(profile, meals):

    if profile is None:
        return "Please create profile first."

    # Prompt ko "Persona" aur "Structure" ke saath improve kiya hai
    prompt = f"""
    Role: You are a professional Nutritionist and Fitness Coach.
    Goal: Provide a high-impact, data-driven meal plan based on the user's profile and history.

    User Profile:
    - {profile.age} years old, {profile.gender}
    - {profile.height}cm, {profile.weight}kg (Target: {profile.target_weight}kg)
    - Body Type: {profile.body_type}
    - Fitness Goal: {profile.fitness_goal}
    - Activity Level: {profile.activity_level}
    - Diet Preference: {profile.diet_preference}

    User's Recent Meal History:
    {meals}

    Task:
    1. Critique: Analyze the nutritional gaps in the current meal history.
    2. Meal Suggestions: Suggest 5 specific high-performance meals optimized for the user's goal.
    3. Numerical Targets: Provide a daily caloric intake and protein goal (in grams).
    4. Actionable Habits: Give 5 simple daily habits to improve results.
    5. Scientific Reasoning: Explain briefly why these changes will work.

    Constraints:
    - Be direct, professional, and encouraging.
    - Keep response under 5500 characters.
    - Use clear headings.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a world-class nutritionist assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content