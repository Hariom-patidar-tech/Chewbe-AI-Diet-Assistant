from groq import Groq
from app.core.config import settings

client = Groq(
    api_key=settings.GROQ_API_KEY
)

def generate_meal_suggestion(profile, meals):

    if profile is None:
        return "Please create profile first."

    # Prompt mein ye instruction add kar di hai
    prompt = f"""
    User Details:
    Age: {profile.age}
    Gender: {profile.gender}
    Height: {profile.height}
    Weight: {profile.weight}
    Target Weight: {profile.target_weight}
    Body Type: {profile.body_type}
    Diet Preference: {profile.diet_preference}
    Fitness Goal: {profile.fitness_goal}
    Activity Level: {profile.activity_level}

    Existing Meals:
    {meals}

    Suggest:
    1. Better meals
    2. Diet improvements
    3. Calories recommendation
    4. Protein recommendation

    Explain why.

    The total length of your response MUST NOT exceed 2500 characters.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content