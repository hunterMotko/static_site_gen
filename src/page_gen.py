import os
from markdown_blocks import markdown_to_html_node


def generate_page(from_path, template_path, dest_path, basepath):
    with open(from_path, 'r') as f:
        markdown_content = f.read()
    with open(template_path, 'r') as f:
        template = f.read()

    html_node = markdown_to_html_node(markdown_content)
    content_html = html_node.to_html()
    title = extract_title(markdown_content)

    full_html = template.replace("{{ Title }}", title).replace(
        "{{ Content }}", content_html)
    full_html = full_html.replace('href="/', f'href="{basepath}')
    full_html = full_html.replace('src="/', f'src="{basepath}')

    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, 'w') as f:
        f.write(full_html)


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No h1 header found in markdown")


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    entries = os.listdir(dir_path_content)
    for entry in entries:
        from_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)
        if os.path.isfile(from_path):
            if from_path.endswith(".md"):
                html_dest_path = dest_path.replace(".md", ".html")
                generate_page(from_path, template_path,
                              html_dest_path, basepath)
        else:
            generate_pages_recursive(
                from_path, template_path, dest_path, basepath)
