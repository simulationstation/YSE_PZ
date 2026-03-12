import os


def settings_file_path(file_path, filename="settings.ini"):
    return os.path.join(os.path.dirname(os.path.abspath(file_path)), filename)


def normalize_script_name(value):
    value = (value or "").strip()
    if not value or value == "/":
        return ""
    return "/" + value.strip("/")


def normalize_url_path(value, default="/"):
    value = (value or default or "/").strip()
    if value == "/":
        return "/"
    return "/" + value.strip("/") + "/"


def prefix_url_path(script_name, path, default="/"):
    script_name = normalize_script_name(script_name)
    path = normalize_url_path(path, default=default)

    if path == "/":
        return script_name + "/" if script_name else "/"

    if script_name and (path == script_name + "/" or path.startswith(script_name + "/")):
        return path

    return script_name + path if script_name else path
