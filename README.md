# HabibOil AI Video & Reels Creator Skill 🎥🛢️

Production-ready AI Agent Skill and Brand Assets for generating viral, high-converting, 9:16 vertical short-form videos (**Instagram Reels**, **YouTube Shorts**, **TikTok**, and **Facebook Reels**) for **HabibOil** (خالص سرسوں کا تیل / Pure Cold-Pressed Mustard Oil from Rustam, Mardan, KPK, Pakistan).

---

## 📁 Repository Structure

```text
.
├── assets/                                                # Brand & Product Visual Assets
│   ├── me.jpg                                            # Brand Owner & Influencer persona
│   ├── logo bes.png                                      # Transparent Cutout Brand Logo (Watermark)
│   ├── Logo.jpeg                                         # Square Brand Logo (Outro Badge)
│   ├── 250 gram Habiboil Mustard oil.png                 # Haircare & Scalp Massage SKU
│   ├── 500ML Habiboil Mustard oil.png                    # Kitchen Helper & Tarka SKU
│   ├── 1 liter Habiboil Mustard oil.png                  # Household Cooking Flagship SKU
│   ├── 5 liter Habiboil Mustard oil.png                  # Joint Family Bulk Savings SKU
│   ├── backgroud_music_habiboil.mp3                      # Official Video Reel BGM (ducked at -18dB)
│   └── Habib_oil_song.mp3                                # Official Brand Theme Song & Outro Jingle
│
└── .agents/skills/habib-oil-video-reels-creator/          # AI Agent Skill Directory
    ├── SKILL.md                                          # Master Agent Runbook & Production Workflow
    ├── references/                                       # Deep Knowledge & Playbooks
    │   ├── brand_assets_and_visual_guide.md              # Safe zones, 9:16 overlays, color tokens
    │   ├── social_engineering_and_marketing_playbook.md  # FMCG psychology, Pakistani hooks, retention
    │   └── urdu_script_vault.md                          # Production-ready Urdu & Roman Urdu scripts
    ├── resources/                                        # Storyboards & Prompts
    │   ├── reels_storyboard_template.md                  # Frame-by-frame 9:16 visual storyboard
    │   └── video_prompt_templates.json                   # AI Video Prompts (Runway, Kling, Veo, Luma)
    └── scripts/                                          # Automation Utilities
        ├── video_asset_helper.py                         # Asset integrity & safe-zone validator
        └── generate_reel_script.py                       # Automated reel script generator CLI
```

---

## 🚀 How to Use with AI Agents

1. Place this skill folder into your agent's workspace customization root:
   ```text
   .agents/skills/habib-oil-video-reels-creator/
   ```
2. Ensure the `assets/` directory is accessible in the workspace root or parent directory.
3. Your agent will automatically discover the skill and utilize the exact prompt templates, voiceover scripts, and asset guidelines for HabibOil short-form video campaigns.
