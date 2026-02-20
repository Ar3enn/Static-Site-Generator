# Static Site Generator

A lightweight static site generator written in Python. It converts a directory of Markdown files into a fully rendered HTML site using a shared template, and copies static assets alongside the generated pages.

**Live example:** [https://ar3enn.github.io/Static-Site-Generator/](https://ar3enn.github.io/Static-Site-Generator/)

## How it works

- Recursively walks the `content/` directory and converts every `.md` file to an `.html` file
- Injects the page title and rendered HTML content into `template.html`
- Copies everything in `static/` (CSS, images, etc.) directly into the output directory
- Supports a configurable base path so the site can be hosted at a subdirectory (e.g. on GitHub Pages)

## Usage

### Local development

Run the development server with the default base path (`/`):

```bash
python3 src/main.py
```

Then open your browser to `http://localhost:8888` (or whichever port your local server uses).

### Production build

Run the build script to generate the site with the correct base path for GitHub Pages:

```bash
./build.sh
```

The site is output to the `docs/` directory, which is what GitHub Pages serves from.

## Project structure

```
.
├── content/          # Markdown source files (mirrors output structure)
├── static/           # Static assets (CSS, images)
├── template.html     # Shared HTML template with {{ Title }} and {{ Content }} placeholders
├── src/
│   └── main.py       # Site generator
└── build.sh          # Production build script
```

## Running tests

```bash
./test.sh
```
