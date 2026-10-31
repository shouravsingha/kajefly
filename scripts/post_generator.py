"""
Kajefly AI Micro-Agency: Post & Ad Copy Generator
Generates high-converting social media posts (Facebook & Instagram) with Bengali/English hooks, CTAs, and hashtags.
"""

import sys
import json
import argparse
from datetime import datetime

TEMPLATES = {
    "product_launch": {
        "hook": "🔥 নতুন চমক! আপনার পছন্দের {product_name} এখন আরও প্রিমিয়াম কোয়ালিটিতে!",
        "body": (
            "আপনি কি খুঁজছেন পারফেক্ট {product_name}? Kajefly নিয়ে এসেছে সেরা কালেকশন।\n\n"
            "✨ কেন নেবেন আমাদের থেকে?\n"
            "✔️ প্রিমিয়াম কোয়ালিটি ও ১০০% অরিজিনাল\n"
            "✔️ ক্যাশ অন ডেলিভারি সারা দেশে\n"
            "✔️ ঝামেলাহীন এক্সচেঞ্জ সুবিধা\n\n"
            "💰 আকর্ষণীয় ডিসকাউন্ট অফার চলছে সীমিত সময়ের জন্য!"
        ),
        "cta": "👉 অর্ডার করতে ইনবক্স করুন অথবা ভিজিট করুন আমাদের ওয়েবসাইট। দ্রুত স্টক শেষ হওয়ার আগেই বুক করুন!",
        "hashtags": "#{niche} #BangladeshiBrand #ShopLocalBD #OnlineShoppingBD #Kajefly"
    },
    "offer_discount": {
        "hook": "⚡ মেগা অফার অ্যালার্ট! সর্বোচ্চ {discount}% পর্যন্ত ছাড়!",
        "body": (
            "এই সুযোগ মিস করলে কিন্তু আফসোস করবেন! 🤩\n"
            "আমাদের বেস্ট সেলিং {product_name}-এ এখন পাচ্ছেন বিশাল ডিসকাউন্ট।\n\n"
            "⏰ অফারটি শুধুমাত্র প্রথম ৫০ জন ক্রেতার জন্য প্রযোজ্য।"
        ),
        "cta": "📲 ইনবক্সে মেসেজ দিয়ে এখনই আপনার পছন্দের ভ্যারিয়েন্ট কনফার্ম করুন।",
        "hashtags": "#SpecialOfferBD #DiscountAlert #FlashSale #{niche} #Kajefly"
    },
    "engagement_tips": {
        "hook": "💡 জেনে নিন {niche} নিয়ে ৩টি গোপন টিপস যা আপনার জানা দরকার!",
        "body": (
            "১. সঠিক কোয়ালিটি যাচাই করে কিনুন।\n"
            "২. সবসময় অথেনটিক রিভিউ দেখে সিদ্ধান্ত নিন।\n"
            "৩. রেগুলার কেয়ার নিন যাতে দীর্ঘস্থায়ী থাকে।\n\n"
            "আপনার অভিজ্ঞতা কেমন? কমেন্টে জানান তো!"
        ),
        "cta": "📌 পোস্টটি সেভ করে রাখুন এবং বন্ধুদের সাথে শেয়ার করুন!",
        "hashtags": "#TipsAndTricks #KnowledgeSharing #{niche}Tips #Bangladesh"
    }
}

def generate_post(product_name: str, niche: str, post_type: str = "product_launch", discount: str = "20"):
    template = TEMPLATES.get(post_type, TEMPLATES["product_launch"])
    hook = template["hook"].format(product_name=product_name, niche=niche, discount=discount)
    body = template["body"].format(product_name=product_name, niche=niche, discount=discount)
    cta = template["cta"]
    hashtags = template["hashtags"].format(niche=niche.replace(" ", ""))
    
    full_post = f"{hook}\n\n{body}\n\n{cta}\n\n{hashtags}"
    return full_post

def main():
    parser = argparse.ArgumentParser(description="Kajefly Social Media Post Generator")
    parser.add_argument("--product", default="প্রিমিয়াম ফ্যাশন কালেকশন", help="Product/service name")
    parser.add_argument("--niche", default="FashionBD", help="Niche or category")
    parser.add_argument("--type", choices=["product_launch", "offer_discount", "engagement_tips"], default="product_launch")
    parser.add_argument("--discount", default="25", help="Discount percentage")
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("🚀 K A J E F L Y   P O S T   G E N E R A T O R")
    print("=" * 60)
    post = generate_post(args.product, args.niche, args.type, args.discount)
    print(post)
    print("=" * 60)

if __name__ == "__main__":
    main()
