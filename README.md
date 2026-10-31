# 🚀 Kajefly (কাজেফ্লাই) — ছোট ব্র্যান্ড, বড় উড়ান

> **AI-Powered Digital Growth Micro-Agency for F-Commerce & Local Brands in Bangladesh**

---

## 📂 Project Structure

```
kajefly/
├── index.html                    # Complete modern Agency Landing & Portfolio Website
├── content_calendar_30days.csv   # Auto-generated 30-Day Content Plan (CSV)
├── content_calendar_30days.md    # Formatted 30-Day Content Plan (Markdown)
├── scripts/
│   ├── post_generator.py         # AI Post & Ad Copy Creator (Bengali/English)
│   ├── content_calendar.py       # 30-Day Content Calendar Planner
│   └── lead_finder.py            # Targeted Lead Pitch & Audit Generator
└── assets/
    ├── css/
    ├── js/
    └── images/
```

---

## 🛠️ How to Run Automation Scripts

### 1. Generate Social Media Post / Ad Copy:
```powershell
python scripts/post_generator.py --product "প্রিমিয়াম কটন শার্ট" --niche "FashionBD" --type "product_launch"
```

### 2. Generate 30-Day Content Calendar:
```powershell
python scripts/content_calendar.py --brand "StyleBD" --niche "Boutique & Lifestyle"
```

### 3. Generate Personalized Client Pitch:
```powershell
python scripts/lead_finder.py --brand "Fashionista BD" --person "তানভীর" --type "audit_hook"
```

---

## 🌐 Deploy to GitHub Pages

1. Create a new repository on GitHub (e.g. `kajefly` or `kajefly.github.io`).
2. Run in terminal:
```powershell
git remote add origin https://github.com/<YOUR_USERNAME>/<REPO_NAME>.git
git branch -M main
git push -u origin main
```
3. In GitHub repo settings -> **Pages** -> Source: `main` branch -> **Save**.
Your agency website will be live globally!
