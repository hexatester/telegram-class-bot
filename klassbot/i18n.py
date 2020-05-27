import i18n

i18n.set("filename_format", "{locale}.{format}")
i18n.set("skip_locale_root_data", True)
i18n.set("locale", "Indonesian")
i18n.set("fallback", "Indonesian")
i18n.load_path.append("./i18n/")

supported_languages = [
    "Indonesian"
]