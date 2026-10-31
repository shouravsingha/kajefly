"""
Kajefly AI Micro-Agency: Lead Management & Personalized Pitch Generator
Organizes prospective client outreach (F-Commerce pages, local businesses) and auto-crafts customized value-first pitch messages.
"""

import json
import argparse
import os

SAMPLE_LEADS_FILE = "C:/Users/HP/kajefly/leads.json"

PITCH_TEMPLATES = {
    "audit_hook": (
        "আসসালামু আলাইকুম {contact_person} ভাই/আপু,\n\n"
        "আপনাদের পেজ '{brand_name}'-এর কালেকশনগুলো বেশ চমৎকার! "
        "তবে একটা বিষয় লক্ষ্য করলাম — আপনাদের সাম্প্রতিক পোস্টগুলোতে অর্গানিক রিচ এবং এনগেজমেন্ট আগের চেয়ে কম হচ্ছে।\n\n"
        "আমি Kajefly (ডিজিটাল গ্রোথ এজেন্সি) থেকে বলছি। আপনাদের পেজের জন্য আমি একদম ফ্রিতে একটি 'Before vs After' "
        "কন্টেন্ট মকআপ ও ছোট অডিট তৈরি করেছি, যা ব্যবহার করলে পোস্টের ভিজিবিলিটি দ্বিগুণ হতে পারে।\n\n"
        "আপনি কি ২ মিনিটের জন্য স্যাম্পল ডিজাইনটি দেখতে চান? কোনো চার্জ নেই, ভালো লাগলে মতামত জানাবেন। 😊\n\n"
        "ধন্যবাদ,\nKajefly টিম 🚀"
    ),
    "website_hook": (
        "আসসালামু আলাইকুম {contact_person},\n\n"
        "আপনার '{brand_name}' পেজে প্রোডাক্টের প্রচুর ডিমান্ড দেখা যাচ্ছে। কিন্তু শুধুমাত্র ইনবক্সে অর্ডার ম্যানেজ করা সময়সাপেক্ষ এবং কাস্টমার ড্রপ হয়।\n\n"
        "আমরা আপনাদের ব্র্যান্ডের নামে একটি ফাস্ট-লোডিং, মোবাইল-ফ্রেন্ডলি ডেমো ওয়েবসাইট তৈরি করেছি যাতে কাস্টমাররা এক ক্লিকেই bKash/COD দিয়ে অর্ডার দিতে পারে।\n\n"
        "ডেমো লিঙ্কটি কি আপনাকে এখানে শেয়ার করতে পারি?\n\n"
        "শুভকামনা,\nKajefly"
    )
}

def generate_pitch(lead: dict, pitch_type: str = "audit_hook") -> str:
    template = PITCH_TEMPLATES.get(pitch_type, PITCH_TEMPLATES["audit_hook"])
    return template.format(
        contact_person=lead.get("contact_person", "ওনার"),
        brand_name=lead.get("brand_name", "আপনার ব্র্যান্ড")
    )

def main():
    parser = argparse.ArgumentParser(description="Kajefly Lead Pitch Generator")
    parser.add_argument("--brand", default="Style Haven BD", help="Target Brand Name")
    parser.add_argument("--person", default="রাকিব", help="Contact Person Name")
    parser.add_argument("--type", choices=["audit_hook", "website_hook"], default="audit_hook")
    
    args = parser.parse_args()
    
    lead = {
        "brand_name": args.brand,
        "contact_person": args.person
    }
    
    pitch = generate_pitch(lead, args.type)
    print("=" * 60)
    print(f"📩 CUSTOMIZED OUTREACH PITCH FOR: {args.brand}")
    print("=" * 60)
    print(pitch)
    print("=" * 60)

if __name__ == "__main__":
    main()
