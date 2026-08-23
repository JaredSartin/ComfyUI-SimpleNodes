from .simple_tags_node import SimpleTagsNode
from .resolution_selector import ResolutionSelectorNode

# The master mapping ComfyUI reads
NODE_CLASS_MAPPINGS = {
    "SimpleTagsNode": SimpleTagsNode,
    "ResolutionSelectorNode": ResolutionSelectorNode,
}

# The user-friendly names shown in the UI menu
NODE_DISPLAY_NAME_MAPPINGS = {
    "SimpleTagsNode": "Simple Prompt Tags",
    "ResolutionSelectorNode": "Resolution Selector",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
