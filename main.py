import base64

import requests

token = ""
avatar_path = "./Animated-Avatar.gif"

try:
    with open(avatar_path, "rb") as file:
        new_avatar = base64.b64encode(file.read()).decode("utf-8")

    headers = {"Authorization": f"Bot {token}", "Content-Type": "application/json"}

    json = {"avatar": f"data:image/gif;base64,{new_avatar}"}

    response = requests.patch(
        "https://discord.com/api/v10/users/@me", headers=headers, json=json
    )

    if response.ok:
        print("Avatar Updated!")
    else:
        print("Failed to Update Avatar:", response.status_code)
        print("Response body:", response.text)

except Exception as error:
    print("There is an Error here:", error)
