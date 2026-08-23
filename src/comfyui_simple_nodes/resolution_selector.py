class ResolutionSelectorNode:
    RESOLUTIONS = {
        # --- Ultra-Wide & Large (4K / High-Res) ---
        "3840 x 2160 (16:9 4K UHD)": (3840, 2160),
        "2560 x 1440 (16:9 2K QHD)": (2560, 1440),
        "2560 x 1080 (21:9 Ultra-Wide)": (2560, 1080),
        "1920 x 1080 (16:9 Full HD)": (1920, 1080),
        "1600 x 1200 (4:3 High-Res UXGA)": (1600, 1200),

        # --- Mid-Range / Modern SDXL / Flux Standards ---
        "1536 x 1024 (3:2 Medium Widescreen)": (1536, 1024),
        "1344 x 768 (16:9 Modern Widescreen)": (1344, 768),
        "1280 x 1024 (5:4 Standard Landscape)": (1280, 1024),
        "1280 x 720 (16:9 720p HD)": (1280, 720),
        "1152 x 864 (4:3 Mid-Range)": (1152, 864),
        "1152 x 896 (9:7 Modern Aspect)": (1152, 896),
        "1024 x 1024 (1:1 Square)": (1024, 1024),

        # --- Smaller / Legacy SD 1.5 & Compact Sizes ---
        "1024 x 768 (4:3 Classic XGA)": (1024, 768),
        "1024 x 576 (16:9 SD Widescreen)": (1024, 576),
        "896 x 640 (7:5 Compact Widescreen)": (896, 640),
        "800 x 600 (4:3 SVGA)": (800, 600),
        "768 x 512 (3:2 Compact Widescreen)": (768, 512),
        "640 x 480 (4:3 Classic VGA)": (640, 480),
        "512 x 512 (1:1 Legacy Square)": (512, 512),
    }

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "preset": (list(s.RESOLUTIONS.keys()), {"default": "1280 x 1024 (5:4 Standard Landscape)"}),
                "portrait": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "get_resolution"
    CATEGORY = "Simple Tools"

    def get_resolution(self, preset, portrait):
        width, height = self.RESOLUTIONS.get(preset, (1280, 1024))

        # If portrait toggle is ON, flip width and height
        if portrait:
            width, height = height, width

        return (width, height)
