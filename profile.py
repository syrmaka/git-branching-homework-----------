def get_profile():
    return {
        "name": "Perfileva Arina",
        "group": "РПО-1",
        "role": "student",
        "skills": ["Git", "VS Code", "Python"]
    }


def print_profile():
    profile = get_profile()
    print(f"Student: {profile['name']}")
    print(f"Group: {profile['group']}")
    print("Skills:", ", ".join(profile["skills"]))
