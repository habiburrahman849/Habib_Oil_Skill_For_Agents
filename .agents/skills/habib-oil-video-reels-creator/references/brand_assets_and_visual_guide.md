# HabibOil Brand Assets & Visual Identity Guide 🎨🛢️

This document defines the strict visual standards, asset specifications, and cinematic guidelines for HabibOil short-form video production (Reels, Shorts, TikTok).

---

## 1. Local Workspace Assets

All video projects must load from or reference files located in `assets/`:

| File | Specs / Dimensions | How to Use in Video |
| :--- | :--- | :--- |
| `assets/me.jpg` | 55.9 KB, Portrait photograph | **The Face of HabibOil**: Brand owner and influencer. Represents honesty, traditional KPK values, and approachable craftsmanship. Used as the character reference for AI avatars, talking head shorts, founder reels, and behind-the-scenes narration. |
| `assets/logo bes.png` | 383 KB, PNG with transparent background | **Watermark & End Screen**: Overlay at the top-right corner (scale: 18-22% of video width, 12% from top margin to clear UI bars). Also appears in the final 2 seconds on the CTA card. |
| `assets/Logo.jpeg` | 112 KB, JPEG square image | **Branded Outro Card / Badge**: For end-card freeze frames and profile roundels. |
| `assets/250 gram Habiboil Mustard oil.png` | 733 KB, PNG | **Personal & Hair Care Hero**: Compact, portable, perfect for one-handed presentation, bedside table, vanity mirror, or gym bag. Ideal for scalp massage demonstrations. |
| `assets/500ML Habiboil Mustard oil.png` | 773 KB, PNG | **Kitchen Tarka & Small Household Hero**: Stood next to a hot tawa or iron karahi. Sits gracefully beside sliced onions, garlic, whole red chilies. |
| `assets/1 liter Habiboil Mustard oil.png` | 815 KB, PNG | **Main Flagship SKU**: The standard family cooking bottle. Used in recipes, frying fish, chicken karahi, chapli kabab, saag preparation. |
| `assets/5 liter Habiboil Mustard oil.png` | 886 KB, PNG | **Grand Family Can / Value Pack**: Symbol of abundance and economy for big joint families, wedding feasts, and winter bulk stock. |
| `assets/backgroud_music_habiboil.mp3` | 4.3 MB, MP3 audio | **Official Video BGM Track**: Authentic ambient instrumental bed. Leveling: Duck to -18dB to -22dB beneath voiceover, swell to -8dB during silent visual reveals. |
| `assets/Habib_oil_song.mp3` | 2.6 MB, MP3 audio | **Official Brand Song & Jingle**: High-energy musical signature track. Use for brand anthems, montage transitions, and hook/outro stingers. |

---

## 2. Color Palette & Lighting Standards

HabibOil videos must evoke warmth, appetite, purity, and organic nature. Avoid cold blues, neon pinks, or sterile corporate white.

### Color Tokens:
- **Mustard Gold (Primary)**: `#D4A017` / `#E5A823` – The radiant amber-gold color of freshly pressed mustard oil.
- **Natural Desi Green (Secondary)**: `#1E5E3A` / `#2D7A4D` – Lush mustard fields, fresh coriander, mint chutney, green chilies.
- **Warm Terracotta / Clay**: `#8B4513` / `#A0522D` – Traditional clay handis, clay bowls, rustic wooden cutting boards.
- **Deep Karahi Charcoal**: `#1C1C1C` / `#2B2B2B` – Black cast-iron cooking vessels that make golden sizzling oil pop in high contrast.
- **Crisp Cream White**: `#FAF8F2` – Contrast tone for bold Urdu subtitles and UI captions.

### Cinematic Lighting:
1. **The "Golden Hour" Glow**: Morning or late afternoon natural sunlight filtering through windows or outdoor mustard fields in Rustam.
2. **Backlit Oil Pour**: Backlight oil streams or drops so the liquid glows with an amber liquid-gold translucency.
3. **Warm Desi Kitchen Tones**: High color-rendering index (CRI) warm lights (3200K - 4000K), making food look mouth-watering and appetizing.

---

## 3. Safe Zones for 9:16 Vertical Video (1080 x 1920)

When composing frames and laying down captions or graphics, respect the platform UI overlay:

```text
+------------------------------------------+  0 px
|           [Platform Header UI]           |
|        Audio name, Search icon           |
|   SAFE FOR LOGO WATERMARK (Top-Right)    |
+------------------------------------------+  230 px (Top Safe Zone Margin)
|                                          |
|                                          |
|             PRIMARY ACTION               |
|            & VISUAL FOCUS                |
|                                          |
|   - Influencer Face (me.jpg)             |
|   - Product Bottle (assets/*.png)        |
|   - Pouring Oil & Sizzling Food          |
|                                          |
|   ------------------------------------   |
|   URDU HEADLINES / SUBTITLES GO HERE     |
|   (Between 1150px and 1420px)            |
|   ------------------------------------   |
|                                          |
+------------------------------------------+  1490 px (Bottom Safe Zone Margin)
|   [Platform Bottom & Right Sidebar UI]   |
|   Account Name, Caption, Audio Disc      |
|   Like, Comment, Share, Save Buttons     |
+------------------------------------------+  1920 px
```

---

## 4. Character Continuity Guidelines (`me.jpg`)

When generating scenes with the brand owner / influencer:
- **Facial Features**: Match the real face in `assets/me.jpg`—well-groomed beard/stubble, warm expressive eyes, approachable friendly smile.
- **Wardrobe**: Respectful, neat traditional Pakistani clothing:
  - White, cream, soft earth-toned, or olive green cotton/linen shalwar kameez.
  - Optional dark waistcoat or rustic woolen KPK chadar/shawl in winter outdoor scenes.
- **Tone & Delivery**: He speaks like an honest brother or knowledgeable friend from Rustam, never like a pushy TV salesman. His posture is grounded, confident, and sincere.

---

## 5. Bottle Consistency & Anti-Hallucination Rules

When using generative AI video models (Veo, Runway, Kling, Luma):
1. **Reference-First Generation**: Always feed the original PNG file of the exact bottle as the visual reference prompt.
2. **Do Not Alter Label Elements**: The "HabibOil" emblem, mustard flower illustration, and product size text on the bottle must remain authentic.
3. **No Phantom Bottles**: Do not allow AI to spawn generic green Heineken-style bottles or unmarked cooking oil jugs. The bottle must match the distinct HabibOil silhouette.
