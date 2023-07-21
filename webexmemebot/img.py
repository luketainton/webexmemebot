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


def generate_api_url(template: str, top_str: str, btm_str: str) -> str:
    tmpl_name, tmpl_ext = template.split(".")

    # https://memegen.link/#special-characters

    top_str = top_str.replace("_", "__")
    top_str = top_str.replace("-", "--")
    top_str = top_str.replace(" ", "_")
    top_str = top_str.replace("?", "~q")
    top_str = top_str.replace("&", "~a")
    top_str = top_str.replace("%", "~p")
    top_str = top_str.replace("#", "~h")
    top_str = top_str.replace("/", "~s")
    top_str = top_str.replace("\\", "~b")
    top_str = top_str.replace("<", "~l")
    top_str = top_str.replace(">", "~g")
    top_str = top_str.replace('"', "''")

    btm_str = btm_str.replace("_", "__")
    btm_str = btm_str.replace("-", "--")
    btm_str = btm_str.replace(" ", "_")
    btm_str = btm_str.replace("?", "~q")
    btm_str = btm_str.replace("&", "~a")
    btm_str = btm_str.replace("%", "~p")
    btm_str = btm_str.replace("#", "~h")
    btm_str = btm_str.replace("/", "~s")
    btm_str = btm_str.replace("\\", "~b")
    btm_str = btm_str.replace("<", "~l")
    btm_str = btm_str.replace(">", "~g")
    btm_str = btm_str.replace('"', "''")

    url: str = (
        f"https://api.memegen.link/images/{tmpl_name}/{top_str}/{btm_str}.{tmpl_ext}"
    )
    return url
