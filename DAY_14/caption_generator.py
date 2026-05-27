from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=""
)

def generate_captions(topic, platform, total_captions=3):

    user_prompt = f"""
    Create {total_captions} attractive and human-like captions for {platform}
    based on this topic: {topic}

    Add suitable emojis and trending hashtags.
    Keep the captions natural, engaging, and social-media friendly.
    """

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a creative social media content writer."
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    return response.choices[0].message.content


topic_name = "AI internship progress"
social_platform = "Instagram"

captions = generate_captions(topic_name, social_platform)

print("\nGenerated Captions:\n")
print(captions)