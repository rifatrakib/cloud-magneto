def build_base_url(config, subdomain):
    target_domain = config.get("TARGET_DOMAIN")
    protocol = config.get("PROTOCOL")
    return f"{protocol}://{subdomain}.{target_domain}"
