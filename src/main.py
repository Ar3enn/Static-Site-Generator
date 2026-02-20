import os
import shutil

from inline_markdown import markdown_to_html_node


def copy_static(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        if os.path.isfile(src_path):
            print(f"Copying {src_path} -> {dst_path}")
            shutil.copy(src_path, dst_path)
        else:
            copy_static(src_path, dst_path)


def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No h1 header found in markdown")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f:
        markdown = f.read()

    with open(template_path) as f:
        template = f.read()

    html_content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    page = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(page)


def generate_pages_recursive(content_dir, template_path, dest_dir):
    for item in os.listdir(content_dir):
        src_path = os.path.join(content_dir, item)
        dest_path = os.path.join(dest_dir, item)
        if os.path.isfile(src_path) and src_path.endswith(".md"):
            dest_html = dest_path[:-3] + ".html"
            generate_page(src_path, template_path, dest_html)
        elif os.path.isdir(src_path):
            generate_pages_recursive(src_path, template_path, dest_path)


def main():
    copy_static("static", "public")
    generate_pages_recursive("content", "template.html", "public")


if __name__ == "__main__":
    main()