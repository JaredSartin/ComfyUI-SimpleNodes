import re

class SimpleTagsNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": "<Bill> painted the <tall house> in the <pattern>",
                    "dynamicPrompts": False,
                }),
                "rules": ("STRING", {
                    "multiline": True,
                    "default": "Tall House | top | A really big house\nBill | bottom | A dude\nPattern | inline | Criss Cross",
                    "dynamicPrompts": True,
                }),
                "ignore_case": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("processed_text",)
    FUNCTION = "process_text"
    CATEGORY = "Simple Tools"

    def process_text(self, text, rules, ignore_case):
        top_inserts = []
        bottom_inserts = []
        processed_text = text
        flags = re.IGNORECASE if ignore_case else 0

        for line in rules.strip().splitlines():
            line = line.strip()
            # Ignore empty lines or comments
            if not line or line.startswith("#"):
                continue

            # Format expected: Key | Location | Replacement
            parts = [p.strip() for p in line.split("|")]
            key = parts[0]
            location = parts[1].lower() if len(parts) > 1 else "inline"
            replacement = parts[2] if len(parts) > 2 else ""

            if not key:
                continue

            # Strip brackets from key to get clean word (e.g., <Tall House> -> Tall House)
            clean_key = re.sub(r'^[<\[\(\{\s]+|[>\]\)\}\s]+$', '', key)
            pattern = rf"<{re.escape(clean_key)}>"

            # Only run if tag actually exists in prompt
            if re.search(pattern, processed_text, flags=flags):

                if location in ("top", "bottom"):
                    # Keep the key in the prompt sentence body (strip brackets)
                    processed_text = re.sub(pattern, clean_key, processed_text, flags=flags)

                    # Format as "Key: Replacement"
                    entry = f"{clean_key}: {replacement}" if replacement else clean_key

                    if location == "top":
                        top_inserts.append(entry)
                    else:
                        bottom_inserts.append(entry)

                elif location in ("xtop", "xbottom"):
                    # REMOVE the tag entirely from the prompt sentence body
                    processed_text = re.sub(pattern, "", processed_text, flags=flags)

                    # Use ONLY the replacement string (fallback to clean_key if blank)
                    entry = replacement if replacement else clean_key

                    if location == "xtop":
                        top_inserts.append(entry)
                    else:
                        bottom_inserts.append(entry)

                else:  # inline / inplace
                    # Replace <pattern> directly inline
                    processed_text = re.sub(pattern, replacement, processed_text, flags=flags)

        # Cleanup whitespace and double spaces
        processed_text = re.sub(r'\s*,\s*,', ',', processed_text)
        processed_text = re.sub(r'\s+', ' ', processed_text).strip()

        # Combine top tags, sentence body, and bottom tags
        full_output = []
        if top_inserts:
            full_output.append("\n".join(top_inserts))
        if processed_text:
            full_output.append(processed_text)
        if bottom_inserts:
            full_output.append("\n".join(bottom_inserts))

        return ("\n\n".join(full_output),)


# Node registration
NODE_CLASS_MAPPINGS = {
    "SimpleTagsNode": SimpleTagsNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SimpleTagsNode": "Simple Tags"
}
