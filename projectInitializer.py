import os
import subprocess
import json

# Define the project structure
project_structure = {
    "docs": {
        "ideas.md": ""
    },
    "src": {
        "js": {
            "main.js": ""
        },
        "scss": {
            "style.scss": ""
        },
        "media": {
            "img": {},
            "vid": {}
        },
        "css": {
            "style.css": ""
        }
    },
    "index.html": "",
    ".gitignore": "node_modules\n",  # Add "node_modules" to the .gitignore file
    "README.md": ""
}

def create_structure(base_path, structure):
    for name, value in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(value, dict):
            # Create directory and recursively create the structure
            os.makedirs(path, exist_ok=True)
            create_structure(path, value)
        else:
            # Create file and write content (empty or specified content)
            with open(path, "w") as file:
                file.write(value)

# Get the name of the parent folder
parent_folder_name = os.path.basename(os.getcwd())

# Define the content for the package.json file
package_json_content = {
    "name": parent_folder_name,
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "directories": {
        "doc": "docs"
    },
    "scripts": {
        "dev": "sass --watch src/scss/style.scss:src/css/style.css & live-server"
    },
    "keywords": [],
    "author": "fr4xx",
    "license": "ISC",
    "devDependencies": {
        "live-server": "^1.2.2",
        "sass": "^1.83.1"
    }
}

# Make sure the script is running in the project folder
current_directory = os.getcwd()

# Create the project structure in the current directory
create_structure(current_directory, project_structure)

# Write the package.json file with the specified content
package_json_path = os.path.join(current_directory, "package.json")
with open(package_json_path, "w") as package_file:
    json.dump(package_json_content, package_file, indent=4)

# Run npm install to install the devDependencies
subprocess.run(["npm", "install"], check=True)

print("Project structure created, package.json written, and devDependencies installed successfully.")
