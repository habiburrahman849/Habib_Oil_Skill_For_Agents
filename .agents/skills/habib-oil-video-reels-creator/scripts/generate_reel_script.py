#!/usr/bin/env python3
"""
HabibOil Reel Script & Storyboard Generator
------------------------------------------
A CLI tool and module that generates complete 9:16 vertical video production
packets (Reels, Shorts, TikTok) for HabibOil.

Outputs:
  - Timed 5-beat storyboard
  - Urdu voiceover script with Roman Urdu guide
  - Pashto regional translation hook
  - Video AI generative prompts (for Runway Gen-3, Kling, Google Veo, Luma)
  - Asset attachment references (assets/me.jpg, assets/*.png)
  - Social captions & hashtag suite
"""

import argparse
import json
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

BOTTLE_SKUS = {
    "250g": {
        "file": "250 gram Habiboil Mustard oil.png",
        "label": "250 Gram (Haircare & Scalp Massage)",
        "default_pillar": "haircare",
    },
    "500ml": {
        "file": "500ML Habiboil Mustard oil.png",
        "label": "500 ML (Kitchen Helper & Tarka)",
        "default_pillar": "cooking",
    },
    "1l": {
        "file": "1 liter Habiboil Mustard oil.png",
        "label": "1 Litre (Household Cooking Flagship)",
        "default_pillar": "cooking",
    },
    "5l": {
        "file": "5 liter Habiboil Mustard oil.png",
        "label": "5 Litre (Joint Family Bulk Savings)",
        "default_pillar": "savings",
    },
}

