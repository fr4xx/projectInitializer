# projectInitializer

This project initializer script sets up a basic web project structure with essential files and configurations. It includes:
- An organized folder structure
- A `package.json` file with development dependencies (`sass` and `live-server`)
- A simple `index.html` template
- A `.gitignore` to ignore `node_modules`

## Features

- Automatically creates the following directory structure:

`
new-project/ \
├── docs/ \
│ └── ideas.md \
├── src/ \
│ ├── js/ \
│ │ └── main.js \
│ ├── scss/ \
│ │ └── style.scss \
│ ├── media/ \
│ │ ├── img/ \
│ │ └── vid/ \
│ └── css/ \
│ └── style.css \
├── index.html \
├── .gitignore \
├── package.json \
└── README.md \
`

- Generates a `package.json` file with the following:
- Project dependencies: `sass` and `live-server` (dev dependencies)
- Custom development script (`npm run dev`) for live server and Sass watching

- Creates an `index.html` file with:
- A dynamic title based on the parent folder name
- Links to the generated CSS file and JavaScript
- A basic structure to start building your project

## Requirements

- [Python](https://www.python.org/) 3.x or above (for running the script)
- [Node.js](https://nodejs.org/) and [npm](https://www.npmjs.com/) installed (for running `npm install`)

## How to Use

### Step 1: Run the Script

1. Navigate to the directory where you want the project structure to be created.
2. Download or copy the `projectInitializer.py` script into the desired directory.
3. Run the script from your terminal/command prompt:

 ```bash
 python projectInitializer.py
