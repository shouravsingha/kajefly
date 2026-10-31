"""
Kajefly AI Micro-Agency: 30-Day Content Calendar Planner
Generates a complete 30-day social media schedule with post types, hooks, and content formats.
Outputs to CSV and Markdown.
"""

import csv
import argparse
from datetime import datetime, timedelta

POST_PILLARS = [
    {"type": "Product Showcase", "focus": "হাইলাইট ও স্পেসিফিকেশন", "format": "Single Image / Carousel"},
    {"type": "Behind The Scenes", "focus": "প্যাকেজিং / মেকিং প্রসেস", "format": "Reels / Short Video"},
    {"type": "Customer Review / Social Proof", "focus": "হ্যাপি কাস্টমার রিভিউ ও আনবক্সিং", "format": "Screenshot / Testimonial Grid"},
    {"type": "Educational / Tips", "focus": "ব্যবহারের নিয়ম বা ভ্যালু টিপস", "format": "Infographic / Carousel"},
    {"type": "Interactive / Poll", "focus": "কোন কালার বা ডিজাইন পছন্দ?", "format": "Story / Engagement Post"},
    {"type": "Flash Offer / Weekend Sale", "focus": "সীমিত সময়ের বিশেষ ডিসকাউন্ট", "format": "Promotional Banner"}
]

def generate_calendar(brand_name: str, niche: str, start_date_str: str = None, days: int = 30):
    if not start_date_str:
        current_date = datetime.now()
    else:
        current_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        
    calendar = []
    for day in range(1, days + 1):
        pillar = POST_PILLARS[(day - 1) % len(POST_PILLARS)]
        date_str = (current_date + timedelta(days=day-1)).strftime("%Y-%m-%d (%A)")
        
        entry = {
            "Day": f"Day {day}",
            "Date": date_str,
            "Brand": brand_name,
            "Pillar": pillar["type"],
            "Format": pillar["format"],
            "Content Idea": f"{brand_name} - {pillar['focus']} ({niche})",
            "Call To Action": "ইনবক্স করুন / ওয়েবসাইটে অর্ডার দিন",
            "Status": "Draft"
        }
        calendar.append(entry)
    return calendar

def save_to_csv(calendar, filename):
    keys = calendar[0].keys()
    with open(filename, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(calendar)

def save_to_markdown(calendar, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("# 📅 30-Day Content Calendar - Kajefly\n\n")
        f.write("| Day | Date | Pillar | Format | Content Idea | Status |\n")
        f.write("|-----|------|--------|--------|--------------|--------|\n")
        for row in calendar:
            f.write(f"| {row['Day']} | {row['Date']} | {row['Pillar']} | {row['Format']} | {row['Content Idea']} | {row['Status']} |\n")

def main():
    parser = argparse.ArgumentParser(description="Kajefly Content Calendar Generator")
    parser.add_argument("--brand", default="Demo Brand", help="Client or Brand Name")
    parser.add_argument("--niche", default="F-Commerce Fashion", help="Industry/Niche")
    parser.add_argument("--days", type=int, default=30, help="Number of days")
    parser.add_argument("--out_csv", default="C:/Users/HP/kajefly/content_calendar_30days.csv", help="CSV Output Path")
    parser.add_argument("--out_md", default="C:/Users/HP/kajefly/content_calendar_30days.md", help="Markdown Output Path")
    
    args = parser.parse_args()
    
    cal = generate_calendar(args.brand, args.niche, days=args.days)
    save_to_csv(cal, args.out_csv)
    save_to_markdown(cal, args.out_md)
    print("[SUCCESS] 30-Day Content Calendar generated successfully!")
    print(f"File CSV: {args.out_csv}")
    print(f"File Markdown: {args.out_md}")

if __name__ == "__main__":
    main()
