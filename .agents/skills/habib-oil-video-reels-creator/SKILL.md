---
name: habib-oil-video-reels-creator
description: >-
  Expert runbook and production workflow for AI agents to create viral, high-converting
  vertical short-form videos (Instagram Reels, YouTube Shorts, TikTok, Facebook Reels)
  for HabibOil pure cold-pressed mustard oil. Instructs AI on using local brand assets
  (me.jpg influencer photo, 250g/500ml/1L/5L bottles, logo), crafting Urdu voiceover scripts,
  Pakistani FMCG social engineering, and generating AI video prompts.
---

# HabibOil Vertical Video & Reels Creator Skill 🎥✨

A specialized, end-to-end production skill for AI agents creating viral, high-converting, 9:16 vertical short-form videos (**Instagram Reels**, **YouTube Shorts**, **TikTok**, and **Facebook Reels**) for **HabibOil** (خالص سرسوں کا تیل / Pure Cold-Pressed Mustard Oil from Rustam, Mardan, KPK, Pakistan).

---

## 1. Brand Essence & Core Assets

HabibOil stands for **purity, tradition, and honesty** (رستم کی پہچان، ہر گھر کی شان). The brand bridges authentic village cold-press heritage with hygienic modern filtration.

### Asset Inventory (`assets/`)
Every AI agent must reference and utilize these exact local files:

| Asset Name | Relative Path | Purpose & Rules |
| :--- | :--- | :--- |
| **Brand Ambassador / Influencer** | `assets/me.jpg` | **Primary Character**: The real brand owner. Always depict him in clean, dignified, traditional Pakistani attire (shalwar kameez, optional waistcoat/chadar in winter). Warm, welcoming smile, honest and humble body language. Never replace his face. and she is a female always use a female consist voiceover. |
| **250 Gram Bottle** | `assets/250 gram Habiboil Mustard oil.png` | **Haircare, Trial & Scalp Massage**: Target audience: youth, individuals, hair care routines, hostelites. Highlight portable size, easy grip. |
| **500 ML Bottle** | `assets/500ML Habiboil Mustard oil.png` | **Kitchen Helper & Tarka | and Sir ki Malash**: Target audience: small families, daily dal tarka, evening snacks, pakoras, homemade pickle (اچار). |
| **1 Litre Bottle** | `assets/1 liter Habiboil Mustard oil.png` | **Core Household Cooking**: Target audience: daily home cooking, frying fish, chapli kabab, traditional sarson ka saag. |
| **5 Litre Can / Bottle** | `assets/5 liter Habiboil Mustard oil.png` | **Family Savings & Feasts**: Target audience: joint families, bulk monthly grocery, winter feasts, wedding seasons, maximum value per rupee. |
| **Transparent Logo** | `assets/logo bes.png` | **Overlay Logo**: High-res cutout logo for top-right / top-center screen corner watermark. |
| **Square Logo** | `assets/Logo.jpeg` | **Profile / End Card**: Brand card ending for outro screens and packaging badges. |

### Strict Product Integrity Rules:
1. **Never Hallucinate Labels**: Do not alter, translate, or redraw the printed bottle label. The label on `assets/*.png` is the genuine Pakistani registered trademark.
2. **True Proportions**: When multiple bottles appear, 250g is smallest, 5L is largest. Maintain realistic physical scale.
3. **No Artificial / Plastic Look**: Oil must have an authentic deep golden-amber glow (`#D4A017` to `#FFB800`), viscous natural pour, and realistic droplet refraction.
4. **Cultural Grounding**: Visuals must reflect real Khyber Pakhtunkhwa (KPK) and Pakistani domestic life—brass karahis, clay handis, wooden charpoys, mustard fields, warm brick/stone textures, clean shalwar kameez.

---

## 2. Technical Specifications for Reels & Shorts (9:16)

Short-form video algorithms reward **high watch time**, **instant visual retention**, and **clean safe-zone compliance**.

- **Aspect Ratio**: `9:16` vertical (`1080 x 1920 px`).
- **Optimal Duration**:
  - *Micro-Hooks (Curiosity/Bait)*: 12 – 18 seconds.
