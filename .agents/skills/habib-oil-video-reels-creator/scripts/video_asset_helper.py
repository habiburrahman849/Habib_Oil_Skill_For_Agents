#!/usr/bin/env python3
"""
HabibOil Video Asset & Safe Zone Validator
-----------------------------------------
Validates local workspace assets for video production, checks file integrity,
and prints 9:16 safe zone overlay coordinates.
"""

import os
import sys

# Ensure UTF-8 output on Windows console
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

def find_workspace_root():
    curr = os.path.dirname(os.path.abspath(__file__))
    for _ in range(6):
        if os.path.exists(os.path.join(curr, "assets")):
            return curr
        parent = os.path.dirname(curr)
        if parent == curr:
            break
        curr = parent
    return os.path.dirname(os.path.abspath(__file__))

BASE_DIR = find_workspace_root()
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

EXPECTED_ASSETS = [
    ("me.jpg", "Influencer / Brand Owner Photo"),
    ("logo bes.png", "Transparent Cutout Brand Logo"),
    ("Logo.jpeg", "Square Brand Logo Card"),
    ("250 gram Habiboil Mustard oil.png", "250g Haircare & Scalp Massage SKU"),
    ("500ML Habiboil Mustard oil.png", "500ml Kitchen & Tarka SKU"),
    ("1 liter Habiboil Mustard oil.png", "1L Flagship Household Cooking SKU"),
    ("5 liter Habiboil Mustard oil.png", "5L Joint Family & Bulk Savings SKU"),
]

# Standard Vertical Video Specs
CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 1920


def get_safe_zones():
    return {
        "canvas": (CANVAS_WIDTH, CANVAS_HEIGHT),
        "top_ui_margin_px": 230,       # 12% top clear zone
        "bottom_ui_margin_px": 420,    # 22% bottom clear zone (1500px to 1920px)
        "action_zone_y_range": (230, 1500),
        "logo_overlay_rect": {
            "x": int(CANVAS_WIDTH * 0.72),   # top-right placement
            "y": 140,
            "width": int(CANVAS_WIDTH * 0.22),
            "description": "Top-right corner, clears Instagram and TikTok header audio pill",
        },
        "subtitle_zone_y_range": (1180, 1450),
    }


def validate_assets():
    print("=" * 65)
    print("🔎 HABIBOIL ASSET HEALTH & VIDEO READINESS REPORT")
    print("=" * 65)
    print(f"Target Resolution: {CANVAS_WIDTH}x{CANVAS_HEIGHT} (9:16 Vertical Video)")
    print(f"Assets Directory:  {ASSETS_DIR}\n")

    all_found = True
    for filename, description in EXPECTED_ASSETS:
        full_path = os.path.join(ASSETS_DIR, filename)
        if os.path.exists(full_path):
            size_kb = os.path.getsize(full_path) / 1024
            print(f"  [OK] {filename:<35} ({size_kb:>6.1f} KB) -> {description}")
        else:
            print(f"  [MISSING] {filename:<35} -> {description}")
            all_found = False

    print("\n" + "-" * 65)
    safe = get_safe_zones()
    print("📐 9:16 SAFE ZONE SPECIFICATIONS (Instagram Reels & TikTok):")
    print(f"  • Top UI Margin:      0px to {safe['top_ui_margin_px']}px (Clear of primary text)")
    print(f"  • Action Safe Center: {safe['action_zone_y_range'][0]}px to {safe['action_zone_y_range'][1]}px (Focal action, me.jpg, bottles)")
    print(f"  • Subtitle Sweetspot: {safe['subtitle_zone_y_range'][0]}px to {safe['subtitle_zone_y_range'][1]}px (Urdu Nastaliq subtitles)")
    print(f"  • Bottom UI Margin:   {1920 - safe['bottom_ui_margin_px']}px to 1920px (Reserved for handle & captions)")
    print(f"  • Watermark Rect:     x={safe['logo_overlay_rect']['x']}, y={safe['logo_overlay_rect']['y']}, w={safe['logo_overlay_rect']['width']}")
    print("=" * 65)

    if all_found:
        print("✅ ALL ASSETS READY FOR AI AGENT VIDEO PRODUCTION!")
    else:
        print("⚠️ SOME ASSETS ARE MISSING. CHECK THE FILE NAMES ABOVE.")
    return all_found


if __name__ == "__main__":
    success = validate_assets()
    sys.exit(0 if success else 1)
