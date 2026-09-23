import os
import re
import shutil
from urllib.parse import unquote

posts_dir = r"C:\Users\Lenovo\Documents\blog_hugo\content\posts\posts"
attachments_dir = r"C:\Users\Lenovo\Documents\Life"   # <-- widened
static_images_dir = r"C:\Users\Lenovo\Documents\blog_hugo\static\images"

LINK_PATTERN = re.compile(r'/images/([^)]+\.(?:png|jpg|jpeg))', re.IGNORECASE)


def find_image(filename, search_dir):
    for root, dirs, files in os.walk(search_dir):
        if filename in files:
            return os.path.join(root, filename)
    return None


for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)

        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()

        fixed_content = content.replace("![Image Description]", "!![Image Description]")
        if fixed_content != content:
            print(f"Fixed double '!!' in: {filename}")
            content = fixed_content

        links = LINK_PATTERN.findall(content)
        for encoded_name in links:
            real_name = unquote(encoded_name)

            image_source = find_image(real_name, attachments_dir)
            if image_source:
                shutil.copy(image_source, static_images_dir)
                print(f"✓ Copied: {real_name}")
            else:
                print(f"✗ NOT FOUND: {real_name}")

        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

print("Done — markdown fixed and images copied.")