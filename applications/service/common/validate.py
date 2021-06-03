# xss过滤
def xss_escape(s: str):
    if s is None:
        return None
    else:
        return s.replace("&", "&amp;").replace(">", "&gt;").replace("<", "&lt;").replace("'", "&#39;").replace('"', "&#34;")
