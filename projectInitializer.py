import os
import subprocess
import json

# define the project structure
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
    ".gitignore": "node_modules\n",  # add "node_modules" to .gitignore
    "README.md": ""
}

def create_structure(base_path, structure):
    for name, value in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(value, dict):
            # create directory and recursively create the structure
            os.makedirs(path, exist_ok=True)
            create_structure(path, value)
        else:
            # create file and write content
            with open(path, "w") as file:
                file.write(value)

# get name of parent folder
parent_folder_name = os.path.basename(os.getcwd())

# define content for index.html
index_html_content = f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{parent_folder_name}</title>
    <link rel="stylesheet" href="src/css/style.css">
    <link rel="icon" href="src/media/img/icon.ico" type="image/x-icon">
    <script src="src/js/index.js"></script>
  </head>
  <body>
    <main>
        <h1>Welcome to My Website</h1>  
    </main>
  </body>
</html>
"""

# ddefine content for package.json
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

# make sure the script is running in the project folder
current_directory = os.getcwd()

# create project structure in current directory
create_structure(current_directory, project_structure)

# write index.html file with defined content
index_html_path = os.path.join(current_directory, "index.html")
with open(index_html_path, "w") as index_file:
    index_file.write(index_html_content)

# write package.json file with defined content
package_json_path = os.path.join(current_directory, "package.json")
with open(package_json_path, "w") as package_file:
    json.dump(package_json_content, package_file, indent=4)

# run "npm install" to install devDependencies
subprocess.run(["npm", "install"], check=True)

print("Project structure created, index.html and package.json written, and devDependencies (SASS & Live-Server) installed successfully.")
