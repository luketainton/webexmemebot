import requests


def get_templates() -> list[dict]:
    url: str = "https://api.memegen.link/templates"
    req: requests.Response = requests.get(url=url, timeout=5)
    req.raise_for_status()
    data: dict = req.json()
    templates: list = []
    for tmpl in data:
        if tmpl["lines"] != 2:
            continue
        if tmpl["id"] == "oprah":
            tmpl["name"] = "Oprah You Get A..."
        tmpl_ext: str = "gif" if "animated" in tmpl["styles"] else "jpg"
        tmpl_data: dict = {
            "id": tmpl["id"],
            "name": tmpl["name"],
            "ext": tmpl_ext,
            "choiceval": tmpl["id"] + "." + tmpl_ext,
        }
        templates.append(tmpl_data)
    templates = sorted(templates, key=lambda d: d["name"])
    return templates


def format_meme_string(input_string: str) -> str:
    # https://memegen.link/#special-characters
    out_string: str = input_string.replace("_", "__")
    out_string: str = out_string.replace("-", "--")
    out_string: str = out_string.replace(" ", "_")
    out_string: str = out_string.replace("?", "~q")
    out_string: str = out_string.replace("&", "~a")
    out_string: str = out_string.replace("%", "~p")
    out_string: str = out_string.replace("#", "~h")
    out_string: str = out_string.replace("/", "~s")
    out_string: str = out_string.replace("\\", "~b")
    out_string: str = out_string.replace("<", "~l")
    out_string: str = out_string.replace(">", "~g")
    out_string: str = out_string.replace('"', "''")
    return out_string


def generate_api_url(template: str, top_str: str, btm_str: str) -> str:
    tmpl_name: str
    tmpl_ext: str
    tmpl_name, tmpl_ext = template.split(".")

    top_str = format_meme_string(top_str)
    btm_str = format_meme_string(btm_str)

    url: str = f"https://api.memegen.link/images/{tmpl_name}/{top_str}/{btm_str}.{tmpl_ext}"
    return url
