prompts = {
    "zero_shot": """
Write a simple and attractive product description for this product:

Product: {product}
""",

    "few_shot": """
Product: Coffee
Tagline: "Wake up to greatness"

Product: Shoes
Tagline: "Walk your path"

Product: {product}
Tagline:
""",

    "chain_of_thought": """
Product: {product}

Who will use this product?
What problem does it solve?
Create a catchy tagline for it.
"""
}

for name, prompt in prompts.items():
    print(f"\n{name.upper()}\n")
    print(prompt.format(product="AI Laptop"))