- **Safe Zones (UI Overlay Protection)**:
  - **Top 12% (`0 - 230px`)**: Keep clear of crucial text (reserved for platform audio tags, search icon, logo watermark).
  - **Bottom 22% (`1490 - 1920px`)**: Keep clear of core focal points (account handle, captions, like/comment sidebar buttons sit here).
  - **Action Center (`230 - 1490px`)**: All key subject action (the bottle, pouring oil, influencer's face, frying sizzle) must reside in this central viewport.
- **Frame Rate**: 30 fps or 60 fps for smooth slow-motion pours.

---

## 3. Social Engineering & Pakistani FMCG Marketing Strategy

The audience in Pakistan and overseas Pakistani diaspora responds powerfully to specific psychological triggers. When guiding content creation, the AI agent must apply these 5 **Social Engineering Pillars**:

### Pillar 1: The "Adulteration Alarm" Hook (ملاوٹ کا خوف بمقابلہ خالص کا سکون)
- **Psychological Trigger**: Cooking oil and ghee fraud is a major fear in Pakistan. Chemical refining, synthetic scents, and recycled oils worry every homemaker and parent.
- **Content Angle**: Show the stark difference between industrial chemical refining and cold-pressed HabibOil from Rustam. Frame HabibOil not as a luxury, but as *health security* for the family's heart and digestive system.

### Pillar 2: Desi Nostalgia & The "Dadi-Nani" Memory Trigger
- **Psychological Trigger**: Longing for the pure village lifestyle (گاؤں کی خالص خوراک) before chemicalized foods.
- **Content Angle**: Sunday morning winter sunshine, warm wool shawls, traditional head massage (چپڑی مالش), smell of freshly fried pakoras on a rainy afternoon, sarson ka saag with homemade makki ki roti and white butter.

### Pillar 3: Sensory ASMR & Culinary Sizzle (تڑکے کی خوشبو اور آواز)
- **Psychological Trigger**: Instant appetite stimulation and sensory immersion.
- **Content Angle**: Macro shots of mustard oil heating in a heavy iron karahi, the crackle of cumin seeds (زیرہ), red round chilies, sizzling chapli kababs, and golden fish fillets.

### Pillar 4: The Honest Founder Persona (`me.jpg`)
- **Psychological Trigger**: In Pakistan, people buy from people they trust, not faceless corporations.
- **Content Angle**: The brand owner is positioned as an honest, hardworking local entrepreneur from Rustam, Mardan. He shows the factory, shakes hands with farmers, stands by his product, and offers personal guarantee.

### Pillar 5: Comment-Baiting & Algorithmic Debate Triggers
- **Psychological Trigger**: The urge to express personal opinion and regional pride.
- **Formulas**:
  - *"سرسوں کے تیل میں پکوڑے زیادہ کرسپی بنتے ہیں یا سموسے؟ کمنٹ میں فیصلہ کریں!"* (Pakoras vs Samosas?)
  - *"آپ کے گھر سرسوں کا تیل کس کام آتا ہے؟ کھانے میں یا بالوں کی مالش میں؟ (A یا B لکھیں)"*
  - *"کیا آپ کے گاؤں یا شہر میں اصلی سرسوں کا تیل ملتا ہے؟ اپنا شہر کمنٹ کریں۔"*

---

## 4. Video Storyboard Architecture: The 5-Beat Formula

Every Reel or Short generated under this skill must adhere to this proven high-retention structure:

```
[0:00 - 0:03] BEAT 1: Visual & Auditory Hook (Stop the scroll immediately)
[0:03 - 0:10] BEAT 2: Problem / Desi Curiosity (State common frustration or secret)
[0:10 - 0:22] BEAT 3: HabibOil Hero Moment (Golden pour, bottle reveal, influencer test)
[0:22 - 0:32] BEAT 4: Sensory Climax / Result (Crispy bite, lustrous hair, pure drop)
[0:32 - 0:40] BEAT 5: Trust CTA & WhatsApp Trigger (Comment below / Order from Rustam)
```

---

## 5. Scripting & Language Guidelines: Authentic Urdu & Pashto

AI agents must write scripts tailored for Pakistani social media audiences. 

### Language Tone:
- **Urdu (اردو)**: Warm, respectful, conversational, modern Desi (باوقار، اپنائیت سے بھرپور، عام فہم اور پر اثر). Avoid stiff textbook Urdu. Use terms like *خالص*, *قدرتی خوشبو*, *رستم کی پہچان*, *سرسوں کا ساگ*, *ہلکا تڑکہ*.
- **Roman Urdu**: Accurate conversational spelling for teleprompters, voiceover directors, or AI voice generators (ElevenLabs / Murf / OpenAI Voice).

---

## 6. Step-by-Step AI Agent Runbook

When a user asks to create video content, ideas, or scripts for HabibOil:

1. **Step 1: Determine the Video Objective & Bottle SKU**
   - Haircare / Totka -> select `assets/250 gram Habiboil Mustard oil.png`.
   - Daily cooking / Tarka -> select `assets/500ML Habiboil Mustard oil.png` or `assets/1 liter Habiboil Mustard oil.png`.
   - Family grocery / Savings -> select `assets/5 liter Habiboil Mustard oil.png`.
   - Founder story / Factory tour -> include `assets/me.jpg` + all bottles.

2. **Step 2: Generate the Scene-by-Scene Storyboard**
   - Write timestamps (0-3s, 3-10s, etc.).
   - Define visual actions (Camera movement, lighting, actor action, bottle placement).
   - Write exact Urdu Voiceover (اردو وائس اوور) and Roman Urdu pronunciation.
   - Specify on-screen bold text (Urdu Nastaliq / Naskh subtitle hooks).

3. **Step 3: Generate Generative Video Prompts**
   - Provide exact prompt strings compatible with modern Video AI models (Runway Gen-3 Alpha, Luma Ray 2, Google Veo, Kling AI, Pika, Stable Video Diffusion).
   - Reference `assets/me.jpg` for face/character consistency and `assets/*.png` for product accuracy.

4. **Step 4: Produce Post-Production Directives**
   - Logo watermark placement (`assets/logo bes.png` at top-right corner with 85% opacity).
   - Background Audio / Sound Design (Rabab plucked notes, flute, ambient village sounds, or hot oil sizzle ASMR).
   - Instagram/TikTok Caption with Urdu, Pashto, call-to-action, and optimized hashtags (`#HabibOil #RustamKiPehchan #SarsonKaTel`).

---

 Use the atached backgroud music whcih is offical song of habiboil. Zindagi mi layi Rang habiboil Harpal behtar.
