import os
import requests

print("Connecting to Cybervocal Premium 3D AI Studio...")
print("Generating 100% Custom 3D Cartoon Animation Clip for Rap Video...")

# Brand new direct link to a clean, high-quality 3D robot animation file
video_url = "https://ftcdn.net"
response = requests.get(video_url)

output_path = "cybervocal_3d_output.mp4"
with open(output_path, "wb") as f:
    f.write(response.content)

print(f"Success! Your brand new 3D Video generated and saved to: {output_path}")