PRESET_PILLARS = {
    "haircare": {
        "title": "Haircare & Traditional Scalp Routine (نانی کا پرانا راز)",
        "sku": "250g",
        "hook_urdu": "اگر کیمیکل والے شیمپو اور مہنگے سیرم آزما کر تھک چکے ہیں، تو صرف ایک منٹ میری بات سنیں!",
        "hook_roman": "Agar chemical wale shampoo aur mehnge serum aazma kar thak chuke hain, to sirf ek minute meri baat sunein!",
        "body_urdu": "ہمارے بزرگوں کے بال آخری عمر تک مضبوط کیوں رہتے تھے؟ کیونکہ وہ استعمال کرتے تھے خالص، کولڈ پریسڈ سرسوں کا تیل۔ HabibOil کا یہ 250 گرام کا چھوٹا پیک ہلکا سا نیم گرم کریں اور انگلیوں کی پوروں سے جڑوں میں مالش کریں۔ نہ کوئی کیمیکل، نہ کوئی ملاوٹ۔",
        "body_roman": "Hamare buzurgon ke baal aakhri umar tak mazboot kyun rehte the? Kyunke wo istemal karte the khalis, cold-pressed sarson ka tel. HabibOil ka yeh 250 gram ka chota pack halka sa neem-garam karein aur ungliyon ki poron se jaron mein malish karein. Na koi chemical, na koi milawat.",
        "pashto": "که غواړئ چې وېښتان مو تل پياوړي او ښکلي وي، د رستم خالص HabibOil وکاروئ.",
        "cta_urdu": "آج ہی اپنا 250 گرام پیک منگوانے کے لیے واٹس ایپ پر میسج کریں۔",
        "cta_roman": "Aaj hi apna 250 gram pack mangwane ke liye WhatsApp par message karein.",
        "ai_prompt": "Cinematic 9:16 vertical video. A clean white-clad Pakistani man (matching me.jpg) gently pouring amber-gold oil from a 250g bottle into a brass bowl in warm morning sunshine. Wooden comb and neem leaves nearby. Photorealistic, shallow depth of field, 4k.",
    },
    "cooking": {
        "title": "The Authentic Desi Sizzle & Tarka (پشاوری ذائقہ اور تڑکہ)",
        "sku": "1l",
        "hook_urdu": "کیا آپ نے کبھی خالص سرسوں کے تیل میں پشاوری چپلی کباب یا مچھلی تل کر کھائی ہے؟",
        "hook_roman": "Kya aap ne kabhi khalis sarson ke tel mein Peshawari chapli kabab ya machli tal kar khayi hai?",
        "body_urdu": "سرسوں کے تیل کا تڑکہ اور وہ کڑک دار آواز جو پورے محلے کو کھانے پر مجبور کر دے! HabibOil کی ملٹی اسٹیج فلٹریشن کھانوں کو بناتی ہے بے حد کرسپی، لذیذ اور ہاضمے کے لیے ہلکا۔ بازار کے کیمیکل والے تیل کو خدا حافظ کہیں۔",
        "body_roman": "Sarson ke tel ka tarka aur wo karak-dar aawaz jo poore mohallay ko khane par majboor kar de! HabibOil ki multi-stage filtration khanon ko banati hai behad crispy, lazeez aur hazme ke liye halka. Bazaar ke chemical wale tel ko khuda-hafiz kahein.",
        "pashto": "د پېښوري خوړو اصلي او خوندور خوند په خالصو شړشمو تېلو کې دی.",
        "cta_urdu": "اپنے کچن کے لیے خالص ایک لیٹر بوتل ابھی واٹس ایپ پر آرڈر کریں۔",
        "cta_roman": "Apne kitchen ke liye khalis 1 litre botal abhi WhatsApp par order karein.",
        "ai_prompt": "Commercial food cinematography 9:16. Slow-motion sizzling chapli kabab frying in bubbling amber mustard oil inside a heavy black iron pan. 1L HabibOil bottle standing on stone counter with sliced red tomatoes and green chilies. 4k resolution.",
    },
    "purity_test": {
        "title": "Asli vs Naqli 3-Second Purity Test (اصلی اور نقلی تیل کی پہچان)",
        "sku": "1l",
        "hook_urdu": "رک جائیں! کیا آپ جانتے ہیں کہ آپ جو تیل بازار سے لا رہے ہیں وہ اصلی ہے یا کیمیکل ملا ہوا؟",
        "hook_roman": "Ruk jayein! Kya aap jante hain ke aap jo tel bazaar se laa rahe hain wo asli hai ya chemical mila hua?",
        "body_urdu": "اصلی سرسوں کے تیل کی دو بڑی نشانیاں ہیں: پہلی اس کا قدرتی گہرا سنہری رنگ جو شیشے کی طرح چمکتا ہے، اور دوسری اس کی تیز قدرتی مہک جو سونگھتے ہی بتا دیتی ہے کہ کوئی ملاوٹ نہیں کی گئی۔ HabibOil رستم کی سچی پہچان ہے۔",
        "body_roman": "Asli sarson ke tel ki do badi nishaniyan hain: Pehli is ka qudrati gehra sunehri rang jo sheeshe ki tarah chamakta hai, aur doosri is ki teez qudrati mehak jo soonghte hi bata deti hai ke koi milawat nahi ki gayi. HabibOil Rustam ki sachi pehchan hai.",
        "pashto": "د اصلي او نقلي شړشمو تېلو توپیر په څو ثانیو کې وپېژنئ او خپله کورنۍ وساتئ.",
        "cta_urdu": "ملاوٹ سے پاک اصلی سرسوں کا تیل حاصل کرنے کے لیے ابھی واٹس ایپ کریں۔",
        "cta_roman": "Milawat se paak asli sarson ka tel hasil karne ke liye abhi WhatsApp karein.",
        "ai_prompt": "Photorealistic 9:16 video. Brand owner (matching me.jpg) holding two glass cups on wooden table: one murky yellow, one sparkling golden amber HabibOil. Warm rustic KPK room, clear visual purity demonstration, 4k 60fps.",
    },
    "savings": {
        "title": "The Joint Family 5-Litre Bulk Savings (بڑا خاندان، بڑی بچت)",
        "sku": "5l",
        "hook_urdu": "کیا آپ ہر ہفتے تیل کی چھوٹی بوتلیں خرید کر بجٹ سے تنگ آ چکے ہیں؟",
        "hook_roman": "Kya aap har hafte tel ki choti botalen khareed kar budget se tang aa chuke hain?",
        "body_urdu": "مشترکہ خاندانوں اور روزمرہ کھانوں کے لیے HabibOil کا 5 لیٹر فیملی کین سب سے سمجھدار انتخاب ہے۔ ایک بار منگوائیں اور پورا مہینہ خالص رستم کے تیل سے بے فکر ہو جائیں۔ پیسے کی بھی بڑی بچت اور خاندان کی صحت بھی محفوظ۔",
        "body_roman": "Mushtarka khandano aur rozmarrah khanon ke liye HabibOil ka 5 litre family can sab se samajhdar intekhab hai. Ek baar mangwayein aur poora maheena khalis Rustam ke tel se befikar ho jayein. Paise ki bhi badi bachat aur khandan ki sehat bhi mehfooz.",
        "pashto": "د لویې کورنۍ لپاره د ۵ لیټرو بوتل تر ټولو اقتصادي او غوره پرېکړه ده.",
        "cta_urdu": "5 لیٹر فیملی کین پر رعایتی قیمت حاصل کرنے کے لیے ابھی میسج کریں۔",
        "cta_roman": "5 litre family can par riayati qeemat hasil karne ke liye abhi message karein.",
        "ai_prompt": "Cinematic vertical 9:16 commercial. Large 5-liter container with authentic printed HabibOil label standing on an authentic Pakistani wooden dining table. Delicious clay handi and fresh warm roti spread in background. Soft golden light.",
    },
}


def build_reel_packet(pillar_key, custom_title=None, use_face=True):
    pillar = PRESET_PILLARS.get(pillar_key, PRESET_PILLARS["cooking"])
    sku_key = pillar["sku"]
    bottle_info = BOTTLE_SKUS[sku_key]

    packet = {
        "title": custom_title or pillar["title"],
        "pillar": pillar_key,
        "aspect_ratio": "9:16 (1080x1920 vertical)",
        "duration_target": "30 Seconds",
        "assets_used": {
            "primary_bottle": f"assets/{bottle_info['file']}",
            "brand_influencer": "assets/me.jpg" if use_face else None,
            "logo_watermark": "assets/logo bes.png",
        },
        "storyboard": [
            {
                "beat": "1. The 3-Second Hook (0-3s)",
                "visual": f"Instant visual scroll-stopper. High-impact macro shot featuring {bottle_info['label']}.",
                "text_on_screen": pillar["hook_urdu"][:40] + "...",
                "voiceover_urdu": pillar["hook_urdu"],
                "voiceover_roman": pillar["hook_roman"],
                "sound_design": "Dramatic ASMR sizzle or tension riser",
            },
            {
                "beat": "2. Problem / Desi Relatability (3-10s)",
                "visual": "Depicting common chemical oil problems or the longing for authentic village heritage.",
                "text_on_screen": "خالص بمقابلہ کیمیکل",
                "voiceover_urdu": "بازار کے غیر معیاری تیل سے بچیں، اصل پہچان سیکھیں۔",
                "voiceover_roman": "Bazaar ke ghair-meyari tel se bachein, asal pehchan seekhein.",
                "sound_design": "Acoustic traditional KPK rabab strum",
            },
            {
                "beat": "3. The HabibOil Hero Solution (10-20s)",
                "visual": f"Brand owner (me.jpg) presenting {bottle_info['file']} with genuine label facing camera.",
                "text_on_screen": "رستم کی پہچان: HabibOil",
                "voiceover_urdu": pillar["body_urdu"],
                "voiceover_roman": pillar["body_roman"],
                "sound_design": "Warm comforting melody",
            },
            {
                "beat": "4. Sensory / Proof Climax (20-25s)",
                "visual": "Golden translucent stream poured in slow motion. Radiant liquid amber refraction.",
                "text_on_screen": "100٪ کولڈ پریسڈ سرسوں کا تیل",
                "voiceover_urdu": "نہ کوئی کیمیکل، نہ کوئی ملاوٹ۔ صرف خالص رستم کا خلوص۔",
                "voiceover_roman": "Na koi chemical, na koi milawat. Sirf khalis Rustam ka khuloos.",
                "sound_design": "Gentle fluid pour sound effect",
            },
            {
                "beat": "5. Outro & Call to Action (25-30s)",
                "visual": "Brand card with WhatsApp button pulsate, Cash on Delivery badge, logo bes.png overlay.",
                "text_on_screen": "ابھی واٹس ایپ پر آرڈر کریں",
                "voiceover_urdu": pillar["cta_urdu"],
                "voiceover_roman": pillar["cta_roman"],
                "pashto_subtitle": pillar["pashto"],
                "sound_design": "Uplifting closing chord with chime",
            },
        ],
        "video_generation_ai_prompt": pillar["ai_prompt"],
        "social_media_distribution": {
            "urdu_caption": f"{pillar['title']}\n\n{pillar['body_urdu']}\n\nآرڈر کرنے کے لیے ابھی واٹس ایپ پر رابطہ فرمائیں!",
            "pashto_caption": f"{pillar['pashto']}\n\nد رستم خالص کیفیت اوس ستاسو په کور کې دی.",
            "hashtags": "#HabibOil #RustamKiPehchan #SarsonKaTel #PureMustardOil #DesiCooking #KPK #Mardan #PakistanFood",
            "best_posting_time": "7:00 PM - 9:30 PM PKT",
        },
    }
    return packet


def main():
    parser = argparse.ArgumentParser(description="HabibOil Reel Script Generator")
    parser.add_argument(
        "--pillar",
        choices=["haircare", "cooking", "purity_test", "savings"],
        default="cooking",
        help="Content marketing pillar",
    )
    parser.add_argument("--title", type=str, default=None, help="Custom reel title")
    parser.add_argument(
        "--no-face", action="store_true", help="Omit influencer me.jpg"
    )
    parser.add_argument(
        "--json", action="store_true", help="Output raw JSON instead of formatted text"
    )

    args = parser.parse_args()
    packet = build_reel_packet(args.pillar, args.title, use_face=not args.no_face)

    if args.json:
        print(json.dumps(packet, indent=2, ensure_ascii=False))
        return

    print("=" * 70)
    print(f"🎬 HABIBOIL REEL PRODUCTION PACKET: {packet['title']}")
    print("=" * 70)
    print(f"Format: {packet['aspect_ratio']} | Duration: {packet['duration_target']}")
    print(f"Primary Bottle: {packet['assets_used']['primary_bottle']}")
    print(f"Influencer (me.jpg): {packet['assets_used']['brand_influencer']}")
    print(f"Logo Overlay: {packet['assets_used']['logo_watermark']}")
    print("-" * 70)
    print("📜 SCENE-BY-SCENE STORYBOARD:")
    for scene in packet["storyboard"]:
        print(f"\n▶ {scene['beat']}")
        print(f"  Visual: {scene['visual']}")
        print(f"  Screen Text (Urdu): {scene['text_on_screen']}")
        print(f"  VO (Urdu): {scene['voiceover_urdu']}")
        print(f"  VO (Roman): {scene['voiceover_roman']}")
        if "pashto_subtitle" in scene:
            print(f"  Pashto Subtitle: {scene['pashto_subtitle']}")

    print("\n" + "-" * 70)
    print("🤖 AI VIDEO GENERATOR PROMPT (Veo / Runway Gen-3 / Kling):")
    print(packet["video_generation_ai_prompt"])

    print("\n" + "-" * 70)
    print("📱 SOCIAL CAPTION & HASHTAGS:")
    print(packet["social_media_distribution"]["urdu_caption"])
    print(f"\n{packet['social_media_distribution']['hashtags']}")
    print(f"Best Posting Time: {packet['social_media_distribution']['best_posting_time']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
