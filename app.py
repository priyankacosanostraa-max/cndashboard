# ============================================================
# COSA NOSTRAA — V23.3 (STABLE FINAL — no-crash build)
# V23.3:
#   • CRASH FIX (512MB OOM): data ab chunks mein process hota hai (full
#     copy nahi banti), sales dataframe kaam khatam hote hi free, bg
#     refresh 10-min interval — RAM peak ~40% kam. Crash band.
#   • EMPLOYEE: MRP wapas dikhega (cards, details, AI, exports) —
#     sirf REVENUE har jagah hidden rahega.
# ============================================================
# COSA NOSTRAA — V23.2 (PRODUCTION FINAL)
# V23.2:
#   • Repeat Orders TRANSACTIONS view: har row par checkbox + select-all
#     (multi-select karke export), Dimensions column table mein bhi.
#   • Product Dimensions ab transactions ke saath hi attach hota hai —
#     export mein 100% aayega (admin + employee dono).
#   • SPEED: /api/data ab per-role serialized+gzipped cache se serve
#     hota hai (10-20x chhota transfer, CPU bachat) — site fast.
#   • SKU Finder: startup self-test (logs mein OK/FAIL turant dikhega)
#     + /api/vision-status diagnostic endpoint.
#   • Saare typing/search inputs: white field + BLACK bold text.
# ============================================================
# COSA NOSTRAA — V23.1 (PRODUCTION / cosanostraamanagement.com)
# V23.1: SKU FINDER ab LITE servers (bina torch, 512MB free tier) par
#   bhi chalta hai — query image ki DINOv2 embedding Hugging Face API
#   se banti hai (HF_TOKEN), catalog matching local numpy se. Torch
#   installed ho to pehle jaisa local mode hi chalega.
# ============================================================
# COSA NOSTRAA — V23 (PRODUCTION / cosanostraamanagement.com)
# NEW in V23:
#   • REAL SERVER-SIDE LOGIN: credentials ab server par verify hote
#     hain (session cookies, 14 din). Public internet par bhi data
#     secure — /api/* bina login ke 401 deta hai. Role spoof-proof.
#     Production par env vars se badlo: ADMIN_USER, ADMIN_PASS,
#     EMP_USER, EMP_PASS, SECRET_KEY.
#   • EMPLOYEE: ab MRP samet HAR ₹ value blocked — server se aata hi
#     nahi, UI me dikhta nahi, AI price/MRP questions refuse karta hai.
#   • DEPLOY-READY: PORT env se; gunicorn compatible; torch/transformers
#     optional (lite server par bhi chalega — visual features gracefully
#     off). DEPLOY=1 par tunnel skip.
#   • SMART INDEX: encoder self-test — agar images download ho gayi par
#     AI encoding fail hui to ab SAHI error dikhega (pehle galat
#     "links failed" aata tha) + exact fix command.
# ============================================================
# COSA NOSTRAA — V22 (OBSIDIAN PRO + EMPLOYEE PRIVACY)
# NEW in V22:
#   • EMPLOYEE ROLE LOCKDOWN: Insights tab hidden; revenue NEVER sent
#     to employee browsers (/api/data strips it server-side); revenue
#     rows removed from cards, SKU details, exports, home stats; AI
#     refuses revenue/sales-value questions for employees and strips
#     revenue from all AI answers, cards and Gemini context.
#   • SMART SEARCH: browser-grade headers (Cloudflare/WordPress hotlink
#     protection pass) + exact per-link failure reasons (HTTP code etc.)
#     shown in the error so root cause turant dikhe.
# ============================================================
# COSA NOSTRAA — V21 (OBSIDIAN PRO)
# NEW in V21:
#   • New login page: floating COSA NOSTRAA watermarks drifting across
#     the screen, dark-glass sign-in card, violet glow.
#   • SMART SEARCH is now its OWN tab (menu -> Smart Search) with a
#     hero header — removed from Repeat Orders.
#   • Index build diagnostics: live downloaded/failed counters, and on
#     failure it tells you exactly whether the server lacks internet
#     or the Drive links are not public (with sample links).
#   • AI upgrades: "Daily briefing" one-shot business report (KPIs,
#     hot SKUs, restock alerts) + smart follow-up suggestion chips
#     after every answer.
#   • Entrance animations: staggered card/KPI reveal, view transitions.
# ============================================================
# COSA NOSTRAA — V20 (OBSIDIAN EDITION)
# NEW in V20:
#   • OBSIDIAN UI: bold modern dark theme — Space Grotesk display,
#     heavy weights everywhere, platinum + violet accents, true 3D
#     depth (layered shadows, hover lift, tilt), clean English copy.
#   • All UI text rewritten in professional English; clutter removed.
#   • SMART SEARCH index fix: Google Drive image links auto-convert
#     to direct URLs (3 variants tried per image) — index ab banega.
#   • Multi-device ready: threaded server + data-refresh lock so 4-5
#     users ek saath chala sakte hain bina atke.
# ============================================================
# COSA NOSTRAA — V19 (ROYAL ATELIER EDITION)
# NEW in V19:
#   • ROYAL ATELIER UI: quiet-luxury redesign — champagne gold +
#     charcoal, Playfair serif display, hairline borders, editorial
#     spacing, refined hovers. Expensive-agency look, zero clutter.
#   • Cloudflare Workers AI credentials configured (design engine #1
#     after Gemini) — FREE ~100+ images/day.
#   • Live sheet sync (cache-busted) from V18 included.
# ============================================================
# COSA NOSTRAA — V18 (3D LUXE + CLOUDFLARE + LIVE SYNC FIX)
# NEW in V18:
#   • LIVE SYNC FIX: Google published-CSV ka CDN cache bypass (cache-
#     buster + no-cache headers + 3 retries) — Sync dabate hi sheet ka
#     LATEST data aayega. Auto-refresh ab 5 min (pehle 15 min tha).
#   • CLOUDFLARE WORKERS AI design engine (FREE ~100+ images/day):
#     CF_ACCOUNT_ID + CF_API_TOKEN bharo (steps line ~22 par likhe hain).
#     Chain: Gemini -> Cloudflare -> Pollinations -> HuggingFace.
# ============================================================
# COSA NOSTRAA — V17 (3D LUXE UI)
# NEW in V17:
#   • Pura UI 3D luxury overhaul: animated ambient background, glass
#     panels (blur), layered depth shadows, 3D hover lift + tilt on
#     KPIs/home cards, shimmer gold headings, Playfair Display serif,
#     neumorphic inputs, glow buttons, slim gold scrollbar.
#   • Saari functionality 100% same — sirf look upgrade.
# ============================================================
# COSA NOSTRAA — V16 (AI STUDIO ULTIMATE)
# NEW in V16:
#   • SMART SEARCH ab 100% OFFLINE: CLIP model text ko seedha aapke
#     catalog images se match karta hai (internet image-gen par koi
#     dependency nahi). Pehli baar "Build Visual Index" dabana hota
#     hai (one-time; clip_index.pkl banta hai — download karke
#     sku_finder.pkl ke saath rakho to dobara nahi banana padega).
#   • Design generation: Gemini -> Pollinations -> HuggingFace (free
#     HF_TOKEN optional, line ~20) — teen engines ki chain.
#   • SKU photo-cards ab sirf tab jab aap SKUs maango (dikhao/kaunse/
#     top/list) ya specific SKU pucho — totals ke saath nahi.
#   • Aur bhi strict concise answers.
# ============================================================
# COSA NOSTRAA — V15 (AI STUDIO ULTRA)
# NEW in V15:
#   • Concise answers — jo poocha sirf wahi (extra stats nahi).
#   • AI FORECASTING (Prophet): "is mahine Website me kitni sale ho
#     sakti hai aur kaunse SKU?" — month-end projection + top SKUs.
#     Best results: Colab mein ek baar  !pip install prophet
#     (bina Prophet ke trend model se kaam chalta hai).
#   • AI answers ke saath ⬇ CSV / ⬇ Excel export buttons.
#   • Repeat Orders par 🔮 SMART SEARCH: "lion" likho to lion wale
#     designs images ke saath — free AI image + DINOv2 visual match.
#   • Free design engine ab zyada robust (retries, 2 models, variants).
# ============================================================
# COSA NOSTRAA — V14 (AI STUDIO PRO MAX + FREE DESIGN ENGINE)
# NEW in V14:
#   • Design generation ka FREE fallback: Pollinations.ai (FLUX) — koi
#     API key nahi chahiye, koi quota nahi. Gemini quota khatam ho ya
#     key na ho, design phir bhi banegi (sirf reference images skip
#     hoti hain free engine mein).
# ============================================================
# COSA NOSTRAA — V13 (AI STUDIO PRO MAX)
# NEW in V13:
#   • Design generation ab Gemini 3 "Nano Banana Pro" use karta hai
#     (gemini-3-pro-image-preview), fallback: Nano Banana (2.5-flash-image)
#     + key par available image models auto-discover hote hain.
#   • SKU cards sirf SKU-related answers ke saath dikhte hain
#     (totals/summary/chat ke saath nahi).
#   • Transaction-level questions: "SOR me June 2025 ka revenue?",
#     "kal kya kya SKU bika?", "aaj ki sale", specific month/date/FY,
#     sales Type (channel) aur customer-wise — sab supported.
# ============================================================
# COSA NOSTRAA — V12 (AI STUDIO PRO)
# NEW in V12:
#   • Follow-up memory: SKU poochne ke baad "last 7 days?", "30 din ka?",
#     "iska revenue?" jaise follow-ups usi SKU par answer hote hain.
#   • 🗑 Clear Chat button.
#   • 🎨 CREATE NEW DESIGN: prompt + (optional) reference SKUs dekar
#     Gemini se naya jewellery design image generate karo — existing
#     best-sellers se style inspiration leta hai. POST /api/ai-design
#     (NOTE: design generation ke liye VALID Gemini key zaroori hai.)
# ============================================================
# COSA NOSTRAA — V11 (AI STUDIO EDITION)
# NEW in this version:
#   1. ✦ AI STUDIO tab — chat assistant (Hinglish) for all dashboard
#      data: top sellers, stock, revenue, SKU details with image cards.
#      Uses Gemini when GEMINI_KEY is valid; otherwise a built-in local
#      query engine answers — so it ALWAYS works.
#      Endpoint: POST /api/ai-chat  {message, history}
#   2. Fixed quote-escaping bug in SKU card onclick handlers.
#   3. Fixed period_kpis tuple index in data unpacking.
# ============================================================
# COSA NOSTRAA — V2 (Overall Details + SKU Finder + Repeat Orders)
# Changes from V1:
#   1. Taxon filter added in Overall Details (from inventory sheet)
#   2. Net Revenue ONLY from COSSA "Net Revenue" column — no calc
#   3. Dispatch Date = primary date
#   4. New "Repeat Orders" tab with 7d/15d/30d qty, forecast
# FIXES: Bulletproof Qty/Rev Parsing + Fuzzy SKU Matching + Unified Grand Totals
# ============================================================

# Path to the cloudflared executable. If it's in the same folder as this
# script (or on your PATH), the defaults below will find it automatically.
# You can also hard-code an absolute path, e.g.:
#   CLOUDFLARED_PATH = r"C:\Users\You\Downloads\cloudflared-windows-386.exe"
CLOUDFLARED_PATH = ""   # leave "" to auto-detect; set to skip detection
USE_TUNNEL  = True      # set False to run local-only (http://localhost:5000)
GEMINI_KEY  = "AQ.Ab8RN6KN6B49A6nKMMeyvQsu8jIs6LMfyTy6ciNA88zSkJ88Pg"
# OPTIONAL free backup for design generation: huggingface.co/settings/tokens
# se FREE token banakar yahan daalo (Read access kaafi hai). Khali bhi chalega.
HF_TOKEN    = "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"
# Apne HF Space ka id (e.g. "username/cosa-embedder") — lite server par
# SKU Finder isi se photo embeddings banata hai. Env var SPACE_ID se override.
# Default pre-filled taaki Render (bina torch) par bhi SKU Finder ON rahe.
SPACE_ID    = "mayuresh2026/cosa-embedder"

# ★ CLOUDFLARE WORKERS AI (FREE, design generation ka main free engine) ★
# Kaise milega:
#  1. dash.cloudflare.com par FREE account banao (sirf email)
#  2. ACCOUNT ID: login ke baad Workers & Pages page kholo — right side
#     mein "Account ID" likha milega (ya browser URL mein bhi hota hai)
#  3. API TOKEN: My Profile (upar right) -> API Tokens -> Create Token ->
#     "Workers AI" template -> Continue -> Create -> token copy karo
#  4. Dono neeche paste karo:
CF_ACCOUNT_ID = "975ea2d6d03cfa63e40b32a683d472df"
CF_API_TOKEN  = "cfut_lYVrtys6IQLlG0P6Db5sQyIesEjEhKxxQoP9LSWb548628c7"

import os, re, io, sys, time, glob, base64, pickle, shutil, threading, subprocess, difflib, uuid, json
import gzip as _gzip_mod
import gc as _gc
from sys import intern as _intern_raw
def _si(v):
    """Repeated chhote strings (customer, type, FY, dates...) ek hi object share karein — RAM bachat."""
    return _intern_raw(v) if isinstance(v, str) and len(v) < 64 else v
_RESP_CACHE = {}
_RESP_LOCK = threading.Lock()
SPACE_ID = os.environ.get("SPACE_ID", SPACE_ID) or SPACE_ID
from datetime import datetime, timedelta, date
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
import requests
# ── PIL optional: image SKU-Finder ke liye; missing ho to boot crash na ho ──
try:
    from PIL import Image
    PIL_AVAILABLE = True
except Exception as _pil_err:
    Image = None
    PIL_AVAILABLE = False
    print("Pillow not installed — image features limited.", str(_pil_err)[:120])
# ── ML stack DISABLED at startup ──
# Render free tier = 512MB. torch/transformers load karne se hi ~300-400MB chala
# jata tha, aur 59k-row data ke saath OOM (502 Bad Gateway) ho raha tha.
# Smart Search / vision SKU-finder UI se hata diya gaya hai, isliye in heavy
# models ki zarurat nahi. Agar kabhi chahiye to ENABLE_ML=1 set kar dena.
ML_AVAILABLE = False
torch = None
AutoImageProcessor = AutoModel = None
if os.environ.get("ENABLE_ML") == "1":
    try:
        import torch
        from transformers import AutoImageProcessor, AutoModel
        ML_AVAILABLE = True
    except Exception as _ml_err:
        torch = None
        AutoImageProcessor = AutoModel = None
        ML_AVAILABLE = False
        print("ML stack not installed — vision disabled.", str(_ml_err)[:120])
# ── google-genai optional: AI Studio + SKU match fallback ──
try:
    from google import genai
    from google.genai import types
    GENAI_AVAILABLE = True
except Exception as _genai_err:
    genai = None
    types = None
    GENAI_AVAILABLE = False
    print("google-genai not installed — AI Studio disabled (baaki sab chalega).",
          str(_genai_err)[:120])
from flask import Flask, request, jsonify, render_template_string, session

# ── Config ───────────────────────────────────────────────────
INV_URL   = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSFHmWRlOplM6iDI4JYJA6gB8UnAJliu-Nuo3av_f2hThuOItMlhhaTA_qiyAo8tbClJLiwsYrC12I-/pub?gid=1511690188&single=true&output=csv"
COSSA_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSFHmWRlOplM6iDI4JYJA6gB8UnAJliu-Nuo3av_f2hThuOItMlhhaTA_qiyAo8tbClJLiwsYrC12I-/pub?gid=1305194055&single=true&output=csv"
# Target sheet (Date, Stake Holder, Channel Type, Qty Target, SP Target)
TARGET_URL = os.environ.get("TARGET_URL", "https://docs.google.com/spreadsheets/d/e/2PACX-1vSFHmWRlOplM6iDI4JYJA6gB8UnAJliu-Nuo3av_f2hThuOItMlhhaTA_qiyAo8tbClJLiwsYrC12I-/pub?gid=1013197730&single=true&output=csv")
# Production / PPC-WIP sheet (A=Date, B=Order No, E=SKU, G=Channel, I=Order Qty,
# J=Recv Qty, K=Balance Qty, L=Delivery Date, M=Receiving Date)
PRODUCTION_URL = os.environ.get("PRODUCTION_URL", "https://docs.google.com/spreadsheets/d/e/2PACX-1vSFHmWRlOplM6iDI4JYJA6gB8UnAJliu-Nuo3av_f2hThuOItMlhhaTA_qiyAo8tbClJLiwsYrC12I-/pub?gid=433995998&single=true&output=csv")


PKL_FILE  = "sku_finder.pkl"
# Agar pkl file server par nahi hai to is link se download hogi (Google Drive
# share link chalega — file ko "Anyone with the link: Viewer" karna zaroori).
# Render par env var PKL_URL set karo ya yahan paste kar do.
PKL_URL   = os.environ.get("PKL_URL", "")

def _ensure_pkl():
    """sku_finder.pkl missing ho to PKL_URL (Drive) se download karo."""
    if os.path.exists(PKL_FILE):
        return True
    url = (PKL_URL or "").strip()
    if not url:
        return False
    m = re.search(r"[-\w]{25,}", url)
    fid = m.group(0) if m else ""
    cands = []
    if fid:
        cands += [f"https://drive.usercontent.google.com/download?id={fid}&export=download&confirm=t",
                  f"https://drive.google.com/uc?export=download&id={fid}&confirm=t"]
    cands.append(url)
    for cu in cands:
        try:
            print("PKL download try:", cu[:90])
            r = requests.get(cu, timeout=300, stream=True,
                             headers={"User-Agent": "Mozilla/5.0"})
            if not r.ok:
                print("  -> HTTP", r.status_code); continue
            first = next(r.iter_content(8192), b"")
            if first[:1] in (b"<", b"{"):          # HTML/JSON mila, file nahi
                print("  -> not a binary file (HTML page mila)"); continue
            with open(PKL_FILE + ".part", "wb") as f:
                f.write(first)
                for chunk in r.iter_content(1 << 20):
                    f.write(chunk)
            os.replace(PKL_FILE + ".part", PKL_FILE)
            sz = os.path.getsize(PKL_FILE)
            print(f"PKL downloaded OK ({sz/1e6:.1f} MB)")
            if sz < 1e6:
                os.remove(PKL_FILE); continue
            return True
        except Exception as e:
            print("  -> failed:", str(e)[:100])
    return False
PORT      = int(os.environ.get("PORT", 5000))
# Deploy/host detect (Render etc.) — yahan se data-load tez karte hain.
DEPLOY_HOST = bool(os.environ.get("DEPLOY") or os.environ.get("RENDER")
                   or os.environ.get("RAILWAY_ENVIRONMENT") or os.environ.get("DYNO")
                   or os.environ.get("PORT"))
# FAST_LOAD: heavy difflib fuzzy SKU-matching skip karo (sabse bada load-time
# kha raha tha — 55k/59k pe atak jata tha). Exact + normalized match phir bhi
# chalega (99% SKUs cover). Managed host par default ON. Env FAST_LOAD=0 se band.
FAST_LOAD = (os.environ.get("FAST_LOAD", "1" if DEPLOY_HOST else "0") == "1")
CACHE_TTL = 900   # bg refresher (600s) hamesha pehle chal jata hai — users ko inline refresh kabhi nahi jhelni padti
TZ        = ZoneInfo("Asia/Kolkata")

CACHE    = {"data": None, "ts": 0, "debug": {}}
UPLOAD_REPORTS = {}
AI_READY = False
db_data, processor, dino_model, client = None, None, None, None

MARKETPLACE_CACHE = {"data": None, "ts": 0, "error": None}
MARKETPLACE_TTL = 300
MYNTRA_MERCHANT_ID = "K81WKJ4N"
MYNTRA_SECRET_KEY = "d7y4YD2rx1ZXOIY8czG2mxXDEzspTLFgJkqEak"
MYNTRA_WAREHOUSE_CODE = "cosanostraa"

MYNTRA_PORTAL_BASE_URL  = "https://partners.myntrainfo.com/"
MYNTRA_PORTAL_REPORT_URL = "https://partners.myntrainfo.com/Reports/ops-reports"
MYNTRA_PORTAL_COOKIE     = os.getenv("MYNTRA_PORTAL_COOKIE", os.getenv("MYNTRA_PORTAL_COOKIES", ""))
MYNTRA_PORTAL_USER       = os.getenv("MYNTRA_PORTAL_USER", "")
MYNTRA_PORTAL_PASS       = os.getenv("MYNTRA_PORTAL_PASS", "")

# ── Helpers ──────────────────────────────────────────────────
def now_ist():
    return datetime.now(TZ)

def fy_bounds(dt=None):
    dt = dt or now_ist()
    year  = dt.year if dt.month >= 4 else dt.year - 1
    start = datetime(year,   4,  1, tzinfo=TZ)
    end   = datetime(year+1, 3, 31, 23, 59, 59, tzinfo=TZ)
    label = f"FY {year}-{str(year+1)[-2:]}"
    return label, start, end

def prev_fy_label(label):
    m = re.search(r"FY\s*(\d{4})-(\d{2})", label or "")
    if not m: return ""
    y = int(m.group(1)) - 1
    return f"FY {y}-{str(y+1)[-2:]}"

def norm_fy(v):
    s = clean(v, "")
    if not s:
        return ""
    m = re.search(r"(\d{2,4})\s*[-/]\s*(\d{2,4})", s)
    if not m:
        return ""
    y1 = int(m.group(1)); y2 = m.group(2)
    if y1 < 100: y1 += 2000          # 24 -> 2024
    return f"FY {y1}-{str(y1+1)[-2:]}"

def clean(v, default=""):
    if v is None: return default
    s = str(v).strip()
    if s.lower() in ("nan","none","","na","n/a","-"): return default
    return s

def to_num(v):
    # Highly robust number extraction that ignores text/currency like "12 pcs" or "₹1,000"
    if v is None: return 0.0
    if isinstance(v,(int,float)):
        if isinstance(v,float) and (np.isnan(v) or np.isinf(v)): return 0.0
        return float(v)
    s = str(v).strip().lower()
    if s in ("nan","none","","na","n/a","-","nil","null"): return 0.0
    s = s.replace(",", "")  # Remove comma for parsing thousands correctly
    m = re.search(r"[-+]?\d*\.?\d+", s)
    try: return float(m.group()) if m else 0.0
    except: return 0.0

def to_int(v): return int(round(to_num(v)))

def parse_date_any(v):
    if v is None: return None
    if isinstance(v, pd.Timestamp):
        if pd.isna(v): return None
        return v.to_pydatetime().replace(tzinfo=None)
    s = str(v).strip()
    if s.lower() in ("nan","none","","na","n/a","-"): return None

    try:
        fv = float(s)
        if 30000 <= fv <= 60000:
            dt = pd.to_datetime(fv, unit="D", origin="1899-12-30", errors="coerce")
            if not pd.isna(dt): return dt.to_pydatetime().replace(tzinfo=None)
    except: pass

    m_iso = re.match(r"^(\d{4})[-/](\d{1,2})[-/](\d{1,2})", s)
    if m_iso:
        try:
            y, mo, d = int(m_iso.group(1)), int(m_iso.group(2)), int(m_iso.group(3))
            return datetime(y, mo, d)
        except: pass

    m_dmy = re.match(r"^(\d{1,2})[-/](\d{1,2})[-/](\d{2,4})", s)
    if m_dmy:
        d, mo, y = int(m_dmy.group(1)), int(m_dmy.group(2)), int(m_dmy.group(3))
        if y < 100: y += 2000
        try:
            if 1 <= d <= 31 and 1 <= mo <= 12:
                return datetime(y, mo, d)
        except: pass

    for dayfirst in (True, False):
        try:
            dt = pd.to_datetime(s, errors="coerce", dayfirst=dayfirst)
            if not pd.isna(dt): return dt.to_pydatetime().replace(tzinfo=None)
        except: pass
    return None

def base_sku(s): return str(s).strip().upper().split("_")[0]

_TYPE_CANON = {}
_TAXON_CANON = {}
_CUST_CANON = {}

def _canon(v, store, default, title=True):
    s = clean(v, default)
    k = re.sub(r"[^a-z0-9]", "", s.lower())
    if not k:
        return default
    if k not in store:
        store[k] = s.strip().title() if title else s.strip()
    return store[k]

def norm_type(v):  return _canon(v, _TYPE_CANON,  "Regular")

_TAXON_ALIASES = {
    "cufflink":  "Cufflinks",
    "cufflinks": "Cufflinks",
    "bangal":    "Bangle",
    "bangle":    "Bangle",
    "earring":   "Earrings",
    "earrings":  "Earrings",
    "eartop":    "Earrings",
    "eartops":   "Earrings",
}
def norm_taxon(v):
    s = clean(v, "General")
    k = re.sub(r"[^a-z0-9]", "", s.lower())
    if not k:
        return "General"
    if k in _TAXON_ALIASES:
        return _TAXON_ALIASES[k]
    return _canon(v, _TAXON_CANON, "General")

def norm_cust(v):  return _canon(v, _CUST_CANON,  "Unknown", title=False)

def find_col(cols, *cands):
    norm = {re.sub(r"[^a-z0-9]","", str(c).lower()): c for c in cols}
    for cand in cands:
        k = re.sub(r"[^a-z0-9]","", cand.lower())
        if k in norm: return norm[k]
    for cand in cands:
        k = re.sub(r"[^a-z0-9]","", cand.lower())
        for nk, orig in norm.items():
            if k and k in nk: return orig
    return None

def classify_status(item, current_month_key=""):
    # Koi dispatch hi nahi hui (COSSA me record nahi) → "No Record"
    if item["dispatch_count"] == 0:
        return "No Record"
    # "New Launch" = sirf wahi jo IS MAHINE launch hua (launch date se).
    if current_month_key and item.get("launch_key") == current_month_key:
        return "New Launch"
    total_inv = item["inv_stock"] + item["inv_wip"]
    if total_inv >= 20 and item["qty_6m"] == 0: return "Slow Movers"
    return "Good Running"


def simple_forecast(entries, days_ahead=30):
    """Expected DEMAND (units) in the next `days_ahead` days.

    Criteria (velocity-based, recent-weighted):
      • Recent rate (last 60 din) ko 70% weight, lambe rate (last 180 din) ko
        30% weight — taaki recent maang zyada bole par purana bhi count ho.
      • Agar recent data nahi to overall avg daily rate.
      • Trend (OLS slope) thoda upar/niche adjust karta hai (max ±25%).
    Yeh "next 30 days me kitna bikega" batata hai (reorder iske upar banta hai).
    """
    if not entries:
        return 0
    dated = [(e["date"], e["qty"]) for e in entries if e.get("date") and e["date"] != "N/A"]
    if not dated:
        return 0
    today = now_ist().date()
    def _d(iso):
        try: return date(int(iso[0:4]), int(iso[5:7]), int(iso[8:10]))
        except Exception: return None

    q60 = q180 = q_all = 0.0
    first = None
    for iso, qty in dated:
        dd = _d(iso)
        if dd is None:
            continue
        age = (today - dd).days
        if age < 0:
            age = 0
        q_all += qty
        if age <= 60:  q60  += qty
        if age <= 180: q180 += qty
        if first is None or dd < first:
            first = dd

    rate60  = q60  / 60.0
    rate180 = q180 / 180.0
    # blended daily rate (recent weighted)
    if q60 > 0 or q180 > 0:
        daily = 0.70 * rate60 + 0.30 * rate180
    else:
        span_days = max(1, (today - first).days) if first else 1
        daily = q_all / span_days

    base = daily * days_ahead

    # Halka trend nudge (max ±25%): weekly OLS slope ka sign/strength.
    from collections import defaultdict
    weekly = defaultdict(float)
    ref_ord = date(2020, 1, 1).toordinal()
    for iso, qty in dated:
        dd = _d(iso)
        if dd is None:
            continue
        weekly[(dd.toordinal() - ref_ord) // 7] += qty
    if len(weekly) >= 3:
        xs = np.array(sorted(weekly.keys()), dtype=float)
        ys = np.array([weekly[x] for x in xs], dtype=float)
        xm, ym = xs.mean(), ys.mean()
        slope = np.sum((xs - xm) * (ys - ym)) / (np.sum((xs - xm) ** 2) + 1e-9)
        if ym > 0:
            nudge = max(-0.25, min(0.25, (slope / ym)))
            base *= (1.0 + nudge)

    return max(0, int(round(base)))


# ── Data Engine ──────────────────────────────────────────────
def _fetch_csv_fresh(url):
    """Google published-CSV ko Google ~5 min CDN-cache karta hai — cache-buster
    param + no-cache headers se hamesha LATEST data milta hai."""
    bust = ("&" if "?" in url else "?") + f"cachebust={int(time.time()*1000)}"
    headers = {"Cache-Control": "no-cache, no-store, max-age=0",
               "Pragma": "no-cache",
               "User-Agent": "Mozilla/5.0 (CosaNostraaDashboard)"}
    last_err = None
    for attempt in range(3):
        try:
            r = requests.get(url + bust, headers=headers, timeout=45, allow_redirects=True)
            r.raise_for_status()
            txt = r.content.decode("utf-8", errors="replace")
            if "<html" in txt[:200].lower():
                raise ValueError("Received HTML instead of CSV — re-check the sheet's Publish-to-web setting")
            return pd.read_csv(io.StringIO(txt), dtype=str, on_bad_lines="skip")
        except Exception as e:
            last_err = e
            time.sleep(2)
    raise last_err

_DATA_LOCK = threading.Lock()
_DF_REFS = {}

def _df_chunks(df, size=4000):
    """DataFrame ko chhote-chhote dict-chunks mein iterate karo —
    poora .to_dict('records') ek saath banane se RAM double ho rahi thi."""
    n = len(df)
    for start in range(0, n, size):
        for rec in df.iloc[start:start + size].to_dict("records"):
            yield rec

_WARMUP = {"stage": "idle", "detail": "", "done": 0, "total": 0}

def _wstage(stage, detail="", done=0, total=0):
    _WARMUP.update({"stage": stage, "detail": detail, "done": done, "total": total})

def _malloc_trim():
    """Linux par Python freed memory ko hamesha OS ko wapas nahi karta —
    glibc malloc_trim se RSS actually neeche aata hai (512MB tier ke liye zaroori)."""
    try:
        import ctypes
        ctypes.CDLL("libc.so.6").malloc_trim(0)
    except Exception:
        pass

def _free_dataframes():
    """Raw pandas frames ko refresh ke turant baad free karo (100MB+ bachat)."""
    try:
        _DF_REFS.clear()
        _gc.collect()
        _malloc_trim()
    except Exception:
        pass

def get_data(force=False):
    global CACHE
    if not force and CACHE["data"] and (time.time() - CACHE["ts"] < CACHE_TTL):
        return CACHE["data"]
    # multi-device: ek hi waqt par ek hi refresh chale, baaki cached serve karein
    if not _DATA_LOCK.acquire(blocking=False):
        with _DATA_LOCK:
            pass
        if CACHE["data"]:
            return CACHE["data"]
        _DATA_LOCK.acquire()
    try:
        # Purana data ko None mat karo jab tak naya ready na ho — warna refresh
        # ke beech /api/data ko data None milta tha aur site reload-loop me ja
        # rahi thi. _refresh_data() khud CACHE ko atomically set karta hai.
        _prev = CACHE.get("data")
        try:
            result = _refresh_data()
        except Exception:
            CACHE["data"] = _prev      # fail ho to purana wapas
            raise
        finally:
            _prev = None
        _gc.collect()
        _free_dataframes()
        return result
    finally:
        _DATA_LOCK.release()

def _refresh_data():
    global CACHE
    dbg = {"errors": []}
    try:
        _wstage("fetching", "Downloading inventory sheet…")
        inv   = _fetch_csv_fresh(INV_URL)
        _wstage("fetching", "Downloading sales sheet (54k rows)…")
        cossa = _fetch_csv_fresh(COSSA_URL)
        _DF_REFS["inv"] = inv; _DF_REFS["cossa"] = cossa
        inv.columns   = [str(c).strip() for c in inv.columns]
        cossa.columns = [str(c).strip() for c in cossa.columns]
    except Exception as e:
        dbg["errors"].append(f"load: {e}")
        CACHE["debug"] = dbg
        return [], [], [], [], [], [], [], "", "", "", "", "", 0.0, 0.0, {"total":0,"yesterday":0,"this_month":0,"this_fy":0,"prev_fy":0}

    dbg["inv_cols"]   = list(inv.columns)
    dbg["cossa_cols"] = list(cossa.columns)

    # ── Inventory columns ────────────────────────────────────
    I_SKU = find_col(inv.columns, "SKU") or inv.columns[0]
    I_IMG = find_col(inv.columns, "Image Link","imagelink") or find_col(inv.columns,"image","img")
    I_MRP  = find_col(inv.columns, "MRP", "mrp", "m.r.p")
    I_COST = find_col(inv.columns, "Cost", "cost", "product cost", "hi cost", "item cost") \
             or (inv.columns[12] if len(inv.columns) > 12 else None)   # fallback → M column
    I_TAX = find_col(inv.columns, "Taxon","category","collection")
    I_PLT = find_col(inv.columns, "Plating","finish","metal")
    I_DIM = find_col(inv.columns, "Product Dimensions","Dimensions","Dimension","Size")
    I_LNCH = find_col(inv.columns, "Launch Date","Launching Date","Launch","Launched")
    I_STONE = find_col(inv.columns, "Stone Details","Stone Detail","Remarks","Remark","combo","combo sku","combo skus","combo_skus","stone")
    I_PACK  = find_col(inv.columns, "Pack Details","Pack Detail","Packing Details","Packing","Pack")
    stk_cands = [c for c in inv.columns if "inv" in c.lower() and "stock" in c.lower()
                 and "3p" not in c.lower() and "web" not in c.lower() and "myntr" not in c.lower()]
    I_STK = stk_cands[0] if stk_cands else find_col(inv.columns,"Inv. Stock","stock")
    wip_exact = [c for c in inv.columns if re.sub(r"[^a-z0-9]","",c.lower()) == "invwip"]
    if wip_exact:
        I_WIP = wip_exact[0]
    else:
        wip_cands = [c for c in inv.columns if "wip" in c.lower()
                     and "website" not in c.lower() and "designer" not in c.lower()
                     and "customer" not in c.lower() and "sor" not in c.lower()]
        I_WIP = wip_cands[0] if wip_cands else find_col(inv.columns,"Inv (WIP)","wip")

    # Channel-specific WIP columns
    def _find_wip_col(keywords):
        for c in inv.columns:
            cl = c.lower()
            if "wip" in cl and all(k in cl for k in keywords):
                return c
        return None

    I_WIP_WEBSITE  = _find_wip_col(["website"]) or find_col(inv.columns,"WIP (Website Repeat)","wip website","website wip")
    I_WIP_DESIGNER = _find_wip_col(["designer"]) or find_col(inv.columns,"WIP (Designer)","wip designer","designer wip")
    I_WIP_CUSTOMER = _find_wip_col(["customer"]) or find_col(inv.columns,"WIP (Customer)","wip customer","customer wip")
    # SOR WIP — some sheets may have a dedicated SOR WIP column; fallback to None
    I_WIP_SOR = _find_wip_col(["sor"]) or find_col(inv.columns,"WIP (SOR)","wip sor","sor wip")

    # Blocked Qty (column U = index 20). Naam pehle, warna position.
    _inv_cols = list(inv.columns)
    def _inv_at(i): return _inv_cols[i] if len(_inv_cols) > i else None
    I_BLOCKED = (find_col(inv.columns, "Blocked Qty", "blocked qty", "blocked", "block qty")
                 or _inv_at(20))

    # ── COSSA columns ────────────────────────────────────────
    cols = list(cossa.columns)
    def _at(idx): return cols[idx] if len(cols) > idx else None

    C_DATE  = _at(0)  or find_col(cossa.columns, "Dispatch Date","date")
    C_FY    = _at(1)  or find_col(cossa.columns, "FY Year","fy","financial year")
    C_SKU   = _at(2)  or find_col(cossa.columns, "SKU","item code") or cols[0]
    # G (index 6) = Final Qty (confirmed layout). Header-match pehle "Final Qty"
    # par exact, warna column G. (Sirf "qty" match karne se "Total Qty"=E pakad
    # leta tha — isliye exact "Final Qty" + fixed index G hi bharosemand hai.)
    C_QTY   = (find_col(cossa.columns, "Final Qty","final quantity","final_qty")
               or _at(6) or find_col(cossa.columns, "qty","quantity") or _at(5))
    # F = Return Qty (index 5)
    C_RET   = find_col(cossa.columns, "Return Qty","return qty","returns","returned qty") or _at(5)
    # H = Selling Price (per-unit SP recorded in COSSA), I = Net Revenue
    C_SP    = find_col(cossa.columns, "Selling Price","selling price","sp","unit price") or _at(7)
    C_REV   = _at(8)  or find_col(cossa.columns, "Net Revenue","net rev","revenue")
    C_CUST  = _at(9)  or find_col(cossa.columns, "Customer Name","customer","client","party")
    C_TYPE  = _at(10) or find_col(cossa.columns, "Type","channel","mode")

    dbg["resolved"] = {
        "inv":   {"sku":I_SKU,"stock":I_STK,"wip":I_WIP,"mrp":I_MRP,"img":I_IMG,"tax":I_TAX,"plt":I_PLT,"combo":I_STONE},
        "cossa": {"sku":C_SKU,"qty":C_QTY,"revenue":C_REV,"date":C_DATE,"fy":C_FY,"cust":C_CUST,"type":C_TYPE},
    }

    # Extract all valid known Inventory SKUs for fuzzy matching fallback
    _wstage("processing", "Indexing inventory SKUs…")
    inv_skus_map = {}
    for r in _df_chunks(inv):
        raw_inv = clean(r.get(I_SKU,"")) if I_SKU else ""
        if raw_inv:
            # Map normalized alphanumeric string to standard uppercase SKU
            n_key = re.sub(r'[^A-Z0-9]', '', raw_inv.upper())
            if n_key not in inv_skus_map:
                inv_skus_map[n_key] = raw_inv.upper()

    sales_exact = {}
    custs, types_, fyears = set(), set(), set()
    _TYPE_CANON.clear(); _TAXON_CANON.clear(); _CUST_CANON.clear()

    # Unified Grand Totals logic: Everything aggregates line-by-line
    grand_net_revenue = 0.0
    grand_final_qty   = 0.0
    kpi_yesterday = kpi_month = kpi_fy = kpi_prev_fy = 0.0

    today_dt = now_ist().replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
    yest_dt  = today_dt - timedelta(days=1)
    cm_start = today_dt.replace(day=1)
    fy_label_cur, fy_start_cur, fy_end_cur = fy_bounds(now_ist())
    fy_label_prev = prev_fy_label(fy_label_cur)
    fy_start_cur_n = fy_start_cur.replace(tzinfo=None)
    fy_end_cur_n   = fy_end_cur.replace(tzinfo=None)

    # ── Last full month vs SAME month last year (month-on-month YoY) ──
    lm_end   = cm_start - timedelta(days=1)        # last day of previous month
    lm_start = lm_end.replace(day=1)               # first day of previous month
    lm_key   = lm_start.strftime("%Y-%m")
    lm_label = lm_start.strftime("%b %Y")
    ly_start = lm_start.replace(year=lm_start.year - 1)
    ly_key   = ly_start.strftime("%Y-%m")
    ly_label = ly_start.strftime("%b %Y")
    kpi_last_month = kpi_last_year_month = 0.0

    _fuzzy_cache = {}
    # SPEED: prefix buckets — fuzzy sirf same-prefix SKUs par chale (10k -> ~50 candidates)
    _prefix_buckets = {}
    for _k in inv_skus_map.keys():
        _prefix_buckets.setdefault(_k[:4], []).append(_k)
    _n_rows = len(cossa)
    for _ri, r in enumerate(_df_chunks(cossa)):
        if (_ri % 2500) == 0:
            _wstage("processing", "Matching sales records…", _ri, _n_rows)
        qty = to_num(r.get(C_QTY, 0)) if C_QTY else 0.0
        rev = to_num(r.get(C_REV, 0)) if C_REV else 0.0
        sp  = to_num(r.get(C_SP, 0))  if C_SP  else 0.0   # per-unit Selling Price (COSSA col H)
        ret = to_num(r.get(C_RET, 0)) if C_RET else 0.0   # Return Qty (COSSA col F)

        # SANITY: ek order ki qty itni badi nahi ho sakti. Agar koi cell me galti
        # se bada number/ID/date aa gaya (galat column), to use 0 maan lo — warna
        # Total Final Qty kharab (10^16 jaisa) ho jata tha.
        if not (-100000 <= qty <= 100000): qty = 0.0
        if not (-100000 <= ret <= 100000): ret = 0.0

        grand_final_qty += qty
        grand_net_revenue += rev

        dt = parse_date_any(r.get(C_DATE,"")) if C_DATE else None
        date_iso = dt.strftime("%Y-%m-%d") if dt else "N/A"
        
        # FY logic
        fy = norm_fy(r.get(C_FY,"")) if C_FY else ""
        if not fy:
            fy = fy_bounds(dt if dt else now_ist())[0] if dt else "N/A"
        
        # Period KPIs (Aggregated across ALL rows, even without SKU)
        if dt is not None:
            d0 = dt.replace(hour=0, minute=0, second=0, microsecond=0)
            if d0 == yest_dt:
                kpi_yesterday += rev
            if cm_start <= d0 <= today_dt.replace(hour=23, minute=59, second=59):
                kpi_month += rev
            mk = d0.strftime("%Y-%m")
            if mk == lm_key: kpi_last_month += rev
            if mk == ly_key: kpi_last_year_month += rev

        if fy != "N/A":
            if fy == fy_label_cur: kpi_fy += rev
            elif fy == fy_label_prev: kpi_prev_fy += rev
        elif dt is not None:
            if fy_start_cur_n <= dt <= fy_end_cur_n: kpi_fy += rev

        raw_sku = clean(r.get(C_SKU,"")) if C_SKU else ""
        if not raw_sku: continue
        
        # ── Fuzzy + Alphanumeric Match ──
        n_key = re.sub(r'[^A-Z0-9]', '', raw_sku.upper())
        mapped_sku = raw_sku.upper()  # Default exactly as it is

        if n_key in inv_skus_map:
            mapped_sku = inv_skus_map[n_key]
        elif FAST_LOAD:
            # FAST: difflib fuzzy skip — exact/normalized match na mile to raw
            # key hi use karo. Yeh 55k/59k wala atakna khatam karta hai.
            mapped_sku = raw_sku.upper()
        else:
            # SPEED: fuzzy result memoized — same SKU baar-baar fuzzy nahi chalti
            # (54k rows x 10k keys ka difflib hi pehle minutes kha raha tha)
            cached = _fuzzy_cache.get(n_key)
            if cached is not None:
                mapped_sku = cached
            else:
                cands = _prefix_buckets.get(n_key[:4]) or []
                matches = difflib.get_close_matches(n_key, cands, n=1, cutoff=0.8) if cands else []
                mapped_sku = inv_skus_map[matches[0]] if matches else raw_sku.upper()
                _fuzzy_cache[n_key] = mapped_sku
        
        cust = norm_cust(r.get(C_CUST,"Unknown")) if C_CUST else "Unknown"
        typ  = norm_type(r.get(C_TYPE,"Regular")) if C_TYPE else "Regular"

        # Type = Website ke orders me asli customer naam (D2C buyers) nahi dikhana —
        # uski jagah "Website" hi customer ke roop me aaye.
        if str(typ).strip().lower() == "website":
            cust = "Website"

        custs.add(cust); types_.add(typ)
        if fy != "N/A": fyears.add(fy)

        # Return amount = return qty × us transaction ki selling price (COSSA F × H)
        entry = {"qty":qty,"rev":rev,"sp":sp,"ret":ret,"ret_amt":float(ret*sp),
                 "date":_si(date_iso),"cust":_si(cust),"type":_si(typ),"fy":_si(fy)}
        
        if mapped_sku not in sales_exact: sales_exact[mapped_sku] = {"entries":[],"total_rev":0.0}
        sales_exact[mapped_sku]["entries"].append(entry)
        sales_exact[mapped_sku]["total_rev"] += rev

    # MEMORY: sales dataframe ka kaam khatam — turant free (60-120MB bachat)
    try:
        del cossa
        _DF_REFS.pop("cossa", None)
        _gc.collect()
    except Exception:
        pass

    _lm = float(kpi_last_month); _ly = float(kpi_last_year_month)
    _yoy = round(((_lm - _ly) / _ly * 100), 1) if _ly else None
    period_kpis = {
        "total":      grand_net_revenue,
        "yesterday":  float(kpi_yesterday),
        "this_month": float(kpi_month),
        "this_fy":    float(kpi_fy),
        "prev_fy":    float(kpi_prev_fy),
        "fy_current_label": fy_label_cur,
        "fy_prev_label":    fy_label_prev,
        "last_month":            _lm,
        "last_month_label":      lm_label,
        "last_year_month":       _ly,
        "last_year_month_label": ly_label,
        "mom_yoy_pct":           _yoy,
    }
    
    dbg["grand_net_revenue"] = grand_net_revenue
    dbg["grand_final_qty"]   = grand_final_qty

    # ── Compile inventory items ──────────────────────────────
    compiled  = []
    sku_list  = []
    taxons, platings = set(), set()
    today = now_ist()
    d7   = today - timedelta(days=7)
    d15  = today - timedelta(days=15)
    d30  = today - timedelta(days=30)
    d90  = today - timedelta(days=90)
    d180 = today - timedelta(days=180)
    d365 = today - timedelta(days=365)

    def qty_since(entries, dt_cutoff):
        total = 0.0
        for e in entries:
            if e["date"] == "N/A": continue
            try:
                if datetime.strptime(e["date"],"%Y-%m-%d").replace(tzinfo=TZ) >= dt_cutoff:
                    total += e["qty"]
            except: pass
        return int(round(total))

    # SPEED: date windows ko ISO strings me badlo — har entry par strptime ke
    # bajay sirf string-compare (YYYY-MM-DD lexical compare = date compare).
    # Yeh "Compiling products" wala atakna hata deta hai (10k SKU x N entries
    # x 6 windows ka strptime hi pure load tha).
    s7   = d7.strftime("%Y-%m-%d")
    s15  = d15.strftime("%Y-%m-%d")
    s30  = d30.strftime("%Y-%m-%d")
    s90  = d90.strftime("%Y-%m-%d")
    s180 = d180.strftime("%Y-%m-%d")
    s365 = d365.strftime("%Y-%m-%d")
    yest_s = (today - timedelta(days=1)).strftime("%Y-%m-%d")
    month_s = today.strftime("%Y-%m")

    fy_current, _, _ = fy_bounds(today)
    fy_previous = prev_fy_label(fy_current)

    def _agg_entries(ent):
        """Ek hi pass me saare per-SKU numbers — qty windows, rev windows,
        totals, first/last date, customers. String compare, zero strptime."""
        q7=q15=q1m=q3m=q6m=q1y=0.0
        tot_rev=tot_qty=0.0
        tot_ret=tot_ret_amt=0.0
        rev_y=rev_m=rev_fy=rev_pfy=0.0
        custs=set()
        first_d=None; last_d=None
        for e in ent:
            d=e["date"]; q=e["qty"]; rv=e["rev"]
            tot_rev+=rv; tot_qty+=q
            tot_ret += e.get("ret") or 0
            tot_ret_amt += e.get("ret_amt") or 0
            custs.add(e["cust"])
            if e["fy"]==fy_current: rev_fy+=rv
            elif e["fy"]==fy_previous: rev_pfy+=rv
            if d!="N/A":
                if d>=s7:   q7+=q
                if d>=s15:  q15+=q
                if d>=s30:  q1m+=q
                if d>=s90:  q3m+=q
                if d>=s180: q6m+=q
                if d>=s365: q1y+=q
                if d==yest_s: rev_y+=rv
                if d.startswith(month_s): rev_m+=rv
                if first_d is None or d<first_d: first_d=d
                if last_d is None or d>last_d: last_d=d
        return {
            "q7":int(round(q7)),"q15":int(round(q15)),"q1m":int(round(q1m)),
            "q3m":int(round(q3m)),"q6m":int(round(q6m)),"q1y":int(round(q1y)),
            "tot_rev":tot_rev,"tot_qty":int(round(tot_qty)),
            "tot_ret":int(round(tot_ret)),"tot_ret_amt":tot_ret_amt,
            "rev_y":rev_y,"rev_m":rev_m,"rev_fy":rev_fy,"rev_pfy":rev_pfy,
            "ncust":len(custs),"first":first_d or "N/A","last":last_d or "N/A",
        }

    seen_skus = set()
    _n_inv = len(inv)
    for _ii, r in enumerate(_df_chunks(inv, 2500)):
        if (_ii % 1500) == 0:
            _wstage("processing", "Compiling products…", _ii, _n_inv)
        raw = clean(r.get(I_SKU,"")) if I_SKU else ""
        if not raw: continue
        
        dedupe_key = raw.strip().upper()
        if dedupe_key in seen_skus:
            continue
        seen_skus.add(dedupe_key)
        sku_list.append(raw)

        taxon = norm_taxon(r.get(I_TAX,"General")) if I_TAX else "General"
        plat  = clean(r.get(I_PLT,"N/A"),"N/A")        if I_PLT else "N/A"
        dims  = clean(r.get(I_DIM,""))                  if I_DIM else ""
        # Launch Date — kisi bhi format mein ho, robust parse
        launch_key, launch_label, launch_iso = "", "", ""
        if I_LNCH:
            _lv = r.get(I_LNCH, "")
            if _lv is not None and str(_lv).strip() and str(_lv).strip().lower() not in ("nan", "na", "n/a", "-", "none"):
                _sv = str(_lv).strip()
                _ld = pd.NaT
                if re.match(r"^\d{4}[-/]\d{1,2}([-/]\d{1,2})?$", _sv):
                    _ld = pd.to_datetime(_sv, errors="coerce")          # ISO yyyy-mm(-dd)
                if pd.isna(_ld):
                    _ld = pd.to_datetime(_sv, dayfirst=True, errors="coerce")
                if pd.isna(_ld):
                    _ld = pd.to_datetime(_sv, dayfirst=False, errors="coerce")
                if not pd.isna(_ld):
                    launch_iso   = _ld.strftime("%Y-%m-%d")
                    launch_key   = _ld.strftime("%Y-%m")
                    launch_label = _ld.strftime("%B %Y")
        img   = clean(r.get(I_IMG,""))                  if I_IMG else ""
        stk   = to_int(r.get(I_STK,0))                 if I_STK else 0
        wip   = to_int(r.get(I_WIP,0))                 if I_WIP else 0
        wip_website  = to_int(r.get(I_WIP_WEBSITE,0))  if I_WIP_WEBSITE  else 0
        wip_designer = to_int(r.get(I_WIP_DESIGNER,0)) if I_WIP_DESIGNER else 0
        wip_customer = to_int(r.get(I_WIP_CUSTOMER,0)) if I_WIP_CUSTOMER else 0
        wip_sor      = to_int(r.get(I_WIP_SOR,0))      if I_WIP_SOR      else 0
        blocked      = to_int(r.get(I_BLOCKED,0))       if I_BLOCKED      else 0
        mrp   = to_num(r.get(I_MRP,0))                 if I_MRP  else 0.0
        cost  = to_num(r.get(I_COST,0))                if I_COST else 0.0

        sd  = sales_exact.get(dedupe_key, {"entries": [], "total_rev": 0.0})
        ent = sd["entries"]

        # Selling Price = COSSA col H ka ACTUAL value (latest dated non-zero).
        _sps = [float(e.get("sp") or 0) for e in ent if float(e.get("sp") or 0) > 0]
        avg_sp  = round(sum(_sps) / len(_sps), 2) if _sps else 0.0
        last_sp = 0.0
        _dated_nz = sorted(
            [e for e in ent if e.get("date") not in (None, "N/A") and float(e.get("sp") or 0) > 0],
            key=lambda e: e["date"]
        )
        if _dated_nz:
            last_sp = float(_dated_nz[-1].get("sp") or 0)
        elif _sps:
            last_sp = _sps[-1]

        A = _agg_entries(ent)   # ek hi pass me saare numbers

        item = {
            "sku":         raw,
            "image_url":   img,
            "inv_stock":   stk,
            "inv_wip":     wip,
            "inv_wip_website":  wip_website,
            "inv_wip_designer": wip_designer,
            "inv_wip_customer": wip_customer,
            "inv_wip_sor":      wip_sor,
            "blocked_qty":      blocked,
            "total_inv":   stk + wip,
            "mrp":         mrp,
            "cost":        cost,
            "avg_selling_price":  avg_sp,
            "last_selling_price": last_sp,
            "taxon":       _si(taxon),
            "plating":     _si(plat),
            "dimensions":  _si(dims),
            "launch_date":  _si(launch_iso),
            "launch_key":   _si(launch_key),
            "launch_month": _si(launch_label),
            "combo_skus":   clean(r.get(I_STONE,"")) if I_STONE else "",
            "pack_details": clean(r.get(I_PACK,""))  if I_PACK  else "",
            "sales_entries": ent,
            "total_net_revenue": float(A["tot_rev"]),
            "final_qty":   A["tot_qty"],
            "return_qty":   A["tot_ret"],
            "return_amount": float(A["tot_ret_amt"]),
            "customer_count": A["ncust"],
            "qty_7d":  A["q7"],
            "qty_15d": A["q15"],
            "qty_1m":  A["q1m"],
            "qty_3m":  A["q3m"],
            "qty_6m":  A["q6m"],
            "qty_1y":  A["q1y"],
            "rev_yesterday": A["rev_y"],
            "rev_month":     A["rev_m"],
            "rev_fy":        A["rev_fy"],
            "rev_prev_fy":   A["rev_pfy"],
            "dispatch_count": len(ent),
            "first_dispatch_date": A["first"],
            "last_dispatch_date":  A["last"],
            "forecast_30d": simple_forecast(ent, 30),
            "status": "",
        }
        # Reorder Qty = next 60 din ki expected demand (production lead-time cover)
        # minus jo already available hai (stock + WIP). 0 se neeche nahi.
        _avail = (item["inv_stock"] or 0) + (item["inv_wip"] or 0)
        _demand60 = simple_forecast(ent, 60)
        item["forecast_60d"] = _demand60
        item["reorder_qty"]  = max(0, int(round(_demand60 - _avail)))
        item["status"] = classify_status(item, month_s)
        compiled.append(item)
        taxons.add(taxon)
        if plat != "N/A": platings.add(plat)

    # ── COMBO/GIFT-SET enrichment ──
    # Stone Details (combo_skus) me jo SKUs likhe hain, un sabki Inv Stock + WIP
    # nikaal ke saath jod do. Gift Set / combo SKUs me ye details dikhengi.
    # WIP channel-wise bhi store hoti hai taaki Type filter par us channel ki
    # WIP dikhe (Website/SOR/Designer), warna total.
    _stock_map = {}
    _item_map = {}
    for it in compiled:
        ku = str(it["sku"]).strip().upper()
        _item_map[ku] = it
        _stock_map[ku] = {
            "stock": int(it.get("inv_stock") or 0),
            "wip":   int(it.get("inv_wip") or 0),
            "wip_website":  int(it.get("inv_wip_website") or 0),
            "wip_sor":      int(it.get("inv_wip_sor") or 0),
            "wip_designer": int(it.get("inv_wip_designer") or 0),
        }
    _sku_re = re.compile(r"[A-Za-z]{1,5}[-_ ]?\d{2,5}(?:[-_(][A-Za-z0-9)]+)*")
    for it in compiled:
        combo = it.get("combo_skus") or ""
        it["combo_details"] = []
        if not combo or not combo.strip():
            continue
        seen = set()
        for tok in _sku_re.findall(combo):
            key = tok.strip().upper().replace(" ", "")
            # normalize: "BH 1225" -> "BH-1225" agar map me dash-version ho
            cand = key
            if cand not in _stock_map and ("-" not in cand and "_" not in cand):
                # try inserting dash between letters and digits
                mm = re.match(r"^([A-Za-z]+)(\d.*)$", cand)
                if mm:
                    cand = mm.group(1) + "-" + mm.group(2)
            if cand in seen:
                continue
            seen.add(cand)
            info = _stock_map.get(cand)
            ci = _item_map.get(cand)   # combo SKU ka full item (saari details ke liye)
            it["combo_details"].append({
                "sku": cand,
                "image_url": (ci.get("image_url") if ci else ""),
                "inv_stock": info["stock"] if info else 0,
                "inv_wip":   info["wip"] if info else 0,
                "inv_wip_website":  info["wip_website"] if info else 0,
                "inv_wip_sor":      info["wip_sor"] if info else 0,
                "inv_wip_designer": info["wip_designer"] if info else 0,
                "blocked_qty": (ci.get("blocked_qty") if ci else 0),
                # poori details — CMB jaisi (combo SKU khud bhi inventory me hai)
                "qty_7d":   (ci.get("qty_7d") if ci else 0) or 0,
                "qty_15d":  (ci.get("qty_15d") if ci else 0) or 0,
                "qty_1m":   (ci.get("qty_1m") if ci else 0) or 0,
                "final_qty":(ci.get("final_qty") if ci else 0) or 0,
                "forecast_60d": (ci.get("forecast_60d") if ci else 0) or 0,
                "reorder_qty":  (ci.get("reorder_qty") if ci else 0) or 0,
                "mrp":      (ci.get("mrp") if ci else 0) or 0,
                "taxon":    (ci.get("taxon") if ci else ""),
                "plating":  (ci.get("plating") if ci else ""),
                "found":     info is not None,
            })

    CACHE["data"] = (
        compiled,
        sorted(taxons),
        sorted(types_),
        sorted(custs),
        sorted(platings),
        sorted(set(sku_list)),
        sorted(fyears, reverse=True),
        fy_current, fy_previous,
        today.strftime("%Y-%m-%d"),
        (today-timedelta(days=1)).strftime("%Y-%m-%d"),
        today.strftime("%Y-%m"),
        grand_net_revenue,
        grand_final_qty,
        period_kpis,
    )
    CACHE["ts"]    = time.time()
    _COSTS_CACHE["rows"] = None   # profit margin cache bhi refresh karo
    CACHE["debug"] = dbg
    return CACHE["data"]

# ── Optional SKU Finder (DINOv2) ─────────────────────────────
EMBED_MODE = "none"   # "local" (torch) | "hf" (Hugging Face API) | "none"

def init_vision():
    global AI_READY, db_data, processor, dino_model, client, EMBED_MODE
    if GEMINI_KEY and GENAI_AVAILABLE:
        try:
            client = genai.Client(api_key=GEMINI_KEY)
        except Exception as e:
            print("Gemini client init failed:", e)
    # 1) SKU embeddings database (numpy only — torch ki zaroorat nahi)
    _ensure_pkl()
    try:
        with open(PKL_FILE,"rb") as f: raw_db = pickle.load(f)
        emb_key = next((k for k in ("embeddings","emb","vectors","features") if k in raw_db), None)
        sku_key = next((k for k in ("skus","sku","labels","names","ids")       if k in raw_db), None)
        if emb_key is None or sku_key is None:
            raise KeyError(f"pkl keys found: {list(raw_db.keys())}")
        db_data = {
            "embeddings": np.asarray(raw_db[emb_key], dtype=np.float32),
            "skus":       [str(x) for x in raw_db[sku_key]],
        }
        print(f"SKU embedding DB loaded ({len(db_data['skus'])} SKUs).")
    except FileNotFoundError:
        print(f"{PKL_FILE} not found - SKU Finder disabled.")
        return
    except Exception as e:
        print("SKU DB load issue:", e)
        return
    # 2) Query embedding engine: local DINOv2 (torch) ya HF Inference API
    if ML_AVAILABLE:
        try:
            processor  = AutoImageProcessor.from_pretrained("facebook/dinov2-base")
            dino_model = AutoModel.from_pretrained("facebook/dinov2-base")
            dino_model.eval()
            EMBED_MODE = "local"
            AI_READY = True
            print("SKU Finder ready (local DINOv2).")
            return
        except Exception as e:
            print("Local DINOv2 load failed:", e)
    if SPACE_ID:
        EMBED_MODE = "space"
        AI_READY = True
        print(f"SKU Finder ready (embeddings via HF Space: {SPACE_ID}).")
    elif HF_TOKEN:
        EMBED_MODE = "hf"
        AI_READY = True
        print("SKU Finder ready (Hugging Face API embeddings — lite server mode).")
    else:
        print("No torch and no SPACE_ID/HF_TOKEN — SKU Finder disabled.")

_HF_LAST_ERROR = {"msg": ""}
_SPACE_CLI = {"cli": None}

def _space_dinov2_embedding(path):
    """DINOv2 embedding apne HF Space se (free CPU, 16GB) — lite servers ke liye."""
    try:
        from gradio_client import Client, handle_file
    except Exception as e:
        _HF_LAST_ERROR["msg"] = "gradio_client installed nahi hai: " + str(e)[:80]
        return None
    last = ""
    for attempt in range(2):
        try:
            cli = _SPACE_CLI["cli"]
            if cli is None:
                # gradio_client versions: naya 'token', purana 'hf_token', public space ko kuch nahi chahiye
                for kw in ({}, {"token": HF_TOKEN or None}, {"hf_token": HF_TOKEN or None}):
                    try:
                        cli = Client(SPACE_ID, verbose=False, **kw)
                        break
                    except TypeError:
                        cli = None
                        continue
                if cli is None:
                    cli = Client(SPACE_ID)
                _SPACE_CLI["cli"] = cli
            out = None
            for call_kw in ({"api_name": "/predict"}, {}, {"fn_index": 0}):
                try:
                    out = cli.predict(handle_file(path), **call_kw)
                    break
                except (ValueError, KeyError) as ve:
                    last = f"{type(ve).__name__}: {str(ve)[:100]}"
                    continue
            if out is None:
                raise RuntimeError(last or "no usable endpoint on Space")
            v = np.asarray(out, dtype=np.float32).reshape(-1)
            if v.shape[0] != 768:
                last = f"unexpected embedding size {v.shape}"
                print("Space embed:", last); break
            v = v / (np.linalg.norm(v) + 1e-9)
            _HF_LAST_ERROR["msg"] = ""
            return v
        except Exception as e:
            last = f"{type(e).__name__}: {str(e)[:140]}"
            print("Space embed error:", last)
            _SPACE_CLI["cli"] = None          # stale client reset, retry once
            time.sleep(4)
    _HF_LAST_ERROR["msg"] = last
    return None

def _hf_dinov2_embedding(path):
    """DINOv2 CLS embedding via HF Inference API — torch-free servers ke liye.
    503 (model warm-up) par khud retry karta hai; last error yaad rakhta hai."""
    try:
        with open(path, "rb") as f:
            data = f.read()
    except Exception:
        _HF_LAST_ERROR["msg"] = "could not read query image"
        return None
    bases = ("https://router.huggingface.co/hf-inference/models/facebook/dinov2-base",
             "https://api-inference.huggingface.co/models/facebook/dinov2-base")
    last = ""
    for attempt in range(4):                      # warm-up ke liye 4 rounds
        for base in bases:
            try:
                r = requests.post(base, data=data, timeout=(15, 120),
                                  headers={"Authorization": f"Bearer {HF_TOKEN}",
                                           "Content-Type": "image/jpeg",
                                           "x-wait-for-model": "true",
                                           "x-use-cache": "false"})
                if r.ok:
                    arr = np.asarray(r.json(), dtype=np.float32)
                    if arr.ndim == 3:
                        arr = arr[0]
                    if arr.ndim != 2 or arr.shape[-1] != 768:
                        last = f"unexpected shape {arr.shape}"
                        print("HF dinov2:", last); continue
                    v = arr[0]                    # CLS token (same as local path)
                    v = v / (np.linalg.norm(v) + 1e-9)
                    _HF_LAST_ERROR["msg"] = ""
                    return v
                last = f"HTTP {r.status_code}: {str(r.text)[:160]}"
                print("HF dinov2:", last)
                if r.status_code not in (503, 429, 500, 502):
                    # 401/403/404 jaise errors retry se theek nahi honge
                    _HF_LAST_ERROR["msg"] = last
                    return None
            except Exception as e:
                last = f"{type(e).__name__}: {str(e)[:120]}"
                print("HF dinov2 error:", last)
        time.sleep(6)                              # warm-up wait
    _HF_LAST_ERROR["msg"] = last
    return None

def get_embedding(path):
    if EMBED_MODE == "space":
        try:
            img = Image.open(path).convert("RGB")
            img.thumbnail((512, 512))
            small = "/tmp/_q_small.jpg"
            img.save(small, format="JPEG", quality=88)
            return _space_dinov2_embedding(small)
        except Exception as e:
            print("space embed prep failed:", e)
            return None
    if EMBED_MODE == "hf":
        # HF API ko chhota JPEG bhejo (fast + reliable)
        try:
            img = Image.open(path).convert("RGB")
            img.thumbnail((512, 512))
            small = "/tmp/_q_small.jpg"
            img.save(small, format="JPEG", quality=88)
            return _hf_dinov2_embedding(small)
        except Exception as e:
            print("hf embed prep failed:", e)
            return None
    try:
        img    = Image.open(path).convert("RGB")
        inputs = processor(images=img, return_tensors="pt")
        with torch.no_grad(): out = dino_model(**inputs)
        emb = out.last_hidden_state[:,0]
        emb = emb / emb.norm(dim=-1, keepdim=True)
        return emb.squeeze().numpy()
    except: return None

def vision_search(img_bytes, inventory, top_k=10):
    if not AI_READY or db_data is None: return None
    tmp = "/tmp/query.jpg"
    with open(tmp,"wb") as f: f.write(img_bytes)
    q = get_embedding(tmp)
    if q is None: return None
    sims   = db_data["embeddings"] @ q
    top    = np.argsort(sims)[::-1][:top_k]
    top_skus   = [db_data["skus"][i] for i in top]
    top_scores = [float(sims[i]) for i in top]
    if top_scores and top_scores[0] < 0.92 and client is not None:
        try:
            cands = "\n".join(f"{i+1}. {s}" for i,s in enumerate(top_skus[:5]))
            resp  = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=[
                    types.Part.from_bytes(data=img_bytes, mime_type="image/jpeg"),
                    types.Part.from_text(text=f"Match this product image to the most likely SKU. Candidates:\n{cands}\nReply ONLY the SKU code.")
                ],
            )
            top_skus[0] = resp.text.strip()
        except: pass
    out = []
    for sku, score in zip(top_skus, top_scores):
        m = next((i for i in inventory if i["sku"].upper()==str(sku).upper()), None)
        if not m: m = next((i for i in inventory if base_sku(i["sku"])==base_sku(sku)), None)
        if m:
            it = m.copy(); it["confidence"] = round(score*100,1)
        else:
            it = {"sku":sku,"confidence":round(score*100,1),"inv_stock":0,"inv_wip":0,"total_inv":0,"mrp":0,
                  "image_url":"","taxon":"General","plating":"N/A","pack_details":"","sales_entries":[],"total_net_revenue":0,
                  "qty_7d":0,"qty_15d":0,"qty_1m":0,"qty_3m":0,"qty_6m":0,"qty_1y":0,
                  "dispatch_count":0,"first_dispatch_date":"N/A","last_dispatch_date":"N/A",
                  "status":"No Record","rev_yesterday":0,"rev_month":0,"rev_fy":0,"rev_prev_fy":0,"forecast_30d":0,"forecast_60d":0,"reorder_qty":0}
        out.append(it)
    return out





# ── AI STUDIO (Dashboard Chat Assistant) ────────────────────
AI_CHAT_MODEL = "gemini-2.0-flash"
_AI_CLIENT = None

def _gemini_client():
    """Lazy Gemini client — returns None if key missing/invalid so the
    local fallback engine can take over."""
    global _AI_CLIENT
    if _AI_CLIENT is None and GEMINI_KEY and GENAI_AVAILABLE:
        try:
            _AI_CLIENT = genai.Client(api_key=GEMINI_KEY)
        except Exception as e:
            print("AI Studio: Gemini client init failed:", e)
    return _AI_CLIENT

_AI_METRICS = {
    "total_net_revenue": "Net Revenue (all time)",
    "final_qty":         "Final Qty (all time units)",
    "qty_7d":  "Qty last 7 days",  "qty_15d": "Qty last 15 days",
    "qty_1m":  "Qty last 1 month", "qty_3m":  "Qty last 3 months",
    "qty_6m":  "Qty last 6 months","qty_1y":  "Qty last 1 year",
    "rev_yesterday": "Revenue yesterday", "rev_month": "Revenue this month",
    "rev_fy": "Revenue this FY", "rev_prev_fy": "Revenue previous FY",
    "inv_stock": "Inventory stock", "inv_wip": "WIP stock",
    "total_inv": "Total inventory (stock+WIP)", "mrp": "MRP",
    "forecast_30d": "30-day forecast", "dispatch_count": "Dispatch count",
    "customer_count": "Unique customers",
}

def _ai_norm(s):
    return re.sub(r"[^A-Z0-9]", "", str(s).upper())

def _ai_find_skus_in_text(text, comp):
    """Detect SKU codes mentioned in the user's message (exact normalized
    match first, then prefix / base-SKU fallback)."""
    by_norm = {}
    for i in comp:
        k = _ai_norm(i.get("sku", ""))
        if k and k not in by_norm:
            by_norm[k] = i
    found, seen = [], set()
    tokens = re.findall(r"[A-Za-z0-9][A-Za-z0-9\-_/\.]{2,}", text)
    for tok in tokens:
        k = _ai_norm(tok)
        if len(k) < 3 or k in seen:
            continue
        if not re.search(r"\d", k):       # SKU codes contain digits
            continue
        item = by_norm.get(k)
        if item is None:
            pref = [v for nk, v in by_norm.items() if nk.startswith(k)]
            if 1 <= len(pref) <= 6:
                for p in pref:
                    nk = _ai_norm(p["sku"])
                    if nk not in seen:
                        seen.add(nk); found.append(p)
                continue
        if item is not None:
            seen.add(k); found.append(item)
    return found[:24]

def _ai_match_canon(val, options):
    """Loose match a value (e.g. taxon typed by user/Gemini) to canonical list."""
    if not val:
        return ""
    v = str(val).strip().lower()
    for o in options:
        if str(o).lower() == v:
            return o
    for o in options:
        ol = str(o).lower()
        if v in ol or ol in v:
            return o
    m = difflib.get_close_matches(v, [str(o).lower() for o in options], n=1, cutoff=0.75)
    if m:
        for o in options:
            if str(o).lower() == m[0]:
                return o
    return ""

# ── AI FORECASTING (Prophet + trend fallback) ───────────────
_PROPHET_OK = None

def _prophet_available():
    global _PROPHET_OK
    if _PROPHET_OK is None:
        try:
            import logging as _lg
            for nm in ("prophet", "cmdstanpy"):
                _lg.getLogger(nm).setLevel(_lg.ERROR)
            from prophet import Prophet  # noqa
            _PROPHET_OK = True
        except Exception:
            _PROPHET_OK = False
            print("Prophet not installed — trend forecast use hoga. "
                  "(Colab: !pip install prophet)")
    return _PROPHET_OK

def _ai_daily_series(comp, f, lookback_days, today):
    """Daily {date: {rev, qty}} for entries matching type/customer/taxon filters."""
    typ   = str(f.get("type") or "").strip().lower()
    cust  = str(f.get("customer") or "").strip().lower()
    taxon = str(f.get("taxon") or "").strip().lower()
    start = (today - timedelta(days=lookback_days)).strftime("%Y-%m-%d")
    daily = {}
    for i in comp:
        if taxon and taxon not in str(i.get("taxon", "")).lower():
            continue
        for e in i.get("sales_entries", []):
            d = e.get("date", "N/A")
            if d == "N/A" or d < start:
                continue
            if typ and typ not in str(e.get("type", "")).lower(): continue
            if cust and cust not in str(e.get("cust", "")).lower(): continue
            slot = daily.setdefault(d, {"rev": 0.0, "qty": 0.0})
            slot["rev"] += float(e.get("rev") or 0)
            slot["qty"] += float(e.get("qty") or 0)
    return daily

def _forecast_series(daily, key, days_ahead, today):
    """Forecast next `days_ahead` daily values. Prophet if available,
    else weighted moving-average trend. Returns (list, method)."""
    if days_ahead <= 0:
        return [], "none"
    dates = sorted(daily.keys())
    vals  = [daily[d][key] for d in dates]
    # need a continuous daily frame (fill missing days with 0)
    if dates:
        d0 = datetime.strptime(dates[0], "%Y-%m-%d")
        frame, cur = [], d0
        end = today.replace(tzinfo=None)
        dd = {d: daily[d][key] for d in dates}
        while cur <= end:
            ds = cur.strftime("%Y-%m-%d")
            frame.append((ds, float(dd.get(ds, 0.0))))
            cur += timedelta(days=1)
    else:
        frame = []

    if len(frame) >= 14 and _prophet_available():
        try:
            from prophet import Prophet
            import pandas as _pd
            df = _pd.DataFrame({"ds": [a for a, _ in frame], "y": [b for _, b in frame]})
            mdl = Prophet(weekly_seasonality=True, daily_seasonality=False,
                          yearly_seasonality=False, interval_width=0.8)
            mdl.fit(df)
            fut = mdl.make_future_dataframe(periods=days_ahead)
            fc  = mdl.predict(fut).tail(days_ahead)
            return [max(0.0, float(v)) for v in fc["yhat"]], "prophet"
        except Exception as e:
            print("Prophet fit failed, trend fallback:", str(e)[:140])
    # trend fallback: weighted avg (recent weeks heavier)
    vals28 = [b for _, b in frame[-28:]] or [0.0]
    vals7  = [b for _, b in frame[-7:]] or vals28
    base = 0.6 * (sum(vals7) / max(len(vals7), 1)) + 0.4 * (sum(vals28) / max(len(vals28), 1))
    return [base] * days_ahead, "trend"

def _ai_exec_forecast(plan, comp, today):
    """Project sales for the rest of the current month (default) or next N days.
    Returns (items, summary)."""
    f      = plan.get("filters") or {}
    period = plan.get("period") or {}
    top_n  = max(1, min(24, int(plan.get("top_n") or 10)))

    # horizon: default = current month end
    tn = today.replace(tzinfo=None)
    if period.get("days_ahead"):
        days_ahead = max(1, min(90, int(period["days_ahead"])))
        horizon_label = f"next {days_ahead} days"
        h_start = tn + timedelta(days=1)
    else:
        if tn.month == 12:
            nxt = tn.replace(year=tn.year + 1, month=1, day=1)
        else:
            nxt = tn.replace(month=tn.month + 1, day=1)
        month_end = nxt - timedelta(days=1)
        days_ahead = max(0, (month_end - tn).days)
        horizon_label = tn.strftime("%B %Y")
        h_start = tn + timedelta(days=1)

    daily = _ai_daily_series(comp, f, 120, tn)
    month_pref = tn.strftime("%Y-%m")
    mtd_rev = sum(v["rev"] for d, v in daily.items() if d.startswith(month_pref))
    mtd_qty = sum(v["qty"] for d, v in daily.items() if d.startswith(month_pref))

    fc_rev, method = _forecast_series(daily, "rev", days_ahead, tn)
    fc_qty, _      = _forecast_series(daily, "qty", days_ahead, tn)
    rem_rev, rem_qty = sum(fc_rev), sum(fc_qty)

    # per-SKU projection from last-30d velocity (filter-aware)
    typ   = str(f.get("type") or "").strip().lower()
    cust  = str(f.get("customer") or "").strip().lower()
    taxon = str(f.get("taxon") or "").strip().lower()
    start30 = (tn - timedelta(days=30)).strftime("%Y-%m-%d")
    per = []
    for i in comp:
        if taxon and taxon not in str(i.get("taxon", "")).lower():
            continue
        q30 = r30 = 0.0
        for e in i.get("sales_entries", []):
            d = e.get("date", "N/A")
            if d == "N/A" or d < start30: continue
            if typ and typ not in str(e.get("type", "")).lower(): continue
            if cust and cust not in str(e.get("cust", "")).lower(): continue
            q30 += float(e.get("qty") or 0); r30 += float(e.get("rev") or 0)
        if q30 > 0:
            pred_q = q30 / 30.0 * days_ahead
            per.append({"item": i, "pred_qty": pred_q, "pred_rev": r30 / 30.0 * days_ahead})
    per.sort(key=lambda x: x["pred_qty"], reverse=True)
    items = [p["item"] for p in per[:top_n]]

    flt_bits = {k: v for k, v in {"type": f.get("type"), "customer": f.get("customer"),
                                  "taxon": f.get("taxon")}.items() if v}
    summary = {
        "action": "forecast", "method": method, "horizon": horizon_label,
        "days_remaining": days_ahead, "filters": flt_bits,
        "month_so_far": {"revenue": round(mtd_rev), "qty": int(round(mtd_qty))},
        "projected_remaining": {"revenue": round(rem_rev), "qty": int(round(rem_qty))},
        "projected_month_total": {"revenue": round(mtd_rev + rem_rev),
                                  "qty": int(round(mtd_qty + rem_qty))},
        "top_predicted_skus": [{"sku": p["item"]["sku"],
                                "pred_qty": int(round(p["pred_qty"])),
                                "pred_rev": round(p["pred_rev"])} for p in per[:top_n]],
        "note": "prophet model" if method == "prophet" else
                "trend model (install Prophet for better accuracy: run !pip install prophet in Colab)",
    }
    return items, summary

_AI_MONTHS = {"jan":1,"january":1,"feb":2,"february":2,"mar":3,"march":3,"apr":4,"april":4,
              "may":5,"jun":6,"june":6,"jul":7,"july":7,"aug":8,"august":8,
              "sep":9,"sept":9,"september":9,"oct":10,"october":10,
              "nov":11,"november":11,"dec":12,"december":12}

def _ai_parse_period_text(m, today):
    """Find a date / month-year / relative period mentioned in the message.
    Returns dict like {"date_from","date_to"} or {"month":"YYYY-MM"} or {}."""
    # explicit YYYY-MM
    g = re.search(r"\b(20\d{2})[-/](0?[1-9]|1[0-2])\b", m)
    if g:
        return {"month": f"{g.group(1)}-{int(g.group(2)):02d}"}
    # "june 2025" / "2025 june" / "june" alone
    for name, num in sorted(_AI_MONTHS.items(), key=lambda x: -len(x[0])):
        if re.search(r"\b" + name + r"\b", m):
            y = re.search(r"\b(20\d{2})\b", m)
            if y:
                return {"month": f"{y.group(1)}-{num:02d}"}
            yr = today.year if num <= today.month else today.year - 1
            return {"month": f"{yr}-{num:02d}"}
    # specific date like 5/6/2026 or 05-06-2026 (DD-MM-YYYY)
    g = re.search(r"\b(0?[1-9]|[12]\d|3[01])[-/](0?[1-9]|1[0-2])[-/](20\d{2})\b", m)
    if g:
        d = f"{g.group(3)}-{int(g.group(2)):02d}-{int(g.group(1)):02d}"
        return {"date_from": d, "date_to": d}
    if re.search(r"\bkal\b|yesterday", m):
        d = (today - timedelta(days=1)).strftime("%Y-%m-%d")
        return {"date_from": d, "date_to": d}
    if re.search(r"\baaj\b|today", m):
        d = today.strftime("%Y-%m-%d")
        return {"date_from": d, "date_to": d}
    if re.search(r"last\s*7|pichl\w*\s*7|7\s*din", m):
        return {"date_from": (today - timedelta(days=7)).strftime("%Y-%m-%d"),
                "date_to": today.strftime("%Y-%m-%d")}
    if re.search(r"last\s*30|pichl\w*\s*30|30\s*din|last\s*month|pichl\w*\s*mah", m):
        first_this = today.replace(day=1)
        last_prev = first_this - timedelta(days=1)
        if re.search(r"last\s*month|pichl\w*\s*mah", m):
            return {"month": last_prev.strftime("%Y-%m")}
        return {"date_from": (today - timedelta(days=30)).strftime("%Y-%m-%d"),
                "date_to": today.strftime("%Y-%m-%d")}
    if re.search(r"is\s*mah?ine|this\s*month", m):
        return {"month": today.strftime("%Y-%m")}
    g = re.search(r"\bfy\s*(20\d{2})[-–\s]*(\d{2,4})?", m)
    if g:
        y1 = g.group(1); y2 = g.group(2) or str(int(y1) + 1)[-2:]
        return {"fy": f"FY {y1}-{y2[-2:]}"}
    return {}

def _ai_exec_transactions(plan, comp, today):
    """Query at transaction (sales-entry) level: date range / month / FY /
    sales Type (channel) / customer. Returns (items, summary)."""
    f      = plan.get("filters") or {}
    period = plan.get("period") or {}
    top_n  = max(1, min(24, int(plan.get("top_n") or 12)))
    want_skus = [_ai_norm(s) for s in (plan.get("skus") or [])]

    typ   = str(f.get("type") or "").strip().lower()
    cust  = str(f.get("customer") or "").strip().lower()
    taxon = str(f.get("taxon") or "").strip().lower()
    month = str(period.get("month") or "").strip()
    fy    = str(period.get("fy") or "").strip().lower()
    d_from = str(period.get("date_from") or "").strip()
    d_to   = str(period.get("date_to") or "").strip()

    per_sku, total_rev, total_qty, txn = {}, 0.0, 0.0, 0
    type_break, cust_break = {}, {}
    for i in comp:
        if want_skus:
            k = _ai_norm(i["sku"])
            if not any(k == w or k.startswith(w) for w in want_skus):
                continue
        if taxon and taxon not in str(i.get("taxon", "")).lower():
            continue
        srev = sqty = 0.0; scount = 0
        for e in i.get("sales_entries", []):
            d = e.get("date", "N/A")
            if month and not str(d).startswith(month): continue
            if d_from and (d == "N/A" or d < d_from): continue
            if d_to and (d == "N/A" or d > d_to): continue
            if fy and fy not in str(e.get("fy", "")).lower(): continue
            if typ and typ not in str(e.get("type", "")).lower(): continue
            if cust and cust not in str(e.get("cust", "")).lower(): continue
            srev += float(e.get("rev") or 0); sqty += float(e.get("qty") or 0); scount += 1
            tkey = e.get("type", "Regular");  type_break[tkey] = type_break.get(tkey, 0.0) + float(e.get("rev") or 0)
            ckey = e.get("cust", "Unknown");  cust_break[ckey] = cust_break.get(ckey, 0.0) + float(e.get("rev") or 0)
        if scount:
            per_sku[i["sku"]] = {"item": i, "rev": srev, "qty": sqty, "txn": scount}
            total_rev += srev; total_qty += sqty; txn += scount

    ranked = sorted(per_sku.values(), key=lambda x: x["rev"], reverse=True)
    items  = [r["item"] for r in ranked[:top_n]]

    if month:
        plabel = month
    elif d_from and d_from == d_to:
        plabel = d_from
    elif d_from or d_to:
        plabel = f"{d_from or '…'} → {d_to or '…'}"
    elif fy:
        plabel = period.get("fy")
    else:
        plabel = "all time"

    summary = {
        "action": "transactions",
        "period_label": plabel,
        "filters": {k: v for k, v in {"type": f.get("type"), "customer": f.get("customer"),
                                      "taxon": f.get("taxon")}.items() if v},
        "total_revenue": round(total_rev), "total_qty": int(round(total_qty)),
        "transactions": txn, "unique_skus": len(per_sku),
        "top_skus": [{"sku": r["item"]["sku"], "revenue": round(r["rev"]),
                      "qty": int(round(r["qty"])), "txns": r["txn"]} for r in ranked[:top_n]],
        "type_breakup": {k: round(v) for k, v in sorted(type_break.items(), key=lambda x: -x[1])[:8]},
        "top_customers": {k: round(v) for k, v in sorted(cust_break.items(), key=lambda x: -x[1])[:5]},
    }
    return items, summary

def _ai_exec_briefing(comp, period_kpis):
    """One-shot business briefing: KPIs, momentum, stock alerts, top movers."""
    by_7d = sorted(comp, key=lambda i: float(i.get("qty_7d") or 0), reverse=True)
    movers = [i for i in by_7d if float(i.get("qty_7d") or 0) > 0][:5]
    zero_stock_selling = [i for i in comp
                          if float(i.get("total_inv") or 0) <= 0 and float(i.get("qty_1m") or 0) > 0]
    low_stock_fast = [i for i in comp
                      if 0 < float(i.get("total_inv") or 0) <= 10 and float(i.get("qty_1m") or 0) >= 5]
    slow = sum(1 for i in comp if float(i.get("qty_3m") or 0) == 0 and float(i.get("total_inv") or 0) > 0)
    summary = {
        "action": "briefing",
        "kpis": period_kpis,
        "total_skus": len(comp),
        "top_movers_7d": [{"sku": i["sku"], "qty_7d": i["qty_7d"],
                           "stock": i["total_inv"]} for i in movers],
        "out_of_stock_but_selling": len(zero_stock_selling),
        "low_stock_fast_sellers": len(low_stock_fast),
        "slow_movers_with_stock": slow,
        "restock_urgent": [i["sku"] for i in (zero_stock_selling + low_stock_fast)[:5]],
    }
    items = (zero_stock_selling[:3] + low_stock_fast[:3] + movers[:3])[:9]
    # dedupe preserving order
    seen, uniq = set(), []
    for i in items:
        if i["sku"] not in seen:
            seen.add(i["sku"]); uniq.append(i)
    return uniq, summary

def _ai_default_plan():
    return {"action": "aggregate", "skus": [], "filters": {}, "period": {},
            "metric": "total_net_revenue", "sort": "desc", "top_n": 10}

def _ai_parse_json(text):
    if not text:
        return None
    t = text.strip()
    t = re.sub(r"^```(?:json)?", "", t).strip()
    t = re.sub(r"```$", "", t).strip()
    m = re.search(r"\{.*\}", t, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except Exception:
        return None

def _ai_gemini_plan(cli, msg, history, taxons, statuses, platings, context_skus=None, sale_types=None):
    """Step 1: ask Gemini to turn the question into a structured query plan."""
    try:
        hist_txt = "\n".join(f"{h.get('role','user')}: {h.get('text','')[:300]}"
                             for h in history[-6:])
        ctx_txt = (", ".join(context_skus[:10]) if context_skus else "none")
        types_txt = ", ".join([str(t) for t in (sale_types or [])][:30]) or "Regular"
        today = now_ist()
        today_s = today.strftime("%Y-%m-%d")
        yest_s  = (today - timedelta(days=1)).strftime("%Y-%m-%d")
        prompt = f"""You convert a question about a jewellery e-commerce dashboard into a JSON query plan.
The dashboard has one record per SKU with these numeric fields:
{json.dumps(_AI_METRICS, indent=1)}
And text fields: sku, taxon (category), plating, status, combo_skus, first_dispatch_date, last_dispatch_date.
Available taxons: {", ".join(taxons[:60])}
Available statuses: {", ".join(statuses)}
Available platings: {", ".join(platings[:40])}

Each SKU also has "sales_entries": individual sale transactions with date (YYYY-MM-DD),
qty, rev, fy, customer name and sales TYPE (channel). Available sales types: {types_txt}.
Today is {today_s}, yesterday was {yest_s}.

Reply ONLY with JSON (no markdown, no explanation) in this exact schema:
{{
 "action": "sku_lookup" | "filter_rank" | "aggregate" | "transactions" | "forecast" | "briefing" | "compare" | "chat",
 "skus": ["exact SKU codes mentioned by user, else empty"],
 "filters": {{"taxon":"", "plating":"", "status":"", "search":"", "type":"", "customer":"", "mrp_min":0, "mrp_max":0, "stock":"any|zero|low|in_stock"}},
 "period": {{"month":"YYYY-MM or empty", "date_from":"YYYY-MM-DD or empty", "date_to":"YYYY-MM-DD or empty", "fy":"FY 2025-26 or empty"}},
 "metric": "one key from the numeric fields above",
 "sort": "desc|asc",
 "top_n": 10
}}
Rules:
- "top/best selling" => filter_rank, metric final_qty (or a qty_* period if a period is mentioned).
- "highest revenue" => filter_rank, metric total_net_revenue (rev_month/rev_fy/rev_yesterday if period mentioned).
- "out of stock / stock khatam" => filter_rank with filters.stock="zero", metric total_inv, sort asc.
- "low stock / kam stock" => filters.stock="low".
- "slow moving / not selling" => filter_rank, metric qty_3m, sort asc.
- totals like "total revenue", "is mahine ki sale" => aggregate (set metric to the matching period field).
- a specific SKU code => sku_lookup with that code in skus.
- Use action "briefing" when the user asks for a business briefing/summary/daily report/overview.
- Use action "compare" when the user asks to COMPARE last month with the same month last year /
  month-on-month / YoY ("compare with last month", "pichhle saal ke is mahine se compare",
  "month on month", "last month vs last year"). No skus/filters needed.
- Use action "forecast" for FUTURE/prediction questions: "is mahine kitni sale HO SAKTI hai",
  "agle mahine kitna bikega", "kaunse SKU bikenge", "expected/projected revenue". Channel like
  Website/SOR => filters.type. For "agle N din" set period.days_ahead=N (add it inside "period").
- Use action "transactions" whenever the question involves: a specific month/year
  ("june 2025 me kitna revenue"), a specific date, "kal/aaj kya kya bika" (what sold
  yesterday/today => set date_from=date_to to that date), a sales TYPE/channel like SOR
  ("SOR me kitna revenue" => filters.type="SOR"), or a customer name. Fill "period" accordingly.
- greetings/small-talk/questions not about data => action "chat".
- The user often writes in Hinglish (Hindi+English mix).
- CONTEXT SKUs currently being discussed: {ctx_txt}. If the question is a follow-up about them
  (e.g. "last 7 days?", "iska revenue?", "30 din ka batao", "aur is mahine?") then use
  action "sku_lookup" with those SKU codes in "skus" and set "metric" to the asked period/field.

Conversation so far:
{hist_txt}

User question: {msg}"""
        resp = cli.models.generate_content(model=AI_CHAT_MODEL, contents=prompt)
        plan = _ai_parse_json(getattr(resp, "text", "") or "")
        if not isinstance(plan, dict) or "action" not in plan:
            return None
        base = _ai_default_plan()
        base.update({k: v for k, v in plan.items() if v is not None})
        if not isinstance(base.get("filters"), dict):
            base["filters"] = {}
        return base
    except Exception as e:
        print("AI Studio: Gemini plan failed:", e)
        return None

def _ai_local_plan(msg, taxons, statuses, platings, sale_types=None, customers=None):
    """Rule-based fallback planner (works without Gemini)."""
    m = msg.lower()
    plan = _ai_default_plan()
    f = plan["filters"] = {}

    # period → metric suffix
    rev_metric, qty_metric = "total_net_revenue", "final_qty"
    if re.search(r"\bkal\b|yesterday", m):
        rev_metric, qty_metric = "rev_yesterday", "qty_7d"
    elif re.search(r"is\s*mah?ine|this\s*month|mahina", m):
        rev_metric, qty_metric = "rev_month", "qty_1m"
    elif re.search(r"pichl\w*\s*(fy|saal|year)|previous\s*fy|last\s*fy", m):
        rev_metric = "rev_prev_fy"
    elif re.search(r"\bfy\b|financial\s*year|is\s*saal|this\s*year", m):
        rev_metric, qty_metric = "rev_fy", "qty_1y"
    elif re.search(r"7\s*d|7\s*din|week|hafte", m):
        qty_metric = "qty_7d"
    elif re.search(r"15\s*d|15\s*din", m):
        qty_metric = "qty_15d"
    elif re.search(r"30\s*d|30\s*din|1\s*mah|ek\s*mah|1\s*month|last\s*month", m):
        rev_metric, qty_metric = "rev_month", "qty_1m"
    elif re.search(r"3\s*m|3\s*mah|90\s*d", m):
        qty_metric = "qty_3m"
    elif re.search(r"6\s*m|6\s*mah|180\s*d", m):
        qty_metric = "qty_6m"

    if re.search(r"forecast|agla\s*mahin|next\s*month|aage\s*kitn", m):
        qty_metric = rev_metric = "forecast_30d"

    n = re.search(r"top\s*(\d+)|(\d+)\s*(?:sku|best|top)", m)
    if n:
        plan["top_n"] = max(1, min(24, int(n.group(1) or n.group(2))))

    tx = _ai_match_canon(next((t for t in taxons if str(t).lower() in m), ""), taxons)
    if not tx:
        for t in taxons:
            tl = str(t).lower()
            if len(tl) >= 4 and tl in m:
                tx = t; break
    if tx: f["taxon"] = tx
    for p in platings:
        if len(str(p)) >= 4 and str(p).lower() in m:
            f["plating"] = p; break

    # transaction-level intent: explicit month/date/period + sales type/customer channel
    today = now_ist()
    period = _ai_parse_period_text(m, today)

    # Daily briefing / business summary
    if re.search(r"briefing|business\s*summary|daily\s*(report|summary)|aaj\s*ka\s*(summary|report)|"
                 r"morning\s*report|how\s*is\s*(the\s*)?business|overview\s*do", m):
        plan["action"] = "briefing"
        return plan

    # Compare-with-last-month / month-on-month YoY intent
    if re.search(r"\bcompare\b|comparison|vs\s*last|last\s*month\s*(se|vs|comparison)|"
                 r"pichl\w*\s*mah?in\w*\s*(se|tulna)|month\s*on\s*month|\bmom\b|"
                 r"same\s*month\s*last\s*year|pichl\w*\s*saal\s*(ka)?\s*(is)?\s*mah", m):
        plan["action"] = "compare"
        return plan

    # FUTURE / forecast intent (check pehle — "ho sakti hai" jaise words)
    if re.search(r"ho\s*sakt[ai]|hoga\b|hogi\b|bikeg|bik\s*sakt|forecast|predict|"
                 r"expect|project|estimat|anuman|agle\s*(mah|month|\d+\s*din)|next\s*month", m):
        plan["action"] = "forecast"
        nd = re.search(r"agle\s*(\d+)\s*din|next\s*(\d+)\s*day", m)
        if nd:
            plan["period"] = {"days_ahead": int(nd.group(1) or nd.group(2))}
        for t in (sale_types or []):
            ts = str(t).strip()
            if len(ts) >= 2 and re.search(r"\b" + re.escape(ts.lower()) + r"\b", m):
                f["type"] = ts; break
        for cu in (customers or []):
            cs = str(cu).strip()
            if len(cs) >= 3 and re.search(r"\b" + re.escape(cs.lower()) + r"\b", m):
                f["customer"] = cs; break
        if tx: f["taxon"] = tx
        return plan
    typ_hit = ""
    for t in (sale_types or []):
        ts = str(t).strip()
        if len(ts) >= 2 and re.search(r"\b" + re.escape(ts.lower()) + r"\b", m):
            typ_hit = ts; break
    cust_hit = ""
    for cu in (customers or []):
        cs = str(cu).strip()
        if len(cs) >= 3 and re.search(r"\b" + re.escape(cs.lower()) + r"\b", m):
            cust_hit = cs; break
    explicit_month = bool(period.get("month") and re.search(r"\b(20\d{2})\b|" + "|".join(_AI_MONTHS), m))
    sale_word = re.search(r"\bsale|sales|revenue|bik|bech|becha|sold|sell|dispatch|order|kamai\b", m)
    sold_what = re.search(r"(kya\s*kya|kaun\s*s\w*|which|what)\s*.*\b(sku|bik|sell|sale|dispatch)|\b(bik[ae]|sold|sell\s*hue)\b", m)
    if (typ_hit or cust_hit or explicit_month
            or (period.get("date_from") and (sold_what or sale_word))
            or (period and sold_what)):
        plan["action"] = "transactions"
        plan["period"] = period
        if typ_hit:  f["type"] = typ_hit
        if cust_hit: f["customer"] = cust_hit
        if tx: f["taxon"] = tx
        plan["top_n"] = max(plan.get("top_n") or 12, 12)
        return plan

    if re.search(r"out\s*of\s*stock|stock\s*(?:0|zero|khatam|khtm|nahi|nil)|zero\s*stock", m):
        plan["action"] = "filter_rank"; f["stock"] = "zero"
        plan["metric"] = qty_metric; plan["sort"] = "desc"
    elif re.search(r"low\s*stock|kam\s*stock|stock\s*kam", m):
        plan["action"] = "filter_rank"; f["stock"] = "low"
        plan["metric"] = qty_metric; plan["sort"] = "desc"
    elif re.search(r"slow|nahi\s*bik|not\s*sell|no\s*sale|dead\s*stock", m):
        plan["action"] = "filter_rank"; plan["metric"] = "qty_3m"; plan["sort"] = "asc"
        f["stock"] = "in_stock"
    elif re.search(r"top|best|sabse\s*(?:zyada|jyada|accha)|highest|max", m):
        plan["action"] = "filter_rank"
        plan["metric"] = rev_metric if re.search(r"rev|sale\s*amount|amount|₹|kamai", m) else qty_metric
        plan["sort"] = "desc"
    elif re.search(r"total|kitn[ai]|kitna|overall|grand|summary|revenue|sale|qty|quantity", m):
        plan["action"] = "aggregate"
        plan["metric"] = rev_metric if re.search(r"rev|sale|amount|kamai|₹", m) else qty_metric
    elif re.search(r"^(hi|hii+|hello|hey|namaste|namaskar|kaise|how are|kya kar)", m.strip()):
        plan["action"] = "chat"
    else:
        plan["action"] = "filter_rank"
        plan["metric"] = qty_metric
        if tx == "" and not f:
            f["search"] = msg.strip()[:60]
    return plan

def _ai_execute_plan(plan, comp, period_kpis, fy_cur, fy_prev):
    """Run the plan locally over the compiled inventory. Returns (items, summary)."""
    action  = plan.get("action", "aggregate")
    metric  = plan.get("metric") if plan.get("metric") in _AI_METRICS else "total_net_revenue"
    sort_d  = plan.get("sort", "desc") != "asc"
    top_n   = max(1, min(24, int(plan.get("top_n") or 10)))
    filters = plan.get("filters") or {}

    if action == "chat":
        return [], {"action": "chat", "period_kpis": period_kpis,
                    "fy_current": fy_cur, "fy_previous": fy_prev,
                    "total_skus": len(comp)}

    if action == "compare":
        return [], {"action": "compare", "period_kpis": period_kpis,
                    "fy_current": fy_cur, "fy_previous": fy_prev}

    if action == "transactions":
        return _ai_exec_transactions(plan, comp, now_ist())

    if action == "forecast":
        return _ai_exec_forecast(plan, comp, now_ist())

    if action == "briefing":
        return _ai_exec_briefing(comp, period_kpis)

    # SKU lookup
    if action == "sku_lookup" and plan.get("skus"):
        wanted, items = [_ai_norm(s) for s in plan["skus"]], []
        for i in comp:
            k = _ai_norm(i["sku"])
            if k in wanted or any(k.startswith(w) or w.startswith(k) for w in wanted if len(w) >= 4):
                items.append(i)
        items = items[:24]
        summary = {"action": "sku_lookup", "found": len(items),
                   "metric": metric, "metric_label": _AI_METRICS.get(metric, metric),
                   "items": [{ "sku": i["sku"], "taxon": i["taxon"], "plating": i["plating"],
                               "status": i["status"], "mrp": i["mrp"],
                               "inv_stock": i["inv_stock"], "inv_wip": i["inv_wip"],
                               "total_inv": i["total_inv"],
                               "total_net_revenue": round(i["total_net_revenue"]),
                               "final_qty": i["final_qty"],
                               "qty_7d": i["qty_7d"], "qty_15d": i["qty_15d"],
                               "qty_1m": i["qty_1m"], "qty_3m": i["qty_3m"],
                               "qty_6m": i["qty_6m"], "qty_1y": i["qty_1y"],
                               "rev_yesterday": round(i["rev_yesterday"]),
                               "rev_month": round(i["rev_month"]), "rev_fy": round(i["rev_fy"]),
                               "rev_prev_fy": round(i["rev_prev_fy"]),
                               "forecast_30d": i["forecast_30d"],
                               "first_dispatch_date": i["first_dispatch_date"],
                               "last_dispatch_date": i["last_dispatch_date"],
                               "dispatch_count": i["dispatch_count"],
                               "combo_skus": i.get("combo_skus",""),
                               "customer_count": i["customer_count"]} for i in items]}
        return items, summary

    # Filtering
    def keep(i):
        tx = filters.get("taxon")
        if tx and str(i.get("taxon", "")).lower() != str(tx).lower():
            return False
        pl = filters.get("plating")
        if pl and str(pl).lower() not in str(i.get("plating", "")).lower():
            return False
        st = filters.get("status")
        if st and str(st).lower() not in str(i.get("status", "")).lower():
            return False
        srch = filters.get("search")
        if srch:
            blob = f"{i.get('sku','')} {i.get('taxon','')} {i.get('plating','')} {i.get('status','')}".lower()
            if not all(w in blob for w in str(srch).lower().split() if len(w) > 2):
                return False
        try:
            if filters.get("mrp_min") and float(i.get("mrp") or 0) < float(filters["mrp_min"]):
                return False
            if filters.get("mrp_max") and float(i.get("mrp") or 0) > float(filters["mrp_max"]):
                return False
        except Exception:
            pass
        stock = filters.get("stock", "any")
        tinv = float(i.get("total_inv") or 0)
        if stock == "zero" and tinv > 0: return False
        if stock == "low" and not (0 < tinv <= 10): return False
        if stock == "in_stock" and tinv <= 0: return False
        return True

    pool = [i for i in comp if keep(i)]
    pool.sort(key=lambda i: float(i.get(metric) or 0), reverse=sort_d)

    agg = {
        "matched_skus":   len(pool),
        "sum_net_revenue": round(sum(float(i.get("total_net_revenue") or 0) for i in pool)),
        "sum_final_qty":   int(sum(float(i.get("final_qty") or 0) for i in pool)),
        "sum_rev_month":   round(sum(float(i.get("rev_month") or 0) for i in pool)),
        "sum_rev_fy":      round(sum(float(i.get("rev_fy") or 0) for i in pool)),
        "sum_rev_prev_fy": round(sum(float(i.get("rev_prev_fy") or 0) for i in pool)),
        "sum_rev_yesterday": round(sum(float(i.get("rev_yesterday") or 0) for i in pool)),
        "sum_stock":       int(sum(float(i.get("inv_stock") or 0) for i in pool)),
        "sum_wip":         int(sum(float(i.get("inv_wip") or 0) for i in pool)),
        "zero_stock_skus": sum(1 for i in pool if float(i.get("total_inv") or 0) <= 0),
    }

    items = pool[:top_n]
    summary = {
        "action": action, "metric": metric, "metric_label": _AI_METRICS.get(metric, metric),
        "sort": "desc" if sort_d else "asc", "filters": filters,
        "aggregates": agg, "fy_current": fy_cur, "fy_previous": fy_prev,
        "period_kpis": period_kpis,
        "top_items": [{"sku": i["sku"], "taxon": i["taxon"], "status": i["status"],
                       "value": round(float(i.get(metric) or 0), 2),
                       "inv_stock": i["inv_stock"], "mrp": i["mrp"],
                       "final_qty": i["final_qty"],
                       "total_net_revenue": round(i["total_net_revenue"])} for i in items],
    }
    if action == "aggregate":
        items = items[:6]
    return items, summary

def _ai_gemini_answer(cli, msg, history, plan, summary, items):
    """Step 2: Gemini writes the final reply using ONLY computed results."""
    try:
        hist_txt = "\n".join(f"{h.get('role','user')}: {h.get('text','')[:300]}"
                             for h in history[-6:])
        prompt = f"""You are "Cosa AI", the in-dashboard assistant for COSA NOSTRAA (premium brass jewellery brand, Jaipur).
Answer the user's question using ONLY the RESULTS JSON below — never invent numbers.
Style: reply in the SAME language style as the user (they usually write Hinglish — Hindi-English mix).
CRITICAL RULES:
1. Answer ONLY the exact question — zero extra information. One number asked = ONE short sentence.
2. Never add summaries, totals, breakdowns, or tips that were not asked.
3. Max 3 short sentences (or max 5 bullets ONLY if user asked for a list).
4. Use ₹ with Indian number format (e.g. ₹1,23,456). 
The matching SKU cards (with image, stock, revenue etc.) are shown below your message automatically, so do NOT list every field of every SKU — just give the headline insight and mention the top 2-3 SKU codes if relevant.
If RESULTS has action "chat", just chat normally as a helpful dashboard assistant and tell them what you can do (top sellers, stock, revenue, SKU details, category analysis).

Conversation so far:
{hist_txt}

User question: {msg}

RESULTS JSON:
{json.dumps(summary, ensure_ascii=False)[:14000]}"""
        resp = cli.models.generate_content(model=AI_CHAT_MODEL, contents=prompt)
        txt = (getattr(resp, "text", "") or "").strip()
        return txt or None
    except Exception as e:
        print("AI Studio: Gemini answer failed:", e)
        return None

def _inr(n):
    try:
        v = int(round(float(n or 0)))
        sign = "-" if v < 0 else ""
        s = str(abs(v))
        if len(s) > 3:
            head, tail = s[:-3], s[-3:]
            parts = []
            while len(head) > 2:
                parts.insert(0, head[-2:]); head = head[:-2]
            if head: parts.insert(0, head)
            s = ",".join(parts) + "," + tail
        return "₹" + sign + s
    except Exception:
        return "₹0"

def _ai_local_answer(msg, plan, summary, items):
    """Template answer when Gemini is unavailable — still fully functional."""
    a = summary.get("action")
    if a == "compare":
        k = summary.get("period_kpis") or {}
        lm = k.get("last_month") or 0
        ly = k.get("last_year_month") or 0
        lm_l = k.get("last_month_label") or "last month"
        ly_l = k.get("last_year_month_label") or "same month last year"
        yoy = k.get("mom_yoy_pct")
        tm = k.get("this_month") or 0
        if not lm and not ly:
            return "No monthly data available for comparison yet. Please try again in a moment."
        lines = [f"**Month comparison (Net Revenue):**"]
        lines.append(f"• {lm_l}: **{_inr(lm)}**")
        lines.append(f"• {ly_l}: **{_inr(ly)}**")
        if yoy is not None:
            arrow = "▲ +" if yoy >= 0 else "▼ "
            verdict = "higher" if yoy >= 0 else "lower"
            lines.append(f"• YoY change: **{arrow}{yoy}%** — **{verdict}** than the same month last year.")
        elif ly == 0:
            lines.append("• No data for the same month last year, so % change could not be computed.")
        lines.append(f"• This month (running): {_inr(tm)}")
        return "\n".join(lines)
    if a == "chat":
        k = summary.get("period_kpis") or {}
        rev_line = (f"All-time revenue {_inr(k.get('total'))}; this month {_inr(k.get('this_month'))}.\n"
                    if (k.get('total') or k.get('this_month')) else "")
        return ("Hello! I am **Cosa AI**, your business assistant.\n"
                f"The catalog currently has **{summary.get('total_skus',0)} SKUs**. " + rev_line +
                "Ask me about *top sellers*, *out of stock items*, *any SKU's details*, "
                "*category-wise sales*, *forecasts* — anything.")
    if a == "sku_lookup":
        if not items:
            return "This SKU was not found in the catalog. Please check the code and try again."
        met = summary.get("metric") or ""
        met_label = summary.get("metric_label") or met
        period_metric = met in ("qty_7d","qty_15d","qty_1m","qty_3m","qty_6m","qty_1y",
                                "rev_yesterday","rev_month","rev_fy","rev_prev_fy","forecast_30d")
        lines = [f"**{len(items)} SKU{'s' if len(items)>1 else ''} found:**"]
        for i in items[:4]:
            if period_metric:
                v = i.get(met, 0)
                v_txt = _inr(v) if met.startswith("rev") else f"{int(round(float(v or 0)))} pcs"
                lines.append(f"• **{i['sku']}** — *{met_label}*: **{v_txt}** | "
                             f"Stock {i['inv_stock']} (+{i['inv_wip']} WIP)")
            else:
                ml = (msg or "").lower()
                want = []
                if re.search(r"stock|inventory|inv\b|bach[ae]", ml):
                    want.append(f"Stock **{i['inv_stock']}** (+{i['inv_wip']} WIP)")
                if re.search(r"revenue|sale|kamai|amount|₹|becha", ml):
                    want.append(f"Revenue **{_inr(i['total_net_revenue'])}**")
                if re.search(r"qty|quantity|kitn[ae]\s*(pc|piece|bik)|units", ml):
                    want.append(f"Qty **{i['final_qty']} pcs**")
                if re.search(r"mrp|price|daam|rate", ml) and i.get('mrp'):
                    want.append(f"MRP **₹{int(i['mrp'] or 0)}**")
                if re.search(r"dimension|size|naap|length|width|height|kitna bada", ml) and i.get('dimensions'):
                    want.append(f"Dimensions **{i['dimensions']}**")
                if re.search(r"customer|client|party", ml):
                    want.append(f"**{i['customer_count']}** customers")
                if re.search(r"status|halat", ml):
                    want.append(f"Status *{i['status']}*")
                if not want:
                    want = [f"Stock **{i['inv_stock']}** (+{i['inv_wip']} WIP)",
                            f"qty {i['final_qty']}"]
                    if i.get('total_net_revenue'):
                        want.append(f"revenue {_inr(i['total_net_revenue'])}")
                    want.append(f"*{i['status']}*")
                lines.append(f"• **{i['sku']}** — " + " | ".join(want))
        return "\n".join(lines)
    if a == "briefing":
        k = summary.get("kpis") or {}
        tm = summary.get("top_movers_7d") or []
        lines = ["**Business Briefing**"]
        if any(k.get(x) for x in ("yesterday", "this_month", "this_fy")):
            lines.append(f"• Yesterday: **{_inr(k.get('yesterday'))}** | This month: **{_inr(k.get('this_month'))}** | This FY: {_inr(k.get('this_fy'))}")
        lines.append(f"• Catalog: {summary.get('total_skus',0)} SKUs | Slow movers holding stock: {summary.get('slow_movers_with_stock',0)}")
        if tm:
            lines.append("• Hot this week: " + ", ".join(f"**{t['sku']}** ({t['qty_7d']} pcs)" for t in tm[:3]))
        urgent = summary.get("restock_urgent") or []
        oos = summary.get("out_of_stock_but_selling", 0)
        lsf = summary.get("low_stock_fast_sellers", 0)
        if oos or lsf:
            lines.append(f"• ⚠ Restock alert: {oos} selling SKUs are OUT of stock, {lsf} fast sellers are low" +
                         (f" — priority: {', '.join(urgent[:4])}" if urgent else ""))
        return "\n".join(lines)

    if a == "forecast":
        flt = summary.get("filters") or {}
        bits = []
        if flt.get("type"): bits.append(f"*{flt['type']}*")
        if flt.get("customer"): bits.append(f"*{flt['customer']}*")
        if flt.get("taxon"): bits.append(f"*{flt['taxon']}*")
        where = (" (" + ", ".join(bits) + ")") if bits else ""
        pm = summary.get("projected_month_total") or {}
        sf = summary.get("month_so_far") or {}
        pr = summary.get("projected_remaining") or {}
        hz = str(summary.get('horizon') or '')
        has_rev = "revenue" in (pm or {})
        if hz.startswith('agle') or hz.startswith('next'):
            est = f"**~{_inr(pr.get('revenue'))} ({pr.get('qty',0)} pcs)**" if has_rev else f"**~{pr.get('qty',0)} pcs**"
            lines = [f"**{hz}**{where} projection ({summary.get('method')}):",
                     f"• Estimate: {est}"]
        elif has_rev:
            lines = [f"**{hz}**{where} projection ({summary.get('method')}):",
                     f"• So far: {_inr(sf.get('revenue'))} ({sf.get('qty',0)} pcs) | "
                     f"Next {summary.get('days_remaining',0)} days: ~{_inr(pr.get('revenue'))} ({pr.get('qty',0)} pcs)",
                     f"• **Projected month total: {_inr(pm.get('revenue'))} ({pm.get('qty',0)} pcs)**"]
        else:
            lines = [f"**{hz}**{where} projection ({summary.get('method')}):",
                     f"• So far: {sf.get('qty',0)} pcs | Next {summary.get('days_remaining',0)} days: ~{pr.get('qty',0)} pcs",
                     f"• **Projected month total: {pm.get('qty',0)} pcs**"]
        tops = summary.get("top_predicted_skus") or []
        if tops:
            lines.append("Most likely top sellers:")
            for t in tops[:5]:
                if "pred_rev" in t:
                    lines.append(f"• **{t['sku']}** — ~{t['pred_qty']} pcs ({_inr(t['pred_rev'])})")
                else:
                    lines.append(f"• **{t['sku']}** — ~{t['pred_qty']} pcs")
        if summary.get("method") != "prophet":
            lines.append(f"_{summary.get('note','')}_")
        return "\n".join(lines)

    if a == "transactions":
        flt = summary.get("filters") or {}
        bits = []
        if flt.get("type"): bits.append(f"Type *{flt['type']}*")
        if flt.get("customer"): bits.append(f"Customer *{flt['customer']}*")
        if flt.get("taxon"): bits.append(f"Category *{flt['taxon']}*")
        where = (" — " + ", ".join(bits)) if bits else ""
        if not summary.get("transactions"):
            return (f"No sales entries found for **{summary.get('period_label','this period')}**{where}. "
                    "Please verify the period, type or SKU.")
        if "total_revenue" in summary:
            stat = f"• Revenue: **{_inr(summary.get('total_revenue'))}** | Qty: **{summary.get('total_qty',0)} pcs** | "
        else:
            stat = f"• Qty: **{summary.get('total_qty',0)} pcs** | "
        lines = [f"**{summary.get('period_label')}**{where}:",
                 stat + f"{summary.get('transactions',0)} entries | {summary.get('unique_skus',0)} unique SKUs"]
        tops = summary.get("top_skus") or []
        if tops:
            lines.append("Top SKUs:")
            for t in tops[:5]:
                if "revenue" in t:
                    lines.append(f"• **{t['sku']}** — {_inr(t['revenue'])} ({t['qty']} pcs)")
                else:
                    lines.append(f"• **{t['sku']}** — {t['qty']} pcs")
        tb = summary.get("type_breakup") or {}
        if len(tb) > 1 and not flt.get("type"):
            lines.append("Type-wise: " + ", ".join(f"*{k}* {_inr(v)}" for k, v in list(tb.items())[:4]))
        return "\n".join(lines)

    agg = summary.get("aggregates") or {}
    flt = summary.get("filters") or {}
    where = f" ({flt.get('taxon')})" if flt.get("taxon") else ""
    if a == "aggregate":
        met = summary.get("metric") or "total_net_revenue"
        n_skus = agg.get('matched_skus', 0)
        metric_map = {
            "rev_month":        ("Is mahine ka revenue", _inr(agg.get('sum_rev_month'))),
            "rev_yesterday":    ("Kal ka revenue", _inr(agg.get('sum_rev_yesterday'))),
            "rev_fy":           ("Is FY ka revenue", _inr(agg.get('sum_rev_fy'))),
            "rev_prev_fy":      ("Previous FY ka revenue", _inr(agg.get('sum_rev_prev_fy'))),
            "total_net_revenue":("All-time revenue", _inr(agg.get('sum_net_revenue'))),
            "final_qty":        ("Total quantity", f"{agg.get('sum_final_qty',0)} pcs"),
            "inv_stock":        ("Total stock", f"{agg.get('sum_stock',0)} (+{agg.get('sum_wip',0)} WIP)"),
            "total_inv":        ("Total inventory", f"{agg.get('sum_stock',0)} (+{agg.get('sum_wip',0)} WIP)"),
        }
        label, val = metric_map.get(met, metric_map["total_net_revenue"])
        if met.startswith("qty_"):
            label, val = _AI_METRICS.get(met, met), f"{int(agg.get('sum_final_qty',0))} pcs"
        return f"{label}{where}: **{val}**" + (f" ({n_skus} SKUs)" if where else "")
    label = summary.get("metric_label", "value")
    if not items:
        return f"No SKUs matched this filter{where}."
    top = summary.get("top_items") or []
    head = f"**Top {len(items)}{where}** by *{label}* 👇"
    def _v(x):
        return _inr(x) if "rev" in (summary.get("metric") or "") or summary.get("metric") == "total_net_revenue" else f"{int(round(float(x or 0))):,}"
    bl = [f"• **{t['sku']}** — {_v(t['value'])}" for t in top[:5]]
    return head + "\n" + "\n".join(bl)


# ── Marketplace Live Sync ───────────────────────────────────

MYNTRA_V4_SEARCH_URL = "https://api.pretr.com/partner/v4/inventory/search"
MYNTRA_V3_SEARCH_URL = "https://api.pretr.com/partner/v3/inventory/search"
MYNTRA_TOKEN_URL      = "https://api.pretr.com/authorization/generate_token"
MYNTRA_REFRESH_URL    = "https://api.pretr.com/authorization/refresh_token"

def _chunks(seq, size):
    for i in range(0, len(seq), size):
        yield seq[i:i+size]

def _safe_json(resp):
    try:
        return resp.json()
    except Exception:
        txt = (getattr(resp, "text", "") or "").strip()
        if not txt:
            return {}
        try:
            return json.loads(txt)
        except Exception:
            return {"raw_text": txt}

def _first_nonempty(*vals):
    for v in vals:
        if v is None:
            continue
        s = str(v).strip()
        if s:
            return s
    return ""

def _status_is_error(resp, body):
    if resp is not None and getattr(resp, "status_code", 0) in (401, 403):
        return True
    if isinstance(body, dict):
        st = str(body.get("statusType", "")).strip().upper()
        sc = body.get("statusCode")
        msg = str(body.get("statusMessage", body.get("message", ""))).lower()
        if st == "ERROR":
            return True
        if sc in (401, 403):
            return True
        if any(k in msg for k in ("invalid token", "expired", "unauthorized", "token required", "authentication")):
            return True
    return False

def _extract_token(resp, body):
    access = _first_nonempty(
        resp.headers.get("access_token") if resp else "",
        resp.headers.get("Access-Token") if resp else "",
        resp.headers.get("access-token") if resp else "",
        body.get("access_token") if isinstance(body, dict) else "",
        body.get("token") if isinstance(body, dict) else "",
        body.get("data", {}).get("access_token") if isinstance(body, dict) else "",
        body.get("data", {}).get("token") if isinstance(body, dict) else "",
    )
    refresh = _first_nonempty(
        resp.headers.get("refresh_token") if resp else "",
        resp.headers.get("Refresh-Token") if resp else "",
        resp.headers.get("refresh-token") if resp else "",
        body.get("refresh_token") if isinstance(body, dict) else "",
        body.get("data", {}).get("refresh_token") if isinstance(body, dict) else "",
    )
    return access, refresh

def _store_cfg():
    return {
        "merchant_id": _first_nonempty(os.getenv("MYNTRA_MERCHANT_ID"), MYNTRA_MERCHANT_ID),
        "secret_key": _first_nonempty(os.getenv("MYNTRA_SECRET_KEY"), MYNTRA_SECRET_KEY),
        "warehouse_code": _first_nonempty(os.getenv("MYNTRA_WAREHOUSE_CODE"), MYNTRA_WAREHOUSE_CODE, "cosanostraa"),
    }

def myntra_refresh_access_token(refresh_token, merchant_id):
    if not refresh_token:
        raise RuntimeError("Myntra refresh token missing")
    rr = requests.post(
        MYNTRA_REFRESH_URL,
        headers={"refresh_token": refresh_token, "Content-Type": "application/json"},
        json={"merchant_id": merchant_id},
        timeout=45,
    )
    body = _safe_json(rr)
    access, refresh = _extract_token(rr, body)
    return access, refresh or refresh_token, body, rr

def myntra_get_token(force=False):
    global MARKETPLACE_CACHE
    cfg = _store_cfg()
    if not cfg["merchant_id"] or not cfg["secret_key"]:
        raise RuntimeError("Myntra credentials are missing")

    token_info = (MARKETPLACE_CACHE.get("data") or {}).get("myntra_token") or {}
    if (not force and token_info.get("access_token") and time.time() - float(token_info.get("ts", 0)) < 20 * 24 * 3600):
        return token_info["access_token"], token_info.get("refresh_token", ""), cfg

    headers = {"secret_key": cfg["secret_key"], "Content-Type": "application/json"}
    payload = {"merchant_id": cfg["merchant_id"]}

    r = requests.post(MYNTRA_TOKEN_URL, headers=headers, json=payload, timeout=45)
    body = _safe_json(r)
    access, refresh = _extract_token(r, body)

    if not access:
        cached_refresh = _first_nonempty(token_info.get("refresh_token"), refresh)
        if cached_refresh:
            try:
                access2, refresh2, body2, rr = myntra_refresh_access_token(cached_refresh, cfg["merchant_id"])
                access = access2
                refresh = refresh2
                body = body2
                r = rr
            except Exception:
                pass

    if not access:
        msg = _first_nonempty(
            body.get("statusMessage") if isinstance(body, dict) else "",
            body.get("message") if isinstance(body, dict) else "",
            body.get("raw_text") if isinstance(body, dict) else "",
            f"Myntra token failed (HTTP {getattr(r, 'status_code', 'NA')})",
        )
        raise RuntimeError(msg)

    data = MARKETPLACE_CACHE.get("data") or {}
    data["myntra_token"] = {
        "access_token": access,
        "refresh_token": refresh,
        "ts": time.time(),
        "merchant_id": cfg["merchant_id"],
    }
    MARKETPLACE_CACHE["data"] = data
    MARKETPLACE_CACHE["ts"] = time.time()
    MARKETPLACE_CACHE["error"] = None
    return access, refresh, cfg

def _myntra_strategy_order():
    return [
        (MYNTRA_V4_SEARCH_URL, "json"),
        (MYNTRA_V4_SEARCH_URL, "form"),
        (MYNTRA_V4_SEARCH_URL, "data"),
        (MYNTRA_V3_SEARCH_URL, "json"),
        (MYNTRA_V3_SEARCH_URL, "form"),
        (MYNTRA_V3_SEARCH_URL, "data"),
    ]

def _request_inventory(url, token, store, batch, mode="json"):
    headers = {"access_token": token, "x-partner-store": store}
    if mode == "json":
        headers["Content-Type"] = "application/json"
        return requests.post(url, headers=headers, json=batch, timeout=60)
    if mode == "form":
        return requests.post(url, headers=headers, files={"List": (None, json.dumps(batch))}, timeout=60)
    if mode == "data":
        return requests.post(url, headers=headers, data={"List": json.dumps(batch)}, timeout=60)
    raise ValueError(f"Unknown mode: {mode}")

def _pick_store_row(stores, desired_store):
    desired = re.sub(r"[^a-z0-9]", "", str(desired_store).lower())
    fallback = None
    for st in stores:
        code = _first_nonempty(
            st.get("stores_code"), st.get("store_code"), st.get("storeCode"),
            st.get("warehouse_code"), st.get("warehouseCode"),
            st.get("code"), st.get("store"), st.get("name")
        )
        if fallback is None and code:
            fallback = (st, code)
        if re.sub(r"[^a-z0-9]", "", str(code).lower()) == desired:
            return st, code
    return (fallback if fallback else (None, ""))

def _qty_from_store(node):
    if not isinstance(node, dict):
        return int(round(to_num(node)))
    for key in (
        "inventoryCount", "inventorycount", "inventory_count",
        "availableQuantity", "available_quantity", "availableQty", "available_qty",
        "quantity", "qty", "count", "stock", "live_qty"
    ):
        if key in node:
            return int(round(to_num(node.get(key))))
    return 0

def _extract_inventory_entries(payload):
    entries = []
    seen = set()

    def add_node(node):
        try:
            key = json.dumps(node, sort_keys=True, default=str)
        except Exception:
            key = repr(node)
        if key in seen:
            return
        seen.add(key)
        entries.append(node)

    def walk(node):
        if isinstance(node, dict):
            if "sku" in node and any(k in node for k in ("stores", "inventoryCount", "inventorycount", "quantity", "qty", "availableQuantity", "available_quantity")):
                add_node(node)
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(payload)
    if entries:
        return entries

    if isinstance(payload, dict):
        for key in ("inventoryDetails", "inventory_details", "inventories", "items", "rows", "data", "result", "payload"):
            v = payload.get(key)
            if isinstance(v, list):
                return [x for x in v if isinstance(x, dict)]
            if isinstance(v, dict) and v.get("sku"):
                return [v]
    if isinstance(payload, list):
        return [x for x in payload if isinstance(x, dict)]
    return []

def _normalize_myntra_row(entry, desired_store, endpoint, mode):
    sku = _first_nonempty(entry.get("sku"), entry.get("sellerSku"), entry.get("seller_sku"), entry.get("itemSku"))
    stores = entry.get("stores")
    store_code = ""
    live_qty = 0
    all_store_qty = 0

    if isinstance(stores, list) and stores:
        picked, store_code = _pick_store_row(stores, desired_store)
        if picked:
            live_qty = _qty_from_store(picked)
        for st in stores:
            all_store_qty += _qty_from_store(st)
        if not live_qty and all_store_qty:
            live_qty = all_store_qty
        if not store_code:
            store_code = _first_nonempty(stores[0].get("stores_code"), stores[0].get("store_code"), stores[0].get("storeCode"), desired_store)
    else:
        live_qty = _qty_from_store(entry)
        store_code = _first_nonempty(entry.get("stores_code"), entry.get("store_code"), entry.get("storeCode"), entry.get("warehouse_code"), entry.get("warehouseCode"), desired_store)

    return {
        "sku": sku,
        "live_qty": int(live_qty or 0),
        "store_code": store_code or desired_store,
        "raw": entry,
        "endpoint": endpoint,
        "mode": mode,
    }

def _call_inventory_search_once(token, store, batch, endpoint, mode):
    resp = _request_inventory(endpoint, token, store, batch, mode=mode)
    body = _safe_json(resp)
    if _status_is_error(resp, body):
        msg = _first_nonempty(
            body.get("statusMessage") if isinstance(body, dict) else "",
            body.get("message") if isinstance(body, dict) else "",
            body.get("raw_text") if isinstance(body, dict) else "",
            f"HTTP {getattr(resp, 'status_code', 'NA')}"
        )
        return None, msg, resp, body
    entries = _extract_inventory_entries(body)
    rows = [_normalize_myntra_row(e, store, endpoint, mode) for e in entries]
    return rows, "", resp, body

def myntra_search_inventory(skus, force_token=False):
    token, refresh, cfg = myntra_get_token(force=force_token)
    store = cfg["warehouse_code"]

    clean_skus = []
    seen = set()
    for s in skus:
        ss = str(s).strip()
        if not ss:
            continue
        key = ss.upper()
        if key not in seen:
            seen.add(key)
            clean_skus.append(ss)

    rows = []
    errors = []
    attempts = []
    returned_keys = set()

    for batch in _chunks(clean_skus, 20):
        batch_rows = None
        batch_errs = []

        for endpoint, mode in _myntra_strategy_order():
            attempts.append(f"{endpoint.split('/')[-2]}/{mode}")
            try:
                rows_try, err, resp, body = _call_inventory_search_once(token, store, batch, endpoint, mode)
                if rows_try is None and _status_is_error(resp, body):
                    try:
                        new_access, new_refresh, body2, rr = myntra_refresh_access_token(refresh, cfg["merchant_id"])
                        if new_access:
                            token = new_access
                            refresh = new_refresh
                            data = MARKETPLACE_CACHE.get("data") or {}
                            data["myntra_token"] = {
                                "access_token": token,
                                "refresh_token": refresh,
                                "ts": time.time(),
                                "merchant_id": cfg["merchant_id"],
                            }
                            MARKETPLACE_CACHE["data"] = data
                            rows_try, err, resp, body = _call_inventory_search_once(token, store, batch, endpoint, mode)
                    except Exception:
                        pass

                if rows_try:
                    batch_rows = rows_try
                    break
                if err:
                    batch_errs.append(err)
            except Exception as e:
                batch_errs.append(str(e))

        if not batch_rows:
            for sku in batch:
                single_row = None
                for endpoint, mode in _myntra_strategy_order():
                    attempts.append(f"single:{endpoint.split('/')[-2]}/{mode}")
                    try:
                        rows_try, err, resp, body = _call_inventory_search_once(token, store, [sku], endpoint, mode)
                        if rows_try is None and _status_is_error(resp, body):
                            try:
                                new_access, new_refresh, body2, rr = myntra_refresh_access_token(refresh, cfg["merchant_id"])
                                if new_access:
                                    token = new_access
                                    refresh = new_refresh
                                    data = MARKETPLACE_CACHE.get("data") or {}
                                    data["myntra_token"] = {
                                        "access_token": token,
                                        "refresh_token": refresh,
                                        "ts": time.time(),
                                        "merchant_id": cfg["merchant_id"],
                                    }
                                    MARKETPLACE_CACHE["data"] = data
                                    rows_try, err, resp, body = _call_inventory_search_once(token, store, [sku], endpoint, mode)
                            except Exception:
                                pass

                        if rows_try:
                            single_row = rows_try[0]
                            break
                        if err:
                            batch_errs.append(f"{sku}: {err}")
                    except Exception as e:
                        batch_errs.append(f"{sku}: {e}")
                if single_row:
                    batch_rows = batch_rows or []
                    batch_rows.append(single_row)

        if batch_rows:
            for r in batch_rows:
                sku_key = str(r.get("sku", "")).strip().upper()
                if not sku_key:
                    continue
                returned_keys.add(sku_key)
                rows.append(r)
        errors.extend(batch_errs)

    missing = [s for s in clean_skus if str(s).strip().upper() not in returned_keys]
    coverage = round((len(returned_keys) / len(clean_skus) * 100.0), 1) if clean_skus else 0.0

    return {
        "marketplace": "myntra",
        "connected": True,
        "synced_at": now_ist().strftime("%Y-%m-%d %H:%M:%S"),
        "store_code": store,
        "merchant_id": cfg["merchant_id"],
        "query_count": len(clean_skus),
        "returned_count": len(returned_keys),
        "coverage": coverage,
        "count": len(rows),
        "live_total_qty": int(sum(r["live_qty"] for r in rows)),
        "low_stock": int(sum(1 for r in rows if r["live_qty"] <= 10)),
        "missing_count": len(missing),
        "missing_skus": missing[:250],
        "attempts": attempts[:80],
        "errors": errors[-50:],
        "items": rows,
    }

def _portal_cookie_dict(cookie_header):
    cookie_header = (cookie_header or "").strip()
    if not cookie_header:
        return {}
    out = {}
    if cookie_header.startswith("{"):
        try:
            obj = json.loads(cookie_header)
            if isinstance(obj, dict):
                return {str(k).strip(): str(v).strip() for k, v in obj.items() if str(k).strip()}
        except Exception:
            pass
    for part in cookie_header.split(";"):
        if "=" not in part:
            continue
        k, v = part.split("=", 1)
        k = k.strip()
        v = v.strip()
        if k:
            out[k] = v
    return out

def _portal_session():
    sess = requests.Session()
    sess.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0 Safari/537.36",
        "Accept-Language": "en-IN,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Referer": MYNTRA_PORTAL_BASE_URL,
    })
    cookies = _portal_cookie_dict(MYNTRA_PORTAL_COOKIE)
    for k, v in cookies.items():
        sess.cookies.set(k, v, domain=".myntrainfo.com")
    return sess

def _looks_like_login_or_loading(html_text):
    t = (html_text or "").lower()
    return ("loading" in t and len(t) < 5000) or ("login" in t and "password" in t and "partner portal" in t)

def _read_html_tables(html_text):
    tables = []
    try:
        from io import StringIO
        dfs = pd.read_html(StringIO(html_text))
        for df in dfs:
            if df is not None and not df.empty:
                tables.append(df)
    except Exception:
        pass
    return tables

def _normalize_table_to_items(df):
    cols = {str(c).strip().lower(): c for c in df.columns}
    sku_col = None
    qty_col = None
    store_col = None
    for cand in ("sku", "seller sku", "seller sku code", "seller_sku", "seller skucode", "skucode", "item sku", "product sku", "style id"):
        if cand in cols:
            sku_col = cols[cand]
            break
    for cand in ("qty", "quantity", "available qty", "available quantity", "inventory", "stock", "current stock", "live qty"):
        if cand in cols:
            qty_col = cols[cand]
            break
    for cand in ("store", "warehouse", "warehouse code", "store code", "location"):
        if cand in cols:
            store_col = cols[cand]
            break
    if sku_col is None and qty_col is None:
        return []
    out = []
    for _, row in df.iterrows():
        sku = clean(row.get(sku_col, "")) if sku_col else ""
        qty = to_int(row.get(qty_col, 0)) if qty_col else 0
        store = clean(row.get(store_col, MYNTRA_WAREHOUSE_CODE), MYNTRA_WAREHOUSE_CODE) if store_col else MYNTRA_WAREHOUSE_CODE
        if sku:
            out.append({"sku": sku, "live_qty": qty, "store_code": store, "raw": row.to_dict(), "endpoint": "portal/ops-reports", "mode": "html"})
    return out

def myntra_portal_ops_sync(skus, force=False):
    sess = _portal_session()
    resp = sess.get(MYNTRA_PORTAL_REPORT_URL, timeout=60, allow_redirects=True)
    html = getattr(resp, "text", "") or ""
    if _looks_like_login_or_loading(html):
        return {
            "marketplace": "myntra",
            "connected": False,
            "synced_at": now_ist().strftime("%Y-%m-%d %H:%M:%S"),
            "store_code": MYNTRA_WAREHOUSE_CODE,
            "merchant_id": MYNTRA_MERCHANT_ID,
            "query_count": len(skus),
            "returned_count": 0,
            "coverage": 0.0,
            "count": 0,
            "live_total_qty": 0,
            "low_stock": 0,
            "missing_count": len(skus),
            "missing_skus": [str(s) for s in skus[:250]],
            "attempts": ["portal/ops-reports"],
            "errors": [
                "Portal session not authenticated or page is JS-loaded.",
                "Set MYNTRA_PORTAL_COOKIE as a browser session cookie string, then resync."
            ],
            "items": [],
            "portal_url": MYNTRA_PORTAL_REPORT_URL,
        }

    items = []
    parsed_tables = _read_html_tables(html)
    for df in parsed_tables:
        items.extend(_normalize_table_to_items(df))

    clean_skus = []
    seen = set()
    for s in skus:
        ss = str(s).strip()
        if not ss:
            continue
        k = ss.upper()
        if k not in seen:
            seen.add(k)
            clean_skus.append(ss)

    if items:
        item_map = {str(i["sku"]).strip().upper(): i for i in items if i.get("sku")}
        rows = []
        returned = set()
        for sku in clean_skus:
            key = sku.upper()
            if key in item_map:
                rows.append(item_map[key])
                returned.add(key)
        if not rows:
            rows = items[:]
            returned = {str(i["sku"]).strip().upper() for i in rows if i.get("sku")}
    else:
        rows = []
        returned = set()

    missing = [s for s in clean_skus if s.upper() not in returned]
    coverage = round((len(returned) / len(clean_skus) * 100.0), 1) if clean_skus else 0.0

    return {
        "marketplace": "myntra",
        "connected": True,
        "synced_at": now_ist().strftime("%Y-%m-%d %H:%M:%S"),
        "store_code": MYNTRA_WAREHOUSE_CODE,
        "merchant_id": MYNTRA_MERCHANT_ID,
        "query_count": len(clean_skus),
        "returned_count": len(returned),
        "coverage": coverage,
        "count": len(rows),
        "live_total_qty": int(sum(to_num(r.get("live_qty", 0)) for r in rows)),
        "low_stock": int(sum(1 for r in rows if to_num(r.get("live_qty", 0)) <= 10)),
        "missing_count": len(missing),
        "missing_skus": missing[:250],
        "attempts": [f"portal:{MYNTRA_PORTAL_REPORT_URL}"],
        "errors": [],
        "items": rows,
        "portal_url": MYNTRA_PORTAL_REPORT_URL,
    }

def get_marketplaces(force=False):
    global MARKETPLACE_CACHE
    if not force and MARKETPLACE_CACHE.get("data") and (time.time() - MARKETPLACE_CACHE.get("ts", 0) < MARKETPLACE_TTL):
        return MARKETPLACE_CACHE["data"]

    master, *_ = get_data(False)
    skus = [i.get("sku") for i in (master or []) if i.get("sku")]

    out = {
        "synced_at": now_ist().strftime("%Y-%m-%d %H:%M:%S"),
        "myntra": {"connected": False, "items": [], "count": 0, "live_total_qty": 0, "low_stock": 0, "coverage": 0, "errors": []},
        "nykaa": {"connected": False, "items": [], "count": 0, "live_total_qty": 0, "low_stock": 0, "errors": ["Pending integration"]},
        "ajio": {"connected": False, "items": [], "count": 0, "live_total_qty": 0, "low_stock": 0, "errors": ["Pending integration"]},
        "tata": {"connected": False, "items": [], "count": 0, "live_total_qty": 0, "low_stock": 0, "errors": ["Pending integration"]},
        "flipkart": {"connected": False, "items": [], "count": 0, "live_total_qty": 0, "low_stock": 0, "errors": ["Pending integration"]},
    }

    portal_err = None
    try:
        portal_result = myntra_portal_ops_sync(skus, force=force)
        out["myntra"] = portal_result
        if not portal_result.get("connected"):
            portal_err = "; ".join(portal_result.get("errors", []) or []) or "Portal sync unavailable"
    except Exception as e:
        portal_err = str(e)

    if (not out["myntra"].get("connected")) or (not out["myntra"].get("items")):
        try:
            api_result = myntra_search_inventory(skus, force_token=force)
            if not out["myntra"].get("items"):
                out["myntra"] = api_result
            else:
                out["myntra"]["api_fallback"] = api_result
            if portal_err:
                out["myntra"]["errors"] = list(dict.fromkeys((out["myntra"].get("errors") or []) + [portal_err]))
        except Exception as e:
            if portal_err:
                out["myntra"]["errors"] = list(dict.fromkeys((out["myntra"].get("errors") or []) + [portal_err, str(e)]))
            else:
                out["myntra"]["errors"] = [str(e)]

    MARKETPLACE_CACHE["data"] = out
    MARKETPLACE_CACHE["ts"] = time.time()
    MARKETPLACE_CACHE["error"] = portal_err
    return out
# ── HTML ─────────────────────────────────────────────────────
HTML = r"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Cosa Nostraa — Live Dashboard</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&family=Playfair+Display:wght@600;800;900&family=Space+Grotesk:wght@500;700&family=Inter:wght@300;400;500;600;700;800&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Montserrat',sans-serif;background:#080808;color:#e8d5a3;min-height:100vh;display:flex;flex-direction:column}

/* ── HERO ── */
.hero{
  text-align:center;
  padding:34px 20px 30px;
  border-bottom:1px solid rgba(212,175,90,.18);
  position:relative;
  background:linear-gradient(135deg,#0b1020 0%,#0f172a 48%,#09111f 100%);
  min-height:180px;
  display:flex;
  align-items:center;
  justify-content:center;
}
.hero-only{text-align:center;max-width:1000px;padding:0 16px}
.hero-title{
  font-size:clamp(28px,4.8vw,66px);
  font-weight:1000;
  letter-spacing:clamp(2px,.5vw,8px);
  line-height:1.02;
  text-transform:uppercase;
  color:#fff6df;
  text-shadow:0 12px 40px rgba(0,0,0,.45);
}
.hero-dev{
  margin-top:12px;
  font-size:clamp(11px,1.25vw,16px);
  letter-spacing:clamp(2px,.35vw,5px);
  color:#d4af5a;
  text-transform:uppercase;
  font-weight:800;
}
.brand{font-weight:900;font-size:40px;letter-spacing:10px;color:#d4af5a;text-transform:uppercase;text-shadow:0 0 40px rgba(212,175,90,.25)}
.brand-sub{font-size:9px;letter-spacing:5px;color:#6a5a2a;margin-top:6px;text-transform:uppercase;font-weight:600}
.gold-line{width:100px;height:1px;background:linear-gradient(90deg,transparent,#d4af5a,transparent);margin:14px auto 0}
.sync-btn{position:absolute;right:20px;top:40px;background:#111;border:1px solid #d4af5a;color:#d4af5a;padding:9px 16px;border-radius:5px;cursor:pointer;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:1.5px;transition:.2s}
.sync-btn:hover{background:#d4af5a;color:#080808}
.dbg-btn{position:absolute;right:74px;top:40px;background:#111;border:1px solid #2a2a2a;color:#555;padding:9px 16px;border-radius:5px;cursor:pointer;font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:1px}
.dbg-btn:hover{border-color:#555;color:#888}

/* ── TABS ── */
.tabs{display:flex;justify-content:center;gap:8px;padding:18px 20px;border-bottom:1px solid #151515;flex-wrap:wrap;background:#050505;position:sticky;top:12px;z-index:45}
.hero.hidden-hero{display:none !important}
.tab{background:#111;border:1px solid rgba(212,175,90,.18);color:#6a5a2a;padding:11px 28px;border-radius:5px;cursor:pointer;font-size:11px;letter-spacing:2.5px;text-transform:uppercase;font-weight:700;transition:.2s}
.tab:hover{border-color:#d4af5a;color:#e8d5a3;background:#161616}
.tab.active{background:linear-gradient(135deg,#d4af5a 0%,#a07830 100%);color:#080808;border-color:transparent;box-shadow:0 4px 20px rgba(212,175,90,.3)}

/* ── LOADER ── */
#loader{display:none;text-align:center;padding:60px 20px;color:#d4af5a;font-size:10px;letter-spacing:3px;background:#0f0f0f;border:1px solid rgba(212,175,90,.2);border-radius:10px;margin:20px}
.spin{width:40px;height:40px;border:2px solid #1a1a1a;border-top:2px solid #d4af5a;border-radius:50%;animation:spin 1s linear infinite;margin:0 auto 18px}
@keyframes spin{to{transform:rotate(360deg)}}

/* ── DEBUG ── */
#dbgbox{display:none;background:#0a0a0a;border:1px solid #2a2a2a;border-radius:8px;margin:14px 20px;padding:18px;font-family:monospace;font-size:11px;color:#6f9;white-space:pre-wrap;word-break:break-word;max-height:340px;overflow:auto}

/* ── LAYOUT ── */
.wrap{max-width:1600px;margin:0 auto;padding:0 20px;flex:1;width:100%}

/* ── KPIs ── */
.kpis{display:flex;flex-wrap:wrap;justify-content:center;gap:14px;padding:22px 0 18px}
.kpi{background:linear-gradient(145deg,#141414,#0e0e0e);border:1px solid rgba(212,175,90,.18);border-radius:10px;padding:18px 28px;min-width:185px;text-align:center;transition:.2s}
.kpi:hover{border-color:rgba(212,175,90,.45);box-shadow:0 8px 24px rgba(0,0,0,.5)}
.kpi-t{font-size:8.5px;letter-spacing:2.5px;text-transform:uppercase;color:#6a5a2a;margin-bottom:8px;font-weight:700}
.kpi-v{font-size:24px;color:#2ecc71;font-weight:900}

/* ── FILTER BOX ── */
.filter-box{background:#0f0f0f;border:1px solid rgba(212,175,90,.12);border-radius:10px;padding:18px;margin-bottom:18px}
.fg{display:grid;grid-template-columns:repeat(auto-fit,minmax(175px,1fr));gap:14px;align-items:end}
.fc{display:flex;flex-direction:column}
.fl{font-size:8.5px;letter-spacing:1.5px;text-transform:uppercase;color:#d4af5a;margin-bottom:6px;font-weight:700}
.fi,.fs{width:100%;padding:10px 12px;background:#161616;border:1px solid rgba(212,175,90,.25);border-radius:5px;color:#e8d5a3;font-size:11px;font-weight:600;outline:none;transition:.2s}
.fi:focus,.fs:focus{border-color:#d4af5a;background:#1a1a1a}
.fs[multiple]{height:76px}

/* ── GRID (cards) ── */
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(265px,1fr));gap:18px;padding-bottom:50px}
.card{background:#111;border:1px solid rgba(212,175,90,.12);border-radius:10px;overflow:hidden;transition:.3s;cursor:default}
.card:hover{transform:translateY(-5px);border-color:rgba(212,175,90,.55);box-shadow:0 12px 35px rgba(0,0,0,.7)}
.img-box{height:215px;background:#050505;display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden}
.img-box img{width:100%;height:100%;object-fit:cover}
.img-ph{font-size:44px;color:#1e1e1e}
.badge-conf{position:absolute;top:10px;right:10px;background:rgba(212,175,90,.95);color:#080808;font-size:10px;font-weight:800;padding:4px 10px;border-radius:5px}
.badge-status{position:absolute;top:10px;left:10px;background:rgba(0,0,0,.75);color:#d4af5a;font-size:8px;font-weight:700;padding:4px 10px;border-radius:12px;letter-spacing:1.5px;text-transform:uppercase;border:1px solid rgba(212,175,90,.3)}
.badge-inv{position:absolute;bottom:10px;right:10px;background:rgba(212,175,90,.9);color:#080808;font-size:9px;font-weight:700;padding:4px 10px;border-radius:12px}
.cb{padding:16px}
.sku{font-size:16px;color:#d4af5a;margin-bottom:10px;font-weight:900;letter-spacing:1px}
.row{display:flex;justify-content:space-between;padding:5px 0;border-bottom:1px solid rgba(255,255,255,.04);font-size:11px}
.row span:first-child{color:#5a4a2a;font-weight:600}
.row span:last-child{color:#e8d5a3;font-weight:800}
.sg{display:grid;grid-template-columns:repeat(4,1fr);gap:5px;margin-top:10px}
.sc{background:#0c0c0c;border:1px solid #1a1a1a;border-radius:4px;padding:6px;text-align:center}
.sl{font-size:7.5px;letter-spacing:1px;color:#4a4a2a;text-transform:uppercase;margin-bottom:3px;font-weight:700}
.sv{font-size:14px;font-weight:900}
.sv.z{color:#e74c3c}.sv.l{color:#e67e22}.sv.g{color:#2ecc71}

/* ── REPEAT ORDERS TABLE ── */
.ro-wrap{padding-bottom:50px}
.ro-table-wrap{overflow:auto;max-height:72vh;border-radius:10px;border:1px solid rgba(212,175,90,.15)}
table.ro{width:100%;border-collapse:collapse;background:#0d0d0d;font-size:11px}
table.ro thead tr{background:linear-gradient(90deg,#161616,#111)}
table.ro thead th{padding:13px 14px;text-align:left;font-size:9px;letter-spacing:2px;text-transform:uppercase;color:#d4af5a;font-weight:700;border-bottom:1px solid rgba(212,175,90,.2);white-space:nowrap}
table.ro tbody tr{border-bottom:1px solid rgba(255,255,255,.04);transition:.15s}
table.ro tbody tr:hover{background:rgba(212,175,90,.05)}
table.ro td{padding:10px 14px;vertical-align:middle;font-weight:700;color:#e8d5a3;white-space:nowrap}
table.ro td.muted{color:#5a4a2a;font-weight:600}
table.ro td.green{color:#2ecc71;font-weight:800}
table.ro td.gold{color:#d4af5a;font-weight:800}
table.ro td.orange{color:#e67e22;font-weight:800}
table.ro td.red{color:#e74c3c;font-weight:800}
/* Google-Sheets-style column filters */
.ro-col-filters{display:flex;flex-wrap:nowrap;gap:6px;align-items:center;padding:8px 10px 8px;background:#f8fafc;border:1px solid rgba(212,175,90,.15);border-radius:8px 8px 0 0;border-bottom:none;overflow-x:auto}
.ro-col-filters .cf-group{display:flex;flex-direction:column;gap:2px;min-width:90px;flex-shrink:0}
.ro-col-filters .cf-group label{font-size:8px;letter-spacing:1.5px;text-transform:uppercase;font-weight:700;color:#8c7a42;white-space:nowrap}
.ro-col-filters .cf-group select,.ro-col-filters .cf-group input{font-size:11px;padding:4px 6px;border:1px solid #d1c090;border-radius:5px;background:#fff;color:#111;outline:none;width:100%;font-weight:600}
.ro-col-filters .cf-group select:focus,.ro-col-filters .cf-group input:focus{border-color:#d4af5a;box-shadow:0 0 0 2px rgba(212,175,90,.2)}
.ro-col-filters .cf-reset{align-self:flex-end;padding:5px 10px;font-size:9px;letter-spacing:1.5px;background:#d4af5a;color:#000;border:none;border-radius:5px;font-weight:800;cursor:pointer;text-transform:uppercase;white-space:nowrap}
.ro-col-filters .cf-reset:hover{background:#c9a84c}
.sku-cell{display:flex;align-items:center;gap:10px}
.sku-thumb{width:44px;height:44px;object-fit:cover;border-radius:5px;border:1px solid rgba(212,175,90,.2);background:#050505;flex-shrink:0}
.sku-name{font-size:12px;font-weight:800;color:#d4af5a;letter-spacing:.5px}
.forecast-pill{background:rgba(46,204,113,.15);border:1px solid rgba(46,204,113,.35);color:#2ecc71;padding:3px 10px;border-radius:12px;font-size:10px;font-weight:800;display:inline-block}

.go-btn{width:100%;padding:12px;background:linear-gradient(135deg,#d4af5a,#a07830);color:#080808;border:none;border-radius:5px;font-size:11px;font-weight:800;letter-spacing:3px;text-transform:uppercase;cursor:pointer;transition:.2s}
.go-btn:hover{opacity:.9;transform:translateY(-1px)}
.go-btn:disabled{background:#1a1a1a;color:#333;cursor:not-allowed;transform:none}
.upload-area{background:#0f0f0f;border:1.5px dashed rgba(212,175,90,.35);border-radius:10px;padding:44px 20px;text-align:center;cursor:pointer;max-width:600px;margin:0 auto 20px;transition:.2s}
.upload-area:hover{background:#141414;border-color:#d4af5a}
#preview{display:none;margin:18px auto 0;max-width:100%;max-height:240px;border-radius:8px;border:1px solid rgba(212,175,90,.25)}
.no-data{grid-column:1/-1;text-align:center;padding:70px;color:#2a2a2a;font-size:11px;letter-spacing:3px;text-transform:uppercase}
.tno-data{text-align:center;padding:50px;color:#2a2a2a;font-size:11px;letter-spacing:3px}
.small-note{font-size:10px;color:#6a5a2a;line-height:1.6;font-weight:600}
.sort-arrow{cursor:pointer;user-select:none}
.sort-arrow:after{content:' ↕';color:#4a3a1a}
.sort-arrow.asc:after{content:' ↑';color:#d4af5a}
.sort-arrow.desc:after{content:' ↓';color:#d4af5a}
footer{background:#040404;border-top:1px solid rgba(212,175,90,.08);padding:28px;text-align:center;margin-top:auto}
.fb{font-weight:900;font-size:17px;letter-spacing:6px;color:#d4af5a;text-transform:uppercase}
.fd{font-size:10px;letter-spacing:3px;color:#2a2a2a;text-transform:uppercase;margin-top:8px;font-weight:700}

/* ========= Light theme overrides ========= */
body{background:#f6f8fc;color:#1f2937}
.hero{background:linear-gradient(180deg,#ffffff,#f8fafc);border-bottom:1px solid #e5e7eb}
.tabs{background:#f8fafc;border-bottom:1px solid #e5e7eb}
.tab{background:#ffffff;border:1px solid #d7dde8;color:#6b7280}
.tab:hover{background:#f8fafc;color:#111827}
.tab.active{background:linear-gradient(135deg,#d4af5a,#c48d26);color:#11;border-color:transparent;box-shadow:0 8px 22px rgba(180,137,43,.18)}
#loader{background:#ffffff;border:1px solid #e5e7eb;color:#b8860b;box-shadow:0 10px 28px rgba(15,23,42,.05)}
#dbgbox{background:#ffffff;border:1px solid #e5e7eb;color:#1f7a56}
.wrap{padding-top:2px}
.kpi,.filter-box,.card,.ro-table-wrap,.upload-area,#vFinder>div:last-child{background:#ffffff;border-color:#e5e7eb;box-shadow:0 10px 24px rgba(15,23,42,.05)}
.kpi-t,.fl,.small-note,.brand-sub,.fd{color:#8c7a42}
.kpi-v,.sku,.row span:last-child,.fb,.brand{color:#b8860b}
.fi,.fs{background:#ffffff;color:#111827;border:1px solid #d8dee9}
.fi::placeholder{color:#94a3b8}
.filter-box{background:#ffffff}
.fi,.fs,.fi:focus,.fs:focus,.fs[multiple],input.fi[type="date"],select.fs{background:#ffffff !important}
.sku-checklist{background:#ffffff !important}
.ro-remark{width:100%;min-width:70px;padding:5px 7px;border:1px solid #d8dee9;border-radius:6px;font-size:12px;background:#fff;color:#1f2937;font-family:inherit}
.ro-remark:focus{outline:none;border-color:#b8924a;box-shadow:0 0 0 2px rgba(184,146,74,.15)}
.no-data,.tno-data{color:#94a3b8}
.img-box{background:#f3f4f6}
.img-ph{color:#d1d5db}
.row{border-bottom:1px solid #f1f5f9}
.row span:first-child{color:#64748b}
.sg .sc{background:#f8fafc;border:1px solid #e5e7eb}
.sl{color:#94a3b8}
.sv{color:#111827}
.sv.g{color:#15803d}.sv.l{color:#d97706}.sv.z{color:#dc2626}
.badge-status{background:#f1f5f9;color:#475569;border:1px solid #e2e8f0}
.badge-inv{background:#fef3c7;color:#92400e}
.badge-conf{background:#d4af5a;color:#111}
table.ro{background:#ffffff;color:#111827}
table.ro thead tr{background:#f8fafc}
table.ro thead th{color:#8c7a42;border-bottom:1px solid #e5e7eb}
table.ro tbody tr:hover{background:#f8fafc}
table.ro td{color:#334155;border-bottom:1px solid #eef2f7}
table.ro td.green{color:#15803d}
.ro-col-filters{background:#f0f4f8;border-color:#e5e7eb}
.ro-col-filters .cf-group label{color:#6b7280}
.ro-col-filters .cf-group select,.ro-col-filters .cf-group input{background:#fff;color:#111;border-color:#d1d5db}
table.ro td.gold{color:#b8860b}
table.ro td.orange{color:#d97706}
table.ro td.red{color:#dc2626}
.sku-checklist{max-height:210px;overflow:auto;padding:10px;background:#ffffff;border:1px solid #d8dee9;border-radius:8px;display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:8px}
.sku-opt{display:flex;align-items:center;gap:8px;padding:7px 8px;border:1px solid #eef2f7;border-radius:8px;background:#fbfdff;font-size:11px;color:#111827}
.sku-opt:hover{background:#f8fafc}
.sku-opt input{accent-color:#b8860b}

.type-checks{display:flex;flex-wrap:wrap;gap:8px;max-height:120px;overflow:auto;padding:8px;background:#ffffff;border:1px solid #d8dee9;border-radius:8px}
.type-opt{display:flex;align-items:center;gap:7px;padding:6px 10px;border:1px solid #eef2f7;border-radius:8px;background:#fbfdff;font-size:11px;color:#111827;cursor:pointer;font-weight:600}
.type-opt:hover{background:#f3f6fb}
.type-opt input{accent-color:#b8860b;width:15px;height:15px;cursor:pointer}

.type-breakdown{display:flex;flex-wrap:wrap;gap:12px}
.td-card{background:#fbfdff;border:1px solid #e5e7eb;border-radius:10px;padding:12px 16px;min-width:160px;box-shadow:0 6px 16px rgba(15,23,42,.04)}
.td-type{font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:#b8860b;margin-bottom:8px;border-bottom:1px solid #eef2f7;padding-bottom:6px}
.td-row{display:flex;justify-content:space-between;font-size:12px;padding:3px 0;color:#475569}
.td-row b{color:#111827;font-weight:800}
.td-row b.green{color:#15803d}

.fg{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:14px;align-items:stretch}
.fg .fc{background:#fbfdff;border:1px solid #eef2f7;border-radius:10px;padding:12px;min-height:96px;justify-content:flex-start}
.fg .fc .fl{margin-bottom:8px}
.ro-tools{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap;margin:8px 0 14px}
.ro-export{display:flex;gap:10px;flex-wrap:wrap}
.ro-export .go-btn{box-shadow:0 8px 18px rgba(15,23,42,.04)}

.ro-thumb-lg{width:110px;height:110px;border-radius:10px}
table.ro td{padding:12px 14px}
.ro-tick,#roSelectAll{width:18px;height:18px;cursor:pointer;accent-color:#b8860b}

.sku-name{cursor:pointer}
.sku-name:hover{text-decoration:underline}
.sku-link{background:none;border:none;color:#b8860b;font-weight:800;font-size:12px;letter-spacing:.5px;cursor:pointer;padding:0;text-align:left}
.sku-link:hover{text-decoration:underline}
.details-btn{background:#b8860b;color:#fff;border:none;border-radius:6px;padding:5px 10px;font-size:9px;font-weight:800;letter-spacing:1px;text-transform:uppercase;cursor:pointer;white-space:nowrap}
.details-btn:hover{opacity:.88}

.sd-head{display:flex;align-items:center;gap:20px;padding:22px;background:#ffffff;border:1px solid #e5e7eb;border-radius:12px;margin:18px 0;box-shadow:0 10px 24px rgba(15,23,42,.05)}
.sd-head-img img{width:120px;height:120px;object-fit:cover;border-radius:10px;border:1px solid #e5e7eb}
.sd-head-img .img-ph{width:120px;height:120px;display:flex;align-items:center;justify-content:center;font-size:48px;background:#f3f4f6;border-radius:10px;color:#d1d5db}
.sd-sku{font-size:26px;font-weight:900;letter-spacing:1px;color:#b8860b}
.sd-meta{margin-top:8px;font-size:12px;color:#64748b;font-weight:600;line-height:1.8}
.sd-meta span{display:inline-block;margin-right:18px}
.sd-meta b{color:#334155}


/* ===== Premium UI overrides ===== */
:root{
  --bg:#f4f7fb;
  --panel:#ffffff;
  --panel-soft:#f9fbff;
  --text:#0f172a;
  --muted:#64748b;
  --line:#e6ebf2;
  --line-2:#edf2f7;
  --gold:#b8860b;
  --gold-2:#d4af5a;
  --gold-soft:rgba(184,134,11,.10);
  --shadow:0 18px 50px rgba(15,23,42,.08);
  --shadow-2:0 10px 28px rgba(15,23,42,.06);
}

body{
  background:
    radial-gradient(circle at top left, rgba(212,175,90,.12), transparent 30%),
    radial-gradient(circle at top right, rgba(184,134,11,.10), transparent 26%),
    linear-gradient(180deg,#fbfdff 0%, #f4f7fb 100%);
  color:var(--text);
}

.hero{
  position:sticky;
  top:0;
  z-index:50;
  backdrop-filter: blur(10px);
  background:rgba(255,255,255,.82);
  border-bottom:1px solid rgba(230,235,242,.9);
  box-shadow:0 8px 30px rgba(15,23,42,.05);
}

.brand{
  letter-spacing:8px;
  font-size:clamp(28px,3vw,42px);
  background:linear-gradient(180deg,#f4d98a 0%, #d4af5a 40%, #9c7726 100%);
  -webkit-background-clip:text;
  background-clip:text;
  color:transparent;
  text-shadow:none;
}

.brand-sub{
  color:#8c7a42;
  letter-spacing:4px;
}

.tabs{
  position:sticky;
  top:116px;
  z-index:45;
  backdrop-filter: blur(10px);
  background:rgba(248,250,252,.86);
}

.tab{
  border-radius:999px;
  padding:10px 18px;
  border:1px solid #d9e1ea;
  color:#667085;
  background:#fff;
  box-shadow:0 4px 12px rgba(15,23,42,.03);
}

.tab.active{
  background:linear-gradient(135deg,#d4af5a 0%, #b8860b 100%);
  color:#fff;
  box-shadow:0 14px 24px rgba(184,134,11,.18);
}

.wrap{
  max-width:1560px;
  padding:0 18px 24px;
}

.kpi,.filter-box,.card,.ro-table-wrap,.upload-area,.sd-head,#vInsights .insight-card{
  background:var(--panel);
  border:1px solid var(--line);
  box-shadow:var(--shadow-2);
}

.kpi{
  border-radius:18px;
  padding:18px 20px;
  min-width:190px;
}

.kpi-v{
  color:#0f172a;
}

.kpi-t,.fl,.small-note,.brand-sub,.fd{
  color:var(--muted);
}

.filter-box{
  border-radius:22px;
  padding:18px;
}

.fg .fc{
  border-radius:16px;
  background:var(--panel-soft);
  border:1px solid var(--line-2);
}

.fi,.fs{
  border-radius:12px;
  border-color:#dbe3ed;
  background:#fff;
  color:var(--text);
}

.grid{
  grid-template-columns:repeat(auto-fill,minmax(285px,1fr));
  gap:18px;
}

.card{
  border-radius:22px;
  overflow:hidden;
  transition:transform .2s ease, box-shadow .2s ease, border-color .2s ease;
}

.card:hover{
  transform:translateY(-4px);
  box-shadow:0 22px 60px rgba(15,23,42,.10);
  border-color:rgba(184,134,11,.35);
}

.img-box{
  height:220px;
  background:linear-gradient(180deg,#f4f7fb 0%, #eef3f8 100%);
}

.badge-status{
  border-radius:999px;
  background:rgba(15,23,42,.78);
  color:#fff;
  border:none;
  padding:5px 10px;
}

.badge-conf{
  border-radius:999px;
  background:rgba(212,175,90,.95);
  color:#111;
}

.badge-inv{
  border-radius:999px;
  background:#ecfdf3;
  color:#15803d;
}

.cb{
  padding:16px 16px 18px;
}

.sku{
  font-size:15px;
  letter-spacing:.5px;
}

.row{
  padding:6px 0;
  font-size:12px;
  border-bottom:1px solid #f1f5f9;
}

.sg{
  gap:8px;
  margin-top:12px;
}

.sc{
  border-radius:12px;
  border:1px solid var(--line-2);
  background:#fbfdff;
}

.sv{
  color:#111827;
}

.pro-strip{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(165px,1fr));
  gap:12px;
  margin:6px 0 12px;
}

.pro-chip{
  background:linear-gradient(180deg,#fff,#fbfdff);
  border:1px solid var(--line);
  border-radius:18px;
  padding:14px 16px;
  box-shadow:var(--shadow-2);
}

.pro-chip .label{
  font-size:10px;
  letter-spacing:2px;
  text-transform:uppercase;
  color:#8a6d34;
  margin-bottom:6px;
  font-weight:800;
}

.pro-chip .value{
  font-size:22px;
  line-height:1;
  font-weight:900;
  color:#0f172a;
}

.pro-chip .sub{
  margin-top:6px;
  font-size:12px;
  color:var(--muted);
}

.pro-rail{
  display:flex;
  gap:10px;
  flex-wrap:wrap;
  margin:0 0 14px;
}

.pro-pill{
  background:#fff;
  border:1px solid var(--line);
  border-radius:999px;
  padding:8px 12px;
  font-size:11px;
  color:#475569;
  box-shadow:0 4px 10px rgba(15,23,42,.03);
}

.pro-pill b{
  color:#0f172a;
}

.card-actions{
  display:flex;
  gap:8px;
  margin-top:12px;
}

.mini-btn{
  flex:1;
  padding:10px 12px;
  border-radius:12px;
  border:1px solid #d8e0ea;
  background:#f8fafc;
  color:#0f172a;
  font-size:10px;
  letter-spacing:1.6px;
  text-transform:uppercase;
  font-weight:800;
  cursor:pointer;
}

.mini-btn:hover{
  background:#eef3f8;
}

.mini-btn.primary{
  border-color:rgba(184,134,11,.26);
  background:linear-gradient(135deg,#d4af5a,#b8860b);
  color:#fff;
}

.card-meta{
  margin-top:10px;
  display:flex;
  gap:8px;
  flex-wrap:wrap;
}

.meta-tag{
  font-size:10px;
  padding:5px 9px;
  border-radius:999px;
  background:#f8fafc;
  border:1px solid #e5eaf1;
  color:#475569;
}

.insights-head{
  display:flex;
  justify-content:space-between;
  align-items:flex-end;
  gap:14px;
  margin:8px 0 18px;
  flex-wrap:wrap;
}

.insights-title{
  font-size:28px;
  font-weight:900;
  letter-spacing:.2px;
  color:#111827;
}

.insights-sub{
  margin-top:6px;
  color:var(--muted);
  font-size:13px;
}

.insights-grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
  gap:16px;
}

.insight-card{
  border-radius:22px;
  padding:16px;
  min-height:290px;
}

.insight-card-head{
  display:flex;
  justify-content:space-between;
  align-items:center;
  gap:10px;
  margin-bottom:14px;
}

.insight-card h3{
  margin:0;
  font-size:16px;
  color:#111827;
}

.insight-pill{
  font-size:10px;
  letter-spacing:1.4px;
  text-transform:uppercase;
  font-weight:800;
  color:#8a6d34;
  background:var(--gold-soft);
  border:1px solid rgba(184,134,11,.12);
  border-radius:999px;
  padding:6px 10px;
}

.insight-pill.warn{
  color:#b45309;
  background:#fff7ed;
}

.insight-pill.ok{
  color:#15803d;
  background:#ecfdf3;
}

.insight-list{
  display:flex;
  flex-direction:column;
  gap:10px;
}

.insight-row{
  display:grid;
  grid-template-columns:1fr auto;
  gap:10px;
  align-items:center;
  padding:10px 12px;
  border:1px solid #edf2f7;
  background:#fbfdff;
  border-radius:14px;
}

.insight-row .name{
  font-size:12px;
  font-weight:800;
  color:#0f172a;
  margin-bottom:4px;
}

.insight-row .sub{
  font-size:11px;
  color:var(--muted);
}

.bar{
  height:7px;
  border-radius:999px;
  background:#e9eff5;
  overflow:hidden;
  margin-top:8px;
}

.bar > span{
  display:block;
  height:100%;
  border-radius:inherit;
  background:linear-gradient(90deg,#d4af5a,#b8860b);
}

.insight-val{
  font-size:12px;
  font-weight:900;
  color:#111827;
  text-align:right;
}

.insight-empty{
  padding:18px 12px;
  text-align:center;
  color:#94a3b8;
  font-size:12px;
}

@media (max-width: 900px){
  .tabs{top:104px}
  .brand{letter-spacing:5px}
  .grid{grid-template-columns:repeat(auto-fill,minmax(250px,1fr))}
}


/* ===== Ultra-premium home + menu ===== */
.menu-btn{
  position:static;
  background:#111;border:1px solid #d4af5a;color:#d4af5a;width:44px;height:44px;border-radius:12px;
  cursor:pointer;font-size:24px;font-weight:900;line-height:1;transition:.2s;display:flex;align-items:center;justify-content:center;flex:0 0 auto
}
.menu-btn:hover{background:#d4af5a;color:#111}
.nav-menu{
  position:fixed;left:16px;top:72px;min-width:250px;max-width:min(92vw,320px);display:none;background:#fff;border:1px solid #e5e7eb;border-radius:18px;
  box-shadow:0 24px 60px rgba(15,23,42,.18);padding:10px;z-index:120;max-height:calc(100vh - 88px);overflow:auto
}
.menu-item{
  width:100%;text-align:left;border:1px solid #eef2f7;background:#fbfdff;color:#111827;padding:11px 14px;border-radius:12px;margin:6px 0;
  font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase;cursor:pointer
}
.menu-item:hover,.menu-item.active{background:linear-gradient(135deg,#d4af5a,#c48d26);color:#111;border-color:transparent}
.home-shell{padding:18px 0 8px}
.home-hero{
  background:linear-gradient(135deg,#ffffff,#f8fafc);border:1px solid #e5e7eb;border-radius:28px;padding:24px 24px 20px;
  box-shadow:0 18px 44px rgba(15,23,42,.07);display:flex;justify-content:space-between;gap:18px;align-items:flex-end;flex-wrap:wrap
}
.home-kicker{
  font-size:11px;letter-spacing:3px;text-transform:uppercase;color:#8c7a42;font-weight:800;margin-bottom:10px
}
.home-title{
  font-size:34px;font-weight:1000;color:#b8860b;letter-spacing:.3px;line-height:1.05
}
.home-sub{margin-top:10px;color:#64748b;font-size:14px;max-width:760px;line-height:1.65;font-weight:600}
.home-actions{display:flex;gap:10px;flex-wrap:wrap;justify-content:flex-end}
.home-grid{
  display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin-top:16px
}
.home-card{
  background:#ffffff;border:1px solid #e5e7eb;border-radius:22px;padding:18px;box-shadow:0 12px 28px rgba(15,23,42,.05)
}
.home-card-title{font-size:14px;font-weight:900;color:#111827;margin-bottom:6px}
.home-card-sub{font-size:12px;color:#64748b;line-height:1.7}
.home-back{
  display:inline-flex;align-items:center;gap:8px;border:1px solid #e5e7eb;background:#fff;border-radius:12px;padding:10px 14px;
  font-weight:900;letter-spacing:1px;text-transform:uppercase;color:#111827;cursor:pointer
}
.home-back:hover{border-color:#d4af5a;color:#b8860b}
.insight-summary{
  display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px;margin:0 0 16px
}
.insight-summary-card{
  background:#fff;border:1px solid #e5e7eb;border-radius:20px;padding:14px 16px;box-shadow:0 12px 28px rgba(15,23,42,.05)
}
.insight-summary-card .label{font-size:10px;letter-spacing:2px;text-transform:uppercase;color:#8c7a42;font-weight:800;margin-bottom:8px}
.insight-summary-card .value{font-size:20px;font-weight:1000;color:#b8860b}


/* ===== Home / Insights premium overrides ===== */
.home-shell{padding:18px 0 8px}
.home-hero{
  background:linear-gradient(135deg,#0f172a 0%,#111827 55%,#0b0f18 100%);
  border:1px solid rgba(212,175,90,.18);
  border-radius:32px;
  padding:28px;
  box-shadow:0 28px 70px rgba(15,23,42,.14);
  align-items:flex-start;
  position:relative;
  overflow:hidden;
}
.home-hero:before{
  content:"";
  position:absolute;
  inset:-40% -20% auto auto;
  width:320px;height:320px;
  background:radial-gradient(circle, rgba(212,175,90,.18), transparent 65%);
  pointer-events:none;
}
.home-kicker{
  color:#e7c77a;
  font-size:10px;
  letter-spacing:4px;
  text-transform:uppercase;
  font-weight:900;
}
.home-title{
  font-size:44px;
  font-weight:1000;
  letter-spacing:2px;
  color:#fff7e1;
  text-transform:uppercase;
}
.home-sub{
  color:#d5dde9;
  font-size:14px;
  max-width:880px;
  line-height:1.8;
}
.home-actions{justify-content:flex-start}
.home-cta-note{
  color:#b7c2d3;
  font-size:11px;
  letter-spacing:2px;
  text-transform:uppercase;
  font-weight:800;
  margin-top:10px;
}
.matrix-page-title{
  font-size:22px;
  font-weight:1000;
  letter-spacing:3px;
  text-transform:uppercase;
  color:#111827;
  margin:18px 0 12px;
}
.home-minimal{
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:18px;
  flex-wrap:wrap;
  padding:22px 24px;
}
.home-minimal-copy{
  min-width:280px;
  flex:1;
}
.home-minimal-kicker{
  color:#b8860b;
  font-size:11px;
  font-weight:900;
  letter-spacing:4px;
  text-transform:uppercase;
}
.home-minimal-title{
  margin-top:8px;
  color:#111827;
  font-size:22px;
  font-weight:1000;
  letter-spacing:1px;
  text-transform:uppercase;
}
.home-minimal-note{
  margin-top:8px;
  color:#64748b;
  font-size:13px;
  line-height:1.8;
  max-width:760px;
}
.home-pill-row{
  display:flex;
  flex-wrap:wrap;
  gap:10px;
  justify-content:flex-end;
}
.home-pill{
  display:inline-flex;
  align-items:center;
  justify-content:center;
  padding:10px 14px;
  border-radius:999px;
  background:#f8fafc;
  border:1px solid #e5e7eb;
  color:#111827;
  font-size:11px;
  font-weight:900;
  letter-spacing:2px;
  text-transform:uppercase;
}
.home-stage{
  margin-top:16px;
  background:linear-gradient(180deg,#0d0d0f,#111214);
  border-radius:32px;
  border:1px solid rgba(212,175,90,.16);
  padding:26px;
  box-shadow:0 22px 58px rgba(15,23,42,.16);
}
.home-scroll-grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(320px,1fr));
  gap:20px;
  align-items:stretch;
}
.home-scroll{
  background:transparent;
  border:none;
  display:flex;
  flex-direction:column;
  align-items:center;
}
.home-scroll-top{
  color:#fff;
  font-size:42px;
  font-weight:1000;
  letter-spacing:6px;
  margin-bottom:16px;
  text-transform:uppercase;
}
.home-scroll-paper{
  position:relative;
  width:100%;
  min-height:380px;
  background:
    linear-gradient(180deg, rgba(255,246,220,.96), rgba(247,226,182,.96)),
    radial-gradient(circle at center, rgba(255,255,255,.7), transparent 55%);
  border:1px solid rgba(149,108,47,.22);
  border-radius:18px;
  box-shadow:inset 0 0 0 1px rgba(255,255,255,.25), 0 18px 32px rgba(0,0,0,.24);
  padding:52px 42px;
  display:flex;
  align-items:center;
  justify-content:center;
  text-align:center;
  color:#111827;
}
.home-scroll-paper:before,
.home-scroll-paper:after{
  content:"";
  position:absolute;
  top:10px; bottom:10px;
  width:34px;
  background:linear-gradient(180deg,#d7a05e,#efc485,#d7a05e);
  border-radius:999px;
  box-shadow:inset 0 0 16px rgba(0,0,0,.14);
}
.home-scroll-paper:before{left:-18px}
.home-scroll-paper:after{right:-18px}
.home-scroll-text{
  font-size:22px;
  line-height:1.65;
  font-weight:800;
  max-width:920px;
}
.home-scroll-text small{
  display:block;
  margin-top:14px;
  font-size:12px;
  letter-spacing:2px;
  text-transform:uppercase;
  color:#8a6d34;
  font-weight:900;
}
.home-grid{
  grid-template-columns:repeat(auto-fit,minmax(240px,1fr));
  margin-top:18px;
}
.home-card{
  border-radius:24px;
  padding:20px;
}
.home-card-title{
  font-size:15px;
  color:#0f172a;
}
.home-card-sub{
  font-size:12.5px;
  line-height:1.8;
}
.home-mini-note{
  margin-top:14px;
  display:inline-flex;
  align-items:center;
  gap:8px;
  padding:10px 14px;
  border-radius:999px;
  background:rgba(212,175,90,.12);
  border:1px solid rgba(212,175,90,.18);
  color:#e7c77a;
  font-size:10px;
  letter-spacing:2px;
  text-transform:uppercase;
  font-weight:900;
}
.insight-toolbar{
  background:#fff;
  border:1px solid #e5e7eb;
  border-radius:26px;
  padding:16px;
  box-shadow:0 12px 28px rgba(15,23,42,.05);
  margin-bottom:18px;
}
.insight-toolbar-head{
  display:flex;
  justify-content:space-between;
  gap:14px;
  align-items:flex-end;
  flex-wrap:wrap;
  margin-bottom:14px;
}
.insight-toolbar-head .title{
  font-size:18px;
  font-weight:1000;
  color:#111827;
}
.insight-toolbar-head .sub{
  margin-top:6px;
  color:#64748b;
  font-size:13px;
  line-height:1.6;
}
.insight-toolbar-actions{
  display:flex;
  gap:8px;
  flex-wrap:wrap;
}
.insight-toolbar .fg{
  grid-template-columns:repeat(auto-fit,minmax(210px,1fr));
}
.insight-toolbar .fc{
  min-height:unset;
}
.insight-summary{
  margin-bottom:16px;
}
.insight-card h3{
  font-size:15px;
}
.insight-list .insight-row .sub{
  line-height:1.5;
}


/* ===== Premium top app bar + navigation polish ===== */
.app-bar{
  position:sticky;
  top:0;
  z-index:70;
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:14px;
  padding:12px 18px;
  background:#ffffff;
  backdrop-filter:blur(16px);
  border-bottom:1px solid rgba(229,231,235,.95);
  box-shadow:0 10px 30px rgba(15,23,42,.05);
}
.app-bar-copy{
  display:flex;
  flex-direction:column;
  justify-content:center;
  min-width:0;
}
.app-bar-brand{
  font-size:12px;
  font-weight:1000;
  letter-spacing:4px;
  text-transform:uppercase;
  color:#b8860b;
  white-space:nowrap;
  overflow:hidden;
  text-overflow:ellipsis;
}
.app-bar-sub{
  margin-top:4px;
  font-size:10px;
  letter-spacing:3px;
  text-transform:uppercase;
  color:#64748b;
  font-weight:800;
}
.app-bar-actions{
  display:flex;
  align-items:center;
  gap:8px;
  flex-wrap:wrap;
  justify-content:flex-end;
}
.app-chip{
  border:1px solid #334155;
  background:#1e293b;
  color:#ffffff;
  border-radius:999px;
  padding:9px 14px;
  font-size:10px;
  font-weight:900;
  letter-spacing:2px;
  text-transform:uppercase;
  cursor:pointer;
  box-shadow:0 4px 12px rgba(15,23,42,.18);
}
.app-chip:hover{background:#0f172a;border-color:#475569;color:#ffffff}
.menu-btn{
  position:static;
  width:42px;
  height:42px;
  border-radius:14px;
  flex:0 0 auto;
}
.hero .menu-btn{
  position:static;
}
body:not([data-tab="home"]) #siteHero{
  display:none !important;
}
body[data-tab="home"] #siteHero{
  display:flex;
}
body[data-tab="home"] .tabs{
  top:10px;
}
body:not([data-tab="home"]) .tabs{
  top:70px;
}
body[data-tab="home"] .app-bar{
  background:#ffffff;
}
body:not([data-tab="home"]) .app-bar{
  background:#ffffff;
}
.hero{
  border-radius:0 0 26px 26px;
}
.hero-only{
  max-width:1100px;
}
.hero-title{
  font-size:clamp(24px,4.5vw,58px);
  letter-spacing:clamp(1px,.45vw,7px);
}
.hero-dev{
  letter-spacing:clamp(1.5px,.3vw,4px);
}

/* Global menu safety */
#navMenu{z-index:120;}
#navMenu .menu-item{display:block;}
.tabs{
  background:rgba(248,250,252,.9);
  backdrop-filter:blur(12px);
}
.tab{
  border-radius:999px;
}
.kpi,.filter-box,.card,.ro-table-wrap,.upload-area,.sd-head,#vInsights .insight-card,.home-card,.home-hero,.home-stage,.insight-summary-card{
  border-radius:22px;
}

/* ===== AI STUDIO ===== */
.ai-shell{max-width:1100px;margin:0 auto;display:flex;flex-direction:column;gap:12px}
.ai-hd{padding:18px 20px;border-radius:14px;background:linear-gradient(135deg,#1a1305 0%,#121212 55%,#0d0d0d 100%);border:1px solid rgba(212,175,90,.35)}
.ai-hd-title{font-size:18px;font-weight:900;letter-spacing:4px;color:#d4af5a}
.ai-hd-sub{margin-top:6px;font-size:12.5px;color:#bdb6a6;letter-spacing:.3px}
.ai-chat{min-height:260px;max-height:58vh;overflow-y:auto;display:flex;flex-direction:column;gap:14px;padding:14px;border-radius:14px;background:rgba(255,255,255,.02);border:1px solid rgba(212,175,90,.18)}
.ai-msg{max-width:88%;padding:12px 15px;border-radius:14px;font-size:13.5px;line-height:1.55;white-space:normal;word-wrap:break-word}
.ai-msg.user{align-self:flex-end;background:linear-gradient(135deg,#d4af5a,#a07830);color:#0b0b0b;font-weight:600;border-bottom-right-radius:4px}
.ai-msg.bot{align-self:flex-start;background:#181818;border:1px solid rgba(212,175,90,.25);color:#eae4d6;border-bottom-left-radius:4px}
.ai-msg.bot b,.ai-msg.bot strong{color:#d4af5a}
.ai-msg.err{align-self:flex-start;background:#2a1212;border:1px solid #7a3a3a;color:#f2b8b8}
.ai-engine{display:block;margin-top:8px;font-size:10px;letter-spacing:1.5px;text-transform:uppercase;color:#7d7666}
.ai-cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(235px,1fr));gap:14px;width:100%;margin-top:4px}
.ai-typing{align-self:flex-start;display:flex;gap:5px;padding:14px 18px;background:#181818;border:1px solid rgba(212,175,90,.25);border-radius:14px}
.ai-typing span{width:7px;height:7px;border-radius:50%;background:#d4af5a;animation:aiBlink 1.2s infinite}
.ai-typing span:nth-child(2){animation-delay:.2s}
.ai-typing span:nth-child(3){animation-delay:.4s}
@keyframes aiBlink{0%,80%,100%{opacity:.25}40%{opacity:1}}
.ai-suggest{display:flex;flex-wrap:wrap;gap:8px}
.ai-chip{padding:8px 14px;border-radius:999px;border:1px solid rgba(212,175,90,.4);background:rgba(212,175,90,.08);color:#d8c89a;font-size:12px;cursor:pointer;transition:.15s}
.ai-chip:hover{background:#d4af5a;color:#111}
.ai-inputbar{display:flex;gap:10px;align-items:flex-end;padding:10px;border-radius:14px;background:#141414;border:1px solid rgba(212,175,90,.3)}
.ai-inputbar textarea{flex:1;resize:none;background:transparent;border:none;outline:none;color:#f0ead8;font-size:14px;line-height:1.4;max-height:120px;font-family:inherit}
.ai-inputbar textarea::placeholder{color:#6f695c}
.ai-sendbtn{width:42px;height:42px;border-radius:11px;border:none;cursor:pointer;font-size:16px;background:linear-gradient(135deg,#d4af5a,#a07830);color:#0b0b0b;font-weight:900;flex:0 0 auto;transition:.15s}
.ai-sendbtn:hover{filter:brightness(1.1)}
.ai-sendbtn:disabled{opacity:.45;cursor:not-allowed}
.ai-hd-row{display:flex;justify-content:space-between;align-items:flex-start;gap:12px;flex-wrap:wrap}
.ai-hd-actions{display:flex;gap:8px;flex-wrap:wrap}
.ai-hbtn{padding:8px 14px;border-radius:9px;border:1px solid rgba(212,175,90,.45);background:rgba(212,175,90,.1);color:#d8c89a;font-size:12px;font-weight:700;cursor:pointer;transition:.15s}
.ai-hbtn:hover{background:#d4af5a;color:#111}
.ai-hbtn.design{background:linear-gradient(135deg,rgba(212,175,90,.25),rgba(160,120,48,.25))}
.ai-hbtn:disabled{opacity:.5;cursor:not-allowed}
.ai-design{display:flex;flex-direction:column;gap:10px;padding:16px;border-radius:14px;background:linear-gradient(135deg,#191204,#121212);border:1px solid rgba(212,175,90,.4)}
.ai-design-title{font-size:13px;font-weight:900;letter-spacing:2px;color:#d4af5a}
.ai-design-sub{font-weight:500;letter-spacing:.3px;color:#9d957f;text-transform:none;font-size:11.5px}
.ai-design textarea,.ai-design input{background:#0e0e0e;border:1px solid rgba(212,175,90,.25);border-radius:9px;padding:10px 12px;color:#f0ead8;font-size:13px;outline:none;font-family:inherit;resize:vertical}
.ai-design textarea::placeholder,.ai-design input::placeholder{color:#6f695c}
.ai-design-foot{display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.ai-design-note{font-size:11px;color:#7d7666}
.ai-genwrap{align-self:flex-start;max-width:88%;display:flex;flex-direction:column;gap:8px}
.ai-genimg{width:100%;max-width:420px;border-radius:14px;border:1px solid rgba(212,175,90,.45);display:block}
.ai-dl{align-self:flex-start;font-size:11.5px;color:#d4af5a;text-decoration:none;border:1px solid rgba(212,175,90,.4);padding:6px 12px;border-radius:999px}
.ai-dl:hover{background:#d4af5a;color:#111}
.ai-exportbar{display:flex;align-items:center;gap:10px;font-size:11.5px;color:#9d957f;margin-top:2px}
.smart-box{margin:0 0 16px;padding:16px;border-radius:14px;background:linear-gradient(135deg,#16100a,#101010);border:1px solid rgba(212,175,90,.4)}
.smart-title{font-size:13px;font-weight:900;letter-spacing:2px;color:#d4af5a;margin-bottom:10px}
.smart-sub{font-weight:500;letter-spacing:.3px;color:#9d957f;text-transform:none;font-size:11.5px}
.smart-row{display:flex;gap:10px;flex-wrap:wrap;align-items:center}
.smart-row .fi{flex:1;min-width:200px}
.smart-note{margin-top:10px;font-size:12px;color:#bdb6a6}
#smartResults{margin-top:14px}
.smart-prog{height:8px;border-radius:99px;background:#222;margin:8px 0;overflow:hidden;border:1px solid rgba(212,175,90,.25)}
.smart-prog-fill{height:100%;background:linear-gradient(90deg,#d4af5a,#a07830);transition:width .6s}
@media (max-width:640px){.ai-msg{max-width:96%}.ai-chat{max-height:52vh}.ai-genimg{max-width:100%}}


/* ═══════════════════════════════════════════════════════════
   COSA NOSTRAA — OBSIDIAN THEME
   Bold modern dark · platinum & violet accents · real 3D depth
   ═══════════════════════════════════════════════════════════ */
:root{
  --bg:#0a0b0f; --bg-2:#0e1016;
  --panel:#13151d; --panel-2:#181b25;
  --txt:#f2f4f8; --txt-2:#aab2c2; --txt-3:#6e7687;
  --acc:#8b7bff; --acc-2:#b3a8ff; --acc-deep:#5f4fd8;
  --plat:#e8ecf4; --plat-2:#c3cad8;
  --gold:#e6c87e;
  --edge:rgba(139,123,255,.22); --edge-soft:rgba(255,255,255,.07);
  --r-xl:22px; --r-lg:18px; --r-md:14px; --r-sm:11px;
  --sh-1:0 2px 4px rgba(0,0,0,.4), 0 14px 34px rgba(0,0,0,.45);
  --sh-2:0 4px 10px rgba(0,0,0,.5), 0 30px 70px rgba(0,0,0,.55);
  --sh-acc:0 14px 40px rgba(139,123,255,.25);
  --ease:cubic-bezier(.22,.9,.3,1.02);
  --disp:'Space Grotesk','Montserrat',sans-serif;
}
*{font-weight:600}
b,strong,th,.kpi-v,.hero-title,button{font-weight:800}
::selection{background:rgba(139,123,255,.35); color:#fff}

/* ── canvas: layered depth field ── */
body{
  font-family:'Montserrat','Inter',sans-serif;
  color:var(--txt);
  background:#0a0b0f;
  background-image:
    radial-gradient(1300px 700px at 80% -10%, rgba(139,123,255,.13), transparent 60%),
    radial-gradient(1100px 700px at -10% 30%, rgba(94,150,255,.07), transparent 60%),
    radial-gradient(900px 600px at 50% 115%, rgba(230,200,126,.05), transparent 60%),
    linear-gradient(180deg,#0c0d13 0%,#090a0e 100%);
  background-attachment:fixed;
}
body::before{
  content:""; position:fixed; inset:-20%; z-index:0; pointer-events:none;
  background:
    radial-gradient(560px 380px at 25% 25%, rgba(139,123,255,.06), transparent 70%),
    radial-gradient(640px 460px at 75% 75%, rgba(94,150,255,.05), transparent 70%);
  animation:obsDrift 24s ease-in-out infinite alternate;
}
@keyframes obsDrift{from{transform:translate3d(-2%,-1%,0)} to{transform:translate3d(2%,2%,0) scale(1.05)}}
body > *{position:relative; z-index:1}

::-webkit-scrollbar{width:10px;height:10px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:#262a36;border-radius:99px;border:2px solid #0a0b0f}
::-webkit-scrollbar-thumb:hover{background:var(--acc-deep)}

/* ── HERO ── */
.hero{
  background:
    radial-gradient(1000px 380px at 50% -35%, rgba(139,123,255,.2), transparent 70%),
    linear-gradient(180deg,#11131c 0%,#0b0c11 100%);
  border-bottom:1px solid var(--edge);
  padding:52px 20px 46px;
  box-shadow:0 30px 60px rgba(0,0,0,.35);
}
.hero-title{
  font-family:var(--disp);
  font-weight:800;
  letter-spacing:clamp(2px,.5vw,8px);
  background:linear-gradient(180deg,#ffffff 20%, var(--plat-2) 55%, var(--acc-2) 100%);
  -webkit-background-clip:text; background-clip:text; color:transparent;
  filter:drop-shadow(0 20px 40px rgba(0,0,0,.6)) drop-shadow(0 0 30px rgba(139,123,255,.15));
}
.hero-dev{color:var(--txt-3); font-weight:700; letter-spacing:clamp(3px,.5vw,6px); margin-top:14px}
.gold-line{
  width:90px; height:2px; margin:18px auto 0;
  background:linear-gradient(90deg,transparent,var(--acc),transparent);
  box-shadow:0 0 16px rgba(139,123,255,.5);
}
.brand{color:var(--acc-2); text-shadow:none; font-weight:800}

/* ── nav: floating dock ── */
.tabs,.app-bar{
  background:rgba(12,13,19,.78);
  backdrop-filter:blur(18px) saturate(1.3);
  -webkit-backdrop-filter:blur(18px) saturate(1.3);
  border-bottom:1px solid var(--edge);
  box-shadow:0 16px 40px rgba(0,0,0,.45);
}
.tab,.app-chip,.menu-btn{
  font-weight:800; letter-spacing:1.5px;
  color:var(--txt-2);
  background:transparent;
  border:1px solid transparent;
  border-radius:var(--r-sm);
  box-shadow:none;
  transition:all .25s var(--ease);
}
.tab:hover,.app-chip:hover,.menu-btn:hover{
  color:#fff; background:rgba(139,123,255,.1);
  border-color:var(--edge);
  transform:translateY(-2px);
  box-shadow:0 8px 20px rgba(0,0,0,.35);
}
.tab:active,.app-chip:active{transform:translateY(0) scale(.97)}
.tab.active{
  background:linear-gradient(135deg,var(--acc-2),var(--acc) 55%,var(--acc-deep));
  color:#0c0a18; border-color:transparent;
  box-shadow:var(--sh-acc), inset 0 1px 0 rgba(255,255,255,.4);
  transform:translateY(-1px);
}
.nav-menu{
  background:rgba(16,17,24,.92);
  backdrop-filter:blur(22px);
  -webkit-backdrop-filter:blur(22px);
  border:1px solid var(--edge);
  border-radius:var(--r-md);
  box-shadow:var(--sh-2);
  max-height:calc(100vh - 96px);
  overflow-y:auto;
  overflow-x:hidden;
}
.menu-item{font-weight:800; letter-spacing:2px; color:var(--txt-2); border-left:3px solid transparent; transition:all .2s var(--ease)}
.menu-item:hover{color:var(--acc-2); padding-left:24px; border-left-color:var(--acc); background:linear-gradient(90deg, rgba(139,123,255,.12), transparent)}

/* ── KPI: floating glass slabs ── */
.kpis{perspective:1100px; gap:18px}
.kpi{
  background:linear-gradient(160deg, rgba(28,31,43,.92), rgba(16,18,26,.96));
  border:1px solid var(--edge-soft);
  border-radius:var(--r-md);
  box-shadow:var(--sh-1), inset 0 1px 0 rgba(255,255,255,.06);
  padding:22px 28px;
  position:relative; overflow:hidden;
  transition:transform .32s var(--ease), box-shadow .32s var(--ease), border-color .32s;
  transform-style:preserve-3d;
}
.kpi::before{
  content:""; position:absolute; inset:0 0 auto 0; height:2px;
  background:linear-gradient(90deg,transparent,var(--acc),transparent); opacity:.6;
}
.kpi:hover{
  transform:translateY(-7px) rotateX(3deg);
  border-color:var(--edge);
  box-shadow:var(--sh-2), 0 0 30px rgba(139,123,255,.08), inset 0 1px 0 rgba(255,255,255,.08);
}
.kpi-t{font-weight:800; color:var(--txt-3); letter-spacing:2.5px; font-size:9.5px}
.kpi-v{
  font-family:var(--disp); font-weight:800;
  background:linear-gradient(180deg,#fff 20%, var(--plat-2) 100%);
  -webkit-background-clip:text; background-clip:text; color:transparent;
  text-shadow:none;
}
.kpi-v.green{background:none;-webkit-background-clip:initial;color:#7fe0a0}
.kpi-v.red{background:none;-webkit-background-clip:initial;color:#ff8f86}
.kpi-v.orange{background:none;-webkit-background-clip:initial;color:#ffc37e}
.kpi-v.gold{background:none;-webkit-background-clip:initial;color:var(--gold)}

/* ── product cards: levitating tiles ── */
.grid{gap:20px}
.card{
  background:linear-gradient(170deg, rgba(26,29,40,.95), rgba(15,16,23,.98));
  border:1px solid var(--edge-soft);
  border-radius:var(--r-md);
  box-shadow:0 6px 18px rgba(0,0,0,.45), inset 0 1px 0 rgba(255,255,255,.05);
  transition:transform .34s var(--ease), box-shadow .34s var(--ease), border-color .34s;
  will-change:transform;
}
.card:hover{
  transform:translateY(-8px) scale(1.02);
  border-color:var(--edge);
  box-shadow:0 28px 60px rgba(0,0,0,.6), 0 0 28px rgba(139,123,255,.1), inset 0 1px 0 rgba(255,255,255,.08);
  z-index:3;
}
.card .img-box{overflow:hidden; background:#0d0e14}
.card .img-box img{transition:transform .6s var(--ease)}
.card:hover .img-box img{transform:scale(1.06)}
.sku{font-weight:800; letter-spacing:1px; color:var(--acc-2)}

/* ── buttons: tactile 3D ── */
.mini-btn,.details-btn,.go-btn,.ai-hbtn,.sync-btn{
  font-weight:800; letter-spacing:1.5px; text-transform:uppercase;
  border-radius:var(--r-sm);
  border:1px solid var(--edge-soft);
  background:linear-gradient(180deg, rgba(35,38,52,.9), rgba(22,24,34,.95));
  color:var(--txt-2);
  box-shadow:0 4px 12px rgba(0,0,0,.4), inset 0 1px 0 rgba(255,255,255,.07);
  transition:all .22s var(--ease);
}
.mini-btn:hover,.details-btn:hover,.go-btn:hover,.ai-hbtn:hover,.sync-btn:hover{
  transform:translateY(-2px); color:#fff;
  border-color:var(--edge);
  box-shadow:0 10px 26px rgba(0,0,0,.5), inset 0 1px 0 rgba(255,255,255,.1);
}
.mini-btn:active,.details-btn:active,.go-btn:active,.ai-hbtn:active{transform:translateY(1px); box-shadow:0 2px 8px rgba(0,0,0,.4)}
.mini-btn.primary,.go-btn,.ai-hbtn.design{
  background:linear-gradient(135deg,var(--acc-2),var(--acc) 55%,var(--acc-deep));
  color:#0c0a18; border-color:transparent;
  box-shadow:var(--sh-acc), inset 0 1px 0 rgba(255,255,255,.45);
}
.mini-btn.primary:hover,.go-btn:hover,.ai-hbtn.design:hover{
  color:#0c0a18; filter:brightness(1.08);
  box-shadow:0 18px 44px rgba(139,123,255,.32), inset 0 1px 0 rgba(255,255,255,.5);
}

/* ── panels ── */
.filter-box,.ro,.insight-card,.insight-summary-card,.td-card,#loader,.upload-area,.type-breakdown,.sku-checklist{
  background:linear-gradient(170deg, rgba(26,29,40,.9), rgba(15,16,23,.96));
  border:1px solid var(--edge-soft);
  border-radius:var(--r-lg);
  box-shadow:var(--sh-1), inset 0 1px 0 rgba(255,255,255,.05);
}
.insight-card{transition:transform .3s var(--ease), box-shadow .3s var(--ease), border-color .3s}
.insight-card:hover{transform:translateY(-5px); border-color:var(--edge); box-shadow:var(--sh-2)}
.insights-title,.matrix-page-title,.home-title,.home-minimal-title,.sd-sku,.home-card-title{font-family:var(--disp); font-weight:800}

/* ── inputs ── */
.fi,select.fi,input.fi,textarea{
  font-weight:600;
  background:rgba(10,11,16,.9);
  border:1px solid var(--edge-soft);
  border-radius:var(--r-sm);
  color:var(--txt);
  box-shadow:inset 0 2px 8px rgba(0,0,0,.5);
  transition:border-color .22s, box-shadow .22s;
}
.fi:focus,textarea:focus{
  outline:none; border-color:var(--acc);
  box-shadow:inset 0 2px 8px rgba(0,0,0,.5), 0 0 0 3px rgba(139,123,255,.18);
}
.fl{font-weight:800; color:var(--txt-3); letter-spacing:2px}

/* ── tables ── */
table{border-collapse:separate; border-spacing:0}
thead th{
  background:#121420 !important; color:var(--txt-3) !important;
  font-weight:800; letter-spacing:2px;
  border-bottom:1px solid var(--edge) !important;
}
tbody tr{transition:background .18s}
tbody tr:hover{background:rgba(139,123,255,.07) !important}

/* ── AI STUDIO ── */
.ai-hd{
  background:
    radial-gradient(560px 200px at 10% -25%, rgba(139,123,255,.22), transparent 70%),
    linear-gradient(170deg,#171a26,#10121a);
  border:1px solid var(--edge);
  border-radius:var(--r-lg);
  box-shadow:var(--sh-1), inset 0 1px 0 rgba(255,255,255,.07);
}
.ai-hd-title{
  font-family:var(--disp); font-weight:800; letter-spacing:5px;
  background:linear-gradient(90deg,#fff,var(--acc-2) 70%);
  -webkit-background-clip:text; background-clip:text; color:transparent;
  animation:none;
}
.ai-hd-sub{color:var(--txt-3); font-weight:600}
.ai-chat{
  background:rgba(12,13,19,.7);
  backdrop-filter:blur(10px);
  -webkit-backdrop-filter:blur(10px);
  border:1px solid var(--edge-soft);
  border-radius:var(--r-lg);
  box-shadow:inset 0 4px 20px rgba(0,0,0,.4);
}
.ai-msg{font-weight:600; box-shadow:0 8px 22px rgba(0,0,0,.4); animation:msgIn .35s var(--ease)}
@keyframes msgIn{from{opacity:0; transform:translateY(10px) scale(.99)} to{opacity:1; transform:none}}
.ai-msg.user{
  background:linear-gradient(135deg,var(--acc-2),var(--acc) 60%,var(--acc-deep));
  color:#0c0a18; font-weight:700;
  box-shadow:var(--sh-acc), inset 0 1px 0 rgba(255,255,255,.45);
}
.ai-msg.bot{
  background:linear-gradient(170deg,#1b1e2a,#13151e);
  border:1px solid var(--edge-soft);
  color:var(--txt);
}
.ai-msg.bot b,.ai-msg.bot strong{color:var(--acc-2)}
.ai-msg.err{background:#2a1518; border:1px solid #7a3a44; color:#ffb4ad}
.ai-engine{color:var(--txt-3); font-weight:700}
.ai-inputbar{
  background:rgba(15,16,24,.9);
  backdrop-filter:blur(14px);
  -webkit-backdrop-filter:blur(14px);
  border:1px solid var(--edge);
  border-radius:var(--r-md);
  box-shadow:var(--sh-1), inset 0 1px 0 rgba(255,255,255,.06);
}
.ai-inputbar textarea{color:var(--txt); font-weight:600}
.ai-sendbtn{
  background:linear-gradient(135deg,var(--acc-2),var(--acc) 55%,var(--acc-deep));
  color:#0c0a18;
  box-shadow:var(--sh-acc), inset 0 1px 0 rgba(255,255,255,.45);
  transition:transform .2s var(--ease), filter .2s;
}
.ai-sendbtn:hover{transform:translateY(-2px) scale(1.03); filter:brightness(1.08)}
.ai-sendbtn:active{transform:scale(.95)}
.ai-chip{
  font-weight:700; letter-spacing:.5px;
  background:linear-gradient(180deg, rgba(35,38,52,.7), rgba(22,24,34,.85));
  border:1px solid var(--edge-soft);
  color:var(--txt-2);
  box-shadow:0 4px 12px rgba(0,0,0,.3), inset 0 1px 0 rgba(255,255,255,.06);
  transition:all .22s var(--ease);
}
.ai-chip:hover{transform:translateY(-2px); border-color:var(--edge); color:#fff; background:rgba(139,123,255,.12); box-shadow:0 10px 24px rgba(0,0,0,.4)}
.ai-design,.smart-box{
  background:
    radial-gradient(440px 170px at 92% -10%, rgba(139,123,255,.16), transparent 70%),
    linear-gradient(170deg,#171a26,#10121a);
  border:1px solid var(--edge);
  border-radius:var(--r-lg);
  box-shadow:var(--sh-1), inset 0 1px 0 rgba(255,255,255,.07);
}
.ai-design-title,.smart-title{font-family:var(--disp); font-weight:800; letter-spacing:3px; color:#fff}
.ai-design-sub,.smart-sub{font-weight:600; color:var(--txt-3); text-transform:none; letter-spacing:.3px}
.ai-design-note,.smart-note{color:var(--txt-3); font-weight:600}
.ai-genimg{
  border-radius:var(--r-md);
  border:1px solid var(--edge);
  box-shadow:var(--sh-2);
  transition:transform .3s var(--ease), box-shadow .3s var(--ease);
}
.ai-genimg:hover{transform:scale(1.015); box-shadow:0 36px 80px rgba(0,0,0,.6), 0 0 40px rgba(139,123,255,.15)}
.ai-dl{border:1px solid var(--edge); color:var(--acc-2); border-radius:99px; font-weight:800; letter-spacing:1.5px}
.ai-dl:hover{background:var(--acc); color:#0c0a18}
.ai-exportbar{color:var(--txt-3); font-weight:700}
.smart-prog{background:#171924; box-shadow:inset 0 2px 6px rgba(0,0,0,.55)}
.smart-prog-fill{background:linear-gradient(90deg,var(--acc-2),var(--acc-deep)); box-shadow:0 0 16px rgba(139,123,255,.5)}

/* ── HOME ── */
.home-grid,.home-scroll-grid{perspective:1200px}
.home-card{
  background:linear-gradient(170deg, rgba(28,31,43,.92), rgba(16,18,26,.96));
  border:1px solid var(--edge-soft);
  border-radius:var(--r-lg);
  box-shadow:var(--sh-1), inset 0 1px 0 rgba(255,255,255,.06);
  position:relative; overflow:hidden;
  transition:transform .32s var(--ease), box-shadow .32s var(--ease), border-color .32s;
}
.home-card::before{
  content:""; position:absolute; inset:0 0 auto 0; height:2px;
  background:linear-gradient(90deg,transparent,var(--acc),transparent); opacity:.55;
}
.home-card:hover{transform:translateY(-7px) rotateX(2.5deg); border-color:var(--edge); box-shadow:var(--sh-2), 0 0 30px rgba(139,123,255,.08)}
.home-pill,.pro-chip,.pro-pill,.insight-pill,.forecast-pill,.meta-tag{
  font-weight:800; letter-spacing:1.5px;
  border:1px solid var(--edge-soft); border-radius:99px;
  box-shadow:inset 0 1px 0 rgba(255,255,255,.06);
}
.home-kicker,.home-minimal-kicker,.insights-sub{font-weight:800; color:var(--txt-3); letter-spacing:3px}

.badge-status,.badge-inv,.badge-conf{
  font-weight:800; letter-spacing:1px; border-radius:8px;
  box-shadow:0 3px 10px rgba(0,0,0,.45), inset 0 1px 0 rgba(255,255,255,.15);
}

#skuModal > div, #loginGate > div{border-radius:var(--r-lg); border:1px solid var(--edge); box-shadow:var(--sh-2)}
#skuModal, #loginGate{backdrop-filter:blur(14px) !important; -webkit-backdrop-filter:blur(14px) !important}

.upload-area{transition:border-color .25s, box-shadow .25s, transform .25s var(--ease)}
.upload-area:hover{transform:translateY(-3px); border-color:var(--acc); box-shadow:var(--sh-2)}

/* ── employee role: revenue elements hidden globally ── */
body.role-employee .rev-only{display:none !important}

/* ── entrance choreography ── */
@keyframes viewIn{from{opacity:0; transform:translateY(14px)} to{opacity:1; transform:none}}
#vHome,#vMatrix,#vRepeat,#vFinder,#vSkuDetails,#vInsights,#vMarketplaces,#vAi,#vSmart{animation:viewIn .45s var(--ease)}
@keyframes cardIn{from{opacity:0; transform:translateY(18px) scale(.98)} to{opacity:1; transform:none}}
.grid .card,.ai-cards .card{animation:cardIn .5s var(--ease) backwards}
.grid .card:nth-child(1),.ai-cards .card:nth-child(1){animation-delay:.03s}
.grid .card:nth-child(2),.ai-cards .card:nth-child(2){animation-delay:.07s}
.grid .card:nth-child(3),.ai-cards .card:nth-child(3){animation-delay:.11s}
.grid .card:nth-child(4),.ai-cards .card:nth-child(4){animation-delay:.15s}
.grid .card:nth-child(5),.ai-cards .card:nth-child(5){animation-delay:.19s}
.grid .card:nth-child(6),.ai-cards .card:nth-child(6){animation-delay:.23s}
.grid .card:nth-child(7),.ai-cards .card:nth-child(7){animation-delay:.27s}
.grid .card:nth-child(8),.ai-cards .card:nth-child(8){animation-delay:.31s}
.kpis .kpi{animation:cardIn .5s var(--ease) backwards}
.kpis .kpi:nth-child(1){animation-delay:.02s}
.kpis .kpi:nth-child(2){animation-delay:.08s}
.kpis .kpi:nth-child(3){animation-delay:.14s}
.kpis .kpi:nth-child(4){animation-delay:.2s}
.kpis .kpi:nth-child(5){animation-delay:.26s}

/* ── smart search hero ── */
.smart-hero{text-align:center; padding:34px 16px 26px}
.smart-hero-kicker{font-weight:800; font-size:10px; letter-spacing:5px; color:var(--acc-2)}
.smart-hero-title{
  font-family:var(--disp); font-weight:800; font-size:clamp(30px,5vw,52px); letter-spacing:2px; margin-top:8px;
  background:linear-gradient(180deg,#fff 25%, var(--plat-2) 60%, var(--acc-2) 100%);
  -webkit-background-clip:text; background-clip:text; color:transparent;
}
.smart-hero-sub{margin-top:8px; color:var(--txt-3); font-weight:600; font-size:13px}
.smart-row .fi{padding:15px 18px; font-size:14px}

/* ── AI follow-up chips ── */
.ai-followups{display:flex; flex-wrap:wrap; gap:8px; align-self:flex-start; max-width:88%}
.ai-followups .ai-chip{font-size:11.5px; padding:7px 13px; text-transform:none; letter-spacing:.3px}

.mini-btn.active{
  background:linear-gradient(135deg,var(--acc-2),var(--acc) 55%,var(--acc-deep)) !important;
  color:#0c0a18 !important; border-color:transparent !important;
  box-shadow:0 10px 26px rgba(139,123,255,.25), inset 0 1px 0 rgba(255,255,255,.4) !important;
}
#roViewToggle{display:none}

/* ── PRODUCT IMAGES: frame mein poori dikhe (crop nahi) ── */
.card .img-box{background:#ffffff}
.card .img-box img{object-fit:contain !important; padding:6px; background:#ffffff}
.sku-thumb, .ro-thumb-lg{object-fit:contain !important; background:#ffffff}
.ai-cards .img-box img{object-fit:contain !important; background:#ffffff; padding:4px}
#sdImg, .sd-img, .sd-img img{object-fit:contain !important; background:#ffffff}
.ai-genimg{object-fit:contain}

/* ── TYPING INPUTS: white field, BLACK bold text (search/paste sab readable) ── */
input[type="text"], input[type="search"], input[type="password"], input[type="number"],
input:not([type]), textarea, input.fi, .smart-row .fi, .lg-in{
  background:#f3f5f9 !important;
  color:#0b0c10 !important;
  font-weight:700 !important;
  border:1px solid #c3c9d6 !important;
  box-shadow:inset 0 1px 3px rgba(0,0,0,.12) !important;
  caret-color:#0b0c10;
}
input::placeholder, textarea::placeholder{color:#7b8294 !important; font-weight:600 !important; opacity:1}
input:focus, textarea:focus{
  border-color:var(--acc) !important;
  box-shadow:inset 0 1px 3px rgba(0,0,0,.12), 0 0 0 3px rgba(139,123,255,.22) !important;
  outline:none;
}
input:-webkit-autofill, input:-webkit-autofill:hover, input:-webkit-autofill:focus{
  -webkit-text-fill-color:#0b0c10 !important;
  -webkit-box-shadow:0 0 0 1000px #f3f5f9 inset !important;
  caret-color:#0b0c10;
}
.ai-inputbar textarea{background:#f3f5f9 !important; color:#0b0c10 !important; border-radius:9px; padding:10px 12px}
input[type="checkbox"]{background:initial !important; box-shadow:none !important; border:initial !important; accent-color:var(--acc); width:16px; height:16px}
input[type="file"]{background:transparent !important; border:none !important; color:var(--txt-2) !important; box-shadow:none !important}

@media (prefers-reduced-motion: reduce){
  *,*::before,*::after{animation:none !important; transition:none !important}
}
@media (max-width:640px){
  .kpi:hover,.card:hover,.home-card:hover{transform:none}
  .hero{padding:36px 16px 30px}
}

/* ════════════════════════════════════════════════════════════
   PREMIUM THEME OVERRIDE (gold / cream) — sirf look badalta hai,
   koi feature/filter/tab/function nahi. End me hai isliye highest priority.
   ════════════════════════════════════════════════════════════ */

:root{
  --cn-cream:#faf8f4; --cn-ivory:#f5f0e8; --cn-gold:#b8960c; --cn-gold2:#d4af37;
  --cn-gold3:#f0d060; --cn-dark:#1a1610; --cn-mid:#6b5e3e; --cn-line:#e8e0cc;
}

body{
  font-family:'Inter',sans-serif !important;
  background:var(--cn-cream) !important;
  color:var(--cn-dark) !important;
}
#pcanvas{position:fixed;inset:0;z-index:0;pointer-events:none;opacity:.85}
#appRoot, .tabs, .app-bar{position:relative;z-index:2}

.hero-title,.section-title,.smart-hero-title,.kpi-v,.sd-name{
  font-family:'Cormorant Garamond',serif !important;
}
.hero-title{
  color:var(--cn-dark) !important;
  background:none !important; -webkit-text-fill-color:var(--cn-dark) !important;
  font-weight:400 !important; letter-spacing:.05em !important;
}
.hero-dev{color:var(--cn-mid) !important;font-weight:400 !important}

.app-bar{
  background:var(--cn-cream) !important;
  border-bottom:1px solid rgba(184,150,12,.18) !important;
  box-shadow:0 8px 26px rgba(26,22,16,.05) !important;
  backdrop-filter:blur(14px) !important;
}
.app-bar-brand{color:var(--cn-gold) !important}
.app-bar-sub{color:var(--cn-mid) !important}
body[data-tab="home"] .app-bar, body:not([data-tab="home"]) .app-bar{background:var(--cn-cream) !important}

.hero{
  background:linear-gradient(180deg,var(--cn-ivory),var(--cn-cream)) !important;
  border:1px solid var(--cn-line) !important;
  border-radius:0 0 26px 26px !important;
  box-shadow:0 20px 50px rgba(26,22,16,.06) !important;
}

.app-chip{
  background:var(--cn-dark) !important; color:var(--cn-cream) !important;
  border:1px solid var(--cn-dark) !important; box-shadow:0 4px 14px rgba(26,22,16,.12) !important;
}
.app-chip:hover{background:var(--cn-gold) !important;border-color:var(--cn-gold) !important;color:#fff !important}

.tabs{background:transparent !important;border-bottom:1px solid var(--cn-line) !important}
.tab{
  background:#fff !important; color:var(--cn-mid) !important;
  border:1px solid var(--cn-line) !important; border-radius:999px !important;
  letter-spacing:2px !important; transition:all .3s !important;
}
.tab:hover{border-color:var(--cn-gold) !important;color:var(--cn-gold) !important;background:#fff !important}
.tab.active{background:var(--cn-dark) !important;color:var(--cn-gold3) !important;border-color:var(--cn-dark) !important}

.kpi{
  background:#fff !important; border:1px solid var(--cn-line) !important;
  border-radius:16px !important; box-shadow:0 12px 30px rgba(26,22,16,.05) !important;
}
.kpi-t{color:var(--cn-mid) !important;letter-spacing:2px !important}
.kpi-v{color:var(--cn-gold) !important;font-weight:300 !important}

.filter-box,.upload-area,.card,.ro-table-wrap,.sd-head,.insight-card,.insight-summary-card,.td-card,#dbgbox,#loader{
  background:#fff !important; border:1px solid var(--cn-line) !important;
  border-radius:16px !important; box-shadow:0 12px 28px rgba(26,22,16,.05) !important;
}
.fl,.section-label,.small-note{color:var(--cn-mid) !important}
.fi,.fs,.form-input,.form-textarea,.ai-design textarea,.ai-design input{
  background:var(--cn-ivory) !important; color:var(--cn-dark) !important;
  border:1px solid var(--cn-line) !important; border-radius:10px !important;
}
.fi:focus,.fs:focus{border-color:var(--cn-gold) !important;background:#fff !important}
.sku-checklist,.type-checks{background:#fff !important;border:1px solid var(--cn-line) !important}

.go-btn,.btn-primary{
  background:var(--cn-dark) !important; color:var(--cn-cream) !important;
  border:none !important; border-radius:999px !important; letter-spacing:1.5px !important;
  transition:all .3s !important;
}
.go-btn:hover,.btn-primary:hover{background:var(--cn-gold) !important;transform:translateY(-2px) !important}
.go-btn:disabled{background:#d8d2c2 !important;color:#fff !important;transform:none !important}

table.ro{background:#fff !important;color:var(--cn-dark) !important}
table.ro th{background:var(--cn-ivory) !important;color:var(--cn-gold) !important;border-bottom:1px solid var(--cn-line) !important}
table.ro td{border-bottom:1px solid #f0ece2 !important}
table.ro tr:hover td,table.ro tbody tr:hover{background:var(--cn-ivory) !important}
.sku-link,.details-btn{color:var(--cn-gold) !important}

.ai-msg.bot,.ai-typing,.ai-inputbar{
  background:#fff !important; border:1px solid var(--cn-line) !important; color:var(--cn-dark) !important;
}
.ai-msg.user{background:var(--cn-dark) !important;color:var(--cn-cream) !important}
.ai-inputbar textarea{color:var(--cn-dark) !important}

footer{background:var(--cn-dark) !important;border-top:1px solid rgba(212,175,55,.18) !important;color:rgba(250,248,244,.5) !important}

.ro-remark{background:var(--cn-ivory) !important;border:1px solid var(--cn-line) !important;color:var(--cn-dark) !important}
.ro-remark:focus{border-color:var(--cn-gold) !important;background:#fff !important}
.forecast-pill{background:var(--cn-ivory) !important;color:var(--cn-gold) !important;border:1px solid var(--cn-line) !important}

/* Repeat Orders table — balanced widths, clear details, sticky header */
#roTable{width:100%;border-collapse:collapse}
#roTable th,#roTable td{padding:8px 7px !important;font-size:.82rem;vertical-align:middle}
#roTable th{
  white-space:nowrap;line-height:1.2;
  position:sticky;top:0;z-index:30;
  background:var(--cn-ivory) !important;
  box-shadow:0 2px 0 var(--cn-line);
}
/* SKU column ko poori jagah — image + naam + Details + combo saaf dikhe */
#roTable th:nth-child(2),#roTable td:nth-child(2){min-width:185px}
/* numeric columns compact + centered */
#roTable th:nth-child(3),#roTable td:nth-child(3),
#roTable th:nth-child(4),#roTable td:nth-child(4),
#roTable th:nth-child(5),#roTable td:nth-child(5),
#roTable th:nth-child(6),#roTable td:nth-child(6),
#roTable th:nth-child(7),#roTable td:nth-child(7),
#roTable th:nth-child(8),#roTable td:nth-child(8),
#roTable th:nth-child(9),#roTable td:nth-child(9),
#roTable th:nth-child(10),#roTable td:nth-child(10){text-align:center;white-space:nowrap}
/* remark boxes chote */
#roTable th:nth-child(11),#roTable td:nth-child(11),
#roTable th:nth-child(12),#roTable td:nth-child(12){width:130px}
/* sticky header thead bhi */
#roTable thead th{position:sticky;top:0}


/* Gift Set / combo — Stone Details with stock+wip */
.combo-box{margin-top:4px;padding:8px 10px;background:var(--cn-ivory);border:1px solid var(--cn-line);border-radius:10px;max-width:560px;overflow-x:auto}
.combo-title{font-size:.66rem;letter-spacing:.06em;text-transform:uppercase;color:var(--cn-mid);font-weight:800;margin-bottom:6px}
.combo-row{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:3px 0;border-bottom:1px dashed #e6dcc4}
.combo-row:last-child{border-bottom:none}
.combo-detail{padding:6px 0;border-bottom:1px dashed #e6dcc4}
.combo-detail:last-child{border-bottom:none}
.combo-grid{display:flex;flex-wrap:nowrap;align-items:center;gap:14px;margin-top:4px;font-size:.7rem;color:#6b5e3e;overflow-x:auto;white-space:nowrap}
.combo-grid span{white-space:nowrap;flex:0 0 auto}
.combo-grid b{color:var(--cn-dark);font-weight:800}
.combo-sku{background:none;border:none;color:var(--cn-gold);font-weight:800;font-size:.8rem;cursor:pointer;padding:0;text-decoration:underline}
.combo-iv{font-size:.74rem;color:#5a4a1a;font-weight:600;white-space:nowrap}
.combo-iv b{color:var(--cn-dark)}
.combo-iv b.muted{color:#b0a890}


/* ── Profit Margin tab ── */
.pm-mode{display:flex;justify-content:center;margin:6px 0 6px}
.pm-mode-btn{border:none;background:none;cursor:pointer;font-family:inherit;font-size:13px;font-weight:700;
  letter-spacing:.04em;color:var(--cn-mid);padding:11px 22px;border-radius:999px;transition:.2s;white-space:nowrap}
.pm-mode{background:#fff;border:1px solid var(--cn-line);border-radius:999px;padding:5px;display:inline-flex;
  margin-left:auto;margin-right:auto;box-shadow:0 8px 22px rgba(26,22,16,.08)}
.pm-mode-btn.on{background:var(--cn-dark);color:#fff}
.pm-note{text-align:center;color:var(--cn-mid);font-size:12.5px;margin:10px 0 20px}
.pm-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:20px;align-items:start}
@media(max-width:860px){.pm-grid{grid-template-columns:1fr}}
.pm-inputs{padding:20px !important}
.pm-two{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px}
.pm-num{font-family:'JetBrains Mono',monospace !important;font-weight:700 !important;text-align:right}
.pm-skurow{margin-bottom:16px}
.pm-skulist{position:absolute;left:0;right:0;top:calc(100% + 4px);z-index:40;background:#fff;
  border:1px solid var(--cn-line);border-radius:11px;box-shadow:0 14px 36px rgba(26,22,16,.14);
  max-height:240px;overflow:auto;display:none}
.pm-skulist.show{display:block}
.pm-skuopt{padding:10px 14px;cursor:pointer;font-family:'JetBrains Mono',monospace;font-size:13px;
  font-weight:600;display:flex;justify-content:space-between;gap:12px;border-bottom:1px solid #f3eede}
.pm-skuopt:last-child{border-bottom:none}
.pm-skuopt:hover{background:var(--cn-ivory)}
.pm-skuopt .mrp{color:var(--cn-gold);font-weight:700}
.pm-skustatus{font-size:12px;color:var(--cn-mid);margin-top:8px;min-height:16px}
.pm-sp{display:flex;align-items:center;justify-content:space-between;padding:14px 18px;
  background:linear-gradient(120deg,#fbf6e8,#fdfcf7);border:1px solid var(--cn-line);border-radius:13px;margin-bottom:6px}
.pm-sp-lab{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--cn-mid);font-weight:800}
.pm-sp-val{font-family:'JetBrains Mono',monospace;font-weight:700;font-size:24px;color:var(--cn-dark)}
.pm-seclabel{display:flex;align-items:center;gap:10px;margin:18px 0 14px}
.pm-seclabel span:first-child{font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--cn-mid);font-weight:800}
.pm-seclabel .ln{flex:1;height:1px;background:var(--cn-line)}
.pm-result{position:sticky;top:18px;background:#fff;border:1px solid var(--cn-line);border-radius:16px;
  overflow:hidden;box-shadow:0 14px 40px rgba(26,22,16,.10)}
.pm-hero{padding:24px;text-align:center;background:linear-gradient(160deg,#1f1a12,#13100b);color:#fff}
.pm-hero-lab{font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--cn-gold2);font-weight:800;margin-bottom:8px}
.pm-margin{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:58px;line-height:1}
.pm-margin.pos{color:#9be3a8}.pm-margin.neg{color:#ff9b76}
.pm-profit{margin-top:6px;font-family:'JetBrains Mono',monospace;font-size:15px;font-weight:700;color:#e9e0c8}
.pm-verdict{display:inline-block;margin-top:12px;font-size:11px;font-weight:800;letter-spacing:.1em;
  text-transform:uppercase;padding:6px 14px;border-radius:999px}
.pm-verdict.good{background:rgba(155,227,168,.16);color:#9be3a8}
.pm-verdict.thin{background:rgba(212,175,55,.16);color:var(--cn-gold2)}
.pm-verdict.loss{background:rgba(255,155,118,.16);color:#ff9b76}
.pm-break{padding:18px 20px 20px}
.pm-br{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:8px 0;
  border-bottom:1px dashed var(--cn-line);font-size:13px}
.pm-br:last-child{border-bottom:none}
.pm-br span:first-child{color:var(--cn-mid)}
.pm-br span:last-child{font-family:'JetBrains Mono',monospace;font-weight:700;color:var(--cn-dark)}
.pm-br.head span:first-child{color:var(--cn-dark);font-weight:700}
.pm-br.minus span:last-child{color:var(--cn-red,#b4451f)}
.pm-br.total{margin-top:6px;padding-top:12px;border-top:2px solid var(--cn-dark);border-bottom:none}
.pm-br.total span:first-child{font-weight:800;text-transform:uppercase;letter-spacing:.06em;font-size:11.5px;color:var(--cn-dark)}
.pm-br.total span:last-child{font-size:17px}
.pm-br.profit-row span:last-child{font-size:17px}
.pm-br.profit-row.pos span:last-child{color:#2f6f3e}
.pm-br.profit-row.neg span:last-child{color:#b4451f}


/* Production table: compact rows, wrapped text, clearer SKU images */
#prodContent table.prod-table{width:100%;min-width:960px;table-layout:fixed;font-size:10.5px}
#prodContent table.prod-table th,
#prodContent table.prod-table td{
  padding:7px 8px !important;
  white-space:normal !important;
  overflow-wrap:anywhere;
  word-break:break-word;
  line-height:1.25;
  vertical-align:top;
}
#prodContent table.prod-table th{font-size:8px !important;letter-spacing:1px !important}
/* Freeze header row while scrolling the production table */
#prodContent{overflow:auto;max-height:72vh}
#prodContent table.prod-table thead th{
  position:sticky;top:0;z-index:30;
  background:var(--cn-ivory) !important;
  box-shadow:0 2px 0 var(--cn-line);
}
.prod-sku-cell{display:flex;align-items:center;gap:8px;min-width:0}
.prod-img,.prod-ph{
  width:72px;height:72px;border-radius:8px;flex:0 0 72px;
  background:#fff;border:1px solid var(--cn-line);
}
.prod-img{object-fit:contain}
.prod-ph{display:flex;align-items:center;justify-content:center;color:#b8a06a;font-size:24px}
.prod-sku-text{font-size:11px !important;line-height:1.2;min-width:0;white-space:normal !important}
.prod-order-list{font-size:.76rem;color:var(--cn-mid);max-width:120px}
.prod-num{white-space:nowrap !important;text-align:right}


/* Sheets-jaisa sortable header — saaf arrow + hover highlight */
table.ro th.sort-arrow{cursor:pointer;user-select:none;white-space:nowrap;transition:background .2s}
table.ro th.sort-arrow:hover{background:#efe4c8 !important;color:var(--cn-dark) !important}
table.ro th.sort-arrow:after{content:' ⇅';color:#b8a06a;font-size:.85em}
table.ro th.sort-arrow.asc:after{content:' ▲';color:var(--cn-gold) !important}
table.ro th.sort-arrow.desc:after{content:' ▼';color:var(--cn-gold) !important}


/* ── HOME (admin top SKUs + YoY) ── */
.home-wrap{max-width:1180px;margin:0 auto;padding:8px 16px 40px}
.home-sec-label{font-size:.62rem;letter-spacing:.4em;text-transform:uppercase;color:var(--cn-gold) !important;font-weight:800;margin:6px 0 18px}
.home-top-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-bottom:34px}
@media(max-width:880px){.home-top-grid{grid-template-columns:1fr}}
.top-card{
  background:#fff;border:1px solid var(--cn-line);border-radius:20px;overflow:hidden;
  box-shadow:0 16px 40px rgba(26,22,16,.06);transition:transform .35s ease,box-shadow .35s ease;
  position:relative;display:flex;flex-direction:column;
}
.top-card:hover{transform:translateY(-6px);box-shadow:0 28px 60px rgba(26,22,16,.12);border-color:rgba(184,150,12,.4)}
.top-card .tc-ribbon{
  position:absolute;top:14px;left:14px;z-index:2;
  font-size:.55rem;letter-spacing:.25em;text-transform:uppercase;font-weight:800;
  background:var(--cn-dark);color:var(--cn-gold3);padding:.32rem .8rem;border-radius:999px;
}
.top-card .tc-img{height:210px;background:var(--cn-ivory);display:flex;align-items:center;justify-content:center;overflow:hidden}
.top-card .tc-img img{width:100%;height:100%;object-fit:cover}
.top-card .tc-img .tc-ph{font-size:4rem}
.top-card .tc-body{padding:20px}
.top-card .tc-sku{font-family:'Cormorant Garamond',serif !important;font-size:1.7rem;font-weight:600;color:var(--cn-dark) !important;margin-bottom:4px;cursor:pointer}
.top-card .tc-sku:hover{color:var(--cn-gold) !important}
.top-card .tc-sub{font-size:.66rem;letter-spacing:.12em;text-transform:uppercase;color:var(--cn-mid) !important;font-weight:700;margin-bottom:14px}
.top-card .tc-rows{display:flex;flex-direction:column;gap:9px}
.top-card .tc-row{display:flex;align-items:center;justify-content:space-between;padding-bottom:8px;border-bottom:1px solid #f0ece2}
.top-card .tc-row:last-child{border-bottom:none;padding-bottom:0}
.top-card .tc-k{font-size:.66rem;letter-spacing:.06em;text-transform:uppercase;color:var(--cn-mid) !important;font-weight:700}
.top-card .tc-v{font-size:.95rem;font-weight:800;color:var(--cn-dark) !important}
.top-card .tc-v.gold{color:var(--cn-gold) !important}
.yoy-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:20px}
@media(max-width:880px){.yoy-grid{grid-template-columns:1fr}}
.yoy-card{
  background:linear-gradient(135deg,#fff,var(--cn-ivory));border:1px solid var(--cn-line);
  border-radius:20px;padding:26px 28px;box-shadow:0 16px 40px rgba(26,22,16,.06);
}
.yoy-card .yc-label{font-size:.62rem;letter-spacing:.28em;text-transform:uppercase;color:var(--cn-mid) !important;font-weight:800;margin-bottom:10px}
.yoy-card .yc-val{font-family:'Cormorant Garamond',serif !important;font-size:2.6rem;font-weight:600;color:var(--cn-gold) !important;line-height:1}
.yoy-card .yc-sub{margin-top:10px;font-size:.7rem;color:var(--cn-mid) !important;font-weight:700}
.yoy-card .yc-delta{display:inline-block;margin-top:8px;font-size:.7rem;font-weight:800;padding:.2rem .6rem;border-radius:999px}
.yoy-card .yc-delta.up{background:rgba(21,128,61,.12);color:#15803d}
.yoy-card .yc-delta.down{background:rgba(192,57,43,.12);color:#c0392b}
.home-empty{padding:40px;text-align:center;color:var(--cn-mid) !important;font-weight:700}
.help-q-wrap{display:flex;flex-direction:column;gap:12px;margin-top:6px}
.help-q-item{display:flex;align-items:flex-start;gap:14px;background:#fff;border:1px solid var(--cn-line);border-left:4px solid var(--cn-gold);border-radius:14px;padding:16px 18px;box-shadow:0 10px 26px rgba(26,22,16,.05)}
.help-q-text{font-weight:700;color:var(--cn-dark);font-size:.95rem;line-height:1.5}
.help-q-meta{margin-top:6px;font-size:.72rem;color:var(--cn-mid);font-weight:700;letter-spacing:.04em}
.help-q-x{flex-shrink:0;width:30px;height:30px;border-radius:50%;border:1px solid var(--cn-line);background:var(--cn-ivory);color:var(--cn-mid);cursor:pointer;font-weight:800;font-size:.8rem}
.help-q-x:hover{background:#c0392b;color:#fff;border-color:#c0392b}



/* ── KILL ALL PURPLE: accent vars ko gold/dark bana do (har jagah lagega) ── */
:root{
  --acc:#b8960c !important; --acc-2:#b8960c !important; --acc-deep:#1a1610 !important;
}
.sku, .sku-name, .brand{
  color:var(--cn-gold) !important;
  background:none !important; -webkit-text-fill-color:var(--cn-gold) !important;
}
.ai-msg.bot b, .ai-msg.bot strong{color:var(--cn-gold) !important}
.smart-hero-title{ background:none !important; -webkit-text-fill-color:var(--cn-dark) !important; color:var(--cn-dark) !important; }

/* ── SIDE NAV MENU — premium cream/gold ── */
.menu-btn{
  background:var(--cn-dark) !important; border:1px solid var(--cn-dark) !important;
  color:var(--cn-gold3) !important;
}
.menu-btn:hover{background:var(--cn-gold) !important;color:#fff !important;border-color:var(--cn-gold) !important}
.nav-menu, #navMenu{
  background:var(--cn-cream) !important;
  border:1px solid rgba(184,150,12,.25) !important;
  box-shadow:0 24px 60px rgba(26,22,16,.22) !important;
  max-height:calc(100vh - 96px) !important;
  overflow-y:auto !important;
  overflow-x:hidden !important;
}
.menu-item{
  background:#ffffff !important; color:var(--cn-dark) !important;
  border:1px solid var(--cn-line) !important; border-radius:12px !important;
  font-weight:800 !important; letter-spacing:1px !important;
}
.menu-item:hover, .menu-item.active{
  background:linear-gradient(135deg,var(--cn-gold2),var(--cn-gold)) !important;
  color:#1a1610 !important; border-color:transparent !important; padding-left:14px !important;
  border-left-color:transparent !important;
}

/* ── BOLD (sirf zaroori elements — har div/span par !important se hang hota tha) ── */
.kpi-t,.kpi-v,.fl,.small-note,.section-label,.sku,.sku-name,
.product-sub,.product-name,.info-value,.info-label,.menu-item,.tab,.app-chip,
.forecast-pill,.insight-val,.app-bar-brand,.app-bar-sub,.brand,
table.ro td,table.ro th,.row span,.kpi-v.gold,.kpi-v.green,.kpi-v.red,.kpi-v.orange,
.gold,.green,.red,.orange{
  font-weight:800 !important;
}
.hero-title,b,strong,th{ font-weight:800 !important; }
input::placeholder, textarea::placeholder{font-weight:500 !important;opacity:.8}



</style></head><body data-tab="home">

<canvas id="pcanvas"></canvas>

<div id="loginGate" style="position:fixed;inset:0;z-index:9999;background:radial-gradient(1200px 700px at 70% -10%,rgba(184,150,12,.10),transparent 60%),radial-gradient(1000px 700px at 10% 110%,rgba(212,175,55,.08),transparent 60%),linear-gradient(180deg,#faf8f4,#f5f0e8);display:flex;align-items:center;justify-content:center;overflow:hidden">
<style>
@keyframes lgFloatA{0%,100%{transform:translate3d(0,0,0) rotate(-8deg)}50%{transform:translate3d(30px,-40px,0) rotate(-8deg)}}
@keyframes lgFloatB{0%,100%{transform:translate3d(0,0,0) rotate(6deg)}50%{transform:translate3d(-40px,30px,0) rotate(6deg)}}
@keyframes lgFloatC{0%,100%{transform:translate3d(0,0,0) rotate(-3deg)}50%{transform:translate3d(20px,35px,0) rotate(-3deg)}}
@keyframes lgPulse{0%,100%{opacity:.5}50%{opacity:1}}
.lg-wm{position:absolute;font-family:'Cormorant Garamond','Montserrat',sans-serif;font-weight:400;letter-spacing:.4em;text-transform:uppercase;white-space:nowrap;pointer-events:none;user-select:none;
  background:linear-gradient(180deg,rgba(184,150,12,.14),rgba(212,175,55,.08));-webkit-background-clip:text;background-clip:text;color:transparent}
.lg-card{position:relative;z-index:5;width:380px;max-width:92vw;padding:42px 38px;border-radius:24px;text-align:center;
  background:#ffffff;
  border:1px solid rgba(184,150,12,.28);
  box-shadow:0 40px 110px rgba(26,22,16,.18),0 0 60px rgba(184,150,12,.08),inset 0 1px 0 rgba(255,255,255,.9);
  backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}
.lg-in{width:100%;padding:14px 16px;margin-bottom:12px;border:1px solid rgba(184,150,12,.25);border-radius:12px;font-size:13px;font-weight:600;outline:none;
  background:#f5f0e8;color:#1a1610;box-shadow:inset 0 1px 4px rgba(26,22,16,.05);transition:border-color .2s,box-shadow .2s;font-family:'Inter',sans-serif}
.lg-in:focus{border-color:#b8960c;box-shadow:inset 0 1px 4px rgba(26,22,16,.05),0 0 0 3px rgba(184,150,12,.18)}
.lg-in::placeholder{color:#a89e84}
select.lg-in option{background:#fff;color:#1a1610}
</style>
  <div class="lg-wm" style="top:6%;left:4%;font-size:clamp(20px,3.2vw,44px);animation:lgFloatA 14s ease-in-out infinite">COSA NOSTRAA</div>
  <div class="lg-wm" style="top:14%;right:-2%;font-size:clamp(14px,2.2vw,30px);opacity:.7;animation:lgFloatB 18s ease-in-out infinite">COSA NOSTRAA</div>
  <div class="lg-wm" style="top:34%;left:-4%;font-size:clamp(28px,4.5vw,64px);opacity:.5;filter:blur(1px);animation:lgFloatC 20s ease-in-out infinite">COSA NOSTRAA</div>
  <div class="lg-wm" style="top:48%;right:3%;font-size:clamp(18px,3vw,40px);animation:lgFloatA 16s ease-in-out infinite 2s">COSA NOSTRAA</div>
  <div class="lg-wm" style="bottom:26%;left:6%;font-size:clamp(13px,2vw,26px);opacity:.6;animation:lgFloatB 22s ease-in-out infinite 1s">COSA NOSTRAA</div>
  <div class="lg-wm" style="bottom:12%;right:-3%;font-size:clamp(26px,4vw,58px);opacity:.45;filter:blur(1.5px);animation:lgFloatC 17s ease-in-out infinite 3s">COSA NOSTRAA</div>
  <div class="lg-wm" style="bottom:4%;left:30%;font-size:clamp(12px,1.8vw,24px);opacity:.55;animation:lgFloatA 19s ease-in-out infinite 4s">COSA NOSTRAA</div>
  <div class="lg-wm" style="top:2%;left:42%;font-size:clamp(12px,1.6vw,22px);opacity:.5;animation:lgFloatB 15s ease-in-out infinite 2.5s">COSA NOSTRAA</div>

  <div class="lg-card">
    <div style="font-family:'Cormorant Garamond',serif;font-weight:500;font-size:30px;letter-spacing:6px;text-transform:uppercase;color:#1a1610">Cosa Nostraa</div>
    <div style="margin-top:8px;font-size:9px;letter-spacing:4px;color:#6b5e3e;font-weight:700;text-transform:uppercase">Salasar Balaji Creations Pvt. Ltd.</div>
    <div style="height:1px;background:linear-gradient(90deg,transparent,#b8960c,transparent);margin:22px 0 24px;animation:lgPulse 4s ease-in-out infinite"></div>
    <select id="lgRole" class="lg-in">
      <option value="admin">Admin Login</option>
      <option value="employee">Employee Login</option>
    </select>
    <input id="lgUser" class="lg-in" placeholder="Username" autocomplete="username" onkeydown="if(event.key==='Enter')doLogin()">
    <input id="lgPass" class="lg-in" type="password" placeholder="Password" autocomplete="current-password" onkeydown="if(event.key==='Enter')doLogin()">
    <div id="lgErr" style="color:#c0392b;font-size:11px;font-weight:800;min-height:16px;margin-bottom:10px"></div>
    <button type="button" onclick="doLogin(); return false;"
      style="width:100%;padding:14px;background:#1a1610;color:#faf8f4;border:none;border-radius:12px;font-size:12px;font-weight:800;letter-spacing:4px;text-transform:uppercase;cursor:pointer;
             box-shadow:0 14px 40px rgba(26,22,16,.22),inset 0 1px 0 rgba(255,255,255,.1);font-family:'Inter',sans-serif;transition:transform .2s,filter .2s,background .2s"
      onmouseover="this.style.transform='translateY(-2px)';this.style.background='#b8960c'" onmouseout="this.style.transform='';this.style.background='#1a1610'">Sign In</button>
  </div>
</div>

<div id="appRoot" style="display:none">

<div class="app-bar" id="appBar">
  <button class="menu-btn" onclick="toggleNavMenu()" title="Menu" aria-label="Menu">⋮</button>
  <div class="app-bar-copy">
    <div class="app-bar-brand">COSA NOSTRAA</div>
    <div class="app-bar-sub" id="appBarSub">HOME</div>
  </div>
  <div class="app-bar-actions">
    <button class="app-chip" onclick="doLogout()" style="border-color:rgba(220,38,38,.4);color:#dc2626">Sign Out</button>
  </div>
</div>

<div class="nav-menu" id="navMenu">
  <button class="menu-item" id="m1" onclick="showTab('home')">Home</button>
  <button class="menu-item" id="m2" onclick="showTab('matrix')">Overall Details</button>
  <button class="menu-item" id="m3" onclick="showTab('repeat')">Repeat Orders</button>
  <button class="menu-item" id="m4" onclick="showTab('finder')">SKU Finder</button>
  <button class="menu-item" id="m5" onclick="showTab('skudetails')">SKU Details</button>
  <button class="menu-item" id="m6" onclick="showTab('insights')">Insights</button>
  <button class="menu-item" id="m10" onclick="showTab('target')">Target</button>
  <button class="menu-item" id="m12" onclick="showTab('discount')">Discount Leakage</button>
  <button class="menu-item" id="m13" onclick="showTab('production')">Production</button>
  <button class="menu-item" id="m14" onclick="showTab('profit')">Profit Margin</button>
  <button class="menu-item" id="m16" onclick="showTab('atrisk')">At-Risk Customers</button>
  <button class="menu-item" id="m17" onclick="showTab('payments')">Payments</button>
  <button class="menu-item" id="m8" onclick="showTab('ai')" style="display:none">AI Studio</button>
  <button class="menu-item" id="m11" onclick="showTab('help')">Help</button>
</div>

<div class="hero" id="siteHero">
  <div class="hero-only">
    <div class="hero-title">COSA NOSTRAA</div>
    <div class="hero-dev">MANAGEMENT SYSTEM • DEVELOPED BY TEAM COSA NOSTRAA</div>
  </div>
</div>

<div class="tabs" style="display:none">
  <button class="tab active" id="t1" onclick="showTab('matrix')">Overall Details</button>
  <button class="tab"        id="t2" onclick="showTab('repeat')">Repeat Orders</button>
  <button class="tab"        id="t3" onclick="showTab('finder')">SKU Finder</button>
  <button class="tab"        id="t4" onclick="showTab('skudetails')">SKU Details</button>
  <button class="tab"        id="t5" onclick="showTab('insights')">Insights</button>
</div>




<div id="vHome" style="display:none"><div id="homeContent" class="home-wrap"></div></div>

<div id="dbgbox"></div>

<div class="wrap">
  <div id="loader"><div class="spin"></div>Syncing databases… please wait</div>

  <div id="vMatrix" style="display:none">
    <div class="matrix-page-title">Overall Details</div>
    <div id="kpiLock" style="display:flex;align-items:center;justify-content:center;gap:10px;flex-wrap:wrap;padding:22px 0 8px">
      <span style="font-size:11px;letter-spacing:2px;text-transform:uppercase;color:#8c7a42;font-weight:700">🔒 Revenue KPIs are locked</span>
      <input id="kpiPass" type="password" placeholder="Enter password" onkeydown="if(event.key==='Enter')unlockKpis('matrix')"
        style="padding:9px 12px;border:1px solid #d8dee9;border-radius:8px;font-size:12px;outline:none;background:#fff;color:#111;width:160px">
      <button class="go-btn" style="width:auto;padding:9px 16px;letter-spacing:2px" onclick="unlockKpis('matrix')">Unlock</button>
      <span id="kpiErr" style="color:#dc2626;font-size:11px;font-weight:700"></span>
    </div>
    <div class="kpis" id="kpiBox" style="display:none">
      <div class="kpi"><div class="kpi-t">Yesterday Net Rev</div><div class="kpi-v" id="kY">₹0</div></div>
      <div class="kpi"><div class="kpi-t">This Month Net Rev</div><div class="kpi-v" id="kM">₹0</div></div>
      <div class="kpi"><div class="kpi-t">This FY Net Rev</div><div class="kpi-v" id="kF">₹0</div></div>
      <div class="kpi"><div class="kpi-t">Previous FY Net Rev</div><div class="kpi-v" id="kPF">₹0</div></div>
      <div class="kpi"><div class="kpi-t">Total Net Rev</div><div class="kpi-v" id="kT" style="color:#f1c40f">₹0</div></div>
    </div>

    <div class="filter-box">
      <div class="fg">
        <div class="fc"><label class="fl">Search (SKU / Category)</label>
          <input class="fi" id="fSearch" placeholder='SKU, category, tag…' oninput="applyF_d()"></div>
        <div class="fc" style="grid-column:span 2">
          <label class="fl">SKU Search + Tick</label>
          <input class="fi" id="fSkuSearch" placeholder="search SKU… tick the boxes below" oninput="renderSkuChecklist()">
          <div class="small-note" style="display:flex;justify-content:space-between;align-items:center;margin:6px 0 8px;gap:10px;flex-wrap:wrap">
            <span id="skuSelInfo">0 selected</span>
            <span style="display:flex;gap:8px">
              <button class="go-btn" style="width:auto;padding:7px 12px;letter-spacing:1px" onclick="selectVisibleSkus(true)">Select Visible</button>
              <button class="go-btn" style="width:auto;padding:7px 12px;letter-spacing:1px;background:#eceff4;color:#111" onclick="clearSkuSelection()">Clear</button>
            </span>
          </div>
          <div id="skuChecklist" class="sku-checklist"></div>
        </div>
        <div class="fc"><label class="fl">Customer Name</label>
          <input class="fi" id="fCust" list="custList" placeholder="type customer…" oninput="applyF_d()">
          <datalist id="custList"></datalist></div>
        <div class="fc"><label class="fl">Type (tick one or more)</label>
          <div id="fTypeChecks" class="type-checks"></div></div>
        <div class="fc"><label class="fl">Taxon / Category</label>
          <select class="fs" id="fTaxon" onchange="applyF()"></select></div>
        <div class="fc"><label class="fl">Status</label>
          <select class="fs" id="fStatus" onchange="applyF()">
            <option value="All">All</option>
            <option value="Slow Movers">Slow Movers</option>
            <option value="Good Running">Good Running</option>
            <option value="New Launch">New Launch</option>
            <option value="No Record">No Record</option></select></div>
        <div class="fc"><label class="fl">FY Year</label>
          <select class="fs" id="fFY" onchange="applyF()"></select></div>
        <div class="fc"><label class="fl">Plating</label>
          <select class="fs" id="fPlat" onchange="applyF()"></select></div>
        <div class="fc"><label class="fl">MRP Range</label>
          <select class="fs" id="fMrp" onchange="applyF()">
            <option value="">All Prices</option>
            <option value="0-500">0 – 500</option>
            <option value="500-1000">500 – 1,000</option>
            <option value="1000-1500">1,000 – 1,500</option>
            <option value="1500-2000">1,500 – 2,000</option>
            <option value="2000-3000">2,000 – 3,000</option>
            <option value="3000-5000">3,000 – 5,000</option>
            <option value="5000-10000">5,000 – 10,000</option>
            <option value="10000-">10,000+</option></select></div>
        <div class="fc"><label class="fl">Launch Month</label>
          <select class="fs" id="fLaunch" onchange="applyF()">
            <option value="All">All Months</option></select></div>
        <div class="fc"><label class="fl">Date From</label>
          <input class="fi" type="date" id="fD1" onchange="applyF()" style="margin-bottom:8px">
          <label class="fl">Date To</label>
          <input class="fi" type="date" id="fD2" onchange="applyF()"></div>
        <div class="fc" style="align-self:end">
          <button class="go-btn" style="letter-spacing:2px;padding:10px" onclick="resetFilters()">Reset Filters</button></div>
      </div>
    </div>
    <div class="filter-box" style="margin-top:-10px">
      <span class="small-note"><b>New Launch</b> = launched this month (launch date) &nbsp;|&nbsp; <b>Slow Movers</b> = stock+WIP ≥ 20 &amp; no dispatch last 6 months &nbsp;|&nbsp; <b>No Record</b> = no dispatch in COSSA &nbsp;|&nbsp; <b>Good Running</b> = all others</span>
    </div>
    <div class="grid" id="gMatrix"></div>
  </div>

  <div id="vRepeat" style="display:none">


    <div class="kpis">
      <div class="kpi"><div class="kpi-t">SKUs shown</div><div class="kpi-v" id="rCount" style="color:#d4af5a">0</div></div>
      <div class="kpi"><div class="kpi-t">Total Final Qty</div><div class="kpi-v" id="rQty" style="color:#d4af5a">0</div></div>
      <div class="kpi"><div class="kpi-t">Inv WIP</div><div class="kpi-v" id="rWip" style="color:#e67e22">0</div></div>
      <div class="kpi"><div class="kpi-t">7D Sale Qty</div><div class="kpi-v" id="rQty7d" style="color:#2ecc71">0</div></div>
      <div class="kpi"><div class="kpi-t">15D Sale Qty</div><div class="kpi-v" id="rQty15d" style="color:#2ecc71">0</div></div>
      <div class="kpi"><div class="kpi-t">30D Sale Qty</div><div class="kpi-v" id="rQty30d" style="color:#2ecc71">0</div></div>
      <div class="kpi"><div class="kpi-t">Avg Forecast 60d</div><div class="kpi-v" id="rFc" style="color:#2ecc71">0</div></div>
    </div>

    <div class="filter-box">
      <div class="fg">
        <div class="fc"><label class="fl">Search SKU</label>
          <input class="fi" id="rSearch" placeholder='SKU name…' oninput="applyRO_d()"></div>
        <div class="fc" style="grid-column:span 2">
          <label class="fl">SKU Search + Tick</label>
          <input class="fi" id="rSkuSearch" placeholder="search SKU… tick the boxes below" oninput="renderRoSkuChecklist()">
          <div class="small-note" style="display:flex;justify-content:space-between;align-items:center;margin:6px 0 8px;gap:10px;flex-wrap:wrap">
            <span id="rSkuSelInfo">0 selected</span>
            <span style="display:flex;gap:8px">
              <button class="go-btn" style="width:auto;padding:7px 12px;letter-spacing:1px" onclick="selectVisibleRoSkus()">Select Visible</button>
              <button class="go-btn" style="width:auto;padding:7px 12px;letter-spacing:1px;background:#eceff4;color:#111" onclick="clearSkuSelection()">Clear</button>
            </span>
          </div>
          <div id="rSkuChecklist" class="sku-checklist"></div>
          <label class="fl" style="margin-top:12px">Paste multiple SKUs (any separator — comma, space, or new line)</label>
          <textarea id="rPasteSkus" class="fi" rows="3" placeholder="e.g.&#10;BT-0057&#10;BH-0001, BA-0001&#10;BH-0003"
            style="resize:vertical;font-family:monospace"></textarea>
          <div style="display:flex;gap:8px;margin-top:8px;flex-wrap:wrap">
            <button class="go-btn" style="width:auto;padding:8px 14px;letter-spacing:1px" onclick="applyPastedSkus()">Show Pasted SKUs</button>
            <button class="go-btn" style="width:auto;padding:8px 14px;letter-spacing:1px;background:#eceff4;color:#111" onclick="clearPastedSkus()">Clear Pasted</button>
            <span id="rPasteInfo" class="small-note" style="align-self:center"></span>
          </div>
          <div style="margin-top:12px;display:flex;gap:10px;flex-wrap:wrap;align-items:center">
            <input type="file" id="rUploadFile" accept=".csv,.xls,.xlsx" style="display:none" onchange="handleRepeatUpload(this)">
            <button class="go-btn" style="width:auto;padding:8px 14px;letter-spacing:1px" onclick="document.getElementById('rUploadFile').click()">Upload File</button>
            <span id="rUploadInfo" class="small-note"></span>
          </div>
        </div>
        <div class="fc"><label class="fl">Type (tick one or more)</label>
          <div id="rTypeChecks" class="type-checks"></div></div>
        <div class="fc"><label class="fl">Taxon / Category</label>
          <select class="fs" id="rTaxon" onchange="applyRO()"></select></div>
        <div class="fc"><label class="fl">Pack Details (tick one or more)</label>
          <div id="rPackChecks" class="type-checks"></div></div>
        <div class="fc"><label class="fl">Customer Name</label>
          <input class="fi" id="rCust" list="custList2" placeholder="type customer…" oninput="applyRO_d()">
          <datalist id="custList2"></datalist></div>
        <div class="fc"><label class="fl">Dispatch Date From</label>
          <input class="fi" type="date" id="rD1" onchange="applyRO()" style="margin-bottom:8px">
          <label class="fl">Dispatch Date To</label>
          <input class="fi" type="date" id="rD2" onchange="applyRO()"></div>
        <div class="fc" style="align-self:end">
          <button class="go-btn" style="letter-spacing:2px;padding:10px" onclick="resetRO()">Reset</button></div>
      </div>
    </div>

    <div class="ro-tools">
      <div class="small-note">Tick SKUs to export only those rows — otherwise the whole filtered table is exported. <b><span id="roExportHint">Exporting: all filtered rows</span></b></div>
      <div class="ro-export">
        <button class="go-btn" style="width:auto;padding:9px 14px;letter-spacing:2px" onclick="exportRO('csv')">Export CSV</button>
        <button class="go-btn" style="width:auto;padding:9px 14px;letter-spacing:2px;background:#f3f6fb;color:#111" onclick="exportRO('xls')">Export Excel</button>
      </div>
    </div>
    <div class="ro-wrap">
      <div class="ro-table-wrap">
        <div id="roViewToggle" style="display:none;gap:8px;margin:0 0 12px">
          <button class="mini-btn active" id="roViewPivot" onclick="setRoView('pivot')">SKU PIVOT</button>
          <button class="mini-btn" id="roViewTxns" onclick="setRoView('txns')">TRANSACTIONS</button>
        </div>
        <!-- Google Sheets-style column filters -->
        <div class="ro-col-filters" id="roColFilters">
          <div class="cf-group" style="min-width:110px">
            <label>SKU</label>
            <input type="text" id="cfSku" placeholder="Filter SKU…" oninput="applyColFilters()">
          </div>
          <div class="cf-group">
            <label>7D Sale</label>
            <select id="cfQty7d" onchange="applyColFilters()">
              <option value="">All</option>
              <option value="gt0">&gt; 0</option>
              <option value="gt5">&gt; 5</option>
              <option value="gt10">&gt; 10</option>
              <option value="0">= 0</option>
            </select>
          </div>
          <div class="cf-group">
            <label>15D Sale</label>
            <select id="cfQty15d" onchange="applyColFilters()">
              <option value="">All</option>
              <option value="gt0">&gt; 0</option>
              <option value="gt5">&gt; 5</option>
              <option value="gt10">&gt; 10</option>
              <option value="0">= 0</option>
            </select>
          </div>
          <div class="cf-group">
            <label>30D Sale</label>
            <select id="cfQty30d" onchange="applyColFilters()">
              <option value="">All</option>
              <option value="gt0">&gt; 0</option>
              <option value="gt5">&gt; 5</option>
              <option value="gt10">&gt; 10</option>
              <option value="0">= 0</option>
            </select>
          </div>
          <div class="cf-group">
            <label>Sold Qty</label>
            <select id="cfSoldQty" onchange="applyColFilters()">
              <option value="">All</option>
              <option value="gt0">&gt; 0</option>
              <option value="gt10">&gt; 10</option>
              <option value="gt50">&gt; 50</option>
              <option value="gt100">&gt; 100</option>
              <option value="0">= 0</option>
            </select>
          </div>
          <div class="cf-group">
            <label>Inv Stock</label>
            <select id="cfInvStock" onchange="applyColFilters()">
              <option value="">All</option>
              <option value="gt0">&gt; 0</option>
              <option value="gt10">&gt; 10</option>
              <option value="gt50">&gt; 50</option>
              <option value="0">= 0</option>
            </select>
          </div>
          <div class="cf-group">
            <label>Inv WIP</label>
            <select id="cfInvWip" onchange="applyColFilters()">
              <option value="">All</option>
              <option value="gt0">&gt; 0</option>
              <option value="gt5">&gt; 5</option>
              <option value="gt10">&gt; 10</option>
              <option value="0">= 0</option>
            </select>
          </div>
          <div class="cf-group">
            <label>Forecast 60d</label>
            <select id="cfForecast" onchange="applyColFilters()">
              <option value="">All</option>
              <option value="gt0">&gt; 0</option>
              <option value="gt5">&gt; 5</option>
              <option value="gt10">&gt; 10</option>
              <option value="0">= 0</option>
            </select>
          </div>
          <div class="cf-group">
            <label>Reorder Qty</label>
            <select id="cfReorder" onchange="applyColFilters()">
              <option value="">All</option>
              <option value="gt0">&gt; 0</option>
              <option value="gt5">&gt; 5</option>
              <option value="gt10">&gt; 10</option>
              <option value="0">= 0</option>
            </select>
          </div>
          <div class="cf-group">
            <label>Remark</label>
            <input type="text" id="cfRemark" placeholder="Filter remark…" oninput="applyColFilters()">
          </div>
          <button class="cf-reset" onclick="resetColFilters()">✕ Clear</button>
        </div>
        <table class="ro" id="roTable">
          <thead><tr>
            <th style="width:46px;text-align:center"><input type="checkbox" id="roSelectAll" onclick="roToggleAll(this.checked)" title="Select all"></th>
            <th>SKU</th>
            <th class="sort-arrow" onclick="sortRO('qty_7d',this)">7D Sale</th>
            <th class="sort-arrow" onclick="sortRO('qty_15d',this)">15D Sale</th>
            <th class="sort-arrow" onclick="sortRO('qty_1m',this)">30D Sale</th>
            <th class="sort-arrow" onclick="sortRO('final_qty',this)">Sold Qty</th>
            <th class="sort-arrow" onclick="sortRO('inv_stock',this)">Inv Stock</th>
            <th class="sort-arrow" onclick="sortRO('inv_wip',this)">Inv WIP</th>
            <th class="sort-arrow" onclick="sortRO('forecast_60d',this)" title="Expected units to sell in the next 60 days. Based on recent sales velocity: last 60 days weighted 70%, last 180 days 30%, plus a small trend adjustment.">Forecast Sold Qty (60 days)</th>
            <th class="sort-arrow" onclick="sortRO('reorder_qty',this)">Reorder Qty</th>
            <th style="min-width:160px">Remark</th>
          </tr></thead>
          <tbody id="roBody"></tbody>
        </table>
      </div>
      <div id="roEmpty" class="tno-data" style="display:none">No matching SKUs</div>
    </div>
  </div>

  <div id="vFinder" style="display:none">
    <div style="max-width:620px;margin:24px auto">
      <div class="upload-area" id="finderDrop" tabindex="0" onclick="document.getElementById('imgF').click()" ondragover="event.preventDefault()" ondrop="handleFinderDrop(event)">
        <div style="font-size:38px;margin-bottom:12px">📷</div>
        <div style="font-size:11px;color:#6a5a2a;text-transform:uppercase;letter-spacing:2px;font-weight:700">Click, paste, or drop product photo</div>
        <input type="file" id="imgF" accept="image/*" style="display:none" onchange="onImg(this)">
        <img id="preview">
      </div>
      <button class="go-btn" id="goBtn" onclick="doVision()" disabled>Scan &amp; Find SKU</button>
    </div>
    <div class="grid" id="gFinder"></div>
  </div>

  <div id="vSkudetails" style="display:none">
    <div id="sdEmpty" class="tno-data" style="padding:60px 20px">
      Click any SKU (or its <b>Details</b> button) in the Overall Details or Repeat Orders tab to see its full transaction history here.
    </div>
    <div id="sdContent" style="display:none">
      <div style="display:flex;justify-content:flex-start;margin:8px 0 10px">
        <button id="sdBackBtn" class="home-back" onclick="goBackFromDetails()">← Back</button>
      </div>
      <div class="sd-head">
        <div class="sd-head-img" id="sdImg"></div>
        <div class="sd-head-info">
          <div class="sd-sku" id="sdSku">—</div>
          <div class="sd-meta" id="sdMeta"></div>
        </div>
      </div>
      <div class="kpis" style="justify-content:flex-start">
        <div class="kpi"><div class="kpi-t">Total Orders</div><div class="kpi-v" id="sdOrders" style="color:#d4af5a">0</div></div>
        <div class="kpi"><div class="kpi-t">Total Final Qty</div><div class="kpi-v" id="sdQty" style="color:#d4af5a">0</div></div>
        <div class="kpi rev-only"><div class="kpi-t">Net Revenue (COSSA)</div><div class="kpi-v" id="sdRev">₹0</div></div>
        <div class="kpi"><div class="kpi-t">Unique Customers</div><div class="kpi-v" id="sdCust" style="color:#2ecc71">0</div></div>
      </div>

      <div class="filter-box" style="margin:6px 0 14px">
        <label class="fl" style="margin-bottom:10px;display:block">Sales by Type</label>
        <div id="sdTypeBreakdown" class="type-breakdown"></div>
        <label class="fl" style="margin:14px 0 8px;display:block">Filter by Type (tick to see only those)</label>
        <div id="sdTypeChecks" class="type-checks"></div>
      </div>

      <div class="ro-tools">
        <div class="small-note">Every dispatch recorded in COSSA for this SKU — customer, date, type, final qty and net revenue.</div>
        <div class="ro-export">
          <button class="go-btn" style="width:auto;padding:9px 14px;letter-spacing:2px" onclick="exportSD('csv')">Export CSV</button>
          <button class="go-btn" style="width:auto;padding:9px 14px;letter-spacing:2px;background:#f3f6fb;color:#111" onclick="exportSD('xls')">Export Excel</button>
        </div>
      </div>
      <div class="ro-wrap"><div class="ro-table-wrap">
        <table class="ro" id="sdTable">
          <thead><tr>
            <th>Dispatch Date</th>
            <th>Customer</th>
            <th>Type</th>
            <th>Final Qty</th>
            <th>Net Revenue</th>
          </tr></thead>
          <tbody id="sdBody"></tbody>
        </table>
      </div></div>
    </div>
  </div>
</div>
  <div id="vSmart" style="display:none">
    <div class="smart-hero">
      <div class="smart-hero-kicker">VISUAL INTELLIGENCE</div>
      <div class="smart-hero-title">Smart Search</div>
      <div class="smart-hero-sub">Search your entire catalog by visual concept</div>
    </div>
    <div class="smart-box">
      <div class="smart-row">
        <input class="fi" id="smartQ" placeholder="Type any concept — lion, skull, eagle, om, snake, anchor…"
          onkeydown="if(event.key==='Enter'){smartSearch();}">
        <button class="ai-hbtn design" id="smartBtn" onclick="smartSearch()">SEARCH</button>
        <button class="ai-hbtn" onclick="smartClear()">CLEAR</button>
      </div>
      <div class="smart-note" id="smartNote" style="display:none"></div>
    </div>
    <div class="ai-cards" id="smartResults" style="margin-top:18px"></div>
  </div>

  <div id="vAi" style="display:none"></div>


  <div id="vMarketplaces" style="display:none">
    <div id="marketplaceRoot"></div>
  </div>

  <div id="vHelp" style="display:none">
  <div class="insights-head">
    <div>
      <div class="insights-title">Help &amp; Support</div>
    </div>
  </div>
  <div class="filter-box" style="margin:14px 0;max-width:680px">
    <label class="fl" style="margin-bottom:8px;display:block">Your problem / query</label>
    <textarea id="helpText" rows="5" placeholder="Type your issue here…"
      style="width:100%;padding:14px 16px;border:1px solid var(--cn-line);border-radius:12px;background:var(--cn-ivory);color:var(--cn-dark);font-family:inherit;font-size:14px;font-weight:600;resize:vertical;outline:none"></textarea>
    <div style="display:flex;align-items:center;gap:14px;margin-top:14px">
      <button class="go-btn" style="width:auto;padding:12px 30px;letter-spacing:2px" onclick="submitHelp()">OK · Send</button>
      <span id="helpMsg" style="font-weight:700;color:var(--cn-mid)"></span>
    </div>
  </div>
  </div>


  <div id="vAtrisk" style="display:none">
  <div class="insights-head">
    <div><div class="insights-title">At-Risk Customers</div></div>
    <div class="insight-toolbar-actions">
      <button class="go-btn" style="width:auto;padding:10px 14px;letter-spacing:2px" onclick="loadAtRisk()">Refresh</button>
      <button class="go-btn" style="width:auto;padding:10px 14px;letter-spacing:2px;background:#2f6f3e" onclick="exportAtRisk()">Export CSV</button>
    </div>
  </div>
  <div class="filter-box" style="margin:10px 0 16px;display:flex;gap:16px;flex-wrap:wrap;align-items:flex-end">
    <div class="fc"><label class="fl">Not ordered for</label>
      <select class="fs" id="arGap" onchange="loadAtRisk()">
        <option value="60">60+ days</option>
        <option value="90">90+ days</option>
        <option value="120">120+ days</option>
        <option value="180">180+ days</option>
      </select></div>
  </div>
  <p style="color:var(--cn-mid);font-size:.85rem;margin:0 0 12px">Customers who used to order regularly (2+ orders) but haven't returned. Reach out before they're lost.</p>
  <div id="arSummary" class="yoy-grid" style="margin-bottom:16px;grid-template-columns:repeat(2,1fr)"></div>
  <div id="arContent" class="ro-table-wrap" style="padding:0;overflow:auto;max-height:70vh"></div>
  </div>

  <div id="vPayments" style="display:none">
  <div class="insights-head">
    <div><div class="insights-title">Payments</div>
      <div style="color:var(--cn-mid);font-size:.8rem" id="payAsOf"></div></div>
    <div class="insight-toolbar-actions">
      <button class="go-btn" style="width:auto;padding:10px 14px;letter-spacing:2px" onclick="loadPayments(true)">Refresh</button>
      <button class="go-btn" style="width:auto;padding:10px 14px;letter-spacing:2px;background:#2f6f3e" onclick="exportPayments()">Export CSV</button>
    </div>
  </div>
  <div class="filter-box" style="margin:10px 0 16px;display:flex;gap:16px;flex-wrap:wrap;align-items:flex-end">
    <div class="fc"><label class="fl">Tag / Type</label>
      <select class="fs" id="payTag" onchange="renderPayments()"><option value="">All Tags</option></select></div>
    <div class="fc"><label class="fl">Search Customer</label>
      <input class="fi" id="paySearch" placeholder="Customer name…" oninput="renderPayments()" style="min-width:200px"></div>
    <div class="fc"><label class="fl">Show</label>
      <select class="fs" id="payView" onchange="renderPayments()">
        <option value="overdue">Has Overdue</option>
        <option value="all" selected>All Outstanding</option>
        <option value="due">Has Due (not overdue)</option>
      </select></div>
  </div>
  <div id="paySummary" class="yoy-grid" style="margin-bottom:16px;grid-template-columns:repeat(3,1fr)"></div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-bottom:18px">
    <div><div class="insights-title" style="font-size:1rem;margin-bottom:8px">Outstanding till today</div>
      <div id="payTodayTable" class="ro-table-wrap" style="padding:0;overflow:auto;max-height:60vh"></div></div>
    <div><div class="insights-title" style="font-size:1rem;margin-bottom:8px">Aging Bucket</div>
      <div id="payAgingTable"></div></div>
  </div>
  </div>

  <div id="vProfit" style="display:none">
  <div class="insights-head">
    <div>
      <div class="insights-title">Net Profit Margin</div>
    </div>
    <div class="insight-toolbar-actions">
      <button class="go-btn" style="width:auto;padding:10px 16px;letter-spacing:2px;background:#2f6f3e" onclick="exportProfit()">Export CSV</button>
      <button class="go-btn" style="width:auto;padding:10px 16px;letter-spacing:2px;background:#f3f6fb;color:#111" onclick="resetProfit()">Reset</button>
    </div>
  </div>

  <div class="pm-mode">
    <button class="pm-mode-btn on" id="pmOld" onclick="pmSetMode('old')">Old Product · auto from sheet</button>
    <button class="pm-mode-btn" id="pmNew" onclick="pmSetMode('new')">New Product · manual</button>
  </div>
  <div class="pm-note" id="pmNote">Pick a SKU — MRP and Product Cost load from the All Product sheet. You can still edit anything.</div>

  <div class="pm-grid">
    <div class="filter-box pm-inputs">
      <div class="pm-skurow" id="pmSkuRow">
        <label class="fl">Find SKU</label>
        <div style="position:relative">
          <input class="fi" id="pmSkuSearch" placeholder="Type SKU, e.g. BH-1290" autocomplete="off" oninput="pmSkuType()" onfocus="pmSkuType()" style="font-family:'JetBrains Mono',monospace;font-weight:700">
          <div class="pm-skulist" id="pmSkuList"></div>
        </div>
        <div class="pm-skustatus" id="pmSkuStatus">Loading catalogue…</div>
      </div>

      <div class="pm-two">
        <div class="fc"><label class="fl">MRP (₹)</label><input type="number" class="fi pm-num" id="pmMrp" placeholder="0" min="0" oninput="pmCalc()"></div>
        <div class="fc"><label class="fl">Discount (%)</label><input type="number" class="fi pm-num" id="pmDisc" placeholder="0" min="0" max="100" step="0.5" oninput="pmCalc()"></div>
      </div>

      <div class="pm-sp">
        <span class="pm-sp-lab">Selling Price (SP)</span>
        <span class="pm-sp-val" id="pmSpOut">₹0</span>
      </div>

      <div class="pm-two">
        <div class="fc"><label class="fl">Final Qty (for total)</label><input type="number" class="fi pm-num" id="pmQty" placeholder="1" min="0" oninput="pmCalc()"></div>
        <div class="fc"><label class="fl">Net Revenue (COSSA)</label><input type="number" class="fi pm-num" id="pmNetRev" placeholder="0" min="0" readonly style="background:#f5f0e6"></div>
      </div>

      <div class="pm-seclabel"><span>Deductions</span><span class="ln"></span></div>

      <div class="fc" style="margin-bottom:12px"><label class="fl">Commission (% of SP)</label><input type="number" class="fi pm-num" id="pmComm" placeholder="0" min="0" step="0.1" oninput="pmCalc()"></div>
      <div class="pm-two">
        <div class="fc"><label class="fl">Product Cost (₹)</label><input type="number" class="fi pm-num" id="pmProdCost" placeholder="0" min="0" oninput="pmCalc()"></div>
        <div class="fc"><label class="fl">Box Cost (₹)</label><input type="number" class="fi pm-num" id="pmBox" placeholder="0" min="0" oninput="pmCalc()"></div>
      </div>
      <div class="pm-two">
        <div class="fc"><label class="fl">Pack Fee (₹)</label><input type="number" class="fi pm-num" id="pmPack" placeholder="0" min="0" oninput="pmCalc()"></div>
        <div class="fc"><label class="fl">Shipping Fees (₹)</label><input type="number" class="fi pm-num" id="pmShip" placeholder="0" min="0" oninput="pmCalc()"></div>
      </div>
      <div class="pm-two">
        <div class="fc"><label class="fl">Ad Spend (₹)</label><input type="number" class="fi pm-num" id="pmAd" placeholder="0" min="0" oninput="pmCalc()"></div>
        <div class="fc"><label class="fl">PG Charges (₹)</label><input type="number" class="fi pm-num" id="pmPG" placeholder="0" min="0" oninput="pmCalc()"></div>
      </div>
      <div class="pm-two">
        <div class="fc"><label class="fl">CR / RTO Charges (₹)</label><input type="number" class="fi pm-num" id="pmRTO" placeholder="0" min="0" oninput="pmCalc()"></div>
        <div class="fc"><label class="fl">Inwarding Fee (₹)</label><input type="number" class="fi pm-num" id="pmInward" placeholder="0" min="0" oninput="pmCalc()"></div>
      </div>
      <div class="pm-two">
        <div class="fc"><label class="fl">Storage Fee (₹)</label><input type="number" class="fi pm-num" id="pmStore" placeholder="0" min="0" oninput="pmCalc()"></div>
        <div class="fc"><label class="fl">Fulfillment Fee (₹)</label><input type="number" class="fi pm-num" id="pmFulfil" placeholder="0" min="0" oninput="pmCalc()"></div>
      </div>
      <div class="fc"><label class="fl">Inventory Recall (₹)</label><input type="number" class="fi pm-num" id="pmRecall" placeholder="0" min="0" oninput="pmCalc()"></div>
    </div>

    <div class="pm-result">
      <div class="pm-hero">
        <div class="pm-hero-lab">Net Profit Margin</div>
        <div class="pm-margin pos" id="pmMargin">0.0%</div>
        <div class="pm-profit" id="pmProfitTop">₹0 profit</div>
        <div><span class="pm-verdict thin" id="pmVerdict">Enter values</span></div>
      </div>
      <div class="pm-break">
        <div class="pm-br head"><span>Selling Price</span><span id="pmBrSP">₹0</span></div>
        <div class="pm-br minus"><span>Commission</span><span id="pmBrComm">−₹0</span></div>
        <div class="pm-br minus"><span>Product Cost</span><span id="pmBrProd">−₹0</span></div>
        <div class="pm-br minus"><span>Box Cost</span><span id="pmBrBox">−₹0</span></div>
        <div class="pm-br minus"><span>Pack Fee</span><span id="pmBrPack">−₹0</span></div>
        <div class="pm-br minus"><span>Shipping Fees</span><span id="pmBrShip">−₹0</span></div>
        <div class="pm-br minus"><span>Ad Spend</span><span id="pmBrAd">−₹0</span></div>
        <div class="pm-br minus"><span>PG Charges</span><span id="pmBrPG">−₹0</span></div>
        <div class="pm-br minus"><span>CR / RTO Charges</span><span id="pmBrRTO">−₹0</span></div>
        <div class="pm-br minus"><span>Inwarding Fee</span><span id="pmBrInward">−₹0</span></div>
        <div class="pm-br minus"><span>Storage Fee</span><span id="pmBrStore">−₹0</span></div>
        <div class="pm-br minus"><span>Fulfillment Fee</span><span id="pmBrFulfil">−₹0</span></div>
        <div class="pm-br minus"><span>Inventory Recall</span><span id="pmBrRecall">−₹0</span></div>
        <div class="pm-br total"><span>Total Deductions <span style="opacity:.6;font-weight:600">(per unit)</span></span><span id="pmBrTotal">−₹0</span></div>
        <div class="pm-br profit-row pos"><span>Profit Amount <span style="opacity:.6;font-weight:600">(per unit)</span></span><span id="pmBrProfit">₹0</span></div>
      </div>
      <div class="pm-break" id="pmTotalBox" style="margin-top:14px">
        <div class="pm-br head"><span>Final Qty</span><span id="pmTotQty">1</span></div>
        <div class="pm-br"><span>Total Selling Value</span><span id="pmTotSP">₹0</span></div>
        <div class="pm-br minus"><span>Total Deductions</span><span id="pmTotDed">−₹0</span></div>
        <div class="pm-br profit-row pos"><span>Total Profit (× Qty)</span><span id="pmTotProfit">₹0</span></div>
      </div>
    </div>
  </div>
  </div>

  <div id="vProduction" style="display:none">
  <div class="insights-head">
    <div>
      <div class="insights-title">Production (PPC-WIP)</div>
    </div>
    <div class="insight-toolbar-actions">
      <button class="go-btn" style="width:auto;padding:10px 14px;letter-spacing:2px" onclick="loadProduction()">Refresh</button>
      <button class="go-btn" style="width:auto;padding:10px 14px;letter-spacing:2px;background:#2f6f3e" onclick="exportProduction()">Export CSV</button>
    </div>
  </div>
  <div class="filter-box" style="margin:10px 0 16px;display:flex;gap:14px;flex-wrap:wrap;align-items:flex-end">
    <div class="fc"><label class="fl">Channel</label>
      <select class="fs" id="prodChannel" onchange="loadProduction()"><option value="">All Channels</option></select></div>
    <div class="fc"><label class="fl">Balance Qty</label>
      <select class="fs" id="prodBalance" onchange="loadProduction()">
        <option value="">All</option>
        <option value="yes">Yes (pending only)</option>
        <option value="no">No (completed)</option>
      </select></div>
    <div class="fc"><label class="fl">Type</label>
      <select class="fs" id="prodType" onchange="loadProduction()"><option value="">All Types</option></select></div>
    <div class="fc"><label class="fl">Taxon</label>
      <select class="fs" id="prodTaxon" onchange="loadProduction()"><option value="">All Taxons</option></select></div>
    <div class="fc"><label class="fl">Search SKU</label>
      <input class="fi" id="prodSku" placeholder="type SKU…" oninput="prodSearchDebounced()"></div>
    <div class="fc"><label class="fl">Search Order No.</label>
      <input class="fi" id="prodOrderNo" placeholder="type order no…" oninput="prodSearchDebounced()"></div>
    <div class="fc"><label class="fl">Order date from</label>
      <input class="fi" id="prodOD1" type="date" onchange="loadProduction()"></div>
    <div class="fc"><label class="fl">Order date to</label>
      <input class="fi" id="prodOD2" type="date" onchange="loadProduction()"></div>
    <div class="fc"><label class="fl">Delivery date from</label>
      <input class="fi" id="prodDD1" type="date" onchange="loadProduction()"></div>
    <div class="fc"><label class="fl">Delivery date to</label>
      <input class="fi" id="prodDD2" type="date" onchange="loadProduction()"></div>
    <button class="go-btn" style="width:auto;padding:10px 18px;background:#f3f6fb;color:#111" onclick="resetProduction()">Reset</button>
  </div>
  <div id="prodSummary" class="yoy-grid" style="margin-bottom:16px;grid-template-columns:repeat(3,1fr)"></div>
  <div id="prodContent" class="ro-table-wrap" style="padding:0;overflow-x:auto"></div>
  </div>

  <div id="vDiscount" style="display:none">
  <div class="insights-head">
    <div>
      <div class="insights-title">Discount Leakage</div>
    </div>
    <div class="insight-toolbar-actions">
      <button class="go-btn" style="width:auto;padding:10px 14px;letter-spacing:2px" onclick="loadDiscount()">Refresh</button>
      <button class="go-btn" style="width:auto;padding:10px 14px;letter-spacing:2px;background:#2f6f3e" onclick="exportDiscount()">Export CSV</button>
    </div>
  </div>
  <div class="filter-box" style="margin:10px 0 16px;display:flex;gap:18px;flex-wrap:wrap;align-items:flex-end">
    <div class="fc"><label class="fl">Min Discount %</label>
      <select class="fs" id="discMin" onchange="loadDiscount()">
        <option value="0">All (any discount)</option>
        <option value="10">10%+</option>
        <option value="20">20%+</option>
        <option value="30">30%+</option>
        <option value="40">40%+</option>
        <option value="50">50%+</option>
      </select></div>
    <div class="fc"><label class="fl">Sort By</label>
      <select class="fs" id="discSort" onchange="loadDiscount()">
        <option value="leakage">Leakage (value lost)</option>
        <option value="discount">Discount %</option>
        <option value="qty">Qty sold</option>
        <option value="revenue">Net Revenue</option>
      </select></div>
  </div>
  <div id="discSummary" class="yoy-grid" style="margin-bottom:16px"></div>
  <div id="discContent" class="ro-table-wrap" style="padding:0;overflow-x:auto"></div>
  </div>


  <div id="vTarget" style="display:none">
  <div class="insights-head">
    <div>
      <div class="insights-title">Target vs Actual</div>
    </div>
    <div class="insight-toolbar-actions">
      <button class="go-btn" style="width:auto;padding:10px 14px;letter-spacing:2px" onclick="loadTarget()">Refresh</button>
      <button class="go-btn" style="width:auto;padding:10px 14px;letter-spacing:2px;background:#2f6f3e" onclick="exportTarget()">Export CSV</button>
    </div>
  </div>
  <div class="filter-box" style="margin:10px 0 16px;display:flex;gap:18px;flex-wrap:wrap;align-items:flex-end">
    <div class="fc"><label class="fl">Month</label>
      <select class="fs" id="tgtMonth" onchange="loadTarget()"></select></div>
    <div class="fc"><label class="fl">Stake Holder</label>
      <select class="fs" id="tgtStake" onchange="loadTarget()"><option value="">All Stake Holders</option></select></div>
    <div class="fc"><label class="fl">Channel</label>
      <select class="fs" id="tgtChannel" onchange="loadTarget()"><option value="">All Channels</option></select></div>
  </div>
  <div id="tgtContent" class="ro-table-wrap" style="padding:0;overflow-x:auto"></div>
  </div>


  <div id="vInsights" style="display:none">
  <div class="insights-head">
    <div>
      <div class="insights-title">Performance Insights</div>
      <div class="insights-sub">Filter by type, taxon and dispatch date range. Export the visible result set in one click.</div>
    </div>
    <div class="insight-toolbar-actions">
      <button class="go-btn" style="width:auto;padding:10px 14px;letter-spacing:2px" onclick="applyInsights()">Refresh Insights</button>
      <button class="go-btn" style="width:auto;padding:10px 14px;letter-spacing:2px;background:#f3f6fb;color:#111" onclick="resetInsights()">Reset</button>
      <button class="go-btn" style="width:auto;padding:10px 14px;letter-spacing:2px;background:#f3f6fb;color:#111" onclick="exportInsights('csv')">Export CSV</button>
      <button class="go-btn" style="width:auto;padding:10px 14px;letter-spacing:2px;background:#f3f6fb;color:#111" onclick="exportInsights('xls')">Export Excel</button>
    </div>
  </div>

  <div id="insightKpiLock" style="display:flex;align-items:center;justify-content:center;gap:10px;flex-wrap:wrap;padding:18px 0 8px">
    <span style="font-size:11px;letter-spacing:2px;text-transform:uppercase;color:#8c7a42;font-weight:700">🔒 Insight KPIs are locked</span>
    <input id="iKpiPass" type="password" placeholder="Enter password" onkeydown="if(event.key==='Enter')unlockKpis('insights')"
      style="padding:9px 12px;border:1px solid #d8dee9;border-radius:8px;font-size:12px;outline:none;background:#fff;color:#111;width:160px">
    <button class="go-btn" style="width:auto;padding:9px 16px;letter-spacing:2px" onclick="unlockKpis('insights')">Unlock</button>
    <span id="iKpiErr" style="color:#dc2626;font-size:11px;font-weight:700"></span>
  </div>
  <div class="insight-summary" id="insightSummary" style="display:none"></div>

  <div class="insight-toolbar">
    <div class="insight-toolbar-head">
      <div>
        <div class="title">Insights Filters</div>
        <div class="sub">Use these controls to narrow the analysis and keep exports aligned with what you see.</div>
      </div>

    <div class="fg">
      <div class="fc">
        <label class="fl">Type</label>
        <div id="iTypeChecks" class="type-checks"></div>
      </div>
      <div class="fc">
        <label class="fl">Taxon / Category</label>
        <select class="fs" id="iTaxon" onchange="applyInsights()"></select>
      </div>
      <div class="fc">
        <label class="fl">Sort By</label>
        <select class="fs" id="iSort" onchange="applyInsights()">
          <option value="revenue">By Revenue (high → low)</option>
          <option value="qty">By Quantity (high → low)</option>
        </select>
      </div>
      <div class="fc">
        <label class="fl">Dispatch Date From</label>
        <input class="fi" type="date" id="iD1" onchange="applyInsights()" style="margin-bottom:8px">
        <label class="fl">Dispatch Date To</label>
        <input class="fi" type="date" id="iD2" onchange="applyInsights()">
      </div>
      <div class="fc" style="align-self:end">
        <button class="go-btn" style="width:100%;letter-spacing:2px;padding:10px" onclick="applyInsights()">Apply Filters</button>
      </div>
    </div>
  </div>

  <div class="insights-grid">
    <div class="insight-card">
      <div class="insight-card-head">
        <h3>Top Revenue SKUs</h3>
        <span class="insight-pill">Top 10</span>
      </div>
      <div id="topRevenueList" class="insight-list"></div>
    </div>

    <div class="insight-card">
      <div class="insight-card-head">
        <h3>Low Stock Alerts</h3>
        <span class="insight-pill warn">Need attention</span>
      </div>
      <div id="lowStockList" class="insight-list"></div>
    </div>

    <div class="insight-card">
      <div class="insight-card-head">
        <h3>Category Mix</h3>
        <span class="insight-pill">By revenue</span>
      </div>
      <div id="categoryList" class="insight-list"></div>
    </div>
  </div>

  <div class="insights-grid" style="margin-top:18px">
    <div class="insight-card">
      <div class="insight-card-head">
        <h3>Inventory Health</h3>
        <span class="insight-pill ok">Quick view</span>
      </div>
      <div id="healthList" class="insight-list"></div>
    </div>

    <div class="insight-card">
      <div class="insight-card-head">
        <h3>Top Customers</h3>
        <span class="insight-pill">By final qty</span>
      </div>
      <div id="customerList" class="insight-list"></div>
    </div>

    <div class="insight-card">
      <div class="insight-card-head">
        <h3>Top Returns</h3>
        <span class="insight-pill warn">Return qty &amp; amount</span>
      </div>
      <div id="returnsList" class="insight-list"></div>
    </div>

    <div class="insight-card">
      <div class="insight-card-head">
        <h3>Filtered Summary</h3>
        <span class="insight-pill ok">Live</span>
      </div>
      <div class="insight-list" id="insightMiniSummary"></div>
    </div>
  </div>
</div>

</div>

<footer><div class="fb">Cosa Nostraa</div><div class="fd">© 2026 • Developed by Team Cosa Nostraa</div></footer>

</div><script>
let _masterSkuMap = {};   // SKU.toUpperCase() → item (fast combo lookup)
let master = [], allCusts = [], allTypes = [], allPlatings = [],
    allSkus = [], allFYs = [], allTaxons = [];
let currentFY = "", previousFY = "", todayISO = "",
    yesterdayISO = "", currentMonthKey = "";
let grandNetRevenue = 0, grandFinalQty = 0;
let marketplaceData = null;
let periodKpis = {total:0, yesterday:0, this_month:0, this_fy:0, prev_fy:0};
let imgB64 = null;

let selectedSkuSet = new Set();
let roRemarks = {};   // sku -> remark text (admin/employee dono likh sakte hain)
function setRoRemark(sku, val){ roRemarks[sku] = val; }
let roRemarks2 = {};  // sku -> second remark text
function setRoRemark2(sku, val){ roRemarks2[sku] = val; }
let RO_VIEW = 'pivot';   // 'pivot' (SKU-wise, default) | 'txns' (transaction rows)
function setRoView(v){
  RO_VIEW = v;
  const p = document.getElementById('roViewPivot'), t = document.getElementById('roViewTxns');
  if (p) p.classList.toggle('active', v === 'pivot');
  if (t) t.classList.toggle('active', v === 'txns');
  applyRO();
}
let pastedSkuSet = null;
let roFiltered = [];
let roTxns = null;
let currentSdSku = null;
let currentTab = "home";
let lastTab = "home";
let insightRows = [];
let roSortKey = "total_net_revenue";
let roSortDir = -1;

function fmt(n){ return '₹' + Math.round(n || 0).toLocaleString('en-IN'); }
function safeText(v){ return (v === null || v === undefined) ? '' : String(v); }

function roThumb(url){
  return (url && String(url).trim() && String(url).toLowerCase() !== 'nan')
    ? `<img class="sku-thumb" src="${url}" loading="lazy" decoding="async" onerror="this.style.display='none'">`
    : `<div class="sku-thumb" style="display:flex;align-items:center;justify-content:center;color:#cbd5e1;font-size:18px">💎</div>`;
}

function getSelectedTypes(id){
  const containerId = id === 'fType' ? 'fTypeChecks' : id === 'rType' ? 'rTypeChecks' : id === 'iType' ? 'iTypeChecks' : id;
  const box = document.getElementById(containerId);
  if (!box) return [];
  return Array.from(box.querySelectorAll('input[type=checkbox]:checked')).map(c => c.value);
}

/* ── Debounce: typing par har keystroke pe heavy re-filter (10k+ SKU) nahi
   chalega — user ke rukne ke ~280ms baad ek hi baar chalega. Isse customer
   name / search box me type karte waqt hang nahi hoga. ── */
function _debounce(fn, ms){
  let t = null;
  return function(){ clearTimeout(t); t = setTimeout(fn, ms); };
}
const applyRO_d = _debounce(function(){ try{ applyRO(); }catch(e){ console.error(e); } }, 280);
const applyF_d  = _debounce(function(){ try{ applyF(); }catch(e){ console.error(e); } }, 280);
const applyInsights_d = _debounce(function(){ try{ applyInsights(); }catch(e){ console.error(e); } }, 280);
window.applyRO_d = applyRO_d; window.applyF_d = applyF_d; window.applyInsights_d = applyInsights_d;


function renderTypeChecks(){
  ['fTypeChecks','rTypeChecks','iTypeChecks'].forEach(cid => {
    const box = document.getElementById(cid);
    if (!box) return;
    const onChange = cid === 'fTypeChecks' ? 'applyF()' : cid === 'rTypeChecks' ? 'applyRO()' : 'applyInsights()';
    box.innerHTML = (allTypes || []).map(t => {
      const safe = String(t).replace(/"/g, '&quot;');
      return `<label class="type-opt"><input type="checkbox" value="${safe}" onchange="${onChange}"><span>${t}</span></label>`;
    }).join('') || '<span class="small-note">No types</span>';
  });
}

let allPacks = [];
function getSelectedPacks(){
  const box = document.getElementById('rPackChecks');
  if (!box) return [];
  return Array.from(box.querySelectorAll('input[type=checkbox]:checked')).map(c => c.value);
}
function renderPackChecks(){
  const box = document.getElementById('rPackChecks');
  if (!box) return;
  // Pack Details ki unique values inventory (master) se nikalo.
  const set = new Set();
  (master || []).forEach(i => { const p = (i.pack_details || '').trim(); if (p) set.add(p); });
  allPacks = Array.from(set).sort((a,b) => a.localeCompare(b));
  box.innerHTML = allPacks.length ? allPacks.map(p => {
    const safe = String(p).replace(/"/g, '&quot;');
    return `<label class="type-opt"><input type="checkbox" value="${safe}" onchange="applyRO()"><span>${p}</span></label>`;
  }).join('') : '<span class="small-note">No pack details</span>';
}

function sCls(v){ return v === 0 ? 'z' : v < 5 ? 'l' : 'g'; }

function toggleDbg(){
  const b = document.getElementById('dbgbox');
  if (!b) return;
  b.style.display = (b.style.display === 'none' || !b.style.display) ? 'block' : 'none';
  if (b.style.display === 'block') {
    fetch('/api/debug', {headers:{'ngrok-skip-browser-warning':'true'}})
      .then(r => r.json())
      .then(d => { b.textContent = JSON.stringify(d, null, 2); })
      .catch(e => { b.textContent = 'Debug fetch failed: ' + e.message; });
  }
}

function showTab(t){
  const tabs = ['matrix','repeat','finder','skudetails','marketplaces'];
  tabs.forEach((x,i)=>{
    const el = document.getElementById('v'+x.charAt(0).toUpperCase()+x.slice(1));
    if (el) el.style.display = 'none';
    const btn = document.getElementById('t'+(i+1));
    if (btn) btn.classList.remove('active');
  });
  const showEl = document.getElementById('v'+t.charAt(0).toUpperCase()+t.slice(1));
  if (showEl) showEl.style.display = 'block';
  const idx = {'matrix':0,'repeat':1,'finder':2,'skudetails':3}[t];
  const btn = document.getElementById('t'+(idx+1));
  if (btn) btn.classList.add('active');
  if (t === 'repeat') applyRO();
}

function renderSkuChecklist(){
  const box = document.getElementById('skuChecklist');
  if (!box) return;
  const q = (document.getElementById('fSkuSearch')?.value || '').trim().toLowerCase();
  const list = (allSkus || []).filter(s => !q || String(s).toLowerCase().includes(q));
  const limit = q ? 300 : 180;
  const shown = list.slice(0, limit);
  box.innerHTML = shown.map(s => {
    const checked = selectedSkuSet.has(s) ? 'checked' : '';
    return `<label class="sku-opt"><input type="checkbox" ${checked} onchange="toggleSkuSelection('${String(s).replace(/'/g, "\\\\'")}', this.checked)"><span>${s}</span></label>`;
  }).join('') + (list.length > limit ? `<div class="small-note" style="grid-column:1/-1;padding:6px 2px">Showing first ${limit} matches. Refine search to see more.</div>` : '');
  const info = document.getElementById('skuSelInfo');
  if (info) info.textContent = `${selectedSkuSet.size} selected`;
}

function renderRoSkuChecklist(){
  const box = document.getElementById('rSkuChecklist');
  if (!box) return;
  const q = (document.getElementById('rSkuSearch')?.value || '').trim().toLowerCase();
  const list = (allSkus || []).filter(s => !q || String(s).toLowerCase().includes(q));
  const limit = q ? 300 : 180;
  const shown = list.slice(0, limit);
  box.innerHTML = shown.map(s => {
    const checked = selectedSkuSet.has(s) ? 'checked' : '';
    return `<label class="sku-opt"><input type="checkbox" ${checked} onchange="toggleSkuSelection('${String(s).replace(/'/g, "\\\\'")}', this.checked)"><span>${s}</span></label>`;
  }).join('') + (list.length > limit ? `<div class="small-note" style="grid-column:1/-1;padding:6px 2px">Showing first ${limit} matches. Refine search to see more.</div>` : '');
  const info = document.getElementById('rSkuSelInfo');
  if (info) info.textContent = `${selectedSkuSet.size} selected`;
}

function refreshChecklists(){
  if (document.getElementById('skuChecklist')) renderSkuChecklist();
  if (document.getElementById('rSkuChecklist')) renderRoSkuChecklist();
}

function toggleSkuSelection(sku, checked){
  if (checked) selectedSkuSet.add(sku);
  else selectedSkuSet.delete(sku);
  // Re-render NAHI karte (warna table redraw ho ke selection jhilmilata tha).
  // Bas export hint + "select all" box update karo.
  refreshChecklists();
  const allBox = document.getElementById('roSelectAll');
  if (allBox && roFiltered) {
    const skus = roFiltered.map(i => i.sku);
    allBox.checked = skus.length > 0 && skus.every(s => selectedSkuSet.has(s));
  }
  updateExportHint();
}

function roToggleTxn(sku, checked){
  if (checked) selectedSkuSet.add(sku);
  else selectedSkuSet.delete(sku);
  refreshChecklists();
  updateExportHint();
}

function roToggleAllTxns(checked){
  (roTxns || []).forEach(t => {
    if (checked) selectedSkuSet.add(t.sku);
    else selectedSkuSet.delete(t.sku);
  });
  refreshChecklists();
  applyRO();
}

function roToggleAll(checked){
  (roFiltered || []).forEach(item => {
    if (checked) selectedSkuSet.add(item.sku);
    else selectedSkuSet.delete(item.sku);
  });
  refreshChecklists();
  applyRO();
}

function updateExportHint(){
  const el = document.getElementById('roExportHint');
  if (!el) return;
  if (roTxns) { el.textContent = `Exporting: ${roTxns.length} transaction row${roTxns.length === 1 ? '' : 's'}`; return; }
  const ticked = (roFiltered || []).filter(i => selectedSkuSet.has(i.sku)).length;
  el.textContent = ticked > 0
    ? `Exporting: ${ticked} ticked SKU${ticked === 1 ? '' : 's'}`
    : 'Exporting: all filtered rows';
}

function openSkuDetails(sku){
  currentSdSku = sku;
  lastTab = currentTab || 'home';
  renderSkuDetails(sku);
  showTab('skudetails');
}

function toggleNavMenu(force){
  const menu = document.getElementById('navMenu');
  if (!menu) return;
  const show = typeof force === 'boolean' ? force : menu.style.display !== 'block';
  menu.style.display = show ? 'block' : 'none';
}

function goBackFromDetails(){
  showTab(lastTab || 'home');
}

function renderSkuDetails(sku){
  const item = (master || []).find(i => i.sku === sku);
  const emptyEl = document.getElementById('sdEmpty');
  const contentEl = document.getElementById('sdContent');
  if (!item) {
    if (emptyEl) { emptyEl.style.display = 'block'; emptyEl.textContent = `No data found for ${sku}.`; }
    if (contentEl) contentEl.style.display = 'none';
    return;
  }
  if (emptyEl) emptyEl.style.display = 'none';
  if (contentEl) contentEl.style.display = 'block';

  const imgEl = document.getElementById('sdImg');
  if (imgEl) {
    imgEl.innerHTML = (item.image_url && String(item.image_url).toLowerCase() !== 'nan' && item.image_url !== '')
      ? `<img src="${item.image_url}" loading="lazy" decoding="async" onerror="this.outerHTML='<div class=&quot;img-ph&quot;>💎</div>'">`
      : `<div class="img-ph">💎</div>`;
  }
  const setT = (id,v) => { const el=document.getElementById(id); if (el) el.textContent = v; };
  setT('sdSku', item.sku);
  const metaEl = document.getElementById('sdMeta');
  if (metaEl) metaEl.innerHTML =
    `<span>Category: <b>${safeText(item.taxon)}</b></span>` +
    `<span>Plating: <b>${safeText(item.plating)}</b></span>` +
    (item.dimensions ? `<span>Dimensions: <b>${safeText(item.dimensions)}</b></span>` : '') +
    (item.combo_skus ? `<span>Combo SKUs: <b>${safeText(item.combo_skus)}</b></span>` : '') +
    `<span>Status: <b>${safeText(item.status)}</b></span>` +
    `<span>Inv Stock: <b>${item.inv_stock || 0}</b></span>` +
    `<span>Inv WIP: <b>${item.inv_wip || 0}</b></span>` +
    `<span>MRP: <b>₹${Math.round(item.mrp || 0).toLocaleString('en-IN')}</b></span>`;

  const ents = (item.sales_entries || []);

  const byType = {};
  ents.forEach(e => {
    const t = e.type || 'Regular';
    if (!byType[t]) byType[t] = {orders:0, qty:0, rev:0};
    byType[t].orders += 1;
    byType[t].qty += parseFloat(e.qty) || 0;
    byType[t].rev += parseFloat(e.rev) || 0;
  });
  const types = Object.keys(byType).sort();
  const bd = document.getElementById('sdTypeBreakdown');
  if (bd) {
    bd.innerHTML = types.length ? types.map(t => `
      <div class="td-card">
        <div class="td-type">${t}</div>
        <div class="td-row"><span>Orders</span><b>${byType[t].orders}</b></div>
        <div class="td-row"><span>Qty</span><b>${byType[t].qty}</b></div>
        <div class="td-row"><span>Net Rev</span><b class="green">${fmt(byType[t].rev)}</b></div>
      </div>`).join('') : '<span class="small-note">No sales yet</span>';
  }
  const tc = document.getElementById('sdTypeChecks');
  if (tc) {
    tc.innerHTML = types.length ? types.map(t => {
      const safe = String(t).replace(/"/g,'&quot;');
      return `<label class="type-opt"><input type="checkbox" value="${safe}" onchange="renderSdTable()"><span>${t}</span></label>`;
    }).join('') : '<span class="small-note">No types</span>';
  }

  renderSdTable();
}

function renderSdTable(){
  const item = (master || []).find(i => i.sku === currentSdSku);
  if (!item) return;
  const picked = Array.from(document.querySelectorAll('#sdTypeChecks input:checked')).map(c => c.value);
  let ents = (item.sales_entries || []).slice();
  if (picked.length) ents = ents.filter(e => picked.includes(e.type || 'Regular'));
  ents.sort((a,b) => (a.date < b.date ? 1 : a.date > b.date ? -1 : 0));

  const totalQty = ents.reduce((s,e) => s + (parseFloat(e.qty) || 0), 0);
  const totalRev = ents.reduce((s,e) => s + (parseFloat(e.rev) || 0), 0);
  const setT = (id,v) => { const el=document.getElementById(id); if (el) el.textContent = v; };
  setT('sdOrders', ents.length);
  setT('sdQty', totalQty);
  setT('sdRev', fmt(totalRev));
  setT('sdCust', new Set(ents.map(e => e.cust)).size);

  const body = document.getElementById('sdBody');
  if (body) {
    body.innerHTML = ents.length ? ents.map(e => `<tr>
      <td class="gold">${e.date === 'N/A' ? '—' : e.date}</td>
      <td>${safeText(e.cust)}</td>
      <td>${safeText(e.type)}</td>
      <td class="gold">${parseFloat(e.qty) || 0}</td>
      ${LOGIN_ROLE==='employee' ? '' : `<td class="green">${fmt(parseFloat(e.rev) || 0)}</td>`}
    </tr>`).join('')
    : '<tr><td colspan="5" class="tno-data" style="padding:30px">No transactions for the selected type(s).</td></tr>';
  }
}

function exportSD(fmtType){
  const item = (master || []).find(i => i.sku === currentSdSku);
  if (!item) { alert('Open a SKU first.'); return; }
  const picked = Array.from(document.querySelectorAll('#sdTypeChecks input:checked')).map(c => c.value);
  let ents = (item.sales_entries || []).slice();
  if (picked.length) ents = ents.filter(e => picked.includes(e.type || 'Regular'));
  ents.sort((a,b) => (a.date < b.date ? 1 : a.date > b.date ? -1 : 0));
  if (!ents.length) { alert('No transactions to export.'); return; }
  const emp0 = LOGIN_ROLE === 'employee';
  const headers = ['Dispatch Date','SKU','Product Dimensions','Customer','Type','Final Qty','MRP', ...(emp0 ? [] : ['Selling Price','Net Revenue']), 'Image Link'];
  const data = ents.map(e => ({
    'Dispatch Date': e.date === 'N/A' ? '' : e.date,
    SKU: item.sku,
    'Product Dimensions': item.dimensions || '',
    Customer: e.cust,
    Type: e.type,
    'Final Qty': parseFloat(e.qty) || 0,
    'MRP': parseFloat(item.mrp) || 0,
    ...(emp0 ? {} : {'Selling Price': parseFloat(e.sp) || 0, 'Net Revenue': parseFloat(e.rev) || 0}),
    'Image Link': item.image_url || '',
  }));
  downloadTable(headers, data, `sku_${String(item.sku).replace(/[^A-Za-z0-9_-]/g,'')}`, fmtType);
}

// ── Daily STR (sell-through) injector ───────────────────────────────────────
// Har export mein ek din ka sale (units/day) WHOLE NUMBER, round off karke aata
// hai. Formula: Daily STR = ROUND(window sale / days, 0).
//   • Daily STR (7D)  = ROUND(7D Sale  / 7,  0)
//   • Daily STR (15D) = ROUND(15D Sale / 15, 0)
//   • Daily STR (30D) = ROUND(30D Sale / 30, 0)
//   • Avg Daily Sale  = ROUND(average of the three, 0)
// Agar table mein 7D/15D/30D Sale columns hain to wahi use karta hai; warna SKU
// ke through `master` se window-sales lookup karke nikalta hai. Isse RO, SKU
// Details, Insights, AI Studio — sab exports auto-cover ho jaate hain.
function _strLookupFromMaster(){
  const m = {};
  ((typeof master !== 'undefined' && master) || []).forEach(it => {
    if (it && it.sku != null) {
      m[String(it.sku)] = {
        q7:  parseFloat(it.qty_7d)  || 0,
        q15: parseFloat(it.qty_15d) || 0,
        q30: parseFloat(it.qty_1m)  || 0,   // qty_1m = last 30 days
      };
    }
  });
  return m;
}
function _dailySTR(q7, q15, q30){
  const d7  = Math.round((parseFloat(q7)  || 0) / 7);
  const d15 = Math.round((parseFloat(q15) || 0) / 15);
  const d30 = Math.round((parseFloat(q30) || 0) / 30);
  const avg = Math.round((d7 + d15 + d30) / 3);
  return {'Daily STR (7D)': d7, 'Daily STR (15D)': d15, 'Daily STR (30D)': d30, 'Avg Daily Sale': avg};
}
function augmentWithDailySTR(headers, data){
  const STR_COLS = ['Daily STR (7D)', 'Daily STR (15D)', 'Daily STR (30D)', 'Avg Daily Sale'];
  // Normalize array-style rows (e.g. AI Studio) into objects keyed by header.
  let rows = (data || []).map(r => {
    if (Array.isArray(r)) {
      const o = {}; headers.forEach((h, i) => { o[h] = r[i]; }); return o;
    }
    return r;
  });
  // Already augmented? leave as-is.
  if (STR_COLS.every(c => headers.includes(c))) return {headers: headers.slice(), data: rows};

  const hasWin = headers.includes('7D Sale') && headers.includes('15D Sale') && headers.includes('30D Sale');
  const look = hasWin ? null : _strLookupFromMaster();

  let matched = false;
  const outData = rows.map(r => {
    let q7, q15, q30, ok = false;
    if (hasWin) {
      q7 = r['7D Sale']; q15 = r['15D Sale']; q30 = r['30D Sale']; ok = true;
    } else {
      const k = (r['SKU'] != null) ? String(r['SKU']) : null;
      const w = k && look[k];
      if (w) { q7 = w.q7; q15 = w.q15; q30 = w.q30; ok = true; }
    }
    if (!ok) return r;                 // can't compute → row unchanged (blank STR cells)
    matched = true;
    return Object.assign({}, r, _dailySTR(q7, q15, q30));
  });

  if (!matched) return {headers: headers.slice(), data: rows};  // no sale data anywhere

  // Insert STR columns right after the most relevant anchor.
  const newHeaders = headers.slice();
  const anchor = ['Inv WIP', '30D Sale', 'Inv Stock', 'SKU']
                   .map(a => newHeaders.indexOf(a)).find(i => i >= 0);
  if (anchor != null && anchor >= 0) newHeaders.splice(anchor + 1, 0, ...STR_COLS);
  else newHeaders.push(...STR_COLS);
  return {headers: newHeaders, data: outData};
}

function downloadTable(headers, data, baseName, fmtType){
  ({headers, data} = augmentWithDailySTR(headers, data));
  function downloadBlob(content, mime, filename){
    const blob = new Blob([content], {type: mime});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url; a.download = filename; a.click();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  }
  if (fmtType === 'csv') {
    const esc = v => '"' + String(v).replace(/"/g, '""') + '"';
    const csv = [headers.map(esc).join(',')].concat(data.map(r => headers.map(h => esc(r[h] ?? '')).join(','))).join('\n');
    downloadBlob(csv, 'text/csv;charset=utf-8', baseName + '.csv');
  } else {
    const rowsHtml = data.map(r => `<tr>${headers.map(h => `<td>${String(r[h] ?? '').replace(/</g,'&lt;')}</td>`).join('')}</tr>`).join('');
    const html = `<!DOCTYPE html><html><head><meta charset="utf-8"></head><body><table border="1"><tr>${headers.map(h=>`<th>${h}</th>`).join('')}</tr>${rowsHtml}</table></body></html>`;
    downloadBlob(html, 'application/vnd.ms-excel;charset=utf-8', baseName + '.xls');
  }
}

function selectVisibleSkus(visibleOnly){
  const q = (document.getElementById('fSkuSearch')?.value || '').trim().toLowerCase();
  const list = (allSkus || []).filter(s => !q || String(s).toLowerCase().includes(q));
  list.forEach(s => selectedSkuSet.add(s));
  refreshChecklists();
  applyF();
  applyRO();
}

function selectVisibleRoSkus(){
  const q = (document.getElementById('rSkuSearch')?.value || '').trim().toLowerCase();
  const list = (allSkus || []).filter(s => !q || String(s).toLowerCase().includes(q));
  list.forEach(s => selectedSkuSet.add(s));
  refreshChecklists();
  applyF();
  applyRO();
}

function clearSkuSelection(){
  selectedSkuSet.clear();
  refreshChecklists();
  applyF();
  applyRO();
}

function applyPastedSkus(){
  const raw = (document.getElementById('rPasteSkus')?.value || '').trim();
  const info = document.getElementById('rPasteInfo');
  if (!raw) { clearPastedSkus(); return; }
  const tokens = raw.split(/[\s,;|]+/).map(t => t.trim()).filter(Boolean);
  if (!tokens.length) { clearPastedSkus(); return; }

  const exact = new Map(), base = new Map();
  (master || []).forEach(it => {
    exact.set(String(it.sku).toUpperCase(), it.sku);
    const b = String(it.sku).toUpperCase().split('_')[0];
    if (!base.has(b)) base.set(b, it.sku);
  });

  const matched = new Set();
  const notFound = [];
  tokens.forEach(tok => {
    const u = tok.toUpperCase();
    if (exact.has(u)) matched.add(exact.get(u).toUpperCase());
    else if (base.has(u)) matched.add(base.get(u).toUpperCase());
    else if (base.has(u.split('_')[0])) matched.add(base.get(u.split('_')[0]).toUpperCase());
    else notFound.push(tok);
  });

  pastedSkuSet = matched.size ? matched : new Set(['__none__']); 
  if (info) {
    info.textContent = `${matched.size} matched` + (notFound.length ? ` · not found: ${notFound.slice(0,8).join(', ')}${notFound.length>8?'…':''}` : '');
    info.style.color = notFound.length ? '#d97706' : '#15803d';
  }
  applyRO();
}

function clearPastedSkus(){
  pastedSkuSet = null;
  const ta = document.getElementById('rPasteSkus'); if (ta) ta.value = '';
  const info = document.getElementById('rPasteInfo'); if (info) info.textContent = '';
  applyRO();
}

function loadData(force){
  force = force || false;
  if (force) _warmRetries = 0;   // manual sync resets the warming retry counter
  const L = document.getElementById('loader');
  if (L){
    L.style.display = 'block';
    L.innerHTML = '<div class="spin"></div>' + (force ? 'Fetching fresh data…' : 'Syncing databases… please wait');
  startWarmupPoll();
  }
  ['vMatrix','vRepeat','vFinder'].forEach(id => { const el = document.getElementById(id); if (el) el.style.display = 'none'; });

  const ctrl = new AbortController();
  const timeoutMs = 120000;
  const timer = setTimeout(() => ctrl.abort(), timeoutMs);

  fetch('/api/data?force=' + force + '&role=' + encodeURIComponent(LOGIN_ROLE || 'admin'), {headers:{'ngrok-skip-browser-warning':'true'}, signal: ctrl.signal})
    .then(r => { if (r.status === 401) { const g=document.getElementById('loginGate'); if(g) g.style.display='flex'; const a=document.getElementById('appRoot'); if(a) a.style.display='none'; throw new Error('Session expired — please sign in again.'); } return r; })
    .then(r => {
      // 202 = server abhi data warm kar raha hai. Error mat do — thodi der baad
      // khud retry karo (reload-loop ke bina). Loader warmup-status dikhata rahega.
      if (r.status === 202) {
        clearTimeout(timer);
        _warmRetries = (_warmRetries || 0) + 1;
        if (_warmRetries > 60) {   // ~2.5 min: data load nahi hua, stop looping
          if (L) L.innerHTML = 'Server is still preparing the data (large dataset). '
            + 'Please <button class="go-btn" style="width:auto;padding:9px 16px;display:inline-block" onclick="_warmRetries=0;loadData(false)">Retry</button> in a moment.';
          return null;
        }
        if (L) { L.style.display = 'block'; startWarmupPoll(); }
        setTimeout(() => loadData(false), 2500);
        return null;
      }
      if (!r.ok) throw new Error('Server returned HTTP ' + r.status);
      return r.json();
    })
    .then(d => {
      if (d === null) return;   // warming — retry already scheduled
      clearTimeout(timer);
      if (!d.inventory || d.inventory.length === 0) {
        if (L) L.innerHTML = 'No data found. Open <b>Debug</b> (top-left) to see the column mapping / errors.'
          + '<div style="margin-top:14px"><button class="go-btn" style="width:auto;padding:9px 16px" onclick="loadData(true)">Retry</button></div>';
        return;
      }

      master = d.inventory || [];
      _masterSkuMap = {}; master.forEach(it => { if(it&&it.sku) _masterSkuMap[String(it.sku).toUpperCase()] = it; });
      allCusts = d.customers || [];
      allTypes = d.types || [];
      allPlatings = d.platings || [];
      allSkus = d.skus || [];
      allFYs = d.fys || [];
      allTaxons = d.taxons || [];
      currentFY = d.current_fy || '';
      previousFY = d.previous_fy || '';
      todayISO = d.today || '';
      yesterdayISO = d.yesterday || '';
      currentMonthKey = d.current_month || '';
      grandNetRevenue = parseFloat(d.grand_net_revenue) || 0;
      grandFinalQty   = parseFloat(d.grand_final_qty) || 0;
      periodKpis = d.period_kpis || {total:grandNetRevenue, yesterday:0, this_month:0, this_fy:0, prev_fy:0};

      const custOpts = allCusts.map(c => `<option value="${c}"></option>`).join('');
      const c1 = document.getElementById('custList');
      const c2 = document.getElementById('custList2');
      if (c1) c1.innerHTML = custOpts;
      if (c2) c2.innerHTML = custOpts;

      const taxHtml = '<option value="All">All Categories</option>' + allTaxons.map(t => `<option value="${t}">${t}</option>`).join('');
      const platHtml = '<option value="All">All Platings</option>' + allPlatings.map(p => `<option value="${p}">${p}</option>`).join('');
      const fyHtml = '<option value="All FYs">All FYs</option>' + allFYs.map(f => `<option value="${f}">${f}</option>`).join('');

      renderTypeChecks();
      renderPackChecks();
      ['fTaxon','rTaxon','iTaxon'].forEach(id => { const el = document.getElementById(id); if (el) el.innerHTML = taxHtml; });
      const p = document.getElementById('fPlat'); if (p) p.innerHTML = platHtml;
      // Launch Month options — month-wise (Month + Year combined), ascending
      const lm = new Map();
      master.forEach(it => { if (it.launch_key) lm.set(it.launch_key, it.launch_month); });
      const lmHtml = '<option value="All">All Months</option>' +
        Array.from(lm.entries()).sort((a,b) => a[0].localeCompare(b[0]))
          .map(([k,lab]) => `<option value="${k}">${lab}</option>`).join('');
      const lsel = document.getElementById('fLaunch'); if (lsel) lsel.innerHTML = lmHtml;
      const fy = document.getElementById('fFY'); if (fy) fy.innerHTML = fyHtml;

      selectedSkuSet = new Set();
      refreshChecklists();
      // Sab tab ek saath render karne se data-load par hang hota tha. Ab sirf
      // jo tab khula hai usi ka heavy render chalega — wo bhi defer hoke (UI free).
      setTimeout(() => {
        try {
          if (currentTab === 'matrix') applyF();
          else if (currentTab === 'repeat') applyRO();
          else if (currentTab === 'insights') renderInsights();
          renderHome();   // home content hamesha taiyaar rakho
        } catch(e){ console.error(e); }
      }, 0);

      if (L) L.style.display = 'none'; stopWarmupPoll();
      showTab('home');
    })
    .catch(err => {
      clearTimeout(timer);
      const msg = (err && err.name === 'AbortError')
        ? 'Loading timed out (the dataset is large). The server may still be preparing data.'
        : ('Sync failed: ' + (err && err.message ? err.message : err));
      if (L) L.innerHTML = msg
        + '<div style="margin-top:14px"><button class="go-btn" style="width:auto;padding:9px 16px" onclick="loadData(true)">Retry</button></div>';
    });
}

function mkCard(item, rev, conf, slow){
  const img = (item.image_url && String(item.image_url).trim() && String(item.image_url).toLowerCase() !== 'nan')
    ? `<img src="${item.image_url}" loading="lazy" decoding="async" onerror="this.outerHTML='<div class=&quot;img-ph&quot;>💎</div>'">`
    : '<div class="img-ph">💎</div>';
  const confB = conf ? `<div class="badge-conf">${conf}%</div>` : '';
  const statusB = `<div class="badge-status">${safeText(item.status || '')}</div>`;
  const invB = `<div class="badge-inv">INV ${item.total_inv || 0}</div>`;
  const s = {m1:item.qty_1m||0,m3:item.qty_3m||0,m6:item.qty_6m||0,y1:item.qty_1y||0};
  const sn = parseFloat(item.inv_stock) || 0;
  const wn = parseFloat(item.inv_wip) || 0;
  const r = rev !== undefined ? rev : (item.total_net_revenue || 0);

  const revRows = (LOGIN_ROLE === 'employee') ? '' : `
    <div class="row rev-only"><span>Net Revenue</span><span>${fmt(r)}</span></div>
    <div class="row rev-only"><span>Yesterday</span><span>${fmt(item.rev_yesterday || 0)}</span></div>
    <div class="row rev-only"><span>This Month</span><span>${fmt(item.rev_month || 0)}</span></div>
    <div class="row rev-only"><span>This FY</span><span>${fmt(item.rev_fy || 0)}</span></div>
    <div class="row rev-only"><span>Previous FY</span><span>${fmt(item.rev_prev_fy || 0)}</span></div>`;
  return `<div class="card"><div class="img-box">${img}${statusB}${confB}${invB}</div><div class="cb">
    <div class="sku" style="cursor:pointer" onclick="openSkuDetails('${String(item.sku).replace(/'/g, "\\\\'")}')" title="View full SKU details">${item.sku}</div>
    ${revRows}
    <div class="row"><span>Final Qty</span><span>${item.final_qty || 0}</span></div>
    <div class="row"><span>MRP</span><span>₹${Math.round(item.mrp || 0).toLocaleString('en-IN')}</span></div>
    ${item.dimensions ? `<div class="row"><span>Dimensions</span><span>${escHtml(String(item.dimensions))}</span></div>` : ''}
    <div class="row"><span>Inv. Stock</span><span>${item.inv_stock}</span></div>
    <div class="row"><span>Inv (WIP)</span><span>${item.inv_wip}</span></div>
    <div class="row"><span>Blocked Qty</span><span>${item.blocked_qty || 0}</span></div>
    <div class="row"><span>Plating</span><span>${safeText(item.plating || '')}</span></div>
    ${item.dimensions ? `<div class="row"><span>Dimensions</span><span>${safeText(String(item.dimensions))}</span></div>` : ''}
    <div class="row"><span>Category</span><span>${safeText(item.taxon || '')}</span></div>
    <div class="sg">
      <div class="sc"><div class="sl">1M</div><div class="sv ${sCls(s.m1)}">${s.m1}</div></div>
      <div class="sc"><div class="sl">3M</div><div class="sv ${sCls(s.m3)}">${s.m3}</div></div>
      <div class="sc"><div class="sl">6M</div><div class="sv ${sCls(s.m6)}">${s.m6}</div></div>
      <div class="sc"><div class="sl">1Y</div><div class="sv ${sCls(s.y1)}">${s.y1}</div></div>
    </div></div></div>`;
}

function applyF(){
  const txt = (document.getElementById('fSearch')?.value || '').trim().toLowerCase();
  const custQ = (document.getElementById('fCust')?.value || '').trim().toLowerCase();
  const typeSel = getSelectedTypes('fType');
  const taxonQ = document.getElementById('fTaxon')?.value || 'All';
  const statusQ = document.getElementById('fStatus')?.value || 'All';
  const fyQ = document.getElementById('fFY')?.value || 'All FYs';
  const plat = document.getElementById('fPlat')?.value || 'All';
  const mrpRange = document.getElementById('fMrp')?.value || '';
  let mrpLo = 0, mrpHi = Infinity;
  if (mrpRange){
    const [a, b] = mrpRange.split('-');
    mrpLo = parseFloat(a) || 0;
    mrpHi = (b === '' || b === undefined) ? Infinity : parseFloat(b);
  }
  const launchQ = document.getElementById('fLaunch')?.value || 'All';
  const d1 = document.getElementById('fD1')?.value || '';
  const d2 = document.getElementById('fD2')?.value || '';
  const selected = Array.from(selectedSkuSet);
  const typeOk = t => typeSel.length === 0 || typeSel.includes(t);

  let ky=0, km=0, kf=0, kpf=0, kt=0;
  const cards = [];
  const CAP = 350;
  const drill = !!(custQ || d1 || d2);
  const txns = [];

  master.forEach(item => {
    const hay = `${item.sku} ${item.taxon || ''} ${item.plating || ''} ${item.status || ''} ${(item.combo_skus || '')} ${(item.tags || '')}`.toLowerCase();
    if (txt && !hay.includes(txt)) return;
    if (selected.length > 0 && !selected.includes(item.sku)) return;
    if (taxonQ !== 'All' && item.taxon !== taxonQ) return;
    if (statusQ !== 'All' && item.status !== statusQ) return;
    if (fyQ !== 'All FYs' && !(item.sales_entries || []).some(e => e.fy === fyQ)) return;
    if (plat !== 'All' && item.plating !== plat) return;
    if (mrpRange){
      const _m = parseFloat(item.mrp) || 0;
      if (_m < mrpLo || _m >= mrpHi) return;
    }
    if (launchQ !== 'All' && item.launch_key !== launchQ) return;
    if (typeSel.length > 0 && !(item.sales_entries || []).some(e => typeOk(e.type))) return;
    if (custQ && !(item.sales_entries || []).some(e => e.cust.toLowerCase().includes(custQ))) return;

    const fe = (item.sales_entries || []).filter(e => {
      if (custQ && !e.cust.toLowerCase().includes(custQ)) return false;
      if (!typeOk(e.type)) return false;
      if (fyQ !== 'All FYs' && e.fy !== fyQ) return false;
      if (d1 || d2) {
        if (e.date === 'N/A') return false;
        if (d1 && e.date < d1) return false;
        if (d2 && e.date > d2) return false;
      }
      return true;
    });

    const yRev = fe.filter(e => e.date === yesterdayISO).reduce((s,e) => s + (parseFloat(e.rev) || 0), 0);
    const mRev = fe.filter(e => e.date !== 'N/A' && e.date.startsWith(currentMonthKey)).reduce((s,e) => s + (parseFloat(e.rev) || 0), 0);
    const fRev = fe.filter(e => e.fy === currentFY).reduce((s,e) => s + (parseFloat(e.rev) || 0), 0);
    const pfRev = fe.filter(e => e.fy === previousFY).reduce((s,e) => s + (parseFloat(e.rev) || 0), 0);
    const feRev = fe.reduce((s,e) => s + (parseFloat(e.rev) || 0), 0);

    ky += yRev; km += mRev; kf += fRev; kpf += pfRev;
    const anyEntryFilter = !!(custQ || (d1 || d2) || typeSel.length > 0 || fyQ !== 'All FYs');
    const feQty = fe.reduce((s,e)=>s + (parseFloat(e.qty)||0), 0);
    kt += anyEntryFilter ? feRev : (parseFloat(item.total_net_revenue) || 0);

    if (drill) {
      fe.forEach(e => txns.push({ ...e, sku: item.sku }));
    } else if (cards.length < CAP) {
      cards.push({ mrp: parseFloat(item.mrp) || 0, html: mkCard({
        ...item,
        final_qty: anyEntryFilter ? feQty : item.final_qty,
        customer_count: new Set((fe.length ? fe : item.sales_entries || []).map(e => e.cust)).size,
        rev_yesterday: yRev,
        rev_month: mRev,
        rev_fy: fRev,
        rev_prev_fy: pfRev
      }, anyEntryFilter ? feRev : (parseFloat(item.total_net_revenue) || 0), null, false) });
    }
  });

  const grid = document.getElementById('gMatrix');
  if (grid) {
    if (drill) {
      txns.sort((a,b) => (a.date < b.date ? 1 : a.date > b.date ? -1 : 0));
      if (!txns.length) {
        grid.innerHTML = '<div class="no-data">No transactions match filters</div>';
      } else {
        const invBy = {};
        master.forEach(it => { invBy[it.sku] = {s: it.inv_stock, w: it.inv_wip, b: it.blocked_qty, img: it.image_url}; });
        const rowsHtml = txns.map(t => {
          const skuEsc = String(t.sku).replace(/'/g, "\\\\'");
          const iv = invBy[t.sku] || {s:0, w:0, b:0, img:''};
          const stk = parseInt(iv.s) || 0, wip = parseInt(iv.w) || 0, blk = parseInt(iv.b) || 0;
          return `<tr>
            <td class="gold">${t.date === 'N/A' ? '—' : t.date}</td>
            <td><div class="sku-cell">${roThumb(iv.img)}<button class="sku-link" onclick="openSkuDetails('${skuEsc}')">${t.sku}</button></div></td>
            <td>${safeText(t.cust)}</td>
            <td>${safeText(t.type)}</td>
            <td class="gold">${parseFloat(t.qty) || 0}</td>
            <td class="green">${fmt(parseFloat(t.rev) || 0)}</td>
            <td class="${stk > 10 ? 'red' : stk > 0 ? 'orange' : 'muted'}">${stk}</td>
            <td class="${wip > 10 ? 'orange' : wip > 0 ? 'gold' : 'muted'}">${wip}</td>
            <td class="${blk > 0 ? 'red' : 'muted'}">${blk}</td>
          </tr>`;
        }).join('');
        grid.innerHTML = `<div class="ro-table-wrap" style="grid-column:1/-1">
          <table class="ro"><thead><tr>
            <th>Dispatch Date</th><th>SKU</th><th>Customer</th><th>Type</th><th>Final Qty</th>${LOGIN_ROLE==='employee' ? '' : '<th>Net Revenue</th>'}<th>Inv Stock</th><th>Inv (WIP)</th><th>Blocked Qty</th>
          </tr></thead><tbody>${rowsHtml}</tbody></table></div>`;
      }
    } else {
      // MRP range select hua → low MRP pehle, phir high (ascending).
      let ordered = cards;
      if (mrpRange) ordered = cards.slice().sort((a,b) => a.mrp - b.mrp);
      grid.innerHTML = ordered.map(c => c.html).join('') || '<div class="no-data">No data matches filters</div>';
    }
  }
  const setTxt = (id, val) => { const el=document.getElementById(id); if (el) el.textContent = fmt(val); };

  const noFilter = !(txt || (selected.length>0) || taxonQ!=='All' || statusQ!=='All' ||
                     fyQ!=='All FYs' || plat!=='All' || mrpRange || custQ || d1 || d2 || typeSel.length>0);
  if (noFilter) {
    setTxt('kY', periodKpis.yesterday || 0);
    setTxt('kM', periodKpis.this_month || 0);
    setTxt('kF', periodKpis.this_fy || 0);
    setTxt('kPF', periodKpis.prev_fy || 0);
    setTxt('kT', periodKpis.total || grandNetRevenue);
  } else {
    setTxt('kY', ky); setTxt('kM', km); setTxt('kF', kf); setTxt('kPF', kpf); setTxt('kT', kt);
  }
}

function resetFilters(){
  ['fSearch','fCust','fSkuSearch','fD1','fD2'].forEach(id => { const el=document.getElementById(id); if (el) el.value=''; });
  ['fTaxon','fStatus','fFY','fPlat','fLaunch'].forEach(id => { const el=document.getElementById(id); if (el) el.value = (id === 'fFY') ? 'All FYs' : 'All'; });
  document.querySelectorAll('#fTypeChecks input:checked').forEach(c => c.checked = false);
  const _fm = document.getElementById('fMrp'); if (_fm) _fm.value = '';
  selectedSkuSet.clear();
  refreshChecklists();
  applyF();
  applyRO();
}

function renderSlow(items){
  const g = document.getElementById('gSlow');
  if (!g) return;
  g.innerHTML = (items && items.length) ? items.map(i => mkCard(i, i.total_net_revenue, null, true)).join('') : '<div class="no-data">No SKUs found</div>';
}

function smF(type, btn){
  document.querySelectorAll('.smb').forEach(b => b.classList.remove('active'));
  if (btn) btn.classList.add('active');
  const q = (document.querySelector('.sm-srch input')?.value || '').trim().toLowerCase();
  let d = master.filter(i => i.status === 'Slow Movers' || i.status === 'Good Running' || i.status === 'New Launch');
  if (type === 'zero') d = d.filter(i => (i.qty_6m || 0) === 0);
  if (type === 'high') d = d.filter(i => (i.total_inv || 0) >= 20);
  if (type === 'wip') d = d.filter(i => (parseFloat(i.inv_wip) || 0) >= 10);
  if (q) d = d.filter(i => i.sku.toLowerCase().includes(q));
  renderSlow(d);
}

function smSrch(q){
  smF('all', document.querySelector('.smb.active'));
}

function applyRO(){
  const txt = (document.getElementById('rSearch')?.value || '').trim().toLowerCase();
  const typeSel = getSelectedTypes('rType');
  const taxQ = document.getElementById('rTaxon')?.value || 'All';
  const custQ = (document.getElementById('rCust')?.value || '').trim().toLowerCase();
  const d1 = document.getElementById('rD1')?.value || '';
  const d2 = document.getElementById('rD2')?.value || '';
  const ticked = Array.from(selectedSkuSet);
  const packSel = getSelectedPacks();
  const typeOk = t => typeSel.length === 0 || typeSel.includes(t);

  const drill = !!(custQ || d1 || d2);

  const entOk = e => {
    if (!typeOk(e.type)) return false;
    if (custQ && !String(e.cust).toLowerCase().includes(custQ)) return false;
    if (d1 || d2) {
      if (e.date === 'N/A') return false;
      if (d1 && e.date < d1) return false;
      if (d2 && e.date > d2) return false;
    }
    return true;
  };

  const skuOk = item => {
    if (pastedSkuSet) return pastedSkuSet.has(String(item.sku).toUpperCase());
    if (txt && !item.sku.toLowerCase().includes(txt)) return false;
    if (taxQ !== 'All' && item.taxon !== taxQ) return false;
    if (packSel.length > 0 && !packSel.includes((item.pack_details || '').trim())) return false;
    // Hide SKUs where Stone Details/Remarks (combo_skus) contains the word "customer"
    if ((item.combo_skus || '').toLowerCase().includes('customer')) return false;
    // NOTE: ticked SKUs ko yahan filter NAHI karte — select karne par baaki
    // rows bhi dikhte rehte hain. Ticked sirf export ke liye use hote hain.
    return true;
  };

  let filtered = master.filter(item => {
    if (!skuOk(item)) return false;
    const ents = item.sales_entries || [];
    if (typeSel.length > 0 && !ents.some(e => typeOk(e.type))) return false;
    if (custQ && !ents.some(e => String(e.cust).toLowerCase().includes(custQ))) return false;
    if (d1 || d2) { if (!ents.some(entOk)) return false; }
    return true;
  });

  filtered = filtered.map(item => {
    const fe = (item.sales_entries || []).filter(entOk);
    const totalRev = fe.reduce((s,e) => s + (parseFloat(e.rev) || 0), 0);
    const totalQty = fe.reduce((s,e) => s + (parseFloat(e.qty) || 0), 0);
    return {
      ...item,
      _fe: fe,
      _fRev: totalRev,
      _fQty: totalQty,
      _customer_count: new Set(fe.map(e=>e.cust)).size
    };
  });

  filtered.sort((a,b) => {
    if (roSortKey === 'sku') {
      const sa = String(a.sku || '').toUpperCase();
      const sb = String(b.sku || '').toUpperCase();
      return roSortDir * (sa < sb ? 1 : sa > sb ? -1 : 0);
    }
    const fb = drill ? '_fRev' : 'total_net_revenue';
    const va = Number(a[roSortKey] ?? a[fb] ?? 0);
    const vb = Number(b[roSortKey] ?? b[fb] ?? 0);
    return roSortDir * (vb - va);
  });

  roFiltered = filtered;

  const roNoFilter = !(txt || typeSel.length>0 || taxQ!=='All' || custQ || d1 || d2 || pastedSkuSet || packSel.length>0);
  const qtySum = roNoFilter
    ? grandFinalQty
    : filtered.reduce((s,i) => s + (Number(i._fQty ?? i.final_qty ?? 0) || 0), 0);

  // Channel-aware WIP: if exactly one channel selected, show its specific WIP column
  const singleType = typeSel.length === 1 ? typeSel[0].toLowerCase() : null;
  const wipSum = filtered.reduce((s,i) => {
    if (singleType && singleType.includes('website')) return s + (parseInt(i.inv_wip_website) || 0);
    if (singleType && (singleType.includes('sor') || singleType.includes('s.o.r'))) return s + (parseInt(i.inv_wip_sor) || 0);
    if (singleType && (singleType.includes('purchase') || singleType.includes('designer') || singleType.includes('customer'))) return s + (parseInt(i.inv_wip_designer) || 0);
    return s + (parseInt(i.inv_wip) || 0);
  }, 0);

  // Channel-aware 7d/15d/30d qty: if type filter active, sum only matching entries
  let wip7d = 0, wip15d = 0, wip30d = 0;
  if (!roNoFilter && typeSel.length > 0) {
    filtered.forEach(item => {
      const fe = (item._fe && item._fe.length) ? item._fe : (item.sales_entries || []).filter(e => typeSel.includes(e.type));
      // fe is already filtered by entOk (which includes type filter)
      const s7 = todayISO ? (new Date(todayISO) - 7*86400000) : 0;
      const s15 = todayISO ? (new Date(todayISO) - 15*86400000) : 0;
      const s30 = todayISO ? (new Date(todayISO) - 30*86400000) : 0;
      const iso7  = s7  ? new Date(s7).toISOString().slice(0,10)  : '';
      const iso15 = s15 ? new Date(s15).toISOString().slice(0,10) : '';
      const iso30 = s30 ? new Date(s30).toISOString().slice(0,10) : '';
      fe.forEach(e => {
        if (e.date === 'N/A') return;
        const q = parseFloat(e.qty) || 0;
        if (iso7  && e.date >= iso7)  wip7d  += q;
        if (iso15 && e.date >= iso15) wip15d += q;
        if (iso30 && e.date >= iso30) wip30d += q;
      });
    });
  } else {
    wip7d  = filtered.reduce((s,i) => s + (parseInt(i.qty_7d)  || 0), 0);
    wip15d = filtered.reduce((s,i) => s + (parseInt(i.qty_15d) || 0), 0);
    wip30d = filtered.reduce((s,i) => s + (parseInt(i.qty_1m)  || 0), 0);
  }

  const countEl = document.getElementById('rCount');
  const qtyEl = document.getElementById('rQty');
  const fcEl = document.getElementById('rFc');
  const wipEl = document.getElementById('rWip');
  const qty7El = document.getElementById('rQty7d');
  const qty15El = document.getElementById('rQty15d');
  const qty30El = document.getElementById('rQty30d');
  if (countEl) countEl.textContent = filtered.length;
  if (qtyEl) qtyEl.textContent = Math.round(qtySum).toLocaleString('en-IN');
  if (fcEl) fcEl.textContent = filtered.length ? Math.round(filtered.reduce((s,i) => s + (i.forecast_30d || 0), 0) / filtered.length) : 0;
  if (wipEl) wipEl.textContent = Math.round(wipSum).toLocaleString('en-IN');
  if (qty7El)  qty7El.textContent  = Math.round(wip7d).toLocaleString('en-IN');
  if (qty15El) qty15El.textContent = Math.round(wip15d).toLocaleString('en-IN');
  if (qty30El) qty30El.textContent = Math.round(wip30d).toLocaleString('en-IN');

  const thead = document.querySelector('#roTable thead tr');
  const tbody = document.getElementById('roBody');
  const empty = document.getElementById('roEmpty');

  const vt = document.getElementById('roViewToggle');
  if (vt) vt.style.display = drill ? 'flex' : 'none';
  const colFiltersBar = document.getElementById('roColFilters');

  if (drill && RO_VIEW === 'txns') {
    if (colFiltersBar) colFiltersBar.style.display = 'none';
    const txns = [];
    filtered.forEach(item => (item._fe || []).forEach(e => txns.push({
      ...e, sku: item.sku, inv_stock: item.inv_stock, inv_wip: item.inv_wip,
      image_url: item.image_url, dimensions: item.dimensions || ''
    })));
    txns.sort((a,b) => (a.date < b.date ? 1 : a.date > b.date ? -1 : 0));
    roTxns = txns;

    if (thead) thead.innerHTML = `
      <th style="width:46px;text-align:center"><input type="checkbox" id="roSelectAllTxn" onclick="roToggleAllTxns(this.checked)" title="Select all"></th>
      <th>Dispatch Date</th>
      <th>SKU</th>
      <th>Dimensions</th>
      <th>Customer</th>
      <th>Type</th>
      <th>Final Qty</th>
      <th>Inv Stock</th>
      <th>Inv (WIP)</th>
      <th style="min-width:160px">Remark</th>`;

    if (!txns.length) {
      if (tbody) tbody.innerHTML = '';
      if (empty) empty.style.display = 'block';
      updateExportHint();
      return;
    }
    if (empty) empty.style.display = 'none';

    const TX_CAP = 400;
    const txShown = txns.slice(0, TX_CAP);
    tbody.innerHTML = txShown.map(t => {
      const skuEsc = String(t.sku).replace(/'/g, "\\\\'");
      const stk = parseInt(t.inv_stock) || 0;
      const wip = parseInt(t.inv_wip) || 0;
      const ck = selectedSkuSet.has(t.sku) ? 'checked' : '';
      return `<tr>
        <td style="text-align:center"><input type="checkbox" ${ck} onchange="roToggleTxn('${skuEsc}', this.checked)"></td>
        <td class="gold">${t.date === 'N/A' ? '—' : t.date}</td>
        <td><div class="sku-cell">${roThumb(t.image_url)}<button class="sku-link" onclick="openSkuDetails('${skuEsc}')">${t.sku}</button></div></td>
        <td>${safeText(t.dimensions || '—')}</td>
        <td>${safeText(t.cust)}</td>
        <td>${safeText(t.type)}</td>
        <td class="gold">${parseFloat(t.qty) || 0}</td>
        <td class="${stk > 10 ? 'red' : stk > 0 ? 'orange' : 'muted'}">${stk}</td>
        <td class="${wip > 10 ? 'orange' : wip > 0 ? 'gold' : 'muted'}">${wip}</td>
        <td><input type="text" class="ro-remark" value="${(roRemarks[t.sku]||'').replace(/"/g,'&quot;')}" placeholder="Type remark…" oninput="setRoRemark('${skuEsc}', this.value)"></td>
      </tr>`;
    }).join('') + (txns.length > TX_CAP
      ? `<tr><td colspan="10" style="text-align:center;padding:12px;color:#8c7a42;font-weight:700">Showing first ${TX_CAP} of ${txns.length.toLocaleString('en-IN')} transactions — narrow with filters. (Export includes all.)</td></tr>`
      : '');
    updateExportHint();
    return;
  }

  roTxns = null;
  if (colFiltersBar) colFiltersBar.style.display = 'flex';
  if (thead) thead.innerHTML = `
    <th style="width:46px;text-align:center"><input type="checkbox" id="roSelectAll" onclick="roToggleAll(this.checked)" title="Select all"></th>
    <th class="sort-arrow" onclick="sortRO('sku',this)">SKU</th>
    <th class="sort-arrow" onclick="sortRO('qty_7d',this)">7D Sale</th>
    <th class="sort-arrow" onclick="sortRO('qty_15d',this)">15D Sale</th>
    <th class="sort-arrow" onclick="sortRO('qty_1m',this)">30D Sale</th>
    <th class="sort-arrow" onclick="sortRO('final_qty',this)">Sold Qty</th>
    <th class="sort-arrow" onclick="sortRO('inv_stock',this)">Inv Stock</th>
    <th class="sort-arrow" onclick="sortRO('inv_wip',this)">Inv WIP</th>
    <th class="sort-arrow" onclick="sortRO('blocked_qty',this)" title="Blocked Qty (column U)">Blocked Qty</th>
    <th class="sort-arrow" onclick="sortRO('forecast_60d',this)" title="Expected units to sell in the next 60 days. Based on recent sales velocity: last 60 days weighted 70%, last 180 days 30%, plus a small trend adjustment.">Forecast 60D</th>
    <th class="sort-arrow" onclick="sortRO('reorder_qty',this)" title="Next 60 days expected demand minus current stock + WIP">Reorder Qty</th>
    <th>Remark</th>
    <th>Remark 2</th>`;

  if (!filtered.length) {
    if (tbody) tbody.innerHTML = '';
    if (empty) empty.style.display = 'block';
    updateExportHint();
    return;
  }
  if (empty) empty.style.display = 'none';

  // PERF: 10,000+ rows ek saath render karne se page "load" leta tha (freeze).
  // Sirf pehle 300 dikhao (counts/export poori list par hi chalti hain).
  const RO_CAP = 300;
  const roShown = filtered.slice(0, RO_CAP);
  tbody.innerHTML = roShown.map(item => {
    const img = (item.image_url && item.image_url !== '' && String(item.image_url).toLowerCase() !== 'nan')
      ? `<img class="sku-thumb ro-thumb-lg" src="${item.image_url}" loading="lazy" decoding="async" onerror="this.style.display='none'">`
      : `<div class="sku-thumb ro-thumb-lg" style="display:flex;align-items:center;justify-content:center;color:#cbd5e1;font-size:34px">💎</div>`;
    const stk = parseInt(item.inv_stock) || 0;
    // Channel-aware WIP per row
    let wip;
    if (singleType && singleType.includes('website')) wip = parseInt(item.inv_wip_website) || 0;
    else if (singleType && (singleType.includes('sor') || singleType.includes('s.o.r'))) wip = parseInt(item.inv_wip_sor) || 0;
    else if (singleType && (singleType.includes('purchase') || singleType.includes('designer') || singleType.includes('customer'))) wip = parseInt(item.inv_wip_designer) || 0;
    else wip = parseInt(item.inv_wip) || 0;
    // Channel-aware sale qty per row
    let q7, q15, q30;
    if (!roNoFilter && typeSel.length > 0) {
      const fe = item._fe || [];
      const now = todayISO || new Date().toISOString().slice(0,10);
      const d7  = new Date(new Date(now) - 7*86400000).toISOString().slice(0,10);
      const d15 = new Date(new Date(now) - 15*86400000).toISOString().slice(0,10);
      const d30 = new Date(new Date(now) - 30*86400000).toISOString().slice(0,10);
      q7  = fe.filter(e=>e.date!=='N/A'&&e.date>=d7).reduce((s,e)=>s+(parseFloat(e.qty)||0),0);
      q15 = fe.filter(e=>e.date!=='N/A'&&e.date>=d15).reduce((s,e)=>s+(parseFloat(e.qty)||0),0);
      q30 = fe.filter(e=>e.date!=='N/A'&&e.date>=d30).reduce((s,e)=>s+(parseFloat(e.qty)||0),0);
    } else {
      q7  = item.qty_7d  || 0;
      q15 = item.qty_15d || 0;
      q30 = item.qty_1m  || 0;
    }
    const qty = roNoFilter ? (item.final_qty || 0) : (item._fQty ?? item.final_qty ?? 0);
    const checked = selectedSkuSet.has(item.sku) ? 'checked' : '';
    const skuEsc = String(item.sku).replace(/'/g, "\\\\'");
    // Combo SKU ki WIP — Type filter ke hisaab se channel-wise, warna total.
    const comboWip = (c) => {
      if (singleType && singleType.includes('website')) return c.inv_wip_website || 0;
      if (singleType && (singleType.includes('sor') || singleType.includes('s.o.r'))) return c.inv_wip_sor || 0;
      if (singleType && (singleType.includes('purchase') || singleType.includes('designer') || singleType.includes('customer'))) return c.inv_wip_designer || 0;
      return c.inv_wip || 0;
    };
    const wipLabel = singleType ? (singleType.includes('website') ? 'WIP (Website)'
      : (singleType.includes('sor')||singleType.includes('s.o.r')) ? 'WIP (SOR)'
      : (singleType.includes('purchase')||singleType.includes('designer')||singleType.includes('customer')) ? 'WIP (Designer)'
      : 'WIP') : 'WIP';
    // Filter-aware combo details: Type filter ke hisaab se individual SKU sales
    const comboHtml = _renderComboDetails(item.combo_details, comboWip, wipLabel, typeSel);
    return `<tr>
      <td style="text-align:center"><input type="checkbox" class="ro-tick" ${checked} onclick="toggleSkuSelection('${skuEsc}', this.checked)"></td>
      <td><div class="sku-cell">${img}
        <span style="display:flex;flex-direction:column;gap:6px;align-items:flex-start">
          <button class="sku-link" onclick="openSkuDetails('${skuEsc}')">${item.sku}</button>
          <button class="details-btn" onclick="openSkuDetails('${skuEsc}')">Details</button>
          ${comboHtml}
        </span></div></td>
      <td class="${q7 > 0 ? 'green' : 'muted'}">${Math.round(q7)}</td>
      <td class="${q15 > 0 ? 'green' : 'muted'}">${Math.round(q15)}</td>
      <td class="${q30 > 0 ? 'green' : 'muted'}">${Math.round(q30)}</td>
      <td class="gold">${qty}</td>
      <td class="${stk > 10 ? 'red' : stk > 0 ? 'orange' : 'muted'}">${stk}</td>
      <td class="${wip > 10 ? 'orange' : wip > 0 ? 'gold' : 'muted'}">${wip}</td>
      <td class="${(item.blocked_qty||0) > 0 ? 'red' : 'muted'}">${item.blocked_qty || 0}</td>
      <td><span class="forecast-pill">${item.forecast_60d || 0}</span></td>
      <td><span class="forecast-pill" style="background:#fff4e0;color:#b45309;border-color:#f3d9a8">${item.reorder_qty || 0}</span></td>
      <td><input type="text" class="ro-remark" value="${(roRemarks[item.sku]||'').replace(/"/g,'&quot;')}" placeholder="Type remark…" oninput="setRoRemark('${skuEsc}', this.value)" onclick="event.stopPropagation()"></td>
      <td><input type="text" class="ro-remark" value="${(roRemarks2[item.sku]||'').replace(/"/g,'&quot;')}" placeholder="Type remark…" oninput="setRoRemark2('${skuEsc}', this.value)" onclick="event.stopPropagation()"></td>
    </tr>`;
  }).join('') + (filtered.length > RO_CAP
    ? `<tr><td colspan="13" style="text-align:center;padding:12px;color:#8c7a42;font-weight:700">Showing first ${RO_CAP} of ${filtered.length.toLocaleString('en-IN')} — use filters/search to narrow. (Export includes all ${filtered.length.toLocaleString('en-IN')}.)</td></tr>`
    : '');

  const allBox = document.getElementById('roSelectAll');
  if (allBox) {
    const skus = roShown.map(i => i.sku);
    allBox.checked = skus.length > 0 && skus.every(s => selectedSkuSet.has(s));
  }
  updateExportHint();
}

function sortRO(key, th){
  if (roSortKey === key) roSortDir *= -1;
  else { roSortKey = key; roSortDir = -1; }
  document.querySelectorAll('.sort-arrow').forEach(e => e.classList.remove('asc','desc'));
  if (th) th.classList.add(roSortDir === -1 ? 'desc' : 'asc');
  applyRO();
}

/* ── Google Sheets-style column filters (post-render row visibility) ── */
let _cfActive = false;
function _qVal(val, num){
  if (!val) return true;
  if (val === '0')   return num === 0;
  if (val === 'gt0') return num > 0;
  if (val === 'gt5') return num > 5;
  if (val === 'gt10') return num > 10;
  if (val === 'gt50') return num > 50;
  if (val === 'gt100') return num > 100;
  return true;
}
function applyColFilters(){
  const cfSku    = (document.getElementById('cfSku')?.value    || '').trim().toLowerCase();
  const cfQ7     = document.getElementById('cfQty7d')?.value   || '';
  const cfQ15    = document.getElementById('cfQty15d')?.value  || '';
  const cfQ30    = document.getElementById('cfQty30d')?.value  || '';
  const cfSold   = document.getElementById('cfSoldQty')?.value || '';
  const cfStk    = document.getElementById('cfInvStock')?.value|| '';
  const cfWip    = document.getElementById('cfInvWip')?.value  || '';
  const cfFc     = document.getElementById('cfForecast')?.value|| '';
  const cfReo    = document.getElementById('cfReorder')?.value || '';
  const cfRmk    = (document.getElementById('cfRemark')?.value || '').trim().toLowerCase();

  _cfActive = !!(cfSku || cfQ7 || cfQ15 || cfQ30 || cfSold || cfStk || cfWip || cfFc || cfReo || cfRmk);

  const tbody = document.getElementById('roBody');
  if (!tbody) return;

  // Re-render with colfilters applied (filter roFiltered in memory then render)
  if (!roFiltered) return;

  let colFiltered = roFiltered;
  if (_cfActive) {
    colFiltered = roFiltered.filter(item => {
      const q7  = parseInt(item.qty_7d)  || 0;
      const q15 = parseInt(item.qty_15d) || 0;
      const q30 = parseInt(item.qty_1m)  || 0;
      const sold = parseInt(item.final_qty) || 0;
      const stk  = parseInt(item.inv_stock) || 0;
      const wip  = parseInt(item.inv_wip)   || 0;
      const fc   = parseInt(item.forecast_60d) || 0;
      const reo  = parseInt(item.reorder_qty)  || 0;
      const rmk  = (roRemarks[item.sku] || '').toLowerCase();
      if (cfSku  && !item.sku.toLowerCase().includes(cfSku))  return false;
      if (!_qVal(cfQ7,   q7))   return false;
      if (!_qVal(cfQ15,  q15))  return false;
      if (!_qVal(cfQ30,  q30))  return false;
      if (!_qVal(cfSold, sold)) return false;
      if (!_qVal(cfStk,  stk))  return false;
      if (!_qVal(cfWip,  wip))  return false;
      if (!_qVal(cfFc,   fc))   return false;
      if (!_qVal(cfReo,  reo))  return false;
      if (cfRmk  && !rmk.includes(cfRmk))  return false;
      return true;
    });
  }

  // Re-render tbody only (not thead / KPIs)
  const RO_CAP = 300;
  const roShown = colFiltered.slice(0, RO_CAP);
  const singleType = (() => {
    const typeSel = getSelectedTypes('rType');
    return typeSel.length === 1 ? typeSel[0].toLowerCase() : null;
  })();
  const roNoFilter = !_cfActive && !(
    (document.getElementById('rSearch')?.value || '').trim() ||
    getSelectedTypes('rType').length > 0 ||
    (document.getElementById('rTaxon')?.value || 'All') !== 'All' ||
    (document.getElementById('rCust')?.value  || '').trim() ||
    (document.getElementById('rD1')?.value    || '') ||
    (document.getElementById('rD2')?.value    || '') ||
    pastedSkuSet || getSelectedPacks().length > 0
  );

  if (!roShown.length) {
    tbody.innerHTML = `<tr><td colspan="11" class="tno-data">No rows match column filters</td></tr>`;
    return;
  }

  const todayStr = todayISO || new Date().toISOString().slice(0,10);
  const d7ms  = new Date(todayStr) - 7*86400000;
  const d15ms = new Date(todayStr) - 15*86400000;
  const d30ms = new Date(todayStr) - 30*86400000;
  const iso7  = new Date(d7ms).toISOString().slice(0,10);
  const iso15 = new Date(d15ms).toISOString().slice(0,10);
  const iso30 = new Date(d30ms).toISOString().slice(0,10);

  tbody.innerHTML = roShown.map(item => {
    const imgTag = (item.image_url && item.image_url !== '' && String(item.image_url).toLowerCase() !== 'nan')
      ? `<img class="sku-thumb ro-thumb-lg" src="${item.image_url}" loading="lazy" decoding="async" onerror="this.style.display='none'">`
      : `<div class="sku-thumb ro-thumb-lg" style="display:flex;align-items:center;justify-content:center;color:#cbd5e1;font-size:34px">💎</div>`;
    const stk = parseInt(item.inv_stock) || 0;
    let wip;
    if (singleType && singleType.includes('website'))  wip = parseInt(item.inv_wip_website) || 0;
    else if (singleType && (singleType.includes('sor') || singleType.includes('s.o.r'))) wip = parseInt(item.inv_wip_sor) || 0;
    else if (singleType && (singleType.includes('purchase') || singleType.includes('designer'))) wip = parseInt(item.inv_wip_designer) || 0;
    else wip = parseInt(item.inv_wip) || 0;
    let q7, q15, q30;
    if (!roNoFilter && getSelectedTypes('rType').length > 0) {
      const fe = item._fe || [];
      q7  = fe.filter(e=>e.date!=='N/A'&&e.date>=iso7).reduce((s,e)=>s+(parseFloat(e.qty)||0),0);
      q15 = fe.filter(e=>e.date!=='N/A'&&e.date>=iso15).reduce((s,e)=>s+(parseFloat(e.qty)||0),0);
      q30 = fe.filter(e=>e.date!=='N/A'&&e.date>=iso30).reduce((s,e)=>s+(parseFloat(e.qty)||0),0);
    } else {
      q7  = item.qty_7d  || 0;
      q15 = item.qty_15d || 0;
      q30 = item.qty_1m  || 0;
    }
    const qty = roNoFilter ? (item.final_qty || 0) : (item._fQty ?? item.final_qty ?? 0);
    const checked = selectedSkuSet.has(item.sku) ? 'checked' : '';
    const skuEsc = String(item.sku).replace(/'/g, "\\\\'");
    // Gift Set / combo SKU — Stone Details ke andar jo SKUs hain unki stock+wip
    const comboWip2 = (c) => {
      if (singleType && singleType.includes('website')) return c.inv_wip_website || 0;
      if (singleType && (singleType.includes('sor') || singleType.includes('s.o.r'))) return c.inv_wip_sor || 0;
      if (singleType && (singleType.includes('purchase') || singleType.includes('designer') || singleType.includes('customer'))) return c.inv_wip_designer || 0;
      return c.inv_wip || 0;
    };
    const wipLabel2 = singleType ? (singleType.includes('website') ? 'WIP (Website)'
      : (singleType.includes('sor')||singleType.includes('s.o.r')) ? 'WIP (SOR)'
      : (singleType.includes('purchase')||singleType.includes('designer')||singleType.includes('customer')) ? 'WIP (Designer)'
      : 'WIP') : 'WIP';
    // Filter-aware combo details (col-filter render): Type filter ke hisaab se individual SKU sales
    const comboHtml = _renderComboDetails(item.combo_details, comboWip2, wipLabel2, getSelectedTypes('rType'));
    return `<tr>
      <td style="text-align:center"><input type="checkbox" class="ro-tick" ${checked} onclick="toggleSkuSelection('${skuEsc}', this.checked)"></td>
      <td><div class="sku-cell">${imgTag}
        <span style="display:flex;flex-direction:column;gap:6px;align-items:flex-start">
          <button class="sku-link" onclick="openSkuDetails('${skuEsc}')">${item.sku}</button>
          <button class="details-btn" onclick="openSkuDetails('${skuEsc}')">Details</button>
          ${comboHtml}
        </span></div></td>
      <td class="${q7 > 0 ? 'green' : 'muted'}">${Math.round(q7)}</td>
      <td class="${q15 > 0 ? 'green' : 'muted'}">${Math.round(q15)}</td>
      <td class="${q30 > 0 ? 'green' : 'muted'}">${Math.round(q30)}</td>
      <td class="gold">${qty}</td>
      <td class="${stk > 10 ? 'red' : stk > 0 ? 'orange' : 'muted'}">${stk}</td>
      <td class="${wip > 10 ? 'orange' : wip > 0 ? 'gold' : 'muted'}">${wip}</td>
      <td><span class="forecast-pill">${item.forecast_60d || 0}</span></td>
      <td><span class="forecast-pill" style="background:#fff4e0;color:#b45309;border-color:#f3d9a8">${item.reorder_qty || 0}</span></td>
      <td><input type="text" class="ro-remark" value="${(roRemarks[item.sku]||'').replace(/"/g,'&quot;')}" placeholder="Type remark…" oninput="setRoRemark('${skuEsc}', this.value)" onclick="event.stopPropagation()"></td>
    </tr>`;
  }).join('') + (colFiltered.length > RO_CAP
    ? `<tr><td colspan="11" style="text-align:center;padding:12px;color:#8c7a42;font-weight:700">Showing first ${RO_CAP} of ${colFiltered.length.toLocaleString('en-IN')} — narrow with column filters or the filter panel above.</td></tr>`
    : '');
}

function resetColFilters(){
  ['cfSku','cfRemark'].forEach(id => { const el=document.getElementById(id); if(el) el.value=''; });
  ['cfQty7d','cfQty15d','cfQty30d','cfSoldQty','cfInvStock','cfInvWip','cfForecast','cfReorder'].forEach(id => {
    const el = document.getElementById(id); if(el) el.value='';
  });
  _cfActive = false;
  applyRO(); // full re-render
}
window.applyColFilters = applyColFilters;
window.resetColFilters = resetColFilters;

function resetRO(){
  ['rSearch','rCust','rD1','rD2','rSkuSearch'].forEach(id => { const el=document.getElementById(id); if (el) el.value=''; });
  document.querySelectorAll('#rTypeChecks input:checked').forEach(c => c.checked = false);
  document.querySelectorAll('#rPackChecks input:checked').forEach(c => c.checked = false);
  const rx = document.getElementById('rTaxon'); if (rx) rx.value='All';
  pastedSkuSet = null;
  const ta = document.getElementById('rPasteSkus'); if (ta) ta.value = '';
  const pinfo = document.getElementById('rPasteInfo'); if (pinfo) pinfo.textContent = '';
  selectedSkuSet.clear();
  refreshChecklists();
  applyF();
  applyRO();
}

function exportRO(fmtType){
  if (roTxns) {
    if (!roTxns.length) { alert('No transactions to export.'); return; }
    let txns = roTxns;
    if (selectedSkuSet && selectedSkuSet.size > 0) {
      const narrowed = roTxns.filter(t => selectedSkuSet.has(t.sku));
      if (narrowed.length) txns = narrowed;
    }
    const dimMap = {}, mrpMap = {}, packMap = {};
    ((typeof master !== 'undefined' && master) || []).forEach(it => { if (it && it.sku) { dimMap[it.sku] = it.dimensions || ''; mrpMap[it.sku] = it.mrp || 0; packMap[it.sku] = it.pack_details || ''; } });
    const emp0 = LOGIN_ROLE === 'employee';
    const headers = ['Dispatch Date','SKU','Product Dimensions','Pack Details','Customer','Type','Final Qty','MRP', ...(emp0 ? [] : ['Selling Price']),'Inv Stock','Inv WIP','Remark','Image Link'];
    const data = txns.map(t => ({
      'Dispatch Date': t.date === 'N/A' ? '' : t.date,
      SKU: t.sku,
      'Product Dimensions': (t.dimensions || dimMap[t.sku] || ''),
      'Pack Details': packMap[t.sku] || '',
      Customer: t.cust,
      Type: t.type,
      'Final Qty': parseFloat(t.qty) || 0,
      'MRP': parseFloat(mrpMap[t.sku]) || 0,
      ...(emp0 ? {} : {'Selling Price': parseFloat(t.sp) || 0}),
      'Inv Stock': parseInt(t.inv_stock) || 0,
      'Inv WIP': parseInt(t.inv_wip) || 0,
      'Remark': roRemarks[t.sku] || '',
      'Image Link': t.image_url || '',
    }));
    downloadTable(headers, data, 'repeat_orders_transactions', fmtType);
    return;
  }

  let rows = roFiltered || [];
  const hasTicks = selectedSkuSet && selectedSkuSet.size > 0;
  if (hasTicks) {
    rows = rows.filter(item => selectedSkuSet.has(item.sku));
    if (!rows.length) { alert('None of the ticked SKUs are in the current filtered table.'); return; }
  }
  if (!rows.length) { alert('No rows to export'); return; }

  const emp1 = LOGIN_ROLE === 'employee';
  // Filter context — export ko screen jaisa channel-aware banane ke liye
  const typeSel = getSelectedTypes('rType');
  const singleType = typeSel.length === 1 ? typeSel[0].toLowerCase() : null;
  const roNoFilterX = !(typeSel.length > 0);
  const nowX = todayISO || new Date().toISOString().slice(0,10);
  const _dAgo = n => new Date(new Date(nowX) - n*86400000).toISOString().slice(0,10);
  const D7 = _dAgo(7), D15 = _dAgo(15), D30 = _dAgo(30);
  // entries ko type filter ke hisaab se le aao (filter na ho to saari)
  const filtEnts = (it) => {
    if (typeSel.length > 0) {
      return (it._fe && it._fe.length) ? it._fe : (it.sales_entries || []).filter(e => typeSel.includes(e.type));
    }
    return it.sales_entries || [];
  };
  const winQty = (ents, since) => ents.filter(e=>e.date!=='N/A'&&e.date>=since).reduce((s,e)=>s+(parseFloat(e.qty)||0),0);
  // channel-aware WIP (jaise screen pe)
  const chWip = (o) => {
    if (singleType && singleType.includes('website')) return o.inv_wip_website || 0;
    if (singleType && (singleType.includes('sor')||singleType.includes('s.o.r'))) return o.inv_wip_sor || 0;
    if (singleType && (singleType.includes('purchase')||singleType.includes('designer')||singleType.includes('customer'))) return o.inv_wip_designer || 0;
    return o.inv_wip || 0;
  };
  const headers = ['Row Type','SKU','Set Item Of','Product Dimensions','Pack Details','7D Sale','15D Sale','30D Sale','Sold Qty','MRP', ...(emp1 ? [] : ['Selling Price']),'Inv Stock','Inv WIP','Blocked Qty','Forecast Sold Qty','Reorder Qty','Status','Taxon','Plating','Type','Customer Count','Remark','Remark 2','Image Link'];
  const data = [];
  rows.forEach(item => {
    // Main row: filter ke according 7D/15D/30D/Sold + channel WIP
    let r7, r15, r30, rSold;
    if (!roNoFilterX) {
      const fe = filtEnts(item);
      r7 = winQty(fe, D7); r15 = winQty(fe, D15); r30 = winQty(fe, D30);
      rSold = item._fQty ?? fe.reduce((s,e)=>s+(parseFloat(e.qty)||0),0);
    } else {
      r7 = item.qty_7d||0; r15 = item.qty_15d||0; r30 = item.qty_1m||0;
      rSold = item.final_qty||0;
    }
    data.push({
      'Row Type': (item.combo_details && item.combo_details.length) ? 'Gift Set' : 'Product',
      SKU: item.sku,
      'Set Item Of': '',
      'Product Dimensions': item.dimensions || '',
      'Pack Details': item.pack_details || '',
      '7D Sale': Math.round(r7),
      '15D Sale': Math.round(r15),
      '30D Sale': Math.round(r30),
      'Sold Qty': Math.round(rSold),
      'MRP': parseFloat(item.mrp) || 0,
      ...(emp1 ? {} : {'Selling Price': parseFloat(item.last_selling_price) || 0}),
      'Inv Stock': item.inv_stock || 0,
      'Inv WIP': chWip(item),
      'Blocked Qty': item.blocked_qty || 0,
      'Forecast Sold Qty': item.forecast_60d || 0,
      'Reorder Qty': item.reorder_qty || 0,
      Status: item.status || '',
      Taxon: item.taxon || '',
      Plating: item.plating || '',
      Type: (typeSel.length > 0 ? typeSel.join(', ') : ((item.sales_entries && item.sales_entries[0] && item.sales_entries[0].type) ? item.sales_entries[0].type : '')),
      'Customer Count': item._customer_count || (item.customer_count || 0),
      'Remark': roRemarks[item.sku] || '',
      'Remark 2': roRemarks2[item.sku] || '',
      'Image Link': item.image_url || '',
    });
    // Gift set ke andar wale (stone details) SKUs — filter-aware: Type filter ke hisaab se sales
    (item.combo_details || []).forEach(c => {
      // Type filter active hai to combo SKU ke filtered sales nikalo
      let c7, c15, c30, cSold;
      if (!roNoFilterX && typeSel.length > 0) {
        const masterC = _masterSkuMap[String(c.sku).toUpperCase()];
        if (masterC) {
          const fe = (masterC.sales_entries || []).filter(e => typeSel.includes(e.type));
          c7    = Math.round(winQty(fe, D7));
          c15   = Math.round(winQty(fe, D15));
          c30   = Math.round(winQty(fe, D30));
          cSold = Math.round(fe.reduce((s,e)=>s+(parseFloat(e.qty)||0),0));
        } else {
          c7 = c.qty_7d||0; c15 = c.qty_15d||0; c30 = c.qty_1m||0; cSold = c.final_qty||0;
        }
      } else {
        c7 = c.qty_7d||0; c15 = c.qty_15d||0; c30 = c.qty_1m||0; cSold = c.final_qty||0;
      }
      data.push({
        'Row Type': '— Set Item',
        SKU: c.sku,
        'Set Item Of': item.sku,
        'Product Dimensions': '',
        'Pack Details': '',
        '7D Sale': c7,
        '15D Sale': c15,
        '30D Sale': c30,
        'Sold Qty': cSold,
        'MRP': parseFloat(c.mrp) || 0,
        ...(emp1 ? {} : {'Selling Price': ''}),
        'Inv Stock': c.inv_stock || 0,
        'Inv WIP': chWip(c),
        'Blocked Qty': c.blocked_qty || 0,
        'Forecast Sold Qty': c.forecast_60d || 0,
        'Reorder Qty': c.reorder_qty || 0,
        Status: c.found ? '' : 'Not in inventory',
        Taxon: c.taxon || '',
        Plating: c.plating || '',
        Type: typeSel.length > 0 ? typeSel.join(', ') : '',
        'Customer Count': '',
        'Remark': '',
        'Remark 2': '',
        'Image Link': c.image_url || '',
      });
    });
  });
  downloadTable(headers, data, hasTicks ? 'repeat_orders_selected' : 'repeat_orders_filtered', fmtType);
}

function onImg(inp){
  if (inp.files && inp.files[0]) {
    const r = new FileReader();
    r.onload = e => {
      const p = document.getElementById('preview');
      if (p) { p.src = e.target.result; p.style.display='block'; }
      imgB64 = e.target.result;
      const g = document.getElementById('goBtn');
      if (g) g.disabled = false;
    };
    r.readAsDataURL(inp.files[0]);
  }
}

function setFinderImage(dataUrl){
  imgB64 = dataUrl;
  const p = document.getElementById('preview');
  if (p) { p.src = dataUrl; p.style.display='block'; }
  const g = document.getElementById('goBtn');
  if (g) g.disabled = false;
}

function handleFinderFile(file){
  if (!file || !String(file.type || '').startsWith('image/')) return false;
  const r = new FileReader();
  r.onload = e => setFinderImage(e.target.result);
  r.readAsDataURL(file);
  return true;
}

function handleFinderPaste(ev){
  if (currentTab !== 'finder') return;
  const items = (ev.clipboardData && ev.clipboardData.items) ? Array.from(ev.clipboardData.items) : [];
  const imgItem = items.find(it => it.kind === 'file' && String(it.type || '').startsWith('image/'));
  if (imgItem) {
    const file = imgItem.getAsFile();
    if (file) {
      ev.preventDefault();
      handleFinderFile(file);
    }
  }
}

function handleFinderDrop(ev){
  ev.preventDefault();
  const file = ev.dataTransfer && ev.dataTransfer.files ? ev.dataTransfer.files[0] : null;
  if (file) handleFinderFile(file);
}

function onImg(inp){
  if (inp.files && inp.files[0]) handleFinderFile(inp.files[0]);
}

function handleRepeatUpload(inp){
  const file = inp.files && inp.files[0];
  const info = document.getElementById('rUploadInfo');
  if (!file) return;
  if (info) info.textContent = 'Uploading ' + file.name + '...';
  const fd = new FormData();
  fd.append('file', file, file.name);
  const reportWin = window.open('about:blank', '_blank');
  fetch('/api/upload-report', {method:'POST', body: fd, headers:{'ngrok-skip-browser-warning':'true'}})
    .then(r => r.json().then(j => ({ok:r.ok, data:j})))
    .then(({ok, data}) => {
      if (!ok || data.error) throw new Error(data.error || 'Upload failed');
      if (info) info.textContent = 'Opened report for ' + file.name;
      if (reportWin) reportWin.location = data.url;
      else window.open(data.url, '_blank');
    })
    .catch(e => {
      if (info) info.textContent = '';
      alert('Upload failed: ' + e.message);
    })
    .finally(() => { inp.value = ''; });
}

function doVision(){
  if (!imgB64) return;
  const L = document.getElementById('loader');
  if (L) { L.innerHTML = '<div class="spin"></div>Scanning AI vision model…'; L.style.display='block'; }
  const btn = document.getElementById('goBtn'); if (btn) btn.disabled = true;
  const out = document.getElementById('gFinder'); if (out) out.innerHTML = '';

  fetch('/search', {method:'POST', headers:{'Content-Type':'application/json','ngrok-skip-browser-warning':'true'}, body: JSON.stringify({image:imgB64})})
    .then(r => r.json())
    .then(d => {
      if (d.error) throw new Error(d.error);
      if (out) out.innerHTML = (d.results || []).map(m => mkCard(m, m.total_net_revenue, m.confidence, false)).join('') || '<div class="no-data">No match found</div>';
    })
    .catch(e => alert('Error: ' + e.message))
    .finally(() => {
      if (L) L.style.display='none';
      if (btn) btn.disabled = false;
    });
}

let LOGIN_ROLE = 'admin';
let _loggedIn = false;

// live server warmup progress in the loader (cold start par exact status dikhta hai)
let _warmPoll = null;
let _warmRetries = 0;
function startWarmupPoll(){
  if (_warmPoll) return;
  _warmPoll = setInterval(async () => {
    try{
      const L = document.getElementById('loader');
      if (!L || L.style.display === 'none') { stopWarmupPoll(); return; }
      const d = await (await fetch('/api/warmup-status', {headers:{'ngrok-skip-browser-warning':'true'}})).json();
      if (d && d.stage && d.stage !== 'ready' && d.stage !== 'idle'){
        const prog = (d.total > 0) ? ` — ${Number(d.done).toLocaleString('en-IN')} / ${Number(d.total).toLocaleString('en-IN')}` : '';
        L.innerHTML = '<div class="spin"></div>' + escHtml(d.detail || d.stage) + prog;
      }
    } catch(e){}
  }, 2000);
}
function stopWarmupPoll(){ if (_warmPoll){ clearInterval(_warmPoll); _warmPoll = null; } }

// Har refresh/reload par DOBARA login maange — auto-restore hata diya.
// (Pehle /api/me se session restore ho jati thi; ab nahi.)
document.addEventListener('DOMContentLoaded', () => {
  const gate = document.getElementById('loginGate'); if (gate) gate.style.display = 'flex';
  const app = document.getElementById('appRoot');   if (app) app.style.display = 'none';
});

function applyRoleUI(){
  const isEmployee = LOGIN_ROLE === 'employee';
  document.body.classList.toggle('role-employee', isEmployee);
  const hideIds = ['m2','t1','m7'];   // matrix (Overall Details), marketplaces — employee nahi dekh sakta
  hideIds.forEach(id => { const el = document.getElementById(id); if (el) el.style.display = isEmployee ? 'none' : ''; });
  // Help tab SIRF employee ko (admin ko nahi).
  const helpBtn = document.getElementById('m11');
  if (helpBtn) helpBtn.style.display = isEmployee ? '' : 'none';
  // Discount Leakage SIRF admin ko.
  const discBtn = document.getElementById('m12');
  if (discBtn) discBtn.style.display = isEmployee ? 'none' : '';
  // Production admin + employee dono ko.
  const prodBtn = document.getElementById('m13');
  if (prodBtn) prodBtn.style.display = '';
  // Profit Margin SIRF admin ko (cost/margin sensitive).
  const pmBtn = document.getElementById('m14');
  if (pmBtn) pmBtn.style.display = isEmployee ? 'none' : '';
  // Insights "Sort By" me revenue option employee ko na dikhe → sirf Qty.
  const iSort = document.getElementById('iSort');
  if (iSort) {
    if (isEmployee) iSort.innerHTML = '<option value="qty">By Quantity (high → low)</option>';
    else if (iSort.options.length < 2) iSort.innerHTML =
      '<option value="revenue">By Revenue (high → low)</option><option value="qty">By Quantity (high → low)</option>';
  }
  // Target (m10) and Insights (m6) dono role ko dikhne chahiye
  const tgtBtn = document.getElementById('m10');
  const insBtn = document.getElementById('m6');
  if (tgtBtn) tgtBtn.style.display = '';
  if (insBtn) insBtn.style.display = '';

  if (isEmployee && (currentTab === 'matrix' || currentTab === 'marketplaces')) {
    showTab('home');
  }
}

const KPI_PASS = "Mayuresh";
function unlockKpis(section='matrix'){
  const cfg = section === 'insights'
    ? {passId:'iKpiPass', lockId:'insightKpiLock', boxId:'insightSummary', errId:'iKpiErr', display:'grid'}
    : {passId:'kpiPass', lockId:'kpiLock', boxId:'kpiBox', errId:'kpiErr', display:'flex'};
  const v = (document.getElementById(cfg.passId)?.value || '');
  const err = document.getElementById(cfg.errId);
  if (v === KPI_PASS) {
    const lock = document.getElementById(cfg.lockId); if (lock) lock.style.display = 'none';
    const box = document.getElementById(cfg.boxId);   if (box) box.style.display = cfg.display;
    if (err) err.textContent = '';
  } else {
    if (err) err.textContent = 'Wrong password';
    const p = document.getElementById(cfg.passId); if (p) { p.value=''; p.focus(); }
  }
}

function enterApp(role){
  LOGIN_ROLE = role;
  _loggedIn = true;
  const gate = document.getElementById('loginGate'); if (gate) gate.style.display = 'none';
  const app = document.getElementById('appRoot');   if (app) app.style.display = 'block';
  applyRoleUI();
  if (typeof showTab === 'function') showTab('home');
  if (typeof loadData === 'function') setTimeout(() => { try { loadData(false); } catch(e){ console.error(e); } }, 50);
}

async function doLogin(){
  const u = (document.getElementById('lgUser')?.value || '').trim();
  const p = (document.getElementById('lgPass')?.value || '');
  const err = document.getElementById('lgErr');
  let ok = false, role = 'admin';
  try{
    const r = await fetch('/api/login', {method:'POST', headers:{'Content-Type':'application/json','ngrok-skip-browser-warning':'true'},
      body: JSON.stringify({username:u, password:p})});
    const d = await r.json();
    ok = !!d.ok; role = d.role || 'admin';
  } catch(e){ ok = false; }

  if (ok) {
    if (err) err.textContent = '';
    try { enterApp(role); } catch(e){ console.error('Login flow error:', e); enterApp(role); }
  } else {
    if (err) err.textContent = 'Invalid username or password.';
    const pw = document.getElementById('lgPass'); if (pw) { pw.value = ''; pw.focus(); }
  }
}

window.doLogin = doLogin;

async function doLogout(){
  try {
    await fetch('/api/logout', {method:'POST', headers:{'Content-Type':'application/json','ngrok-skip-browser-warning':'true'}});
  } catch(e){}
  _loggedIn = false;
  LOGIN_ROLE = 'admin';
  const app = document.getElementById('appRoot');   if (app) app.style.display = 'none';
  const gate = document.getElementById('loginGate'); if (gate) gate.style.display = 'flex';
  const pw = document.getElementById('lgPass'); if (pw) pw.value = '';
  const u = document.getElementById('lgUser'); if (u) { u.value=''; u.focus(); }
}
window.doLogout = doLogout;

document.addEventListener('DOMContentLoaded', () => {
  const fs = document.getElementById('fSkuSearch');
  if (fs) fs.addEventListener('input', renderSkuChecklist);
  const r = document.getElementById('lgRole'); if (r) r.addEventListener('change', applyRoleUI);
  const u = document.getElementById('lgUser'); if (u) u.focus();

  window.addEventListener('paste', handleFinderPaste);
});

/* ===== Premium UI enhancements ===== */
function escHtml(v){
  return safeText(v)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

/* ── Helper: combo SKU ka filter-aware HTML (Type filter ke hisaab se
   7D/15D/30D/Sold sales dikhata hai, warna pre-computed totals).
   WIP bhi channel-aware (comboWipFn(c) se). ── */
function _renderComboDetails(combo_details, comboWipFn, wipLabel, typeSel) {
  if (!combo_details || !combo_details.length) return '';
  const now = todayISO || new Date().toISOString().slice(0,10);
  const cd7  = new Date(new Date(now) - 7*86400000).toISOString().slice(0,10);
  const cd15 = new Date(new Date(now) - 15*86400000).toISOString().slice(0,10);
  const cd30 = new Date(new Date(now) - 30*86400000).toISOString().slice(0,10);
  const items_html = combo_details.map(c => {
    let cQ7, cQ15, cQ30, cSold;
    if (typeSel && typeSel.length > 0) {
      const masterC = _masterSkuMap[String(c.sku).toUpperCase()];
      if (masterC) {
        const fe = (masterC.sales_entries || []).filter(e => typeSel.includes(e.type));
        cQ7   = Math.round(fe.filter(e=>e.date!=='N/A'&&e.date>=cd7).reduce((s,e)=>s+(parseFloat(e.qty)||0),0));
        cQ15  = Math.round(fe.filter(e=>e.date!=='N/A'&&e.date>=cd15).reduce((s,e)=>s+(parseFloat(e.qty)||0),0));
        cQ30  = Math.round(fe.filter(e=>e.date!=='N/A'&&e.date>=cd30).reduce((s,e)=>s+(parseFloat(e.qty)||0),0));
        cSold = Math.round(fe.reduce((s,e)=>s+(parseFloat(e.qty)||0),0));
      } else {
        cQ7 = c.qty_7d||0; cQ15 = c.qty_15d||0; cQ30 = c.qty_1m||0; cSold = c.final_qty||0;
      }
    } else {
      cQ7 = c.qty_7d||0; cQ15 = c.qty_15d||0; cQ30 = c.qty_1m||0; cSold = c.final_qty||0;
    }
    const skuEscC = String(c.sku).replace(/'/g, "\\\\'");
    return '<div class="combo-detail">'
      + '<button class="combo-sku" onclick="openSkuDetails(\'' + skuEscC + '\')">' + escHtml(c.sku) + '</button>'
      + (c.found ? '' : ' <span class="muted" style="font-size:.66rem">(not in inv)</span>')
      + '<div class="combo-grid">'
      + '<span>7D <b>' + cQ7 + '</b></span>'
      + '<span>15D <b>' + cQ15 + '</b></span>'
      + '<span>30D <b>' + cQ30 + '</b></span>'
      + '<span>Sold <b>' + cSold + '</b></span>'
      + '<span>Stock <b>' + (c.inv_stock||0) + '</b></span>'
      + '<span>WIP <b>' + (comboWipFn(c)||0) + '</b></span>'
      + '<span>Fcast <b>' + (c.forecast_60d||0) + '</b></span>'
      + '<span>Reorder <b style="color:#b45309">' + (c.reorder_qty||0) + '</b></span>'
      + '</div></div>';
  }).join('');
  return '<div class="combo-box"><div class="combo-title">Stone Details (set items) — '
    + escHtml(wipLabel) + ':</div>' + items_html + '</div>';
}

function copySku(sku){
  const val = safeText(sku);
  if (!val) return;
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(val).then(() => {
      const el = document.getElementById('kpiErr');
      if (el) { el.textContent = `Copied: ${val}`; setTimeout(() => { if (el.textContent === `Copied: ${val}`) el.textContent=''; }, 1500); }
    }).catch(() => {});
  }
}

function topN(items, key, n){
  return (items || []).slice().sort((a,b) => (parseFloat(b[key]) || 0) - (parseFloat(a[key]) || 0)).slice(0, n);
}

function sumBy(items, fn){
  return (items || []).reduce((s, x) => s + (parseFloat(fn(x)) || 0), 0);
}

function renderProHeader(){
  const strip = document.getElementById('proStrip');
  const rail = document.getElementById('proRail');
  if (!strip && !rail) return;

  const totalSkus = (master || []).length;
  const lowStock = (master || []).filter(i => (parseFloat(i.total_inv) || 0) <= 10).length;
  const zeroSales = (master || []).filter(i => (parseFloat(i.final_qty) || 0) === 0).length;
  const launch = (master || []).filter(i => (i.status || '') === 'New Launch').length;
  const totalRevenue = sumBy(master, i => i.total_net_revenue || 0);
  const totalQty = sumBy(master, i => i.final_qty || 0);
  const top = topN(master, 'total_net_revenue', 1)[0];
  const topCat = (() => {
    const g = {};
    (master || []).forEach(i => {
      const k = i.taxon || 'General';
      g[k] = (g[k] || 0) + (parseFloat(i.total_net_revenue) || 0);
    });
    const arr = Object.entries(g).sort((a,b)=>b[1]-a[1])[0];
    return arr ? arr[0] : '—';
  })();

  if (strip) {
    strip.innerHTML = [
      {label:'SKUs', value: totalSkus.toLocaleString('en-IN'), sub:'catalog size'},
      ...(LOGIN_ROLE === 'employee' ? [] : [{label:'Net Revenue', value: fmt(totalRevenue), sub:'all time'}]),
      {label:'Final Qty', value: totalQty.toLocaleString('en-IN'), sub:'units sold'},
      {label:'Low Stock', value: lowStock.toLocaleString('en-IN'), sub:'<= 10 inv'},
      {label:'New Launches', value: launch.toLocaleString('en-IN'), sub:'launched this month'},
      {label:'Top Category', value: topCat, sub: top ? escHtml(top.sku) : '—'},
    ].map(x => `<div class="pro-chip"><div class="label">${escHtml(x.label)}</div><div class="value">${x.value}</div><div class="sub">${escHtml(x.sub)}</div></div>`).join('');
  }

  if (rail) {
    const topLabels = topN(master, 'total_net_revenue', 5);
    rail.innerHTML = [
      `<div class="pro-pill"><b>${totalSkus}</b> SKUs</div>`,
      `<div class="pro-pill"><b>${fmt(totalRevenue)}</b> Revenue</div>`,
      `<div class="pro-pill"><b>${lowStock}</b> Low stock</div>`,
      `<div class="pro-pill"><b>${zeroSales}</b> No sale SKUs</div>`,
      ...topLabels.map(i => `<div class="pro-pill">${escHtml(i.sku)} • <b>${fmt(i.total_net_revenue || 0)}</b></div>`)
    ].join('');
  }
}


function renderHome(){
  const host = document.getElementById('homeContent');
  if (!host) return;
  const data = master || [];
  if (!data.length){ host.innerHTML = '<div class="home-empty">Loading…</div>'; return; }

  const isEmp = (LOGIN_ROLE === 'employee');
  const today = new Date();
  const iso = d => d.toISOString().slice(0,10);

  // LAST WEEK = pichhla poora calendar hafta (Mon–Sun jo abhi khatam hua).
  const dow = (today.getDay() + 6) % 7;              // Mon=0 … Sun=6
  const thisMonday = new Date(today); thisMonday.setDate(today.getDate() - dow); thisMonday.setHours(0,0,0,0);
  const lastMonday = new Date(thisMonday); lastMonday.setDate(thisMonday.getDate() - 7);
  const lastSunday = new Date(thisMonday); lastSunday.setDate(thisMonday.getDate() - 1);
  const wkStart = iso(lastMonday), wkEnd = iso(lastSunday);

  // THIS MONTH = abhi wala calendar mahina (e.g. June 2026): YYYY-MM se match.
  const monKey = today.toISOString().slice(0,7);
  // THIS YEAR = abhi wala calendar saal (e.g. 2026): YYYY se match.
  const yrKey = String(today.getFullYear());

  // Home Type filter (e.g. SOR/Website/Purchase) — selected hone par sirf us
  // type ki sales se top SKU nikalta hai. Default: All Types.
  const homeType = (document.getElementById('homeTypeFilter')?.value || '').trim();

  // Har SKU ke liye QTY (dono roles qty se rank — same dikhe).
  function topByQty(matchFn){
    let best = null, bestQty = -1, bestRev = 0;
    for (const it of data){
      let rev = 0, qty = 0;
      for (const e of (it.sales_entries || [])){
        if (homeType && (e.type || '').trim() !== homeType) continue;
        if (e.date && e.date !== 'N/A' && matchFn(e.date)){
          rev += (parseFloat(e.rev) || 0);
          qty += (parseFloat(e.qty) || 0);
        }
      }
      if (qty > bestQty && qty > 0){ bestQty = qty; bestRev = rev; best = {it, rev, qty}; }
    }
    return best;
  }

  const tWeek  = topByQty(d => d >= wkStart && d <= wkEnd);          // last week (Mon–Sun)
  const tMonth = topByQty(d => d.slice(0,7) === monKey);            // this calendar month
  const tYear  = topByQty(d => d.slice(0,4) === yrKey);             // this calendar year

  function card(ribbon, picked){
    if (!picked){
      return `<div class="top-card"><div class="tc-ribbon">${ribbon}</div>
        <div class="tc-img"><div class="tc-ph">💎</div></div>
        <div class="tc-body"><div class="tc-sku">—</div>
        <div class="tc-sub">No sales in this period</div></div></div>`;
    }
    const it = picked.it;
    const skuEsc = String(it.sku).replace(/'/g, "\\'");
    const img = (it.image_url && String(it.image_url).trim() && String(it.image_url).toLowerCase() !== 'nan')
      ? `<img src="${escHtml(it.image_url)}" loading="lazy" onerror="this.outerHTML='<div class=&quot;tc-ph&quot;>💎</div>'">`
      : `<div class="tc-ph">💎</div>`;
    const revRow = isEmp ? '' :
      `<div class="tc-row"><span class="tc-k">Revenue (period)</span><span class="tc-v gold">${fmt(picked.rev)}</span></div>`;
    return `<div class="top-card">
      <div class="tc-ribbon">${ribbon}</div>
      <div class="tc-img">${img}</div>
      <div class="tc-body">
        <div class="tc-sku" onclick="openSkuDetails('${skuEsc}')" title="View details">${escHtml(it.sku)}</div>
        <div class="tc-sub">${escHtml(it.taxon || 'General')}${it.plating && it.plating!=='N/A' ? ' • '+escHtml(it.plating) : ''}</div>
        <div class="tc-rows">
          <div class="tc-row"><span class="tc-k">Qty sold (period)</span><span class="tc-v">${Math.round(picked.qty).toLocaleString('en-IN')}</span></div>
          ${revRow}
          <div class="tc-row"><span class="tc-k">MRP</span><span class="tc-v">${fmt(it.mrp||0)}</span></div>
          <div class="tc-row"><span class="tc-k">In stock</span><span class="tc-v">${(parseInt(it.inv_stock)||0)} + ${(parseInt(it.inv_wip)||0)} WIP</span></div>
          ${it.dimensions ? `<div class="tc-row"><span class="tc-k">Size</span><span class="tc-v">${escHtml(it.dimensions)}</span></div>` : ''}
        </div>
      </div>
    </div>`;
  }

  // YoY: same month last year (periodKpis se)
  const k = periodKpis || {};
  const lymLabel = k.last_year_month_label || 'Same month last year';
  const lymRev = k.last_year_month || 0;
  const lmLabel = k.last_month_label || 'Last month';
  const lmRev = k.last_month || 0;
  const yoy = (typeof k.mom_yoy_pct === 'number') ? k.mom_yoy_pct : null;
  // same-month-last-year final qty: us mahine ki sari entries se nikaalo
  let lymQty = 0;
  if (k.last_year_month_label){
    // ly key = "YYYY-MM" — label se nahi, dobara compute (entries se)
  }
  const lyKey = (() => {
    const d = new Date(today); d.setMonth(d.getMonth()-12); d.setDate(1);
    // last full month last year:
    const lm = new Date(today.getFullYear(), today.getMonth(), 1); // 1st of this month
    const prevMonth = new Date(lm); prevMonth.setMonth(prevMonth.getMonth()-1); // last month
    const lym = new Date(prevMonth); lym.setFullYear(lym.getFullYear()-1);
    return lym.toISOString().slice(0,7);
  })();
  for (const it of data){
    for (const e of (it.sales_entries||[])){
      if (e.date && e.date.slice(0,7) === lyKey) lymQty += (parseFloat(e.qty)||0);
    }
  }

  const yoyBlock = isEmp ? '' : `
    <p class="home-sec-label">Same Month — Last Year vs This Year</p>
    <div class="yoy-grid">
      <div class="yoy-card">
        <div class="yc-label">${escHtml(lymLabel)} — Revenue</div>
        <div class="yc-val">${fmt(lymRev)}</div>
        <div class="yc-sub">Final Qty: ${Math.round(lymQty).toLocaleString('en-IN')} units</div>
      </div>
      <div class="yoy-card">
        <div class="yc-label">${escHtml(lmLabel)} — Revenue (this year)</div>
        <div class="yc-val">${fmt(lmRev)}</div>
        ${yoy !== null ? `<div class="yc-delta ${yoy>=0?'up':'down'}">${yoy>=0?'▲ +':'▼ '}${yoy}% YoY</div>` : ''}
      </div>
    </div>`;

  // Available types (sales_entries se unique) — dropdown ke liye.
  const typeSet = new Set();
  for (const it of data){ for (const e of (it.sales_entries||[])){ const tp=(e.type||'').trim(); if(tp) typeSet.add(tp); } }
  const typeOpts = ['<option value="">All Types</option>']
    .concat(Array.from(typeSet).sort().map(tp => `<option value="${escHtml(tp)}"${tp===homeType?' selected':''}>${escHtml(tp)}</option>`))
    .join('');

  host.innerHTML = `
    <div style="display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-bottom:6px">
      <p class="home-sec-label" style="margin:0">Top Performers${homeType ? ' — '+escHtml(homeType) : ''}</p>
      <div style="display:flex;align-items:center;gap:8px">
        <label class="fl" style="margin:0">Top in Type</label>
        <select class="fs" id="homeTypeFilter" onchange="renderHome()" style="min-width:160px" title="Filter top SKUs by channel type">${typeOpts}</select>
      </div>
    </div>
    <div class="home-top-grid">
      ${card('Top SKU · Last Week', tWeek)}
      ${card('Top SKU · This Month', tMonth)}
      ${card('Top SKU · This Year', tYear)}
    </div>
    ${yoyBlock}
    <div id="helpQueriesBox"></div>
  `;
  if (LOGIN_ROLE === 'admin') { try { renderHelpQueries(); } catch(e){} }
}
window.renderHome = renderHome;

/* ── TARGET vs ACTUAL (admin) ── */
let _tgtData = null;
let _tgtFilled = false;
function loadTarget(){
  const host = document.getElementById('tgtContent');
  if (!host) return;
  host.innerHTML = '<div class="home-empty" style="padding:30px">Loading target data…</div>';
  const mf = document.getElementById('tgtMonth')?.value || '';
  const sf = document.getElementById('tgtStake')?.value || '';
  const chf = document.getElementById('tgtChannel')?.value || '';
  fetch('/api/target?month=' + encodeURIComponent(mf) + '&stake=' + encodeURIComponent(sf) + '&channel=' + encodeURIComponent(chf),
        {headers:{'ngrok-skip-browser-warning':'true'}})
    .then(r => r.ok ? r.json() : Promise.reject(new Error('HTTP ' + r.status)))
    .then(d => {
      if (d.error){ host.innerHTML = '<div class="home-empty" style="padding:30px">' + escHtml(d.error) + '</div>'; return; }
      _tgtData = d;
      // dropdown ek baar fill karo (filtered call par options na badlein)
      if (!_tgtFilled){
        const mSel = document.getElementById('tgtMonth');
        const sSel = document.getElementById('tgtStake');
        const cSel = document.getElementById('tgtChannel');
        if (mSel && d.months){
          mSel.innerHTML = d.months.map(m => `<option value="${m}">${m}</option>`).join('');
          // Default = present month (server jo select karke aaya).
          mSel.value = d.month_selected || (d.months[0] || '');
        }
        if (sSel && d.stakeholders){
          const cur = sSel.value;
          sSel.innerHTML = '<option value="">All Stake Holders</option>' +
            d.stakeholders.map(s => `<option value="${escHtml(s)}">${escHtml(s)}</option>`).join('');
          sSel.value = cur;
        }
        if (cSel && d.channels){
          const cur = cSel.value;
          cSel.innerHTML = '<option value="">All Channels</option>' +
            d.channels.map(c => `<option value="${escHtml(c)}">${escHtml(c)}</option>`).join('');
          cSel.value = cur;
        }
        _tgtFilled = true;
      }
      renderTargetTable();
    })
    .catch(err => { host.innerHTML = '<div class="home-empty" style="padding:30px">Failed to load: ' + escHtml(err.message||err) + '</div>'; });
}
function renderTargetTable(){
  const host = document.getElementById('tgtContent');
  const d = _tgtData;
  if (!host || !d){ return; }
  if ((!d.leaderboard || !d.leaderboard.length) && (!d.totals || !d.totals.sp_target)){
    host.innerHTML = '<div class="home-empty" style="padding:30px">No target data for this month.</div>';
    return;
  }
  const t = d.totals || {};
  const monLabel = d.month_label || d.month_selected || '';

  // ── 1) Achievement Forecast (overall, this month) ──
  const pctNow = t.pct_achieved || 0;
  const pctProj = t.proj_pct || 0;
  const projCls = pctProj >= 100 ? 'green' : pctProj >= 80 ? 'orange' : 'red';
  const nowCls = pctNow >= 100 ? 'green' : pctNow >= 50 ? 'orange' : 'red';
  const verdict = pctProj >= 100 ? 'On track to HIT target 🎯'
                : pctProj >= 80 ? 'Close — needs a push'
                : 'At risk — below pace';
  const paceNote = d.is_current_month
    ? `Day ${d.day_elapsed} of ${d.days_in_month} — projection at current pace.`
    : `Month complete (${d.days_in_month} days).`;

  const forecastBlock = `
    <p class="home-sec-label" style="margin-top:6px">Achievement Forecast — ${escHtml(monLabel)}</p>
    <div class="yoy-grid" style="margin-bottom:8px">
      <div class="yoy-card">
        <div class="yc-label">Achieved so far</div>
        <div class="yc-val ${nowCls==='green'?'':''}">${fmt(t.sp_actual||0)}</div>
        <div class="yc-sub">of ${fmt(t.sp_target||0)} target &nbsp;•&nbsp; <span class="${nowCls}" style="font-weight:900">${pctNow}%</span></div>
      </div>
      <div class="yoy-card">
        <div class="yc-label">Projected (month end)</div>
        <div class="yc-val">${fmt(t.proj_rev||0)}</div>
        <div class="yc-delta ${pctProj>=100?'up':'down'}">${pctProj}% projected</div>
        <div class="yc-sub" style="margin-top:8px"><b class="${projCls}">${verdict}</b><br>${paceNote}</div>
      </div>
    </div>`;

  // ── 2) Stakeholder Leaderboard ──
  const lb = (d.leaderboard || []);
  const lbRows = lb.map(L => {
    const pct = L.pct_achieved || 0;
    const proj = L.proj_pct || 0;
    const pctCls = pct >= 100 ? 'green' : pct >= 50 ? 'orange' : 'red';
    const projCls2 = proj >= 100 ? 'green' : proj >= 80 ? 'orange' : 'red';
    const medal = L.rank === 1 ? '🥇' : L.rank === 2 ? '🥈' : L.rank === 3 ? '🥉' : L.rank;
    const barW = Math.max(2, Math.min(100, pct));
    return `<tr>
      <td style="text-align:center;font-weight:900;font-size:1.05rem">${medal}</td>
      <td style="font-weight:800">${escHtml(L.stakeholder)}</td>
      <td style="color:var(--cn-mid)">${escHtml(L.channel||'—')}</td>
      <td>${fmt(L.sp_target)}</td>
      <td>${fmt(L.sp_actual)}</td>
      <td class="${(L.sp_short||0)>0?'red':'green'}" style="font-weight:800">${(L.sp_short||0)>0?fmt(L.sp_short):'✓ Met'}</td>
      <td style="min-width:160px">
        <div style="display:flex;align-items:center;gap:8px">
          <div style="flex:1;height:8px;background:#eee3cf;border-radius:6px;overflow:hidden">
            <div style="width:${barW}%;height:100%;background:linear-gradient(90deg,var(--cn-gold2),var(--cn-gold))"></div>
          </div>
          <span class="${pctCls}" style="font-weight:900;min-width:46px;text-align:right">${pct}%</span>
        </div>
      </td>
      <td class="${projCls2}" style="font-weight:800">${proj}%</td>
    </tr>`;
  }).join('');

  const lbBlock = lb.length ? `
    <p class="home-sec-label" style="margin-top:18px">Stakeholder Leaderboard — ${escHtml(monLabel)}</p>
    <div class="ro-table-wrap" style="padding:0;overflow-x:auto">
      <table class="ro" style="width:100%;min-width:760px">
        <thead><tr>
          <th style="width:50px;text-align:center">#</th><th>Stake Holder</th><th>Channel</th>
          <th>Target</th><th>Achieved</th><th>Short</th><th>Achievement</th><th>Projected</th>
        </tr></thead>
        <tbody>${lbRows}</tbody>
      </table>
    </div>` : '';

  host.innerHTML = forecastBlock + lbBlock;
}
function exportTarget(){
  const d = _tgtData;
  if (!d || !d.leaderboard || !d.leaderboard.length){ alert('No target data to export.'); return; }
  const headers = ['Rank','Stake Holder','Channel','SP Target','SP Achieved','SP Short','% Achieved','% Projected'];
  const rows = d.leaderboard.map(L => [L.rank, L.stakeholder, L.channel||'', Math.round(L.sp_target),
    Math.round(L.sp_actual), Math.round(L.sp_short), L.pct_achieved, L.proj_pct]);
  const t = d.totals||{};
  rows.push(['', 'TOTAL', '', Math.round(t.sp_target||0), Math.round(t.sp_actual||0),
    Math.round(t.sp_short||0), t.pct_achieved||0, t.proj_pct||0]);
  const csv = [headers].concat(rows).map(r => r.map(c => {
    const s = String(c==null?'':c);
    return /[",\n]/.test(s) ? '"'+s.replace(/"/g,'""')+'"' : s;
  }).join(',')).join('\n');
  const blob = new Blob([csv], {type:'text/csv'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob); a.download = 'target_leaderboard_' + (d.month_selected||'') + '.csv'; a.click();
}
window.loadTarget = loadTarget; window.exportTarget = exportTarget;

/* ── DISCOUNT LEAKAGE (admin) ── */
let _discData = null;
function loadDiscount(){
  const host = document.getElementById('discContent');
  const sumHost = document.getElementById('discSummary');
  if (!host) return;
  host.innerHTML = '<div class="home-empty" style="padding:30px">Loading…</div>';
  if (sumHost) sumHost.innerHTML = '';
  const md = document.getElementById('discMin')?.value || '0';
  const sk = document.getElementById('discSort')?.value || 'leakage';
  fetch('/api/discount-leakage?min=' + encodeURIComponent(md) + '&sort=' + encodeURIComponent(sk),
        {headers:{'ngrok-skip-browser-warning':'true'}})
    .then(r => r.ok ? r.json() : Promise.reject(new Error('HTTP ' + r.status)))
    .then(d => {
      if (d.error){ host.innerHTML = '<div class="home-empty" style="padding:30px">' + escHtml(d.error) + '</div>'; return; }
      _discData = d;
      renderDiscount();
    })
    .catch(err => { host.innerHTML = '<div class="home-empty" style="padding:30px">Failed: ' + escHtml(err.message||err) + '</div>'; });
}
function renderDiscount(){
  const host = document.getElementById('discContent');
  const sumHost = document.getElementById('discSummary');
  const d = _discData;
  if (!host || !d) return;
  if (sumHost){
    sumHost.innerHTML = `
      <div class="yoy-card">
        <div class="yc-label">Total Discount Leakage</div>
        <div class="yc-val">${fmt(d.total_leakage||0)}</div>
        <div class="yc-sub">Value lost vs MRP across ${ (d.count||0).toLocaleString('en-IN') } SKUs</div>
      </div>
      <div class="yoy-card">
        <div class="yc-label">Units Sold (discounted)</div>
        <div class="yc-val">${(d.total_units||0).toLocaleString('en-IN')}</div>
        <div class="yc-sub">SKUs selling below MRP</div>
      </div>`;
  }
  if (!d.rows || !d.rows.length){
    host.innerHTML = '<div class="home-empty" style="padding:30px">No discounted SKUs for this filter.</div>';
    return;
  }
  const head = `<tr>
    <th>SKU</th><th>Category</th><th>MRP</th><th>Avg SP</th><th>Last SP</th>
    <th>Discount %</th><th>Gap / unit</th><th>Qty Sold</th><th>Leakage</th></tr>`;
  const body = d.rows.map(r => {
    const dCls = r.disc_pct >= 40 ? 'red' : r.disc_pct >= 20 ? 'orange' : 'gold';
    const img = (r.image_url && String(r.image_url).trim() && String(r.image_url).toLowerCase()!=='nan')
      ? `<img src="${escHtml(r.image_url)}" loading="lazy" style="width:34px;height:34px;object-fit:cover;border-radius:6px;margin-right:8px;vertical-align:middle">` : '';
    return `<tr>
      <td><div class="sku-cell">${img}<button class="sku-link" onclick="openSkuDetails('${String(r.sku).replace(/'/g,"\\\\'")}')">${escHtml(r.sku)}</button></div></td>
      <td>${escHtml(r.taxon||'')}</td>
      <td>${fmt(r.mrp)}</td>
      <td>${fmt(r.avg_sp)}</td>
      <td>${fmt(r.last_sp)}</td>
      <td class="${dCls}" style="font-weight:900">${r.disc_pct}%</td>
      <td>${fmt(r.per_unit_gap)}</td>
      <td>${(r.qty||0).toLocaleString('en-IN')}</td>
      <td class="red" style="font-weight:900">${fmt(r.leakage)}</td>
    </tr>`;
  }).join('');
  host.innerHTML = `<table class="ro" style="width:100%;min-width:900px"><thead>${head}</thead><tbody>${body}</tbody></table>`;
}
function exportDiscount(){
  const d = _discData;
  if (!d || !d.rows || !d.rows.length){ alert('No discount data to export.'); return; }
  const headers = ['SKU','Category','Plating','MRP','Avg SP','Last SP','Discount %','Gap per unit','Qty Sold','Leakage','Net Revenue'];
  const rows = d.rows.map(r => [r.sku, r.taxon, r.plating, Math.round(r.mrp), Math.round(r.avg_sp),
    Math.round(r.last_sp), r.disc_pct, Math.round(r.per_unit_gap), r.qty, Math.round(r.leakage), Math.round(r.net_revenue)]);
  const csv = [headers].concat(rows).map(r => r.map(c => {
    const s = String(c==null?'':c);
    return /[",\n]/.test(s) ? '"'+s.replace(/"/g,'""')+'"' : s;
  }).join(',')).join('\n');
  const blob = new Blob([csv], {type:'text/csv'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob); a.download = 'discount_leakage.csv'; a.click();
}
window.loadDiscount = loadDiscount; window.exportDiscount = exportDiscount;

/* ── PRODUCTION (PPC-WIP) — admin ── */
let _prodData = null;
let _prodFilled = false;
let _prodSearchTimer = null;
function prodSearchDebounced(){ clearTimeout(_prodSearchTimer); _prodSearchTimer = setTimeout(loadProduction, 300); }
function loadProduction(){
  const host = document.getElementById('prodContent');
  const sumHost = document.getElementById('prodSummary');
  if (!host) return;
  host.innerHTML = '<div class="home-empty" style="padding:30px">Loading…</div>';
  if (sumHost) sumHost.innerHTML = '';
  const q = id => encodeURIComponent(document.getElementById(id)?.value || '');
  const url = '/api/production?channel=' + q('prodChannel') + '&balance=' + q('prodBalance') + '&type=' + q('prodType')
    + '&taxon=' + q('prodTaxon') + '&sku=' + q('prodSku') + '&order_no=' + q('prodOrderNo')
    + '&od1=' + q('prodOD1') + '&od2=' + q('prodOD2')
    + '&dd1=' + q('prodDD1') + '&dd2=' + q('prodDD2');
  fetch(url, {headers:{'ngrok-skip-browser-warning':'true'}})
    .then(r => r.ok ? r.json() : Promise.reject(new Error('HTTP ' + r.status)))
    .then(d => {
      if (d.error){ host.innerHTML = '<div class="home-empty" style="padding:30px">' + escHtml(d.error) + '</div>'; return; }
      _prodData = d;
      if (!_prodFilled){
        const fill = (id, arr, allLabel) => {
          const el = document.getElementById(id);
          if (el && arr){ const cur = el.value;
            el.innerHTML = `<option value="">${allLabel}</option>` + arr.map(x => `<option value="${escHtml(x)}">${escHtml(x)}</option>`).join('');
            el.value = cur; }
        };
        fill('prodChannel', d.channels, 'All Channels');
        fill('prodType', d.types, 'All Types');
        fill('prodTaxon', d.taxons, 'All Taxons');
        _prodFilled = true;
      }
      renderProduction();
    })
    .catch(err => { host.innerHTML = '<div class="home-empty" style="padding:30px">Failed: ' + escHtml(err.message||err) + '</div>'; });
}
function renderProduction(){
  const host = document.getElementById('prodContent');
  const sumHost = document.getElementById('prodSummary');
  const d = _prodData;
  if (!host || !d) return;
  if (sumHost){
    sumHost.style.gridTemplateColumns = 'repeat(3,1fr)';
    sumHost.innerHTML = `
      <div class="yoy-card"><div class="yc-label">Total Order Qty</div><div class="yc-val">${(d.total_order_qty||0).toLocaleString('en-IN')}</div><div class="yc-sub">${(d.count||0).toLocaleString('en-IN')} rows • ${(d.unique_orders||0).toLocaleString('en-IN')} orders</div></div>
      <div class="yoy-card"><div class="yc-label">Total Received Qty</div><div class="yc-val">${(d.total_recv_qty||0).toLocaleString('en-IN')}</div><div class="yc-sub">${(d.unique_skus||0).toLocaleString('en-IN')} unique SKUs</div></div>
      <div class="yoy-card"><div class="yc-label">Total Balance Qty</div><div class="yc-val">${(d.total_bal_qty||0).toLocaleString('en-IN')}</div><div class="yc-sub">${(d.pending_rows||0).toLocaleString('en-IN')} rows pending</div></div>`;
  }
  if (!d.rows || !d.rows.length){
    host.innerHTML = '<div class="home-empty" style="padding:30px">No production rows for this filter.</div>';
    return;
  }
  const head = `<tr>
    <th>Order Date</th><th>Order No.</th><th>SKU</th><th>Taxon</th><th>Type</th><th>Channel</th><th>All Order Nos.</th>
    <th>Order Qty</th><th>Recv Qty</th><th>Balance Qty</th><th title="Iss SKU ki saare orders ki Balance Qty jodkar (total)">Total Balance (All Orders)</th><th>Delivery Date</th><th>Receiving Date</th></tr>`;
  const body = d.rows.map(r => {
    const hasImg = (r.image_url && String(r.image_url).trim() && String(r.image_url).toLowerCase()!=='nan');
    const img = hasImg
      ? `<img class="prod-img" src="${escHtml(r.image_url)}" loading="lazy" decoding="async" onerror="this.style.display='none'">`
      : `<div class="prod-ph">&#128142;</div>`;
    const allOrders = (r.all_orders||[]).length ? (r.all_orders||[]).join(', ') : '—';
    const balCls = (r.bal_qty||0) > 0 ? 'orange' : 'green';
    return `<tr>
      <td class="gold">${escHtml(r.date_disp || '—')}</td>
      <td style="font-weight:800">${escHtml(r.order_no || '—')}</td>
      <td><div class="prod-sku-cell">${img}<button class="sku-link prod-sku-text" style="font-weight:800" onclick="openSkuDetails('${String(r.sku).replace(/'/g,"\\\\'")}')">${escHtml(r.sku)}</button></div></td>
      <td>${escHtml(r.taxon || '—')}</td>
      <td>${escHtml(r.order_type || '—')}</td>
      <td>${escHtml(r.channel || '—')}</td>
      <td class="prod-order-list" title="This SKU appears in these order numbers">${escHtml(allOrders)}</td>
      <td class="prod-num">${Math.round(r.order_qty||0).toLocaleString('en-IN')}</td>
      <td class="prod-num">${Math.round(r.recv_qty||0).toLocaleString('en-IN')}</td>
      <td class="prod-num ${balCls}" style="font-weight:800">${Math.round(r.bal_qty||0).toLocaleString('en-IN')}</td>
      <td class="prod-num" style="font-weight:800;color:#b8860b">${Math.round(r.sku_total_balance||0).toLocaleString('en-IN')}</td>
      <td>${escHtml(r.delivery_date || '—')}</td>
      <td>${escHtml(r.receiving_date || '—')}</td>
    </tr>`;
  }).join('') + (d.count > d.rows.length
    ? `<tr><td colspan="13" style="text-align:center;padding:12px;color:#8c7a42;font-weight:700">Showing first ${d.rows.length} of ${d.count.toLocaleString('en-IN')} — narrow with filters.</td></tr>`
    : '');
  const colgroup = `<colgroup>
    <col style="width:7%"><col style="width:8%"><col style="width:15%"><col style="width:8%">
    <col style="width:7%"><col style="width:7%"><col style="width:11%">
    <col style="width:6%"><col style="width:6%"><col style="width:6%">
    <col style="width:8%"><col style="width:6%"><col style="width:5%">
  </colgroup>`;
  host.innerHTML = `<table class="ro prod-table">${colgroup}<thead>${head}</thead><tbody>${body}</tbody></table>`;
}
function resetProduction(){
  ['prodSku','prodOrderNo','prodOD1','prodOD2','prodDD1','prodDD2'].forEach(id => { const e=document.getElementById(id); if(e) e.value=''; });
  ['prodChannel','prodType','prodTaxon','prodBalance'].forEach(id => { const e=document.getElementById(id); if(e) e.value=''; });
  loadProduction();
}
function exportProduction(){
  const d = _prodData;
  if (!d || !d.rows || !d.rows.length){ alert('No production data to export.'); return; }
  const headers = ['Order Date','Order No.','SKU','Taxon','Type','Channel','All Order Nos.','Order Qty','Recv Qty','Balance Qty','Total Balance (All Orders)','Delivery Date','Receiving Date'];
  const rows = d.rows.map(r => [r.date_disp, r.order_no, r.sku, r.taxon, r.order_type, r.channel, (r.all_orders||[]).join(' | '),
    Math.round(r.order_qty||0), Math.round(r.recv_qty||0), Math.round(r.bal_qty||0), Math.round(r.sku_total_balance||0), r.delivery_date, r.receiving_date]);
  const csv = [headers].concat(rows).map(r => r.map(c => {
    const s = String(c==null?'':c);
    return /[",\n]/.test(s) ? '"'+s.replace(/"/g,'""')+'"' : s;
  }).join(',')).join('\n');
  const blob = new Blob([csv], {type:'text/csv'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob); a.download = 'production_ppc_wip.csv'; a.click();
}
window.loadProduction = loadProduction; window.exportProduction = exportProduction;
window.resetProduction = resetProduction; window.prodSearchDebounced = prodSearchDebounced;

/* ── PROFIT MARGIN (admin) ── */
let PM_MODE = 'old';
let PM_CATALOG = [];
let pmLoaded = false;
const pmRupee = n => '₹' + Math.round(n).toLocaleString('en-IN');
const pmMinus = n => (n>0?'−':'') + '₹' + Math.round(Math.abs(n)).toLocaleString('en-IN');
const pmNum = id => { const v = parseFloat(document.getElementById(id).value); return isNaN(v)?0:v; };

function pmInit(){
  pmSetMode(PM_MODE);
  pmCalc();
}
function pmSetMode(m){
  PM_MODE = m;
  document.getElementById('pmOld').classList.toggle('on', m==='old');
  document.getElementById('pmNew').classList.toggle('on', m==='new');
  document.getElementById('pmSkuRow').style.display = (m==='old') ? '' : 'none';
  if (m==='old'){
    document.getElementById('pmNote').innerHTML = 'Pick a SKU — MRP and Product Cost load from the All Product sheet. You can still edit anything.';
    if (!pmLoaded) pmLoadCatalog(false); else {
      // already loaded — agar koi bhi MRP/cost 0 hai to fresh load karo
      const needsRefresh = PM_CATALOG.length > 0 && PM_CATALOG.every(c => !c.mrp && !c.cost);
      if (needsRefresh){ pmLoaded = false; pmLoadCatalog(true); }
    }
  } else {
    document.getElementById('pmNote').textContent = 'Enter everything by hand — nothing is pulled from the sheet.';
    const l = document.getElementById('pmSkuList'); if (l) l.classList.remove('show');
  }
}
function pmLoadCatalog(force){
  const st = document.getElementById('pmSkuStatus');
  st.textContent = 'Loading catalogue…';
  const url = '/api/sku-costs' + (force ? '?force=true' : '');
  fetch(url, {headers:{'ngrok-skip-browser-warning':'true'}})
    .then(r => r.ok ? r.json() : Promise.reject(new Error('HTTP ' + r.status)))
    .then(d => {
      if (d.error){ st.textContent = d.error; return; }
      PM_CATALOG = d.rows || [];
      pmLoaded = true;
      const withMrp  = PM_CATALOG.filter(c => c.mrp  > 0).length;
      const withCost = PM_CATALOG.filter(c => c.cost > 0).length;
      st.textContent = PM_CATALOG.length.toLocaleString('en-IN') + ' SKUs loaded'
        + (withMrp  ? ' • ' + withMrp.toLocaleString('en-IN')  + ' with MRP'  : '')
        + (withCost ? ' • ' + withCost.toLocaleString('en-IN') + ' with Cost' : '')
        + ' — start typing a SKU.';
    })
    .catch(err => { st.innerHTML = 'Could not load SKUs. <button onclick="pmLoadCatalog(true)" style="text-decoration:underline;background:none;border:none;cursor:pointer;color:#d4af5a">Retry</button> or switch to <b>New Product</b>.'; });
}
function pmSkuType(){
  const q = (document.getElementById('pmSkuSearch').value || '').trim().toLowerCase();
  const list = document.getElementById('pmSkuList');
  if (!pmLoaded){ pmLoadCatalog(); }
  if (!q){ list.classList.remove('show'); return; }
  const matches = PM_CATALOG.filter(c => c.sku.toLowerCase().includes(q)).slice(0,40);
  list.innerHTML = matches.length
    ? matches.map(c => {
        const im = (c.image_url && String(c.image_url).trim() && String(c.image_url).toLowerCase()!=='nan')
          ? `<img src="${escHtml(c.image_url)}" loading="lazy" style="width:26px;height:26px;object-fit:cover;border-radius:5px;margin-right:8px;vertical-align:middle" onerror="this.style.display='none'">` : '';
        return `<div class="pm-skuopt" onclick="pmPickSku('${c.sku.replace(/'/g,"\\\\'")}')"><span>${im}${escHtml(c.sku)}</span><span class="mrp">${c.mrp?'MRP '+pmRupee(c.mrp):'MRP —'}${c.cost?' · Cost '+pmRupee(c.cost):''}</span></div>`;
      }).join('')
    : '<div class="pm-skuopt" style="cursor:default;color:#a99">No match</div>';
  list.classList.add('show');
}
function pmPickSku(sku){
  const c = PM_CATALOG.find(x => x.sku === sku);
  if (!c) return;
  document.getElementById('pmSkuSearch').value = c.sku;
  document.getElementById('pmSkuList').classList.remove('show');
  document.getElementById('pmMrp').value = c.mrp || '';
  document.getElementById('pmProdCost').value = c.cost || '';
  const qEl = document.getElementById('pmQty'); if (qEl) qEl.value = c.final_qty || '';
  const nrEl = document.getElementById('pmNetRev'); if (nrEl) nrEl.value = c.net_revenue ? Math.round(c.net_revenue) : '';
  const im = (c.image_url && String(c.image_url).trim() && String(c.image_url).toLowerCase()!=='nan')
    ? `<img src="${escHtml(c.image_url)}" style="width:54px;height:54px;object-fit:cover;border-radius:8px;border:1px solid var(--cn-line);margin-right:10px;vertical-align:middle" onerror="this.style.display='none'">` : '';
  document.getElementById('pmSkuStatus').innerHTML = `${im}<b>${escHtml(c.sku)}</b> · MRP ${c.mrp?pmRupee(c.mrp):'—'} · Cost ${c.cost?pmRupee(c.cost):'—'} · Sold Qty ${c.final_qty||0} · Net Rev ${c.net_revenue?pmRupee(c.net_revenue):'—'}. Edit any field if needed.`;
  pmCalc();
}
document.addEventListener('click', e => {
  const l = document.getElementById('pmSkuList');
  if (l && !e.target.closest('#pmSkuRow')) l.classList.remove('show');
});
function pmCalc(){
  const mrp = pmNum('pmMrp'), disc = pmNum('pmDisc');
  const sp = Math.max(0, mrp * (1 - disc/100));
  document.getElementById('pmSpOut').textContent = pmRupee(sp);
  const comm = sp * pmNum('pmComm')/100;
  const items = {
    pmBrComm: comm, pmBrProd: pmNum('pmProdCost'), pmBrBox: pmNum('pmBox'),
    pmBrPack: pmNum('pmPack'), pmBrShip: pmNum('pmShip'), pmBrAd: pmNum('pmAd'),
    pmBrPG: pmNum('pmPG'), pmBrRTO: pmNum('pmRTO'), pmBrInward: pmNum('pmInward'),
    pmBrStore: pmNum('pmStore'), pmBrFulfil: pmNum('pmFulfil'), pmBrRecall: pmNum('pmRecall'),
  };
  let total = 0;
  for (const id in items){ total += items[id]; document.getElementById(id).textContent = pmMinus(items[id]); }
  const profit = sp - total;
  const margin = sp>0 ? (profit/sp*100) : 0;
  document.getElementById('pmBrSP').textContent = pmRupee(sp);
  document.getElementById('pmBrTotal').textContent = pmMinus(total);
  const brProfit = document.getElementById('pmBrProfit');
  brProfit.textContent = (profit<0?'−':'') + '₹' + Math.abs(Math.round(profit)).toLocaleString('en-IN');
  const prow = brProfit.closest('.profit-row');
  prow.classList.toggle('pos', profit>=0); prow.classList.toggle('neg', profit<0);
  const mEl = document.getElementById('pmMargin');
  mEl.textContent = (sp>0?margin.toFixed(1):'0.0') + '%';
  mEl.classList.toggle('pos', profit>=0); mEl.classList.toggle('neg', profit<0);
  document.getElementById('pmProfitTop').textContent = (profit<0?'−':'') + '₹' + Math.abs(Math.round(profit)).toLocaleString('en-IN') + ' profit';
  // Per-unit × Final Qty = Total
  const qty = Math.max(0, pmNum('pmQty')) || 0;
  const tQty = qty || 1;
  document.getElementById('pmTotQty').textContent = (qty||1).toLocaleString('en-IN');
  document.getElementById('pmTotSP').textContent = pmRupee(sp * tQty);
  document.getElementById('pmTotDed').textContent = pmMinus(total * tQty);
  const totProfit = profit * tQty;
  const tp = document.getElementById('pmTotProfit');
  tp.textContent = (totProfit<0?'−':'') + '₹' + Math.abs(Math.round(totProfit)).toLocaleString('en-IN');
  const tprow = tp.closest('.profit-row');
  tprow.classList.toggle('pos', totProfit>=0); tprow.classList.toggle('neg', totProfit<0);
  const v = document.getElementById('pmVerdict');
  if (sp<=0){ v.textContent='Enter values'; v.className='pm-verdict thin'; }
  else if (profit<0){ v.textContent='Loss — below cost'; v.className='pm-verdict loss'; }
  else if (margin<10){ v.textContent='Thin margin'; v.className='pm-verdict thin'; }
  else { v.textContent='Healthy margin'; v.className='pm-verdict good'; }
}
function resetProfit(){
  document.querySelectorAll('#vProfit input').forEach(i => i.value='');
  const s = document.getElementById('pmSkuSearch'); if (s) s.value='';
  if (PM_MODE==='old' && pmLoaded) document.getElementById('pmSkuStatus').textContent = PM_CATALOG.length.toLocaleString('en-IN') + ' SKUs loaded — start typing a SKU.';
  pmCalc();
}
window.pmInit = pmInit; window.pmSetMode = pmSetMode; window.pmSkuType = pmSkuType;
window.pmPickSku = pmPickSku; window.pmCalc = pmCalc; window.resetProfit = resetProfit;

function exportProfit(){
  const g = id => pmNum(id);
  const mrp = g('pmMrp'), disc = g('pmDisc');
  const sp = Math.max(0, mrp*(1-disc/100));
  const comm = sp * g('pmComm')/100;
  const ded = [
    ['MRP', mrp], ['Discount %', disc], ['Selling Price (SP)', Math.round(sp)],
    ['Commission % of SP', g('pmComm')], ['Commission ₹', Math.round(comm)],
    ['Product Cost', g('pmProdCost')], ['Box Cost', g('pmBox')], ['Pack Fee', g('pmPack')],
    ['Shipping Fees', g('pmShip')], ['Ad Spend', g('pmAd')], ['PG Charges', g('pmPG')],
    ['CR/RTO Charges', g('pmRTO')], ['Inwarding Fee', g('pmInward')], ['Storage Fee', g('pmStore')],
    ['Fulfillment Fee', g('pmFulfil')], ['Inventory Recall', g('pmRecall')],
  ];
  const totalDed = comm + g('pmProdCost')+g('pmBox')+g('pmPack')+g('pmShip')+g('pmAd')+g('pmPG')+g('pmRTO')+g('pmInward')+g('pmStore')+g('pmFulfil')+g('pmRecall');
  const profit = sp - totalDed;
  const margin = sp>0 ? (profit/sp*100) : 0;
  const qty = Math.max(0, g('pmQty')) || 1;
  const sku = (document.getElementById('pmSkuSearch')?.value || '').trim();
  const rows = [['SKU', sku || '(manual)']];
  ded.forEach(d => rows.push(d));
  rows.push(['Total Deductions (per unit)', Math.round(totalDed)]);
  rows.push(['Profit Amount (per unit)', Math.round(profit)]);
  rows.push(['Net Profit Margin %', margin.toFixed(1)]);
  rows.push(['Final Qty', qty]);
  rows.push(['Total Selling Value', Math.round(sp*qty)]);
  rows.push(['Total Deductions', Math.round(totalDed*qty)]);
  rows.push(['Total Profit', Math.round(profit*qty)]);
  const csv = [['Field','Value']].concat(rows).map(r => r.map(c => {
    const s = String(c==null?'':c);
    return /[",\n]/.test(s) ? '"'+s.replace(/"/g,'""')+'"' : s;
  }).join(',')).join('\n');
  const blob = new Blob([csv], {type:'text/csv'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'profit_margin_' + (sku||'manual').replace(/[^A-Za-z0-9_-]/g,'') + '.csv';
  a.click();
}
window.exportProfit = exportProfit;

/* ── AT-RISK CUSTOMERS ── */
let _arData = null;
function loadAtRisk(){
  const host = document.getElementById('arContent');
  const sumHost = document.getElementById('arSummary');
  if (!host) return;
  host.innerHTML = '<div class="home-empty" style="padding:30px">Loading…</div>';
  if (sumHost) sumHost.innerHTML = '';
  const gap = encodeURIComponent(document.getElementById('arGap')?.value || '60');
  fetch('/api/at-risk?gap=' + gap, {headers:{'ngrok-skip-browser-warning':'true'}})
    .then(r => r.ok ? r.json() : Promise.reject(new Error('HTTP ' + r.status)))
    .then(d => {
      if (d.error){ host.innerHTML = '<div class="home-empty" style="padding:30px">' + escHtml(d.error) + '</div>'; return; }
      _arData = d; renderAtRisk();
    })
    .catch(err => { host.innerHTML = '<div class="home-empty" style="padding:30px">Failed: ' + escHtml(err.message||err) + '</div>'; });
}
function renderAtRisk(){
  const host = document.getElementById('arContent');
  const sumHost = document.getElementById('arSummary');
  const d = _arData; if (!host || !d) return;
  const emp = (LOGIN_ROLE === 'employee');
  if (sumHost){
    sumHost.innerHTML = `
      <div class="yoy-card"><div class="yc-label">At-Risk Customers</div><div class="yc-val">${(d.count||0).toLocaleString('en-IN')}</div><div class="yc-sub">${d.gap_days}+ days inactive</div></div>` +
      (emp ? '' : `<div class="yoy-card"><div class="yc-label">Value at Risk</div><div class="yc-val">${fmt(d.total_value_at_risk||0)}</div><div class="yc-sub">lifetime revenue of these customers</div></div>`);
  }
  if (!d.rows || !d.rows.length){
    host.innerHTML = '<div class="home-empty" style="padding:30px">No at-risk customers for this window. 🎉</div>';
    return;
  }
  const head = `<tr>
    <th>Customer</th><th>Type</th><th>Orders</th><th>First Order</th><th>Last Order</th>
    <th>Days Since</th><th>Avg Gap</th><th>Total Qty</th>${emp ? '' : '<th>Total Revenue</th>'}</tr>`;
  const body = d.rows.map(r => `<tr>
      <td style="font-weight:800">${escHtml(r.customer)}</td>
      <td>${escHtml(r.type||'—')}</td>
      <td style="text-align:center">${r.orders}</td>
      <td>${escHtml(r.first_order)}</td>
      <td class="gold">${escHtml(r.last_order)}</td>
      <td class="red" style="text-align:center;font-weight:800">${r.days_since}</td>
      <td style="text-align:center">${r.avg_gap_days||'—'}</td>
      <td style="text-align:center">${(r.total_qty||0).toLocaleString('en-IN')}</td>
      ${emp ? '' : `<td style="font-weight:700">${fmt(r.total_rev)}</td>`}
    </tr>`).join('');
  host.innerHTML = `<table class="ro" style="width:100%;min-width:760px"><thead>${head}</thead><tbody>${body}</tbody></table>`;
}
function exportAtRisk(){
  const d = _arData; if (!d || !d.rows || !d.rows.length){ alert('No data to export.'); return; }
  const emp = (LOGIN_ROLE === 'employee');
  const headers = ['Customer','Type','Orders','First Order','Last Order','Days Since','Avg Gap (days)','Total Qty'].concat(emp ? [] : ['Total Revenue']);
  const rows = d.rows.map(r => [r.customer, r.type, r.orders, r.first_order, r.last_order, r.days_since, r.avg_gap_days, r.total_qty].concat(emp ? [] : [Math.round(r.total_rev)]));
  _dlCsv(headers, rows, 'at_risk_customers');
}
window.loadAtRisk = loadAtRisk; window.renderAtRisk = renderAtRisk; window.exportAtRisk = exportAtRisk;

/* ── PAYMENTS ── */
let _payData = null; let _payTagsFilled = false;
function loadPayments(force){
  const todayHost = document.getElementById('payTodayTable');
  if (todayHost) todayHost.innerHTML = '<div class="home-empty" style="padding:24px">Loading…</div>';
  fetch('/api/payments' + (force ? '?force=true' : ''), {headers:{'ngrok-skip-browser-warning':'true'}})
    .then(r => r.json().then(j => ({ok:r.ok, j})))
    .then(({ok, j}) => {
      if (!ok || j.error){
        const extra = j.where ? '<br><span style="font-size:.72rem;color:#999">' + escHtml(JSON.stringify(j.where)) + '</span>' : '';
        if (todayHost) todayHost.innerHTML = '<div class="home-empty" style="padding:24px">' + escHtml(j.error || 'Failed') + extra + '</div>';
        return;
      }
      const d = j;
      _payData = d;
      const asOf = document.getElementById('payAsOf');
      if (asOf) asOf.textContent = 'As of ' + d.today + ' · month-end ' + d.month_end;
      if (!_payTagsFilled){
        const sel = document.getElementById('payTag');
        if (sel && d.tags){
          sel.innerHTML = '<option value="">All Tags</option>' + d.tags.map(t => `<option value="${escHtml(t)}">${escHtml(t)}</option>`).join('');
        }
        _payTagsFilled = true;
      }
      renderPayments();
    })
    .catch(err => { if(todayHost) todayHost.innerHTML = '<div class="home-empty" style="padding:24px">Failed: ' + escHtml(err.message||err) + '</div>'; });
}
function _payFiltered(){
  const d = _payData; if (!d) return [];
  const tag = (document.getElementById('payTag')?.value || '').toLowerCase();
  const q = (document.getElementById('paySearch')?.value || '').trim().toLowerCase();
  const view = document.getElementById('payView')?.value || 'all';
  return d.rows.filter(r => {
    if (tag && (r.tag||'').toLowerCase() !== tag) return false;
    if (q && !(r.customer||'').toLowerCase().includes(q)) return false;
    if (view === 'overdue' && (r.overdue||0) <= 0) return false;
    if (view === 'due' && (r.due||0) <= 0) return false;
    return true;
  });
}
function renderPayments(){
  const d = _payData; if (!d) return;
  const rows = _payFiltered();
  // summary cards
  const sumDue = rows.reduce((s,r)=>s+(r.due||0),0);
  const sumOver = rows.reduce((s,r)=>s+(r.overdue||0),0);
  const sumBal = rows.reduce((s,r)=>s+(r.balance||0),0);
  const sumHost = document.getElementById('paySummary');
  if (sumHost){
    sumHost.innerHTML =
      `<div class="yoy-card"><div class="yc-label">Total Outstanding</div><div class="yc-val">${fmt(sumBal)}</div><div class="yc-sub">${rows.length} customers</div></div>
       <div class="yoy-card"><div class="yc-label">Due (within term)</div><div class="yc-val" style="color:#1f7a3a">${fmt(sumDue)}</div><div class="yc-sub">not overdue yet</div></div>
       <div class="yoy-card"><div class="yc-label">Overdue</div><div class="yc-val" style="color:#c0392b">${fmt(sumOver)}</div><div class="yc-sub">term crossed</div></div>`;
  }
  // outstanding till today table
  const todayHost = document.getElementById('payTodayTable');
  if (todayHost){
    const body = rows.map(r => `<tr>
        <td style="font-weight:700">${escHtml(r.customer)}</td>
        <td style="text-align:center;color:var(--cn-mid)">${escHtml(r.tag||'—')}</td>
        <td style="text-align:center">${r.term_days||0}d</td>
        <td class="${(r.due||0)>0?'green':'muted'}" style="text-align:right">${fmt(r.due)}</td>
        <td class="${(r.overdue||0)>0?'red':'muted'}" style="text-align:right;font-weight:700">${fmt(r.overdue)}</td>
        <td style="text-align:right;font-weight:800">${fmt(r.balance)}</td>
      </tr>`).join('');
    todayHost.innerHTML = `<table class="ro" style="width:100%;min-width:560px"><thead><tr>
        <th>Customer Name</th><th style="text-align:center">Tag</th><th style="text-align:center">Term</th>
        <th style="text-align:right">Due</th><th style="text-align:right">Overdue</th><th style="text-align:right">Balance</th>
      </tr></thead><tbody>${body || '<tr><td colspan="6" style="text-align:center;padding:20px;color:#999">No customers match</td></tr>'}</tbody>
      <tfoot><tr style="font-weight:800;background:var(--cn-ivory)">
        <td>Total</td><td></td><td></td>
        <td style="text-align:right">${fmt(sumDue)}</td>
        <td style="text-align:right">${fmt(sumOver)}</td>
        <td style="text-align:right">${fmt(sumBal)}</td>
      </tr></tfoot></table>`;
  }
  // aging bucket (filtered customers ka recompute nahi hota server-side; total aging server se)
  const agHost = document.getElementById('payAgingTable');
  if (agHost){
    const ag = d.aging || [];
    const body = ag.map(a => `<tr>
        <td>${escHtml(a.bucket)}</td>
        <td style="text-align:right;font-weight:700">${fmt(a.amount)}</td>
      </tr>`).join('');
    agHost.innerHTML = `<table class="ro" style="width:100%"><thead><tr>
        <th>Aging Bucket</th><th style="text-align:right">Sum of Balance</th>
      </tr></thead><tbody>${body}</tbody>
      <tfoot><tr style="font-weight:800;background:var(--cn-ivory)">
        <td>Total</td><td style="text-align:right">${fmt(d.aging_total)}</td>
      </tr></tfoot></table>
      <p style="color:var(--cn-mid);font-size:.75rem;margin-top:8px">Aging = overall (all customers). 0 Days = within term / not overdue.</p>`;
  }
}
function exportPayments(){
  const rows = _payFiltered();
  if (!rows.length){ alert('No rows to export'); return; }
  const headers = ['Customer Name','Tag','Payment Term (days)','Due','Overdue','Balance','Due (till month-end)','Overdue (till month-end)'];
  const data = rows.map(r => [r.customer, r.tag||'', r.term_days||0, r.due||0, r.overdue||0, r.balance||0, r.due_me||0, r.overdue_me||0]);
  _dlCsv(headers, data, 'payments_outstanding');
}
window.loadPayments = loadPayments; window.renderPayments = renderPayments; window.exportPayments = exportPayments;

/* shared tiny CSV downloader */
function _dlCsv(headers, rows, name){
  const csv = [headers].concat(rows).map(r => r.map(c => {
    const s = String(c==null?'':c);
    return /[",\n]/.test(s) ? '"'+s.replace(/"/g,'""')+'"' : s;
  }).join(',')).join('\n');
  const blob = new Blob([csv], {type:'text/csv'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob); a.download = name + '.csv'; a.click();
}
window._dlCsv = _dlCsv;

/* ── HELP: employee apni query bhejta hai ── */
function submitHelp(){
  const ta = document.getElementById('helpText');
  const msg = document.getElementById('helpMsg');
  const text = (ta?.value || '').trim();
  if (!text){ if(msg){msg.textContent='Please type your problem first.';msg.style.color='#c0392b';} return; }
  if (msg){ msg.textContent = 'Sending…'; msg.style.color='var(--cn-mid)'; }
  fetch('/api/help', {method:'POST', headers:{'Content-Type':'application/json','ngrok-skip-browser-warning':'true'},
    body: JSON.stringify({text})})
    .then(r => r.json())
    .then(d => {
      if (d.ok){
        if(ta) ta.value='';
        if(msg){ msg.textContent='✓ Sent to admin. Thank you!'; msg.style.color='#15803d'; }
      } else {
        if(msg){ msg.textContent = d.error || 'Failed to send.'; msg.style.color='#c0392b'; }
      }
    })
    .catch(()=>{ if(msg){msg.textContent='Network error. Try again.';msg.style.color='#c0392b';} });
}
window.submitHelp = submitHelp;

/* ── ADMIN HOME: employee help queries (24h) ── */
function renderHelpQueries(){
  const host = document.getElementById('helpQueriesBox');
  if (!host) return;
  if (LOGIN_ROLE !== 'admin'){ host.innerHTML=''; return; }
  fetch('/api/help-queries', {headers:{'ngrok-skip-browser-warning':'true'}})
    .then(r => r.json())
    .then(d => {
      const qs = d.queries || [];
      if (!qs.length){ host.innerHTML=''; return; }
      const rows = qs.map(q => `
        <div class="help-q-item">
          <div style="flex:1">
            <div class="help-q-text">${escHtml(q.text)}</div>
            <div class="help-q-meta">— ${escHtml(q.user)} &nbsp;•&nbsp; ${q.ago_min < 60 ? (q.ago_min+' min ago') : (Math.floor(q.ago_min/60)+'h '+(q.ago_min%60)+'m ago')}</div>
          </div>
          <button class="help-q-x" onclick="dismissHelp('${q.id}')" title="Dismiss">✕</button>
        </div>`).join('');
      host.innerHTML = `
        <p class="home-sec-label" style="margin-top:24px">Employee Help Queries <span style="color:var(--cn-mid);font-weight:700">(auto-clears after 24h)</span></p>
        <div class="help-q-wrap">${rows}</div>`;
    })
    .catch(()=>{});
}
function dismissHelp(id){
  fetch('/api/help-dismiss', {method:'POST', headers:{'Content-Type':'application/json','ngrok-skip-browser-warning':'true'},
    body: JSON.stringify({id})}).then(()=> renderHelpQueries());
}
window.renderHelpQueries = renderHelpQueries; window.dismissHelp = dismissHelp;

/* Admin home par naye help queries 60s me apne aap aa jayein. */
setInterval(() => {
  if (LOGIN_ROLE === 'admin' && currentTab === 'home' && document.getElementById('helpQueriesBox')) {
    try { renderHelpQueries(); } catch(e){}
  }
}, 60000);



function renderInsights(){
  const topRevenueList = document.getElementById('topRevenueList');
  const lowStockList = document.getElementById('lowStockList');
  const categoryList = document.getElementById('categoryList');
  const healthList = document.getElementById('healthList');
  const customerList = document.getElementById('customerList');
  const summaryEl = document.getElementById('insightSummary');
  if (!topRevenueList && !lowStockList && !categoryList && !healthList && !customerList && !summaryEl) return;

  const typeSel = getSelectedTypes('iType');
  const taxonQ = document.getElementById('iTaxon')?.value || 'All';
  const d1 = document.getElementById('iD1')?.value || '';
  const d2 = document.getElementById('iD2')?.value || '';

  const withinDate = (e) => {
    if (d1 || d2) {
      if (e.date === 'N/A') return false;
      if (d1 && e.date < d1) return false;
      if (d2 && e.date > d2) return false;
    }
    return true;
  };

  const items = (master || []).filter(i => {
    if (taxonQ !== 'All' && i.taxon !== taxonQ) return false;
    const ents = (i.sales_entries || []).filter(e => (!typeSel.length || typeSel.includes(e.type)) && withinDate(e));
    if (!typeSel.length && !(d1 || d2) && taxonQ === 'All') return true;
    return ents.length > 0;
  }).map(i => {
    const ents = (i.sales_entries || []).filter(e => (!typeSel.length || typeSel.includes(e.type)) && withinDate(e));
    const totalRev = ents.reduce((s,e) => s + (parseFloat(e.rev) || 0), 0);
    const totalQty = ents.reduce((s,e) => s + (parseFloat(e.qty) || 0), 0);
    const totalRet = ents.reduce((s,e) => s + (parseFloat(e.ret) || 0), 0);
    const totalRetAmt = ents.reduce((s,e) => s + (parseFloat(e.ret_amt) || 0), 0);
    const lastDate = ents.length ? ents.map(e => e.date).filter(Boolean).sort().slice(-1)[0] : 'N/A';
    const firstDate = ents.length ? ents.map(e => e.date).filter(Boolean).sort()[0] : 'N/A';
    return {...i, _iEnts: ents, _iRev: totalRev, _iQty: totalQty, _iRet: totalRet, _iRetAmt: totalRetAmt, _firstDate:firstDate, _lastDate:lastDate, _typeList:[...new Set(ents.map(e => e.type))].join(', ')};
  });

  // Sort By: revenue (default) ya quantity. Employee ke liye revenue available
  // nahi, isliye qty par force ho jata hai.
  let _iSortBy = (document.getElementById('iSort')?.value || 'revenue');
  if (LOGIN_ROLE === 'employee') _iSortBy = 'qty';
  insightRows = items.slice().sort((a,b) => _iSortBy === 'qty'
    ? (parseFloat(b._iQty) || 0) - (parseFloat(a._iQty) || 0)
    : (parseFloat(b._iRev) || 0) - (parseFloat(a._iRev) || 0));

  const topRevenue = insightRows.slice(0, 10);
  const lowStock = insightRows.slice().sort((a,b) => (parseFloat(a.total_inv) || 0) - (parseFloat(b.total_inv) || 0)).slice(0, 10);
  const catMap = {};
  const customers = {};
  insightRows.forEach(i => {
    const cat = i.taxon || 'General';
    catMap[cat] = catMap[cat] || {revenue:0, count:0};
    catMap[cat].revenue += (parseFloat(i._iRev) || 0);
    catMap[cat].count += 1;
    (i._iEnts || []).forEach(e => { customers[e.cust] = (customers[e.cust] || 0) + 1; });
  });

  const customerMap = {};
  insightRows.forEach(i => {
    const qty = parseFloat(i._iQty) || 0;
    const rev = parseFloat(i._iRev) || 0;
    (i._iEnts || []).forEach(e => {
      const key = e.cust || 'Unknown';
      if (!customerMap[key]) customerMap[key] = {qty:0, orders:0, revenue:0};
      customerMap[key].qty += parseFloat(e.qty) || 0;
      customerMap[key].orders += 1;
      customerMap[key].revenue += parseFloat(e.rev) || 0;
    });
  });

  const categories = Object.entries(catMap).sort((a,b) => b[1].revenue - a[1].revenue).slice(0, 8);
  const custRows = Object.entries(customerMap).sort((a,b)=>b[1].qty-a[1].qty).slice(0, 8);

  const maxRev = Math.max(1, ...topRevenue.map(i => parseFloat(i._iRev) || 0));
  const maxLow = Math.max(1, ...lowStock.map(i => (parseFloat(i.total_inv) || 0)));
  const maxCat = Math.max(1, ...categories.map(x => x[1].revenue));
  const maxCust = Math.max(1, ...custRows.map(x => x[1].qty || 0));
  const invGood = insightRows.filter(i => (parseFloat(i.total_inv) || 0) >= 20).length;
  const invLow = insightRows.filter(i => (parseFloat(i.total_inv) || 0) <= 10).length;
  const noSale = insightRows.filter(i => (parseFloat(i._iQty) || 0) === 0).length;

  const row = (name, sub, value, pct, suffix='', sku=null) => `
    <div class="insight-row">
      <div>
        <div class="name"${sku ? ` style="cursor:pointer" onclick="openSkuDetails('${String(sku).replace(/'/g, "\\'")}')" title="View SKU details"` : ''}>${escHtml(name)}</div>
        <div class="sub">${escHtml(sub || '')}</div>
        <div class="bar"><span style="width:${Math.max(4, Math.min(100, pct))}%"></span></div>
      </div>
      <div class="insight-val">${escHtml(value)}${suffix ? ` <span style="color:#64748b;font-weight:700">${escHtml(suffix)}</span>` : ''}</div>
    </div>`;

  if (topRevenueList) {
    topRevenueList.innerHTML = topRevenue.length ? topRevenue.map(i => row(
      i.sku,
      `${i.taxon || 'General'} • Qty ${i._iQty || 0}${i.combo_skus ? ' • Combo' : ''}`,
      fmt(i._iRev || 0),
      ((parseFloat(i._iRev) || 0) / maxRev) * 100,
      '', i.sku
    )).join('') : '<div class="insight-empty">No items available</div>';
  }

  if (lowStockList) {
    lowStockList.innerHTML = lowStock.length ? lowStock.map(i => row(
      i.sku,
      `Stock ${i.total_inv || 0} • WIP ${i.inv_wip || 0}`,
      `${i.total_inv || 0}`,
      ((parseFloat(i.total_inv) || 0) / maxLow) * 100,
      'units', i.sku
    )).join('') : '<div class="insight-empty">No items available</div>';
  }

  // Top Returns — COSSA F column (Return Qty); amount = return × selling price.
  const returnsList = document.getElementById('returnsList');
  if (returnsList) {
    const retRows = insightRows.filter(i => (parseFloat(i._iRet) || 0) > 0)
      .sort((a,b) => (parseFloat(b._iRet) || 0) - (parseFloat(a._iRet) || 0)).slice(0, 10);
    const maxRet = Math.max(1, ...retRows.map(i => parseFloat(i._iRet) || 0));
    const isEmp = (LOGIN_ROLE === 'employee');
    returnsList.innerHTML = retRows.length ? retRows.map(i => row(
      i.sku,
      `Return Qty ${Math.round(i._iRet || 0)}${isEmp ? '' : ` • ${fmt(i._iRetAmt || 0)}`}`,
      `${Math.round(i._iRet || 0)}`,
      ((parseFloat(i._iRet) || 0) / maxRet) * 100,
      'qty', i.sku
    )).join('') : '<div class="insight-empty">No returns in this filter</div>';
  }

  if (categoryList) {
    categoryList.innerHTML = categories.length ? categories.map(([k,v]) => row(
      k,
      `${v.count} SKUs`,
      fmt(v.revenue),
      (v.revenue / maxCat) * 100
    )).join('') : '<div class="insight-empty">No categories found</div>';
  }

  if (healthList) {
    healthList.innerHTML = [
      row('Healthy Inventory', `${invGood} SKUs with 20+ total stock`, invGood.toLocaleString('en-IN'), (invGood / Math.max(1, insightRows.length)) * 100),
      row('Low Inventory', `${invLow} SKUs at or below 10 total stock`, invLow.toLocaleString('en-IN'), (invLow / Math.max(1, insightRows.length)) * 100),
      row('No Sales', `${noSale} SKUs with zero final qty`, noSale.toLocaleString('en-IN'), (noSale / Math.max(1, insightRows.length)) * 100),
    ].join('');
  }

  if (customerList) {
    customerList.innerHTML = custRows.length ? custRows.map(([k,v]) => row(
      k,
      `Orders ${v.orders.toLocaleString('en-IN')} • Revenue ${fmt(v.revenue || 0)}`,
      Math.round(v.qty || 0).toLocaleString('en-IN'),
      ((v.qty || 0) / maxCust) * 100,
      'qty'
    )).join('') : '<div class="insight-empty">No customer data</div>';
  }

  if (summaryEl) {
    summaryEl.innerHTML = `
      <div class="insight-summary-card"><div class="label">Filtered SKUs</div><div class="value">${insightRows.length.toLocaleString('en-IN')}</div></div>
      <div class="insight-summary-card"><div class="label">Filtered Net Revenue</div><div class="value">${fmt(insightRows.reduce((s,i)=>s + (parseFloat(i._iRev)||0),0))}</div></div>
      <div class="insight-summary-card"><div class="label">Filtered Qty</div><div class="value">${Math.round(insightRows.reduce((s,i)=>s + (parseFloat(i._iQty)||0),0)).toLocaleString('en-IN')}</div></div>
      <div class="insight-summary-card"><div class="label">Low Stock SKUs</div><div class="value">${invLow.toLocaleString('en-IN')}</div></div>`;
  }

  const mini = document.getElementById('insightMiniSummary');
  if (mini) {
    const topCust = custRows[0] ? custRows[0][0] : '—';
    const topQty = custRows[0] ? Math.round(custRows[0][1].qty || 0).toLocaleString('en-IN') : '0';
    const totRetQty = insightRows.reduce((s,i) => s + (parseFloat(i._iRet) || 0), 0);
    const totRetAmt = insightRows.reduce((s,i) => s + (parseFloat(i._iRetAmt) || 0), 0);
    const isEmp = (LOGIN_ROLE === 'employee');
    mini.innerHTML = `
      <div class="insight-row"><div><div class="name">Top customer</div><div class="sub">${escHtml(topCust)}</div></div><div class="insight-val">${topQty}</div></div>
      <div class="insight-row"><div><div class="name">Total Returns (Qty)</div><div class="sub">COSSA Return Qty (col F)</div></div><div class="insight-val">${Math.round(totRetQty).toLocaleString('en-IN')}</div></div>
      ${isEmp ? '' : `<div class="insight-row"><div><div class="name">Return Amount</div><div class="sub">Return qty × selling price</div></div><div class="insight-val">${fmt(totRetAmt)}</div></div>`}
      <div class="insight-row"><div><div class="name">Filtered items</div><div class="sub">After type / taxon / date filters</div></div><div class="insight-val">${insightRows.length.toLocaleString('en-IN')}</div></div>
      <div class="insight-row"><div><div class="name">Combo SKUs</div><div class="sub">Rows carrying stone details / remarks</div></div><div class="insight-val">${insightRows.filter(i => (i.combo_skus || '').trim()).length.toLocaleString('en-IN')}</div></div>`;
  }
}

function applyInsights(){
  renderInsights();
}

function resetInsights(){
  document.querySelectorAll('#iTypeChecks input:checked').forEach(c => c.checked = false);
  const tx = document.getElementById('iTaxon'); if (tx) tx.value = 'All';
  const d1 = document.getElementById('iD1'); if (d1) d1.value = '';
  const d2 = document.getElementById('iD2'); if (d2) d2.value = '';
  renderInsights();
}

function exportInsights(fmtType){
  if (!insightRows || !insightRows.length) { alert('No insights rows to export'); return; }
  const headers = ['SKU','MRP','Selling Price','Net Revenue','Final Qty','Return Qty','Return Amount','Inv Stock','Inv WIP','Status','Taxon','Plating','Type(s)','First Dispatch','Last Dispatch','Combo SKUs','Customer Count','Image Link'];
  const data = insightRows.map(i => ({
    SKU: i.sku,
    'MRP': parseFloat(i.mrp) || 0,
    'Selling Price': parseFloat(i.last_selling_price) || 0,
    'Net Revenue': Math.round(i._iRev || 0),
    'Final Qty': Math.round(i._iQty || 0),
    'Return Qty': Math.round(i._iRet || 0),
    'Return Amount': Math.round(i._iRetAmt || 0),
    'Inv Stock': i.inv_stock || 0,
    'Inv WIP': i.inv_wip || 0,
    Status: i.status || '',
    Taxon: i.taxon || '',
    Plating: i.plating || '',
    'Type(s)': i._typeList || '',
    'First Dispatch': i._firstDate || '',
    'Last Dispatch': i._lastDate || '',
    'Combo SKUs': i.combo_skus || '',
    'Customer Count': i._iEnts ? new Set(i._iEnts.map(e => e.cust)).size : 0,
    'Image Link': i.image_url || '',
  }));
  downloadTable(headers, data, 'insights_filtered', fmtType);
}

function renderMarketplaces(){
  const root = document.getElementById('marketplaceRoot');
  if (!root) return;
  const md = marketplaceData || {};
  const myn = md.myntra || {};
  const cards = [
    {title:'Myntra', status: myn.connected ? 'Live Sync' : 'Not Connected', note: myn.connected ? `Synced ${myn.synced_at || ''}` : 'Live seller portal sync', qty: myn.live_total_qty || 0},
    {title:'Coverage', status: myn.connected ? `${myn.coverage || 0}% matched` : '—', note: myn.connected ? `${myn.returned_count || 0} of ${myn.query_count || 0} SKUs returned` : 'Portal sync coverage', qty: myn.returned_count || 0},
    {title:'Missing', status: myn.connected ? `${myn.missing_count || 0} SKUs` : '—', note: myn.connected ? 'Queried from portal live' : 'Awaiting sync', qty: myn.missing_count || 0},
    {title:'Nykaa', status:'Pending', note:'Credentials and endpoint mapping pending', qty: 0},
    {title:'Ajio', status:'Pending', note:'Credentials and endpoint mapping pending', qty: 0},
    {title:'Flipkart Seller', status:'Pending', note:'Credentials and endpoint mapping pending', qty: 0},
  ];

  const summaryHtml = cards.map(c => `
    <div class="insight-summary-card">
      <div class="label">${c.title}</div>
      <div class="value">${String(c.qty).toLocaleString('en-IN')}</div>
      <div class="home-card-sub">${c.status}</div>
      <div class="home-card-sub">${c.note}</div>
    </div>`).join('');

  const rows = (myn.items || []).slice(0, 200).map((r, idx) => {
    const sku = r.sku || '';
    const masterItem = (master || []).find(x => String(x.sku).trim().toUpperCase() === String(sku).trim().toUpperCase());
    const localQty = masterItem ? (parseInt(masterItem.total_inv || 0, 10) || 0) : 0;
    const diff = (r.live_qty || 0) - localQty;
    const diffCls = diff === 0 ? 'gold' : diff > 0 ? 'green' : 'red';
    return `<tr>
      <td>${idx + 1}</td>
      <td class="gold">${sku}</td>
      <td>${localQty}</td>
      <td class="${diffCls}">${diff >= 0 ? '+' : ''}${diff}</td>
      <td class="green">${r.live_qty || 0}</td>
      <td class="muted">${r.store_code || ''}</td>
    </tr>`;
  }).join('');

  const errHtml = (myn.errors && myn.errors.length) ? `<div class="tno-data" style="padding:14px 0 8px;color:#dc2626">${myn.errors.map(e => String(e)).join(' • ')}</div>` : '';

  root.innerHTML = `
    <div class="insights-head">
      <div>
        <div class="insights-title">Marketplaces</div>
        <div class="insights-sub">Live portal sync. Myntra reads the ops-reports portal page first and falls back to API only when portal parsing is unavailable.</div>
      </div>
      <div class="insight-toolbar-actions">
        <button class="go-btn" style="width:auto;padding:10px 14px;letter-spacing:2px" onclick="loadData(true)">Sync Now</button>
        <button class="go-btn" style="width:auto;padding:10px 14px;letter-spacing:2px;background:#f3f6fb;color:#111" onclick="renderMarketplaces()">Refresh View</button>
      </div>
    </div>
    <div class="insight-summary">${summaryHtml}</div>
    <div class="filter-box">
      <div class="small-note">Myntra live inventory uses the partner portal ops-reports page first. If you provide an authenticated portal cookie, the page can be parsed directly; otherwise API fallback is used.</div>
    </div>
    <div class="ro-table-wrap">
      <table class="ro">
        <thead><tr><th>#</th><th>SKU</th><th>Local Qty</th><th>Diff</th><th>Myntra Live Qty</th><th>Store Code</th></tr></thead>
        <tbody>${rows || '<tr><td colspan="6" class="tno-data">No Myntra live rows</td></tr>'}</tbody>
      </table>
    </div>
    ${errHtml}
  `;
}

function renderProUI(){
  renderProHeader();
  // NOTE: renderInsights() yahan se hata diya — pehle har filter/applyRO par
  // poora Insights (10k SKU) bhi re-render hota tha (chahe woh tab khula na ho),
  // isse bahut hang hota tha. Insights ab apne tab khulne par hi render hota hai.
}

const __origShowTab = showTab;
showTab = function(t){
  // Marketplaces aur Smart Search ab band hain (admin + employee dono ke liye).
  if (t === 'marketplaces' || t === 'smart') t = 'home';
  if (LOGIN_ROLE === 'employee' && (t === 'matrix' || t === 'marketplaces' || t === 'discount' || t === 'profit')) t = 'home';
  if (LOGIN_ROLE === 'admin' && t === 'help') t = 'home';   // admin ko Help tab nahi
  const map = {
    home: {id: 'vHome', btn: 'm1'},
    matrix: {id: 'vMatrix', btn: 'm2'},
    repeat: {id: 'vRepeat', btn: 'm3'},
    finder: {id: 'vFinder', btn: 'm4'},
    skudetails: {id: 'vSkudetails', btn: 'm5'},
    insights: {id: 'vInsights', btn: 'm6'},
    target: {id: 'vTarget', btn: 'm10'},
    discount: {id: 'vDiscount', btn: 'm12'},
    production: {id: 'vProduction', btn: 'm13'},
    profit: {id: 'vProfit', btn: 'm14'},
    atrisk: {id: 'vAtrisk', btn: 'm16'},
    payments: {id: 'vPayments', btn: 'm17'},
    help: {id: 'vHelp', btn: 'm11'},
    marketplaces: {id: 'vMarketplaces', btn: 'm7'},
    ai: {id: 'vAi', btn: 'm8'},
    smart: {id: 'vSmart', btn: 'm9'},
  };
  Object.values(map).forEach(x => {
    const el = document.getElementById(x.id);
    if (el) el.style.display = 'none';
    const b = document.getElementById(x.btn);
    if (b) b.classList.remove('active');
  });
  currentTab = t || 'home';
  const pick = map[t] || map.home;
  const showEl = document.getElementById(pick.id);
  if (showEl) showEl.style.display = 'block';
  const btn = document.getElementById(pick.btn);
  if (btn) btn.classList.add('active');

  document.body.setAttribute('data-tab', t || 'home');
  const hero = document.getElementById('siteHero');
  if (hero) hero.classList.toggle('hidden-hero', t !== 'home');

  const tabs = document.querySelector('.tabs');
  if (tabs) tabs.style.top = (t === 'home' ? '116px' : '70px');

  const appBarSub = document.getElementById('appBarSub');
  if (appBarSub) {
    const labels = {
      home: 'HOME',
      matrix: 'OVERALL DETAILS',
      repeat: 'REPEAT ORDERS',
      finder: 'SKU FINDER',
      skudetails: 'SKU DETAILS',
      insights: 'INSIGHTS',
      target: 'TARGET',
      discount: 'DISCOUNT LEAKAGE',
      production: 'PRODUCTION',
      profit: 'PROFIT MARGIN',
      atrisk: 'AT-RISK CUSTOMERS',
      payments: 'PAYMENTS',
      help: 'HELP',
      marketplaces: 'MARKETPLACES',
      ai: 'AI STUDIO',
      smart: 'SMART SEARCH'
    };
    appBarSub.textContent = labels[t] || 'HOME';
  }

  const backBtn = document.getElementById('sdBackBtn');
  if (backBtn) backBtn.style.display = t === 'skudetails' ? 'inline-flex' : 'none';
  toggleNavMenu(false);
  if (t === 'home') renderProHeader();
  // Heavy renders ko defer karo — tab turant switch ho jaye (UI block na ho),
  // bhaari kaam agle frame me. Isse page badalne par hang nahi hoga.
  if (t === 'repeat')   setTimeout(()=>{ try{ applyRO(); }catch(e){console.error(e);} }, 0);
  if (t === 'matrix')   setTimeout(()=>{ try{ applyF(); }catch(e){console.error(e);} }, 0);
  if (t === 'insights') setTimeout(()=>{ try{ renderInsights(); }catch(e){console.error(e);} }, 0);
  if (t === 'target')   setTimeout(()=>{ try{ loadTarget(); }catch(e){console.error(e);} }, 0);
  if (t === 'discount') setTimeout(()=>{ try{ loadDiscount(); }catch(e){console.error(e);} }, 0);
  if (t === 'production') setTimeout(()=>{ try{ loadProduction(); }catch(e){console.error(e);} }, 0);
  if (t === 'profit') setTimeout(()=>{ try{ pmInit(); }catch(e){console.error(e);} }, 0);
  if (t === 'atrisk') setTimeout(()=>{ try{ loadAtRisk(); }catch(e){console.error(e);} }, 0);
  if (t === 'payments') setTimeout(()=>{ try{ loadPayments(); }catch(e){console.error(e);} }, 0);
  if (t === 'home')     setTimeout(()=>{ try{ renderHome(); }catch(e){console.error(e);} }, 0);
  if (t === 'ai') { /* AI Studio removed */ }
};

const __origMkCard = mkCard;
mkCard = function(item, rev, conf, slow){
  const img = (item.image_url && String(item.image_url).trim() && String(item.image_url).toLowerCase() !== 'nan')
    ? `<img src="${escHtml(item.image_url)}" loading="lazy" decoding="async" onerror="this.outerHTML='<div class=&quot;img-ph&quot;>💎</div>'">`
    : '<div class="img-ph">💎</div>';
  const confB = conf ? `<div class="badge-conf">${conf}%</div>` : '';
  const statusB = `<div class="badge-status">${escHtml(item.status || '')}</div>`;
  const invB = `<div class="badge-inv">INV ${item.total_inv || 0}</div>`;
  const s = {m1:item.qty_1m||0,m3:item.qty_3m||0,m6:item.qty_6m||0,y1:item.qty_1y||0};
  const r = rev !== undefined ? rev : (item.total_net_revenue || 0);
  const low = (parseFloat(item.total_inv) || 0) <= 10 ? ' style="color:#d97706"' : '';
  const code = escHtml(item.sku);
  return `<div class="card">
    <div class="img-box">${img}${statusB}${confB}${invB}</div>
    <div class="cb">
      <div class="sku" style="cursor:pointer" onclick="openSkuDetails('${String(item.sku).replace(/'/g, "\\\\'")}')" title="View full SKU details">${code}</div>
      <div class="card-meta">
        <span class="meta-tag"${low}>${escHtml(item.taxon || 'General')}</span>
        <span class="meta-tag">MRP ₹${Math.round(item.mrp || 0).toLocaleString('en-IN')}</span>
        ${item.dimensions ? `<span class="meta-tag">${escHtml(String(item.dimensions))}</span>` : ''}
        <span class="meta-tag">Plating ${escHtml(item.plating || 'N/A')}</span>
        ${item.combo_skus ? `<span class="meta-tag">Combo SKUs ${escHtml(item.combo_skus)}</span>` : ''}
      </div>
      ${(LOGIN_ROLE === 'employee') ? '' : `
      <div class="row rev-only"><span>Net Revenue</span><span>${fmt(r)}</span></div>
      <div class="row rev-only"><span>Yesterday</span><span>${fmt(item.rev_yesterday || 0)}</span></div>
      <div class="row rev-only"><span>This Month</span><span>${fmt(item.rev_month || 0)}</span></div>
      <div class="row rev-only"><span>This FY</span><span>${fmt(item.rev_fy || 0)}</span></div>
      <div class="row rev-only"><span>Previous FY</span><span>${fmt(item.rev_prev_fy || 0)}</span></div>`}
      <div class="row"><span>Final Qty</span><span>${item.final_qty || 0}</span></div>
      <div class="row"><span>Inv. Stock</span><span>${item.inv_stock}</span></div>
      <div class="row"><span>Inv (WIP)</span><span>${item.inv_wip}</span></div>
      <div class="row"><span>Blocked Qty</span><span>${item.blocked_qty || 0}</span></div>
      <div class="sg">
        <div class="sc"><div class="sl">1M</div><div class="sv ${sCls(s.m1)}">${s.m1}</div></div>
        <div class="sc"><div class="sl">3M</div><div class="sv ${sCls(s.m3)}">${s.m3}</div></div>
        <div class="sc"><div class="sl">6M</div><div class="sv ${sCls(s.m6)}">${s.m6}</div></div>
        <div class="sc"><div class="sl">1Y</div><div class="sv ${sCls(s.y1)}">${s.y1}</div></div>
      </div>
      <div class="card-actions">
        <button class="mini-btn" onclick="copySku('${String(item.sku).replace(/'/g, "\\\\'")}')">Copy SKU</button>
        <button class="mini-btn primary" onclick="openSkuDetails('${String(item.sku).replace(/'/g, "\\\\'")}')">Details</button>
      </div>
    </div>
  </div>`;
};

const __origApplyF = applyF;
applyF = function(){
  __origApplyF();
  renderProUI();
};

const __origApplyRO = applyRO;
applyRO = function(){
  __origApplyRO();
  renderProUI();
};

document.addEventListener('DOMContentLoaded', () => {
  const fs = document.getElementById('fSkuSearch');
  if (fs) fs.addEventListener('input', renderSkuChecklist);
  const rs = document.getElementById('rSkuSearch');
  if (rs) rs.addEventListener('input', renderRoSkuChecklist);
  const u = document.getElementById('lgUser'); if (u) u.focus();
  renderProHeader();
  showTab('home');
});


/* ===== AI STUDIO ===== */
let AI_HISTORY = [];
let AI_BUSY = false;
let AI_WELCOMED = false;
let AI_CTX_SKUS = [];

function aiMd(text){
  let t = escHtml(text || '');
  t = t.replace(/\*\*(.+?)\*\*/g, '<b>$1</b>');
  t = t.replace(/\*(.+?)\*/g, '<i>$1</i>');
  t = t.replace(/^[\-\u2022]\s?/gm, '• ');
  t = t.replace(/\n/g, '<br>');
  return t;
}

function aiScroll(){
  const c = document.getElementById('aiChat');
  if (c) c.scrollTop = c.scrollHeight;
}

function aiAppend(role, html){
  const c = document.getElementById('aiChat');
  if (!c) return null;
  const d = document.createElement('div');
  d.className = 'ai-msg ' + role;
  d.innerHTML = html;
  c.appendChild(d);
  aiScroll();
  return d;
}

let AI_LAST_RESULTS = [];

function aiAppendCards(items){
  const c = document.getElementById('aiChat');
  if (!c || !items || !items.length) return;
  AI_LAST_RESULTS = items;
  const bar = document.createElement('div');
  bar.className = 'ai-exportbar';
  bar.innerHTML = `<span>${items.length} SKU${items.length>1?'s':''}</span>
    <button class="ai-hbtn" onclick="aiExport('csv')">CSV</button>
    <button class="ai-hbtn" onclick="aiExport('excel')">EXCEL</button>`;
  c.appendChild(bar);
  const wrap = document.createElement('div');
  wrap.className = 'ai-cards';
  wrap.innerHTML = items.map(i => mkCard(i)).join('');
  c.appendChild(wrap);
  aiScroll();
}

function aiExport(fmtType){
  const items = AI_LAST_RESULTS || [];
  if (!items.length) return;
  const emp = LOGIN_ROLE === 'employee';
  const headers = ['SKU','Category','Plating','Dimensions','Status','MRP', ...(emp ? [] : ['Selling Price']),'Inv Stock','Inv WIP','Blocked Qty','Total Inv',
                   'Final Qty', ...(emp ? [] : ['Net Revenue']), 'Qty 7d','Qty 1M','Qty 3M','Qty 1Y',
                   ...(emp ? [] : ['Rev This Month','Rev This FY']), 'Forecast 30d','Last Dispatch','Image Link'];
  const data = items.map(i => [i.sku, i.taxon||'', i.plating||'', i.dimensions||'', i.status||'', i.mrp||0,
    ...(emp ? [] : [i.last_selling_price||0]),
    i.inv_stock||0, i.inv_wip||0, i.blocked_qty||0, i.total_inv||0, i.final_qty||0,
    ...(emp ? [] : [Math.round(i.total_net_revenue||0)]), i.qty_7d||0, i.qty_1m||0, i.qty_3m||0, i.qty_1y||0,
    ...(emp ? [] : [Math.round(i.rev_month||0), Math.round(i.rev_fy||0)]), i.forecast_30d||0,
    i.last_dispatch_date||'', i.image_url||'']);
  downloadTable(headers, data, 'AI_Studio_Results', fmtType);
}
window.aiExport = aiExport;

/* ===== SMART VISUAL SEARCH (Repeat Orders, CLIP offline) ===== */
let SMART_BUSY = false;
let SMART_POLL = null;

function smartProgressHtml(p){
  const done = p.done || 0, total = p.total || 0;
  const pct = total ? Math.round(done * 100 / total) : 0;
  const ok = p.ok || 0, fl = p.fail || 0;
  return `<b>Building visual index…</b> ${done}/${total} (${pct}%) — ${ok} downloaded, ${fl} failed
    <div class="smart-prog"><div class="smart-prog-fill" style="width:${pct}%"></div></div>
    <span style="font-size:11px;opacity:.6">One-time process. When finished, download clip_index.pkl and keep it with sku_finder.pkl for instant loading next session.</span>`;
}

async function smartBuildIndex(){
  const note = document.getElementById('smartNote');
  try{
    const r = await fetch('/api/smart-index', {method:'POST', headers:{'ngrok-skip-browser-warning':'true'}});
    const d = await r.json();
    if (d.status === 'ready'){ if (note) note.innerHTML = 'Index ready. Run your search.'; return; }
    if (note) { note.style.display='block'; note.innerHTML = smartProgressHtml(d); }
    if (SMART_POLL) clearInterval(SMART_POLL);
    SMART_POLL = setInterval(async () => {
      try{
        const s = await (await fetch('/api/smart-index-status', {headers:{'ngrok-skip-browser-warning':'true'}})).json();
        if (s.status === 'ready'){
          clearInterval(SMART_POLL); SMART_POLL = null;
          if (note) note.innerHTML = 'Visual index ready — searching…';
          smartSearch();
        } else if (s.status === 'error'){
          clearInterval(SMART_POLL); SMART_POLL = null;
          if (note) note.innerHTML = 'Index build failed: ' + escHtml(s.error || '');
        } else {
          if (note) note.innerHTML = smartProgressHtml(s);
        }
      } catch(e){}
    }, 3000);
  } catch(e){
    if (note) note.textContent = '⚠️ ' + e.message;
  }
}
window.smartBuildIndex = smartBuildIndex;

async function smartSearch(){
  if (SMART_BUSY) return;
  const q = (document.getElementById('smartQ')?.value || '').trim();
  if (!q) return;
  const note = document.getElementById('smartNote');
  const box  = document.getElementById('smartResults');
  const btn  = document.getElementById('smartBtn');
  SMART_BUSY = true;
  if (btn) { btn.disabled = true; btn.textContent = 'SEARCHING…'; }
  if (note) { note.style.display = 'block'; note.innerHTML = '<div class="spin" style="display:inline-block;vertical-align:middle"></div> Searching matches for "' + escHtml(q) + '"…'; }
  if (box) box.innerHTML = '';
  try{
    const r = await fetch('/api/smart-search', {
      method: 'POST',
      headers: {'Content-Type': 'application/json', 'ngrok-skip-browser-warning': 'true'},
      body: JSON.stringify({query: q})
    });
    const d = await r.json();
    if (d.error){
      if (note) note.textContent = '⚠️ ' + d.error;
    } else if (d.need_index){
      const res = d.results || [];
      if (box && res.length) box.innerHTML = res.map(i => mkCard(i)).join('');
      if (d.building){
        if (note) { note.style.display='block'; note.innerHTML = smartProgressHtml(d.progress || {}); }
        smartBuildIndex();
      } else if (note) {
        note.innerHTML = (res.length ? `${res.length} name matches found. ` : 'No name matches. ')
          + `To search inside product images, build the one-time visual index: `
          + `<button class="ai-hbtn design" onclick="smartBuildIndex()">BUILD VISUAL INDEX</button>`;
      }
    } else {
      const res = d.results || [];
      if (note) note.innerHTML = res.length
        ? `<b>${res.length}</b> matches — ${d.text_matches||0} by name, ${d.visual_matches||0} visual (badge = match strength)`
        : 'No matches found. Try another concept — lion, tiger, skull, anchor, cross, om.';
      if (box) box.innerHTML = res.map(i => mkCard(i, undefined, i.confidence)).join('');
    }
  } catch(e){
    if (note) note.textContent = '⚠️ ' + e.message;
  }
  SMART_BUSY = false;
  if (btn) { btn.disabled = false; btn.textContent = 'SEARCH'; }
}
window.smartSearch = smartSearch;

function smartClear(){
  const q = document.getElementById('smartQ'); if (q) q.value = '';
  const box = document.getElementById('smartResults'); if (box) box.innerHTML = '';
  const note = document.getElementById('smartNote'); if (note) note.style.display = 'none';
}
window.smartClear = smartClear;

/* ===== 3D tilt (KPIs + home cards only — light) ===== */
(function(){
  if (window.matchMedia && window.matchMedia('(pointer: coarse)').matches) return; // skip touch
  let raf = null;
  document.addEventListener('mousemove', (e) => {
    const el = e.target.closest && e.target.closest('.kpi, .home-card');
    if (!el) return;
    if (raf) cancelAnimationFrame(raf);
    raf = requestAnimationFrame(() => {
      const r = el.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width - 0.5;
      const py = (e.clientY - r.top) / r.height - 0.5;
      el.style.transform = `translateY(-4px) rotateX(${(-py*2.5).toFixed(2)}deg) rotateY(${(px*2.5).toFixed(2)}deg)`;
    });
  });
  document.addEventListener('mouseout', (e) => {
    const el = e.target.closest && e.target.closest('.kpi, .home-card');
    if (el && (!e.relatedTarget || !el.contains(e.relatedTarget))) el.style.transform = '';
  });
})();

function aiTyping(show){
  const c = document.getElementById('aiChat');
  if (!c) return;
  const ex = document.getElementById('aiTypingEl');
  if (ex) ex.remove();
  if (show){
    const d = document.createElement('div');
    d.id = 'aiTypingEl';
    d.className = 'ai-typing';
    d.innerHTML = '<span></span><span></span><span></span>';
    c.appendChild(d);
    aiScroll();
  }
}

function aiOnOpen(){
  if (AI_WELCOMED) return;
  AI_WELCOMED = true;
  const n = (master || []).length;
  aiAppend('bot', aiMd(
    'Welcome to **Cosa AI** — your business intelligence assistant.\n' +
    (n ? `Live data for **${n.toLocaleString('en-IN')} SKUs** is loaded. ` : '') +
    'Ask about *top sellers*, *stock*, *revenue*, *forecasts*, or any *SKU* — or use the shortcuts below.'
  ));
}

async function aiSend(preset){
  if (AI_BUSY) return;
  const inp = document.getElementById('aiInput');
  const msg = (preset !== undefined ? String(preset) : (inp ? inp.value : '')).trim();
  if (!msg) return;
  if (inp && preset === undefined) inp.value = '';

  aiAppend('user', escHtml(msg));
  AI_HISTORY.push({role: 'user', text: msg});

  AI_BUSY = true;
  const btn = document.getElementById('aiSendBtn');
  if (btn) btn.disabled = true;
  aiTyping(true);

  try{
    const r = await fetch('/api/ai-chat', {
      method: 'POST',
      headers: {'Content-Type': 'application/json', 'ngrok-skip-browser-warning': 'true'},
      body: JSON.stringify({message: msg, history: AI_HISTORY.slice(-10), context_skus: AI_CTX_SKUS, role: LOGIN_ROLE || 'admin'})
    });
    const d = await r.json();
    aiTyping(false);
    if (d.error){
      aiAppend('err', escHtml(d.error));
    } else {
      const eng = d.engine === 'gemini' ? 'Gemini AI' : (d.engine === 'local' ? 'Local engine' : escHtml(d.engine || ''));
      aiAppend('bot', aiMd(d.answer || '...') + `<span class="ai-engine">${eng}</span>`);
      AI_HISTORY.push({role: 'assistant', text: (d.answer || '').slice(0, 600)});
      if (d.context_skus) AI_CTX_SKUS = d.context_skus;
      if (d.skus && d.skus.length) aiAppendCards(d.skus);
      if (d.suggestions && d.suggestions.length){
        const c2 = document.getElementById('aiChat');
        if (c2){
          const sb = document.createElement('div');
          sb.className = 'ai-followups';
          sb.innerHTML = d.suggestions.map(s => `<button class="ai-chip" onclick="aiSend('${String(s).replace(/'/g,"\\'")}')">${escHtml(s)}</button>`).join('');
          c2.appendChild(sb);
          aiScroll();
        }
      }
    }
  } catch(e){
    aiTyping(false);
    aiAppend('err', 'Network error: ' + escHtml(e.message) + '. Please try again.');
  }
  AI_BUSY = false;
  if (btn) btn.disabled = false;
  if (inp) inp.focus();
}
window.aiSend = aiSend;

function aiClearChat(){
  AI_HISTORY = [];
  AI_CTX_SKUS = [];
  AI_WELCOMED = false;
  const c = document.getElementById('aiChat');
  if (c) c.innerHTML = '';
  aiOnOpen();
  const i = document.getElementById('aiInput');
  if (i) { i.value = ''; i.focus(); }
}
window.aiClearChat = aiClearChat;

function aiToggleDesign(forceOpen){
  const p = document.getElementById('aiDesignPanel');
  if (!p) return;
  const open = forceOpen === true ? true : p.style.display === 'none';
  p.style.display = open ? 'flex' : 'none';
  if (open) {
    const t = document.getElementById('aiDesignPrompt');
    if (t) t.focus();
  }
}
window.aiToggleDesign = aiToggleDesign;

async function aiDesign(){
  if (AI_BUSY) return;
  const pEl = document.getElementById('aiDesignPrompt');
  const rEl = document.getElementById('aiDesignRefs');
  const prompt = (pEl ? pEl.value : '').trim();
  const refs = (rEl ? rEl.value : '').trim();
  if (!prompt){ if (pEl) pEl.focus(); return; }

  aiAppend('user', '<b>Design request:</b> ' + escHtml(prompt) + (refs ? '<br><small>Refs: ' + escHtml(refs) + '</small>' : ''));
  AI_HISTORY.push({role: 'user', text: 'Design request: ' + prompt});

  AI_BUSY = true;
  const btn = document.getElementById('aiDesignBtn');
  const sbtn = document.getElementById('aiSendBtn');
  if (btn) { btn.disabled = true; btn.textContent = 'GENERATING…'; }
  if (sbtn) sbtn.disabled = true;
  aiTyping(true);

  try{
    const r = await fetch('/api/ai-design', {
      method: 'POST',
      headers: {'Content-Type': 'application/json', 'ngrok-skip-browser-warning': 'true'},
      body: JSON.stringify({prompt: prompt, ref_skus: refs})
    });
    const d = await r.json();
    aiTyping(false);
    if (d.error){
      aiAppend('err', escHtml(d.error));
    } else {
      const refsTxt = (d.refs_used && d.refs_used.length)
        ? `<span class="ai-engine">Inspiration: ${d.refs_used.map(escHtml).join(', ')} • ${escHtml(d.model || '')}</span>` : '';
      aiAppend('bot', aiMd(d.text || 'Your design is ready.') + refsTxt);
      AI_HISTORY.push({role: 'assistant', text: (d.text || 'design generated').slice(0, 400)});
      const c = document.getElementById('aiChat');
      if (c && d.image){
        const w = document.createElement('div');
        w.className = 'ai-genwrap';
        const fname = 'CosaNostraa_AI_Design_' + Date.now() + '.png';
        w.innerHTML = `<img class="ai-genimg" src="${d.image}" alt="AI generated design">` +
                      `<a class="ai-dl" href="${d.image}" download="${fname}">DOWNLOAD</a>`;
        c.appendChild(w);
        aiScroll();
      }
      if (pEl) pEl.value = '';
    }
  } catch(e){
    aiTyping(false);
    aiAppend('err', 'Network error: ' + escHtml(e.message));
  }
  AI_BUSY = false;
  if (btn) { btn.disabled = false; btn.textContent = 'GENERATE'; }
  if (sbtn) sbtn.disabled = false;
}
window.aiDesign = aiDesign;

/* ── Lightweight premium particle background (gold dust) ──
   Bahut halka: thode particles, 24fps cap, tab hidden par pause, aur
   chhoti screen / kam-core device par bilkul OFF (hang na ho). */
(function(){
  const cv = document.getElementById('pcanvas');
  if (!cv) return;
  // Mobile / chhoti screen / low-core device par particles OFF — pura smooth.
  const lowEnd = (window.innerWidth < 760)
    || (navigator.hardwareConcurrency && navigator.hardwareConcurrency <= 4)
    || (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  if (lowEnd){ cv.style.display='none'; return; }
  const ctx = cv.getContext('2d');
  let W=0,H=0,parts=[],raf=null,run=true;
  const COUNT = Math.min(28, Math.floor((window.innerWidth*window.innerHeight)/60000)); // bahut halka
  function resize(){ W = cv.width = window.innerWidth; H = cv.height = window.innerHeight; }
  function mk(){
    return {x:Math.random()*W, y:Math.random()*H, r:Math.random()*1.5+0.5,
            vy:-(Math.random()*0.22+0.05), vx:(Math.random()-0.5)*0.1,
            a:Math.random()*0.35+0.12};
  }
  function init(){ resize(); parts = Array.from({length:COUNT}, mk); }
  let last=0;
  function frame(ts){
    raf = requestAnimationFrame(frame);
    if (!run) return;
    if (ts-last < 42) return;   // ~24fps cap
    last = ts;
    ctx.clearRect(0,0,W,H);
    for (const p of parts){
      p.y += p.vy; p.x += p.vx;
      if (p.y < -5){ p.y = H+5; p.x = Math.random()*W; }
      if (p.x < -5) p.x = W+5; if (p.x > W+5) p.x = -5;
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, 6.283);
      ctx.fillStyle = 'rgba(184,150,12,'+p.a+')';
      ctx.fill();
    }
  }
  document.addEventListener('visibilitychange', ()=>{ run = !document.hidden; });
  let rt=null;
  window.addEventListener('resize', ()=>{ clearTimeout(rt); rt=setTimeout(init,200); });
  init();
  raf = requestAnimationFrame(frame);
})();

/* ── Nav subtle shadow on scroll ── */
(function(){
  const bar = document.getElementById('appBar');
  if (!bar) return;
  let scrolled = null;
  window.addEventListener('scroll', ()=>{
    const s = window.scrollY > 40;
    if (s === scrolled) return;   // sirf state badalne par update (har scroll par nahi)
    scrolled = s;
    bar.style.boxShadow = s ? '0 10px 30px rgba(26,22,16,.10)' : '0 8px 26px rgba(26,22,16,.05)';
  }, {passive:true});
})();

</script>

</body></html>"""

# ── Flask ────────────────────────────────────────────────────
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "cosa-nostraa-" + base64.b64encode(os.urandom(18)).decode())
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
# Session ab PERMANENT nahi — browser band hote hi / refresh par dobara login.
# (Frontend bhi har load par login gate dikhata hai.)
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(hours=8)

# ── server-side users (production: env vars se override karo) ──
USERS = {
    os.environ.get("ADMIN_USER", "Mayuresh"):
        (os.environ.get("ADMIN_PASS", "Cosanostraa@123"), "admin"),
    os.environ.get("EMP_USER", "cosanostraa2026"):
        (os.environ.get("EMP_PASS", "cn2026"), "employee"),
}

_PUBLIC_API = ("/api/login", "/api/me", "/api/logout", "/api/warmup-status")

@app.before_request
def _auth_guard():
    p = request.path or ""
    if p.startswith("/api/") and p not in _PUBLIC_API:
        if not session.get("role"):
            return jsonify({"error": "auth required"}), 401

@app.route("/api/login", methods=["POST"])
def api_login():
    d = request.get_json(silent=True) or {}
    u = str(d.get("username") or "").strip()
    pw = str(d.get("password") or "")
    rec = USERS.get(u)
    if rec and rec[0] == pw:
        session.permanent = False   # browser-session cookie (refresh par dobara login)
        session["role"] = rec[1]
        session["user"] = u
        return jsonify({"ok": True, "role": rec[1]})
    return jsonify({"ok": False, "error": "Invalid username or password."}), 401

@app.route("/api/me")
def api_me():
    return jsonify({"role": session.get("role"), "user": session.get("user")})

@app.route("/api/logout", methods=["POST"])
def api_logout():
    session.clear()
    return jsonify({"ok": True})

@app.after_request
def add_headers(resp):
    resp.headers['ngrok-skip-browser-warning'] = 'true'
    resp.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    resp.headers['Pragma'] = 'no-cache'
    resp.headers['Expires'] = '0'
    try:
        accepts = request.headers.get('Accept-Encoding', '')
        if ('gzip' in accepts.lower()
                and resp.content_length is not None and resp.content_length > 1024
                and 'Content-Encoding' not in resp.headers
                and resp.status_code == 200
                and resp.direct_passthrough is False):
            import gzip as _gzip
            data = resp.get_data()
            comp = _gzip.compress(data, 6)
            if len(comp) < len(data):
                resp.set_data(comp)
                resp.headers['Content-Encoding'] = 'gzip'
                resp.headers['Content-Length'] = str(len(comp))
                resp.headers['Vary'] = 'Accept-Encoding'
    except Exception:
        pass
    return resp

@app.route("/")
def home():
    return render_template_string(HTML)

REV_ITEM_KEYS = ("total_net_revenue", "rev_yesterday", "rev_month", "rev_fy", "rev_prev_fy",
                 "avg_selling_price", "last_selling_price", "return_amount")

def _employee_view(comp, period_kpis):
    """Employee role: revenue + selling-price data server se nikalta hi nahi.
    MEMORY: copy transient hai — gzip response cache banne ke baad free ho jati hai
    (512MB free tier par permanent duplicate OOM kara raha tha)."""
    safe_comp = []
    for i in comp:
        d = {k: (0 if k in REV_ITEM_KEYS else v) for k, v in i.items() if k != "sales_entries"}
        d["sales_entries"] = [{**e, "rev": 0, "sp": 0, "ret_amt": 0} for e in i.get("sales_entries", [])]
        safe_comp.append(d)
    safe_kpis = {k: (0 if k in ("total", "yesterday", "this_month", "this_fy", "prev_fy",
                                "last_month", "last_year_month", "mom_yoy_pct") else v)
                 for k, v in (period_kpis or {}).items()}
    return safe_comp, safe_kpis

def _build_role_gz(role, force=False):
    """Role ke liye gzipped /api/data response banao (ya cache se lo).
    Background refresher + live requests dono yahi use karte hain."""
    comp, tx, ty, cu, pl, sk, fys, current_fy, previous_fy, today, yesterday, current_month, grand_rev, grand_qty, period_kpis = get_data(force)
    key = (role, CACHE["ts"])
    gz = _RESP_CACHE.get(key)
    if gz is not None:
        return gz
    if role == "employee":
        comp, period_kpis = _employee_view(comp, period_kpis)
        grand_rev = 0
    payload = {
        "inventory":     comp,
        "taxons":        tx,
        "types":         ty,
        "customers":     cu,
        "platings":      pl,
        "skus":          sk,
        "fys":           fys,
        "current_fy":    current_fy,
        "previous_fy":   previous_fy,
        "today":         today,
        "yesterday":     yesterday,
        "current_month": current_month,
        "grand_net_revenue": grand_rev,
        "grand_final_qty":   grand_qty,
        "period_kpis":   period_kpis,
    }
    with _RESP_LOCK:                      # do builders ek saath na chalein (RAM spike)
        gz = _RESP_CACHE.get(key)
        if gz is None:
            raw = json.dumps(payload, default=str).encode("utf-8")
            gz = _gzip_mod.compress(raw, 2)
            del raw
            for _k in [k for k in _RESP_CACHE if k[1] != CACHE["ts"]]:
                _RESP_CACHE.pop(_k, None)      # purane snapshots ke gz turant hatao
            _RESP_CACHE[key] = gz
    if role == "employee":
        del comp
    payload = None
    _gc.collect()
    _malloc_trim()
    return gz

@app.route("/api/data")
def api_data():
    force = request.args.get("force","false").lower() == "true"
    role  = session.get("role") or request.args.get("role", "admin")
    # Agar data abhi warm ho raha hai (pehli baar / refresh), to BLOCK mat karo —
    # 202 "warming" do taaki frontend warmup-status poll kare, reload-loop na bane.
    if CACHE.get("data") is None:
        return jsonify({"warming": True, "stage": _WARMUP.get("stage"),
                        "detail": _WARMUP.get("detail"),
                        "done": _WARMUP.get("done"), "total": _WARMUP.get("total")}), 202
    gz = _build_role_gz(role, force=force)
    if "gzip" in (request.headers.get("Accept-Encoding") or ""):
        resp = app.response_class(gz, mimetype="application/json")
        resp.headers["Content-Encoding"] = "gzip"
        resp.headers["Vary"] = "Accept-Encoding"
        return resp
    return app.response_class(_gzip_mod.decompress(gz), mimetype="application/json")

@app.route("/api/warmup-status")
def api_warmup_status():
    return jsonify({**_WARMUP, "ready": bool(CACHE.get("data"))})

# ════════════════════════════════════════════════════════════════
#  🎯 TARGET vs ACTUAL  (admin only)
#  Target sheet: Date, Stake Holder, Channel Type, Qty Target, SP Target
#  Actual: COSSA se (month + stakeholder[customer] + channel[type] wise)
# ════════════════════════════════════════════════════════════════
_TARGET_CACHE = {"rows": None, "ts": 0}

def _fetch_target_rows():
    """Target sheet ko parse karke normalized rows deta hai (cache 10 min)."""
    if _TARGET_CACHE["rows"] is not None and (time.time() - _TARGET_CACHE["ts"] < 600):
        return _TARGET_CACHE["rows"]
    df = _fetch_csv_fresh(TARGET_URL)
    cols = list(df.columns)
    def _at(i): return cols[i] if len(cols) > i else None
    C_D  = _at(0) or find_col(df.columns, "Date","month")
    C_SH = _at(1) or find_col(df.columns, "Stake Holder","stakeholder","stake","name","person")
    C_CH = _at(2) or find_col(df.columns, "Channel Type","channel","type")
    C_QT = _at(3) or find_col(df.columns, "Qty Target","qty target","quantity target","qty")
    C_ST = _at(4) or find_col(df.columns, "SP Target","sp target","revenue target","value target","sp")
    out = []
    for _, r in df.iterrows():
        dt = parse_date_any(r.get(C_D, "")) if C_D else None
        if dt is None:
            continue
        mk = dt.strftime("%Y-%m")
        sh = clean(r.get(C_SH, "")) if C_SH else ""
        ch = clean(r.get(C_CH, "")) if C_CH else ""
        qt = to_num(r.get(C_QT, 0)) if C_QT else 0.0
        st = to_num(r.get(C_ST, 0)) if C_ST else 0.0
        if not sh and not ch:
            continue
        out.append({"month": mk, "month_label": dt.strftime("%b %Y"),
                    "stakeholder": sh or "—", "channel": ch or "—",
                    "qty_target": qt, "sp_target": st})
    _TARGET_CACHE["rows"] = out
    _TARGET_CACHE["ts"] = time.time()
    return out

# ════════════════════════════════════════════════════════════════
#  🏭 PRODUCTION (PPC-WIP)  — admin only
#  Columns (position-based, jaisa user ne bataya):
#   A=Date, B=Order No, E=SKU, G=Channel, I=Order Qty,
#   J=Recv Qty, K=Balance Qty, L=Delivery Date, M=Receiving Date
#  SKU photo All Product (inv) sheet se.
# ════════════════════════════════════════════════════════════════
_PROD_CACHE = {"rows": None, "ts": 0}

def _build_production(channel_filter="", sku_query="", od1="", od2="", dd1="", dd2="", taxon_filter="", type_filter="", balance_only="", order_query=""):
    # SKU -> image + taxon map (compiled data se, jisme inv image+taxon already hai)
    img_map = {}; tax_map = {}
    try:
        comp = get_data()[0]
        for it in comp:
            sk = str(it.get("sku", "")).strip().upper()
            if not sk:
                continue
            if it.get("image_url"):
                img_map[sk] = it["image_url"]
            if it.get("taxon"):
                tax_map[sk] = it["taxon"]
    except Exception:
        pass

    # Production sheet fetch (10 min cache)
    if _PROD_CACHE["rows"] is not None and (time.time() - _PROD_CACHE["ts"] < 600):
        rows_all = _PROD_CACHE["rows"]
    else:
        df = _fetch_csv_fresh(PRODUCTION_URL)
        cols = list(df.columns)
        def _at(i): return cols[i] if len(cols) > i else None
        C_DATE = _at(0)   # A  Date (order date)
        C_ORD  = _at(1)   # B  Order No.
        C_TYPE = _at(5)   # F  Order Type
        C_CHAN = _at(6)   # G  Channel
        C_SKU  = _at(7)   # H  SKU No.   (E/Image link nahi)
        C_OQTY = _at(8)   # I  Order Qty
        C_RQTY = _at(9)   # J  Recv Qty
        C_BQTY = _at(10)  # K  Balance Qty
        C_DELV = _at(11)  # L  Delivery Date
        C_RECV = _at(12)  # M  Receiving Date
        rows_all = []
        for _, r in df.iterrows():
            sku = clean(r.get(C_SKU, "")).upper() if C_SKU else ""
            order_no = clean(r.get(C_ORD, "")) if C_ORD else ""
            if not sku and not order_no:
                continue
            dt = parse_date_any(r.get(C_DATE, "")) if C_DATE else None
            dv = parse_date_any(r.get(C_DELV, "")) if C_DELV else None
            rv = parse_date_any(r.get(C_RECV, "")) if C_RECV else None
            rows_all.append({
                "date":      dt.strftime("%Y-%m-%d") if dt else "",
                "date_disp": dt.strftime("%d-%b-%Y") if dt else "",
                "order_no":  order_no,
                "sku":       sku,
                "order_type": clean(r.get(C_TYPE, "")) if C_TYPE else "",
                "channel":   clean(r.get(C_CHAN, "")) if C_CHAN else "",
                "order_qty": to_num(r.get(C_OQTY, 0)) if C_OQTY else 0.0,
                "recv_qty":  to_num(r.get(C_RQTY, 0)) if C_RQTY else 0.0,
                "bal_qty":   to_num(r.get(C_BQTY, 0)) if C_BQTY else 0.0,
                "delivery_date": dv.strftime("%d-%b-%Y") if dv else "",
                "delivery_iso":  dv.strftime("%Y-%m-%d") if dv else "",
                "receiving_date": rv.strftime("%d-%b-%Y") if rv else "",
            })
        _PROD_CACHE["rows"] = rows_all
        _PROD_CACHE["ts"] = time.time()

    # Taxon har row me daal do (inv map se)
    for r in rows_all:
        r["taxon"] = tax_map.get(r["sku"], "")

    # Filter dropdown options
    channels = sorted({r["channel"] for r in rows_all if r["channel"]})
    types    = sorted({r["order_type"] for r in rows_all if r["order_type"]})
    taxons   = sorted({r["taxon"] for r in rows_all if r["taxon"]})

    # SKU -> us SKU ke saare order numbers (jis-jis order me hai)
    sku_orders = {}
    for r in rows_all:
        if r["sku"] and r["order_no"]:
            sku_orders.setdefault(r["sku"], [])
            if r["order_no"] not in sku_orders[r["sku"]]:
                sku_orders[r["sku"]].append(r["order_no"])

    # SKU -> uss SKU ki saare orders ki Balance Qty jodke total (sab orders mil ke)
    sku_total_balance = {}
    for r in rows_all:
        if r["sku"]:
            sku_total_balance[r["sku"]] = sku_total_balance.get(r["sku"], 0) + (r["bal_qty"] or 0)

    # Filters apply
    cf = channel_filter.strip().lower()
    sq = sku_query.strip().lower()
    oq = order_query.strip().lower()
    txf = taxon_filter.strip().lower()
    tyf = type_filter.strip().lower()
    bo = (balance_only or "").strip().lower()   # "yes" = sirf balance qty waale, "no" = balance 0 waale
    rows = []
    for r in rows_all:
        if cf and r["channel"].strip().lower() != cf:
            continue
        if tyf and r["order_type"].strip().lower() != tyf:
            continue
        if txf and r["taxon"].strip().lower() != txf:
            continue
        if bo == "yes" and (r["bal_qty"] or 0) <= 0:
            continue
        if bo == "no" and (r["bal_qty"] or 0) > 0:
            continue
        if sq and sq not in r["sku"].lower():
            continue
        if oq and oq not in r["order_no"].lower():
            continue
        # Order date range
        if od1 and (not r["date"] or r["date"] < od1):
            continue
        if od2 and (not r["date"] or r["date"] > od2):
            continue
        # Delivery date range
        if dd1 and (not r["delivery_iso"] or r["delivery_iso"] < dd1):
            continue
        if dd2 and (not r["delivery_iso"] or r["delivery_iso"] > dd2):
            continue
        rr = dict(r)
        rr["image_url"] = img_map.get(r["sku"], "")
        rr["all_orders"] = sku_orders.get(r["sku"], [])
        rr["sku_total_balance"] = sku_total_balance.get(r["sku"], 0)
        rows.append(rr)

    # KPIs
    pending = sum(1 for r in rows if (r["bal_qty"] or 0) > 0)
    uniq_orders = len({r["order_no"] for r in rows if r["order_no"]})
    uniq_skus = len({r["sku"] for r in rows if r["sku"]})
    return {
        "rows": rows[:1000],
        "count": len(rows),
        "channels": channels, "types": types, "taxons": taxons,
        "total_order_qty": int(round(sum(r["order_qty"] for r in rows))),
        "total_recv_qty":  int(round(sum(r["recv_qty"] for r in rows))),
        "total_bal_qty":   int(round(sum(r["bal_qty"] for r in rows))),
        "pending_rows": pending,
        "unique_orders": uniq_orders,
        "unique_skus": uniq_skus,
    }

def _build_target_report(month_filter="", stake_filter="", channel_filter=""):
    """Target vs Actual + Achievement Forecast + Stakeholder Leaderboard.
    Default: present month. Stake Holder ↔ COSSA Customer, Channel ↔ COSSA Type."""
    targets = _fetch_target_rows()
    data = get_data()
    comp = data[0]
    today = now_ist()
    cur_month = today.strftime("%Y-%m")

    # months available
    months_set = set(t["month"] for t in targets)
    stakes_set = set(t["stakeholder"] for t in targets)
    channels_set = set(t["channel"] for t in targets if t.get("channel"))

    # Default month = present month (agar available ho), warna latest.
    if not month_filter:
        month_filter = cur_month if cur_month in months_set else (sorted(months_set, reverse=True)[0] if months_set else cur_month)

    # Forecast factor: mahine me kitne din beet gaye (pace projection).
    import calendar
    y, mo = int(month_filter[:4]), int(month_filter[5:7])
    days_in_month = calendar.monthrange(y, mo)[1]
    if month_filter == cur_month:
        day_elapsed = today.day
    elif month_filter < cur_month:
        day_elapsed = days_in_month     # past month — pura ho chuka
    else:
        day_elapsed = 0                 # future month
    pace = (days_in_month / day_elapsed) if day_elapsed > 0 else 0.0

    # Actual ko (month, channel/type) par aggregate karo.
    # Target ka "Channel Type" (SOR, Website, Purchase…) = COSSA ka "Type".
    # Stake Holder sirf us channel ka naam/owner hai (e.g. Sarthak → SOR).
    act = {}
    for it in comp:
        for e in it.get("sales_entries", []):
            d = e.get("date")
            if not d or d == "N/A":
                continue
            mk = d[:7]
            typ = (e.get("type") or "").strip().lower()
            k = (mk, typ)
            slot = act.setdefault(k, {"rev": 0.0, "qty": 0.0})
            slot["rev"] += float(e.get("rev") or 0)
            slot["qty"] += float(e.get("qty") or 0)

    rows = []
    lb = {}   # stakeholder -> aggregated
    for t in targets:
        mk = t["month"]
        if mk != month_filter:
            continue
        if stake_filter and t["stakeholder"].strip().lower() != stake_filter.strip().lower():
            continue
        if channel_filter and (t.get("channel") or "").strip().lower() != channel_filter.strip().lower():
            continue
        a = act.get((mk, t["channel"].strip().lower()), {"rev": 0.0, "qty": 0.0})
        actual_rev = a["rev"]; actual_qty = a["qty"]
        sp_short  = t["sp_target"] - actual_rev
        qty_short = t["qty_target"] - actual_qty
        pct = round((actual_rev / t["sp_target"] * 100), 1) if t["sp_target"] else 0.0
        # Forecast: current pace se mahine ke end tak projected revenue + %.
        proj_rev = actual_rev * pace if pace else actual_rev
        proj_pct = round((proj_rev / t["sp_target"] * 100), 1) if t["sp_target"] else 0.0
        rows.append({
            "month": mk, "month_label": t["month_label"],
            "stakeholder": t["stakeholder"], "channel": t["channel"],
            "qty_target": t["qty_target"], "qty_actual": actual_qty, "qty_short": qty_short,
            "sp_target": t["sp_target"], "sp_actual": actual_rev, "sp_short": sp_short,
            "pct_achieved": pct, "proj_rev": proj_rev, "proj_pct": proj_pct,
        })
        # leaderboard aggregate (per stakeholder, all channels)
        L = lb.setdefault(t["stakeholder"], {"stakeholder": t["stakeholder"], "channels": set(),
              "sp_target":0.0,"sp_actual":0.0,"qty_target":0.0,"qty_actual":0.0,"proj_rev":0.0})
        if t.get("channel"):
            L["channels"].add(t["channel"])
        L["sp_target"] += t["sp_target"]; L["sp_actual"] += actual_rev
        L["qty_target"] += t["qty_target"]; L["qty_actual"] += actual_qty
        L["proj_rev"] += proj_rev

    # Totals
    tot = {"qty_target":0.0,"qty_actual":0.0,"qty_short":0.0,
           "sp_target":0.0,"sp_actual":0.0,"sp_short":0.0,"proj_rev":0.0}
    for r in rows:
        for k in ("qty_target","qty_actual","qty_short","sp_target","sp_actual","sp_short","proj_rev"):
            tot[k] += r[k]
    tot["pct_achieved"] = round((tot["sp_actual"]/tot["sp_target"]*100),1) if tot["sp_target"] else 0.0
    tot["proj_pct"] = round((tot["proj_rev"]/tot["sp_target"]*100),1) if tot["sp_target"] else 0.0

    # Leaderboard finalize + rank (by % achieved)
    leaderboard = []
    for L in lb.values():
        L["pct_achieved"] = round((L["sp_actual"]/L["sp_target"]*100),1) if L["sp_target"] else 0.0
        L["proj_pct"] = round((L["proj_rev"]/L["sp_target"]*100),1) if L["sp_target"] else 0.0
        L["sp_short"] = L["sp_target"] - L["sp_actual"]
        L["channel"] = ", ".join(sorted(L.pop("channels"))) if L.get("channels") else "—"
        leaderboard.append(L)
    leaderboard.sort(key=lambda x: x["pct_achieved"], reverse=True)
    for i, L in enumerate(leaderboard): L["rank"] = i + 1

    return {
        "rows": rows, "totals": tot, "leaderboard": leaderboard,
        "month_selected": month_filter,
        "month_label": (rows[0]["month_label"] if rows else month_filter),
        "days_in_month": days_in_month, "day_elapsed": day_elapsed,
        "is_current_month": (month_filter == cur_month),
        "months": sorted(months_set, reverse=True),
        "stakeholders": sorted(stakes_set),
        "channels": sorted(channels_set),
    }

@app.route("/api/target")
def api_target():
    if session.get("role") not in ("admin", "employee"):
        return jsonify({"error": "login required"}), 401
    mf = request.args.get("month", "").strip()
    sf = request.args.get("stake", "").strip()
    chf = request.args.get("channel", "").strip()
    try:
        rep = _build_target_report(mf, sf, chf)
        return jsonify(rep)
    except Exception as e:
        return jsonify({"error": f"target build failed: {e}"}), 500

# ════════════════════════════════════════════════════════════════
#  💸 DISCOUNT LEAKAGE REPORT  (admin only)
#  MRP vs actual Selling Price ka gap. Jaha qty zyada × discount zyada,
#  wahan sabse zyada "leakage" (lost value).
# ════════════════════════════════════════════════════════════════
def _build_discount_leakage(min_disc=0.0, sort_key="leakage"):
    data = get_data()
    comp = data[0]
    rows = []
    tot_leak = 0.0
    tot_units = 0.0
    for it in comp:
        mrp = float(it.get("mrp") or 0)
        sp  = float(it.get("last_selling_price") or 0) or float(it.get("avg_selling_price") or 0)
        qty = float(it.get("final_qty") or 0)
        if mrp <= 0 or sp <= 0 or qty <= 0:
            continue
        if sp >= mrp:        # koi discount nahi (ya MRP se upar) → skip
            continue
        disc_pct = round((mrp - sp) / mrp * 100, 1)
        if disc_pct < min_disc:
            continue
        per_unit_gap = mrp - sp
        leakage = per_unit_gap * qty          # total value "lost" vs MRP
        tot_leak += leakage
        tot_units += qty
        rows.append({
            "sku": it.get("sku"), "image_url": it.get("image_url", ""),
            "taxon": it.get("taxon", ""), "plating": it.get("plating", ""),
            "mrp": mrp, "avg_sp": round(float(it.get("avg_selling_price") or 0), 2),
            "last_sp": round(sp, 2), "disc_pct": disc_pct,
            "per_unit_gap": round(per_unit_gap, 2), "qty": int(round(qty)),
            "leakage": round(leakage, 2),
            "net_revenue": float(it.get("total_net_revenue") or 0),
        })
    key = {"leakage":"leakage","discount":"disc_pct","qty":"qty","revenue":"net_revenue"}.get(sort_key, "leakage")
    rows.sort(key=lambda x: x.get(key, 0), reverse=True)
    return {
        "rows": rows[:500],
        "total_leakage": round(tot_leak, 2),
        "total_units": int(round(tot_units)),
        "count": len(rows),
    }

@app.route("/api/discount-leakage")
def api_discount_leakage():
    if session.get("role") != "admin":
        return jsonify({"error": "admin only"}), 403
    try:
        md = float(request.args.get("min", "0") or 0)
    except Exception:
        md = 0.0
    sk = request.args.get("sort", "leakage").strip()
    try:
        return jsonify(_build_discount_leakage(md, sk))
    except Exception as e:
        return jsonify({"error": f"discount leakage build failed: {e}"}), 500

@app.route("/api/production")
def api_production():
    if session.get("role") not in ("admin", "employee"):
        return jsonify({"error": "login required"}), 401
    cf = request.args.get("channel", "").strip()
    sq = request.args.get("sku", "").strip()
    oq = request.args.get("order_no", "").strip()
    od1 = request.args.get("od1", "").strip()
    od2 = request.args.get("od2", "").strip()
    dd1 = request.args.get("dd1", "").strip()
    dd2 = request.args.get("dd2", "").strip()
    txf = request.args.get("taxon", "").strip()
    tyf = request.args.get("type", "").strip()
    bo  = request.args.get("balance", "").strip()
    try:
        return jsonify(_build_production(cf, sq, od1, od2, dd1, dd2, txf, tyf, bo, oq))
    except Exception as e:
        return jsonify({"error": f"production build failed: {e}"}), 500

# ════════════════════════════════════════════════════════════════
#  💰 SKU COSTS (Profit Margin tab) — admin only
#  All Product sheet: column N (index 13)=MRP, column M (index 12)=Cost.
# ════════════════════════════════════════════════════════════════
_COSTS_CACHE = {"rows": None, "ts": 0}

def _build_sku_costs():
    if _COSTS_CACHE["rows"] is not None and (time.time() - _COSTS_CACHE["ts"] < 600):
        return _COSTS_CACHE["rows"]

    # ── Seedha compiled data se — wahi column detection jo main data me hoti hai ──
    # MRP aur Cost dono wahan se lo (I_COST ab compiled items me hai).
    out = []
    seen = set()
    try:
        comp = get_data()[0]
        for it in comp:
            sk = str(it.get("sku", "")).strip()
            if not sk:
                continue
            ku = sk.upper()
            if ku in seen:
                continue
            seen.add(ku)
            mrp_val  = float(it.get("mrp")  or 0)
            cost_val = float(it.get("cost") or 0)
            # agar compiled me cost nahi mila (purana cache) to sheet se try karo
            out.append({
                "sku":         sk,
                "image_url":   it.get("image_url", "") or "",
                "mrp":         mrp_val,
                "cost":        cost_val,
                "final_qty":   int(it.get("final_qty") or 0),
                "net_revenue": float(it.get("total_net_revenue") or 0),
            })
    except Exception:
        pass

    # agar compiled me kuch SKUs ka cost 0 aa raha ho (purana cache), sheet se patch karo
    zero_cost_skus = {r["sku"].upper() for r in out if r["cost"] == 0}
    if zero_cost_skus:
        try:
            df = _fetch_csv_fresh(INV_URL)
            cols = list(df.columns)
            def _at(i): return cols[i] if len(cols) > i else None
            C_SKU  = _at(0)
            C_COST = find_col(df.columns, "Cost", "cost", "product cost", "hi cost", "item cost") or _at(12)
            C_MRP  = find_col(df.columns, "MRP", "mrp", "m.r.p") or _at(13)
            C_IMG2 = find_col(df.columns, "Image Link", "imagelink", "image", "img") or _at(1)
            patch_cost = {}; patch_mrp = {}; patch_img = {}
            for _, r in df.iterrows():
                sku = clean(r.get(C_SKU, "")) if C_SKU else ""
                if not sku:
                    continue
                ku = sku.strip().upper()
                if ku not in patch_cost:
                    patch_cost[ku] = to_num(r.get(C_COST, 0)) if C_COST else 0
                    patch_mrp[ku]  = to_num(r.get(C_MRP,  0)) if C_MRP  else 0
                    patch_img[ku]  = clean(r.get(C_IMG2, "")) if C_IMG2 else ""
            # patch existing rows
            for row in out:
                ku = row["sku"].upper()
                if ku in zero_cost_skus:
                    if patch_cost.get(ku, 0) > 0:
                        row["cost"] = patch_cost[ku]
                    if row["mrp"] == 0 and patch_mrp.get(ku, 0) > 0:
                        row["mrp"] = patch_mrp[ku]
                    if not row["image_url"] and patch_img.get(ku):
                        row["image_url"] = patch_img[ku]
            # add sheet-only SKUs (not in COSSA)
            for _, r in df.iterrows():
                sku = clean(r.get(C_SKU, "")) if C_SKU else ""
                if not sku:
                    continue
                ku = sku.strip().upper()
                if ku not in seen:
                    seen.add(ku)
                    out.append({
                        "sku":         sku,
                        "image_url":   clean(r.get(C_IMG2, "")) if C_IMG2 else "",
                        "mrp":         to_num(r.get(C_MRP,  0)) if C_MRP  else 0,
                        "cost":        to_num(r.get(C_COST, 0)) if C_COST else 0,
                        "final_qty":   0,
                        "net_revenue": 0,
                    })
        except Exception:
            pass

    _COSTS_CACHE["rows"] = out
    _COSTS_CACHE["ts"]   = time.time()
    return out

@app.route("/api/sku-costs")
def api_sku_costs():
    if session.get("role") != "admin":
        return jsonify({"error": "admin only"}), 403
    try:
        # force=true → cache saaf karo aur fresh data lo
        if request.args.get("force", "false").lower() == "true":
            _COSTS_CACHE["rows"] = None
        return jsonify({"rows": _build_sku_costs()})
    except Exception as e:
        return jsonify({"error": f"sku costs failed: {e}"}), 500

# ════════════════════════════════════════════════════════════════
#  ⚠️ AT-RISK CUSTOMERS — pehle regular the, ab 60+ din se nahi aaye
# ════════════════════════════════════════════════════════════════
_RISK_CACHE = {"data": None, "ts": 0}

def _build_at_risk(gap_days=60, min_orders=2):
    if _RISK_CACHE["data"] is not None and (time.time() - _RISK_CACHE["ts"] < 600):
        return _RISK_CACHE["data"]
    comp = get_data()[0]
    today = now_ist().date()
    # customer -> {dates:set, qty, rev, type}
    cust = {}
    for it in comp:
        for e in it.get("sales_entries", []):
            name = (e.get("cust") or "").strip()
            if not name or name.lower() == "website":
                continue
            d = e.get("date")
            if not d or d == "N/A":
                continue
            c = cust.setdefault(name, {"dates": set(), "qty": 0.0, "rev": 0.0, "type": (e.get("type") or "")})
            c["dates"].add(d)
            c["qty"] += float(e.get("qty") or 0)
            c["rev"] += float(e.get("rev") or 0)

    def _d(iso):
        try: return date(int(iso[0:4]), int(iso[5:7]), int(iso[8:10]))
        except Exception: return None

    rows = []
    for name, c in cust.items():
        dts = sorted([x for x in (_d(s) for s in c["dates"]) if x])
        if len(dts) < min_orders:
            continue          # "regular" the tabhi count — kam se kam min_orders
        last = dts[-1]
        gap = (today - last).days
        if gap < gap_days:
            continue          # abhi bhi active
        # average gap between orders (regularity)
        if len(dts) >= 2:
            diffs = [(dts[i] - dts[i-1]).days for i in range(1, len(dts))]
            avg_gap = round(sum(diffs) / len(diffs))
        else:
            avg_gap = 0
        rows.append({
            "customer": name,
            "orders": len(dts),
            "last_order": last.strftime("%d-%b-%Y"),
            "days_since": gap,
            "avg_gap_days": avg_gap,
            "total_qty": int(round(c["qty"])),
            "total_rev": round(c["rev"], 2),
            "type": c["type"],
            "first_order": dts[0].strftime("%d-%b-%Y"),
        })
    # sabse zyada value waale + zyada overdue upar
    rows.sort(key=lambda x: (x["total_rev"], x["days_since"]), reverse=True)
    data = {
        "rows": rows,
        "count": len(rows),
        "total_value_at_risk": round(sum(r["total_rev"] for r in rows), 2),
        "gap_days": gap_days,
    }
    _RISK_CACHE["data"] = data
    _RISK_CACHE["ts"] = time.time()
    cust.clear()
    _gc.collect(); _malloc_trim()
    return data

@app.route("/api/at-risk")
def api_at_risk():
    if session.get("role") not in ("admin", "employee"):
        return jsonify({"error": "login required"}), 401
    try:
        gap = int(request.args.get("gap", "60") or 60)
    except Exception:
        gap = 60
    try:
        return jsonify(_build_at_risk(gap))
    except Exception as e:
        return jsonify({"error": f"at-risk failed: {e}"}), 500

# ════════════════════════════════════════════════════════════════
#  💰 PAYMENTS — Ledger + Payment Terms se Due / Overdue (FIFO aging)
# ════════════════════════════════════════════════════════════════
PAY_LEDGER_URL = os.environ.get("PAY_LEDGER_URL",
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vSsgrfjsrSCqWYZaiyHYKHcyQnca-gsA2asz01Fjsb28J1y04CyLZDpVazFcdnre5zO95VOgQBOugXQ/pub?gid=745089354&single=true&output=csv")
PAY_TERMS_URL = os.environ.get("PAY_TERMS_URL",
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vSsgrfjsrSCqWYZaiyHYKHcyQnca-gsA2asz01Fjsb28J1y04CyLZDpVazFcdnre5zO95VOgQBOugXQ/pub?gid=1240216036&single=true&output=csv")
_PAY_CACHE = {"data": None, "ts": 0}

def _norm_name(s):
    return re.sub(r"\s+", " ", str(s or "").strip()).upper()

def _build_payments():
    if _PAY_CACHE["data"] is not None and (time.time() - _PAY_CACHE["ts"] < 600):
        return _PAY_CACHE["data"]

    # ---- Payment terms (Customer -> days, tag) ----
    term_map = {}; tag_map = {}
    try:
        terms_df = _fetch_csv_fresh(PAY_TERMS_URL)
        tcols = list(terms_df.columns)
        T_CUST = find_col(terms_df.columns, "Customer Name", "customer", "name") or (tcols[0] if tcols else None)
        T_TERM = find_col(terms_df.columns, "Payment Term", "payment terms", "term", "credit days", "days")
        T_TAG  = find_col(terms_df.columns, "Tag", "type", "tag")
        tc = terms_df[T_CUST].tolist() if T_CUST else []
        tt = terms_df[T_TERM].tolist() if T_TERM else [0]*len(tc)
        tg = terms_df[T_TAG].tolist()  if T_TAG  else [""]*len(tc)
        for i in range(len(tc)):
            nm = _norm_name(tc[i])
            if not nm:
                continue
            term_map[nm] = to_int(tt[i])
            tag_map[nm]  = clean(tg[i])
    except Exception as e:
        print("payments terms fetch error:", str(e)[:200])

    # ---- Ledger ----
    led_df = _fetch_csv_fresh(PAY_LEDGER_URL)
    lcols = list(led_df.columns)
    L_DATE = find_col(led_df.columns, "Date", "date", "invoice date", "txn date") or (lcols[0] if lcols else None)
    L_CUST = find_col(led_df.columns, "Customer Name", "customer", "name", "party")
    L_INV  = find_col(led_df.columns, "Invoice No", "invoice", "inv no", "bill no", "voucher")
    L_DEB  = find_col(led_df.columns, "Debit", "invoice amount", "debit (invoice)", "debit_invoice", "dr")
    L_CRED = find_col(led_df.columns, "Credit", "payment", "credit (payment)", "credit_payment", "cr")
    L_BAL  = find_col(led_df.columns, "Balance", "bal", "running balance")

    if not L_CUST:
        raise ValueError(f"Ledger me 'Customer Name' column nahi mila. Columns: {lcols[:12]}")

    by_cust = {}
    # FAST: column lists nikaal ke zip karo (.iterrows bahut dheema hota hai)
    custs = led_df[L_CUST].tolist() if L_CUST else []
    dates = led_df[L_DATE].tolist() if L_DATE else [None]*len(custs)
    debs  = led_df[L_DEB].tolist()  if L_DEB  else [0]*len(custs)
    creds = led_df[L_CRED].tolist() if L_CRED else [0]*len(custs)
    invs  = led_df[L_INV].tolist()  if L_INV  else [""]*len(custs)
    _date_cache = {}
    def _fast_date(v):
        key = str(v)
        if key in _date_cache:
            return _date_cache[key]
        try:
            dd = parse_date_any(v)
        except Exception:
            dd = None
        if isinstance(dd, datetime):
            dd = dd.date()
        _date_cache[key] = dd
        return dd
    for i in range(len(custs)):
        nm = _norm_name(custs[i])
        if not nm:
            continue
        by_cust.setdefault(nm, []).append({
            "date": _fast_date(dates[i]),
            "inv":  clean(invs[i]),
            "debit":  to_num(debs[i]),
            "credit": to_num(creds[i]),
        })

    today = now_ist().date()
    # month-end of current month
    if today.month == 12:
        month_end = date(today.year, 12, 31)
    else:
        month_end = date(today.year, today.month + 1, 1) - timedelta(days=1)

    AG_LABELS = ["0 Days", "0-30 Days", "31-60 Days", "61-90 Days", "91-180 Days", ">180 Days"]
    def _ag_bucket(days):
        if days <= 0:   return "0 Days"
        if days <= 30:  return "0-30 Days"
        if days <= 60:  return "31-60 Days"
        if days <= 90:  return "61-90 Days"
        if days <= 180: return "91-180 Days"
        return ">180 Days"

    rows = []
    aging = {k: 0.0 for k in AG_LABELS}
    tot_due = tot_over = tot_bal = 0.0
    # till month-end totals
    me_due = me_over = 0.0
    tags_set = set()

    for nm, entries in by_cust.items():
        term_days = term_map.get(nm, 0)
        tag = tag_map.get(nm, "")
        if tag: tags_set.add(tag)

        # FIFO: open invoices queue (oldest first), payments knock them off
        ents = sorted(entries, key=lambda e: (e["date"] or date(1900,1,1)))
        open_inv = []   # list of {date, amt_remaining}
        credit_pool = 0.0
        for e in ents:
            credit_pool += e["credit"]
            if e["debit"] > 0:
                open_inv.append({"date": e["date"], "amt": e["debit"]})
        # apply credit pool FIFO
        cp = credit_pool
        for inv in open_inv:
            if cp <= 0: break
            pay = min(cp, inv["amt"])
            inv["amt"] -= pay
            cp -= pay

        cust_due = cust_over = cust_bal = 0.0
        cust_due_me = cust_over_me = 0.0
        for inv in open_inv:
            rem = round(inv["amt"], 2)
            if rem <= 0.009:
                continue
            cust_bal += rem
            idt = inv["date"]
            due_date = (idt + timedelta(days=term_days)) if idt else None
            # as of TODAY
            if due_date and today > due_date:
                cust_over += rem
                od = (today - due_date).days
                aging[_ag_bucket(od)] += rem
            else:
                cust_due += rem
                aging["0 Days"] += rem
            # as of MONTH-END
            if due_date and month_end > due_date:
                cust_over_me += rem
            else:
                cust_due_me += rem

        if cust_bal <= 0.009:
            continue
        rows.append({
            "customer": nm.title(),
            "tag": tag,
            "term_days": term_days,
            "due": round(cust_due, 0),
            "overdue": round(cust_over, 0),
            "balance": round(cust_bal, 0),
            "due_me": round(cust_due_me, 0),
            "overdue_me": round(cust_over_me, 0),
        })
        tot_due += cust_due; tot_over += cust_over; tot_bal += cust_bal
        me_due += cust_due_me; me_over += cust_over_me

    rows.sort(key=lambda x: x["balance"], reverse=True)

    data = {
        "rows": rows,
        "today": today.strftime("%d-%b-%y"),
        "month_end": month_end.strftime("%d-%b-%y"),
        "totals": {
            "due": round(tot_due, 0), "overdue": round(tot_over, 0), "balance": round(tot_bal, 0),
            "due_me": round(me_due, 0), "overdue_me": round(me_over, 0),
        },
        "aging": [{"bucket": k, "amount": round(aging[k], 0)} for k in AG_LABELS],
        "aging_total": round(sum(aging.values()), 0),
        "tags": sorted([t for t in tags_set if t]),
    }
    _PAY_CACHE["data"] = data
    _PAY_CACHE["ts"] = time.time()
    try:
        by_cust.clear(); _gc.collect(); _malloc_trim()
    except Exception:
        pass
    return data

@app.route("/api/payments")
def api_payments():
    if session.get("role") not in ("admin", "employee"):
        return jsonify({"error": "login required"}), 401
    try:
        if request.args.get("force", "").lower() == "true":
            _PAY_CACHE["data"] = None
        return jsonify(_build_payments())
    except Exception as e:
        import traceback
        tb = traceback.format_exc()
        print("PAYMENTS ERROR:\n", tb)
        return jsonify({"error": f"payments failed: {e}", "where": tb.splitlines()[-3:] if tb else ""}), 500


# ════════════════════════════════════════════════════════════════
#  🆘 HELP QUERIES  (employee bhejta hai → admin home par 24h dikhta hai)
# ════════════════════════════════════════════════════════════════
_HELP_QUERIES = []   # [{id, text, user, ts}]
_HELP_LOCK = threading.Lock()

def _purge_help():
    cutoff = time.time() - 24*3600
    with _HELP_LOCK:
        _HELP_QUERIES[:] = [q for q in _HELP_QUERIES if q["ts"] >= cutoff]

@app.route("/api/help", methods=["POST"])
def api_help_submit():
    # Employee (ya admin) apni problem bhej sakta hai.
    role = session.get("role")
    if role not in ("employee", "admin"):
        return jsonify({"ok": False, "error": "login required"}), 401
    body = request.get_json(silent=True) or {}
    text = (body.get("text") or "").strip()
    if not text:
        return jsonify({"ok": False, "error": "empty"}), 400
    text = text[:1000]
    with _HELP_LOCK:
        _HELP_QUERIES.append({
            "id": uuid.uuid4().hex[:10],
            "text": text,
            "user": session.get("user") or role,
            "ts": time.time(),
        })
        # purana 24h+ saaf + max 200 rakho
        cutoff = time.time() - 24*3600
        _HELP_QUERIES[:] = [q for q in _HELP_QUERIES if q["ts"] >= cutoff][-200:]
    return jsonify({"ok": True})

@app.route("/api/help-queries")
def api_help_list():
    # Sirf admin — home page par dikhane ke liye. 24h+ purane apne aap gayab.
    if session.get("role") != "admin":
        return jsonify({"queries": []})
    _purge_help()
    now = time.time()
    with _HELP_LOCK:
        out = [{
            "id": q["id"], "text": q["text"], "user": q["user"],
            "ago_min": int((now - q["ts"]) / 60),
        } for q in sorted(_HELP_QUERIES, key=lambda x: x["ts"], reverse=True)]
    return jsonify({"queries": out})

@app.route("/api/help-dismiss", methods=["POST"])
def api_help_dismiss():
    # Admin ek query ko manually hata sakta hai.
    if session.get("role") != "admin":
        return jsonify({"ok": False}), 403
    qid = (request.get_json(silent=True) or {}).get("id", "")
    with _HELP_LOCK:
        _HELP_QUERIES[:] = [q for q in _HELP_QUERIES if q["id"] != qid]
    return jsonify({"ok": True})

@app.route("/api/vision-status")
def api_vision_status():
    return jsonify({
        "ml_available": ML_AVAILABLE,
        "embed_mode":   EMBED_MODE,
        "ai_ready":     AI_READY,
        "pkl_exists":   os.path.exists(PKL_FILE),
        "pkl_mb":       round(os.path.getsize(PKL_FILE)/1e6, 1) if os.path.exists(PKL_FILE) else 0,
        "space_id":     SPACE_ID,
        "skus_indexed": (len(db_data["skus"]) if db_data else 0),
        "last_embed_error": _HF_LAST_ERROR.get("msg", ""),
    })

def _vision_self_test():
    """Startup par background mein 1 test embedding — logs mein result."""
    try:
        if EMBED_MODE not in ("hf", "space"):
            return
        img = Image.new("RGB", (224, 224), (180, 150, 70))
        p = "/tmp/_selftest.jpg"
        img.save(p, format="JPEG")
        v = get_embedding(p)
        if v is not None:
            print("VISION SELF-TEST: OK — SKU Finder fully working ✔")
        else:
            print("VISION SELF-TEST FAILED:", _HF_LAST_ERROR.get("msg", "unknown"))
    except Exception as e:
        print("VISION SELF-TEST exception:", str(e)[:150])

@app.route("/api/debug")
def api_debug():
    if CACHE["data"] is None: get_data(True)
    return jsonify(CACHE.get("debug", {}))

@app.route("/api/marketplaces")
def api_marketplaces():
    force = request.args.get("force","false").lower() == "true"
    return jsonify(get_marketplaces(force))

@app.route("/search", methods=["POST"])
def search():
    try:
        if not AI_READY:
            # Lazy load: SKU Finder pehli baar use hone par hi model load karo
            # (startup pe memory bachane ke liye defer kiya tha).
            try:
                init_vision()
            except Exception as _e:
                print("lazy init_vision failed:", str(_e)[:140])
        if not AI_READY:
            return jsonify({"error": "AI model not loaded — sku_finder.pkl missing. Render me PKL_URL env var set karo (Google Drive link) ya pkl file repo me daalo."}), 500
        image_data = request.json["image"]
        img_bytes  = base64.b64decode(image_data.split(",")[1])
        comp       = get_data()[0]
        results    = vision_search(img_bytes, comp, top_k=10)
        if results is None:
            why = ""
            if EMBED_MODE == "space":
                why = _HF_LAST_ERROR.get("msg", "")
                if why:
                    why += " — Space chal raha hai ya nahi check karo: huggingface.co par apna Space kholo."
            elif EMBED_MODE == "hf":
                why = _HF_LAST_ERROR.get("msg", "")
                if "404" in why:
                    why += " — HF par yeh model serverless available nahi hai; Render Standard (2GB) par upgrade karke full requirements use karo."
                elif "401" in why or "403" in why:
                    why += " — HF_TOKEN invalid/expired hai; huggingface.co se naya token banao."
            return jsonify({"error": ("Embedding failed" + (": " + why if why else ""))[:400]}), 500
        return jsonify({"results": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500



# ── SMART VISUAL SEARCH (CLIP: text → catalog images, fully offline) ────
# Ek baar visual index banta hai (catalog images download + CLIP encode),
# uske baad "lion", "skull", "om" — kuch bhi likho, images se match hota hai.
# Index file: clip_index.pkl — isse download karke sku_finder.pkl ke saath
# rakho, to agli baar dobara nahi banana padega.
CLIP_INDEX_FILE = "clip_index.pkl"
CLIP_MODEL_NAME = "openai/clip-vit-base-patch32"
_CLIP = {"model": None, "processor": None, "index": None, "building": False,
         "progress": {"done": 0, "total": 0, "status": "idle", "error": ""}}

def _clip_load_model():
    if not ML_AVAILABLE:
        raise RuntimeError("ML stack (torch/transformers) is not installed on this server")
    if _CLIP["model"] is None:
        from transformers import CLIPModel, CLIPProcessor
        print("Loading CLIP model for smart search…")
        _CLIP["model"] = CLIPModel.from_pretrained(CLIP_MODEL_NAME)
        _CLIP["processor"] = CLIPProcessor.from_pretrained(CLIP_MODEL_NAME)
        _CLIP["model"].eval()
        try:
            if torch.cuda.is_available():
                _CLIP["model"].to("cuda")
        except Exception:
            pass
    return _CLIP["model"], _CLIP["processor"]

def _clip_device():
    try:
        return next(_CLIP["model"].parameters()).device
    except Exception:
        return "cpu"

def _clip_load_index():
    if _CLIP["index"] is None and os.path.exists(CLIP_INDEX_FILE):
        try:
            with open(CLIP_INDEX_FILE, "rb") as f:
                raw = pickle.load(f)
            _CLIP["index"] = {"skus": [str(s) for s in raw["skus"]],
                              "embeddings": np.asarray(raw["embeddings"], dtype=np.float32)}
            print(f"Smart search index loaded ({len(_CLIP['index']['skus'])} SKUs).")
        except Exception as e:
            print("clip index load failed:", e)
    return _CLIP["index"]

def _clip_text_embed(text):
    model, proc = _clip_load_model()
    inputs = proc(text=[text], return_tensors="pt", padding=True, truncation=True)
    inputs = {k: v.to(_clip_device()) for k, v in inputs.items()}
    with torch.no_grad():
        feat = model.get_text_features(**inputs)
    feat = feat / feat.norm(dim=-1, keepdim=True)
    return feat[0].detach().cpu().numpy().astype(np.float32)

def _clip_image_embed_batch(pil_images):
    model, proc = _clip_load_model()
    inputs = proc(images=pil_images, return_tensors="pt")
    inputs = {k: v.to(_clip_device()) for k, v in inputs.items()}
    with torch.no_grad():
        feat = model.get_image_features(**inputs)
    feat = feat / feat.norm(dim=-1, keepdim=True)
    return feat.detach().cpu().numpy().astype(np.float32)

def _img_url_candidates(url):
    """Normalize image URLs — Google Drive share links ko direct-image
    URLs mein convert karta hai, plus =IMAGE() formulas handle karta hai."""
    u = str(url or "").strip().strip('"').strip("'")
    m = re.search(r'=?image\s*\(\s*["\']([^"\']+)["\']', u, re.I)
    if m:
        u = m.group(1)
    cands = []
    fid = None
    m = re.search(r"drive\.google\.com/(?:file/d/|open\?id=|uc\?[^ ]*id=)([\w-]{20,})", u)
    if not m:
        m = re.search(r"[?&]id=([\w-]{20,})", u) if "google" in u else None
    if m:
        fid = m.group(1)
    if fid:
        cands.append(f"https://lh3.googleusercontent.com/d/{fid}=w512")
        cands.append(f"https://drive.google.com/thumbnail?id={fid}&sz=w512")
        cands.append(f"https://drive.google.com/uc?export=download&id={fid}&confirm=t")
        cands.append(f"https://drive.google.com/uc?export=view&id={fid}")
    if u.startswith("http"):
        cands.append(u)
    return cands or ([u] if u else [])

def _browser_headers(url):
    """Full browser-grade headers — Cloudflare/WordPress hotlink protection
    aksar plain python requests ko block karta hai, in headers se pass hota hai."""
    try:
        from urllib.parse import urlparse
        p = urlparse(url)
        origin = f"{p.scheme}://{p.netloc}"
    except Exception:
        origin = ""
    return {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": origin + "/",
        "Sec-Fetch-Dest": "image", "Sec-Fetch-Mode": "no-cors", "Sec-Fetch-Site": "same-origin",
        "Connection": "keep-alive",
    }

def _fetch_catalog_image(url, want_reason=False):
    last = "no url"
    for cu in _img_url_candidates(url):
        try:
            r = requests.get(cu, timeout=20, allow_redirects=True, headers=_browser_headers(cu))
            ct = r.headers.get("Content-Type", "")
            if not r.ok:
                last = f"HTTP {r.status_code} ({ct[:30]}) {cu[:70]}"
                continue
            if len(r.content) < 400:
                last = f"too small ({len(r.content)}B) {cu[:70]}"
                continue
            try:
                img = Image.open(io.BytesIO(r.content)).convert("RGB")
            except Exception:
                last = f"not an image ({ct[:30]}) {cu[:70]}"
                continue
            img.thumbnail((224, 224))
            return (img, "ok") if want_reason else img
        except Exception as e:
            last = f"{type(e).__name__}: {str(e)[:60]} {cu[:60]}"
            continue
    return (None, last) if want_reason else None

def _build_clip_index_worker():
    """One-time background job: catalog images → CLIP embeddings → clip_index.pkl"""
    from concurrent.futures import ThreadPoolExecutor
    prog = _CLIP["progress"]
    try:
        comp = get_data()[0]
        targets = [(i["sku"], str(i.get("image_url", "")).strip()) for i in comp
                   if str(i.get("image_url", "")).strip()
                   and str(i.get("image_url", "")).lower() != "nan"]
        prog.update({"done": 0, "total": len(targets), "ok": 0, "fail": 0,
                     "status": "building", "error": "", "sample_errors": []})
        # pehle 3 links ka detailed probe — fail hone par exact reason pata chale
        for _, u in targets[:3]:
            _, reason = _fetch_catalog_image(u, want_reason=True)
            if reason != "ok":
                prog["sample_errors"].append(reason)
        if not targets:
            prog.update({"status": "error", "error": "No Image Link URLs found in the inventory sheet."})
            return
        try:
            _clip_load_model()
            # encoder self-test — 1 dummy image
            _test = Image.new("RGB", (224, 224), (200, 170, 90))
            _clip_image_embed_batch([_test])
        except Exception as e:
            prog.update({"status": "error",
                         "error": "AI encoder failed to start: " + str(e)[:220] +
                                  " — fix: run  !pip install -U transformers torch  and restart."})
            return
        skus, embs, batch_imgs, batch_skus = [], [], [], []
        prog["encode_errors"] = []

        def flush():
            nonlocal batch_imgs, batch_skus
            if batch_imgs:
                try:
                    vecs = _clip_image_embed_batch(batch_imgs)
                    embs.append(vecs); skus.extend(batch_skus)
                except Exception as e:
                    print("clip batch encode failed:", e)
                    if len(prog.get("encode_errors", [])) < 3:
                        prog.setdefault("encode_errors", []).append(str(e)[:150])
                batch_imgs, batch_skus = [], []

        with ThreadPoolExecutor(max_workers=8) as ex:
            for sku, img in zip([t[0] for t in targets],
                                ex.map(lambda t: _fetch_catalog_image(t[1]), targets)):
                prog["done"] += 1
                if img is not None:
                    prog["ok"] += 1
                    batch_imgs.append(img); batch_skus.append(sku)
                    if len(batch_imgs) >= 16:
                        flush()
                else:
                    prog["fail"] += 1
        flush()
        if not skus:
            # diagnose: server internet vs link access
            net_ok = False
            try:
                net_ok = requests.get("https://www.gstatic.com/generate_204", timeout=10).status_code in (200, 204)
            except Exception:
                net_ok = False
            samples = "; ".join(str(t[1])[:90] for t in targets[:2])
            reasons = "; ".join(prog.get("sample_errors", [])[:3])
            enc_reasons = "; ".join(prog.get("encode_errors", [])[:3])
            if prog.get("ok", 0) > 0:
                msg = (f"Downloaded {prog['ok']} images successfully, but the AI encoder failed: "
                       f"[{enc_reasons or 'unknown'}] — fix: run  !pip install -U transformers torch  and restart.")
            elif not net_ok:
                msg = "Server has no internet access for image downloads — check the network of the machine running this dashboard."
            else:
                msg = ("None of the image links returned an image. Exact reasons: [" + (reasons or "unknown") +
                       "]. Sample links: " + samples)
            prog.update({"status": "error", "error": msg})
            return
        index = {"skus": skus, "embeddings": np.vstack(embs)}
        with open(CLIP_INDEX_FILE, "wb") as f:
            pickle.dump(index, f)
        _CLIP["index"] = {"skus": skus, "embeddings": np.asarray(index["embeddings"], dtype=np.float32)}
        prog.update({"status": "ready"})
        print(f"Smart search index READY: {len(skus)} SKUs -> {CLIP_INDEX_FILE}")
    except Exception as e:
        import traceback; traceback.print_exc()
        prog.update({"status": "error", "error": str(e)[:300]})
    finally:
        _CLIP["building"] = False

@app.route("/api/smart-index", methods=["POST"])
def api_smart_index():
    if _CLIP["building"]:
        return jsonify({"status": "building", **_CLIP["progress"]})
    if _clip_load_index() is not None:
        return jsonify({"status": "ready"})
    _CLIP["building"] = True
    _CLIP["progress"] = {"done": 0, "total": 0, "status": "building", "error": ""}
    threading.Thread(target=_build_clip_index_worker, daemon=True).start()
    return jsonify({"status": "building", **_CLIP["progress"]})

@app.route("/api/smart-index-status")
def api_smart_index_status():
    if _clip_load_index() is not None and not _CLIP["building"]:
        return jsonify({"status": "ready"})
    return jsonify({"status": _CLIP["progress"].get("status", "idle"), **_CLIP["progress"]})

@app.route("/api/smart-search", methods=["POST"])
def api_smart_search():
    try:
        payload = request.get_json(silent=True) or {}
        query = (payload.get("query") or "").strip()
        if not query:
            return jsonify({"error": "Please type a search concept — e.g. lion, skull, eagle, om"}), 400
        comp = get_data()[0]
        ql = query.lower()
        tokens = [w for w in re.split(r"\s+", ql) if len(w) > 1]

        # 1) instant text-field matches (sku, taxon, plating, status, combo)
        text_hits, seen = [], set()
        for i in comp:
            blob = f"{i.get('sku','')} {i.get('taxon','')} {i.get('plating','')} {i.get('status','')} {i.get('combo_skus','')}".lower()
            if tokens and all(t in blob for t in tokens):
                text_hits.append(i); seen.add(i["sku"])
                if len(text_hits) >= 24:
                    break

        # 2) CLIP visual matches (offline — index required)
        idx = _clip_load_index()
        if idx is None:
            return jsonify({"results": text_hits[:24], "mode": "text",
                            "text_matches": len(text_hits), "visual_matches": 0,
                            "need_index": True,
                            "building": _CLIP["building"],
                            "progress": _CLIP["progress"]})

        temb = _clip_text_embed(f"a photo of {query} jewellery")
        sims = idx["embeddings"] @ temb
        order = np.argsort(sims)[::-1][:80]
        visual_hits = []
        for pos in order:
            sku = idx["skus"][pos]
            score = float(sims[pos])
            m = next((x for x in comp if x["sku"].upper() == str(sku).upper()), None)
            if m is None:
                m = next((x for x in comp if base_sku(x["sku"]) == base_sku(sku)), None)
            if m and m["sku"] not in seen:
                if score < 0.20 and len(visual_hits) >= 8:
                    continue
                it = m.copy()
                it["confidence"] = round(max(score, 0) * 100, 1)
                visual_hits.append(it); seen.add(m["sku"])
            if len(visual_hits) >= 24:
                break
        results = text_hits[:8] + visual_hits[: (24 - min(len(text_hits), 8))]
        return jsonify({"results": results, "mode": "text+visual",
                        "text_matches": len(text_hits), "visual_matches": len(visual_hits)})
    except Exception as e:
        import traceback; traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@app.route("/api/upload-report", methods=["POST"])
def api_upload_report():
    f = request.files.get("file")
    if not f:
        return jsonify({"error": "No file uploaded"}), 400

    filename = f.filename or "upload"
    ext = os.path.splitext(filename)[1].lower()
    try:
        raw = f.read()
        bio = io.BytesIO(raw)
        if ext in (".xls", ".xlsx"):
            df = pd.read_excel(bio)
        else:
            try:
                df = pd.read_csv(bio, dtype=str, on_bad_lines="skip")
            except Exception:
                df = pd.read_csv(io.BytesIO(raw.decode("utf-8", "ignore").encode("utf-8")), dtype=str, on_bad_lines="skip")
    except Exception as e:
        return jsonify({"error": f"Could not read file: {e}"}), 400

    if df is None or df.empty:
        return jsonify({"error": "Uploaded file is empty"}), 400

    df.columns = [str(c).strip() for c in df.columns]
    sku_col = find_col(df.columns, "SKU", "SKU No", "SKU No.", "SKU No ", "Item Code", "Item code", "Product SKU", "Code") or df.columns[0]

    comp = get_data()[0]
    inv_map = {}
    for i in comp:
        k = re.sub(r"[^A-Z0-9]", "", str(i.get("sku", "")).upper())
        if k and k not in inv_map:
            inv_map[k] = i

    records = []
    for _, row in df.head(5000).iterrows():
        src = {c: clean(row.get(c, "")) for c in df.columns}
        raw_sku = clean(row.get(sku_col, ""))
        n_key = re.sub(r"[^A-Z0-9]", "", raw_sku.upper())
        matched = inv_map.get(n_key)
        if matched is None and n_key:
            m = difflib.get_close_matches(n_key, inv_map.keys(), n=1, cutoff=0.8)
            if m:
                matched = inv_map.get(m[0])

        rec = dict(src)
        rec.update({
            "Matched SKU": matched.get("sku", "") if matched else "",
            "Taxon": matched.get("taxon", "") if matched else "",
            "Status": matched.get("status", "") if matched else "",
            "Inv Stock": matched.get("inv_stock", "") if matched else "",
            "Inv WIP": matched.get("inv_wip", "") if matched else "",
            "Final Qty": matched.get("final_qty", "") if matched else "",
            "Image Link": matched.get("image_url", "") if matched else "",
            "Combo SKUs": matched.get("combo_skus", "") if matched else "",
        })
        records.append(rec)

    token = uuid.uuid4().hex[:12]
    UPLOAD_REPORTS[token] = {
        "name": filename,
        "sku_col": sku_col,
        "created": now_ist().strftime("%Y-%m-%d %H:%M:%S"),
        "rows": records,
        "columns": list(records[0].keys()) if records else [],
        "count": len(records),
    }
    return jsonify({"url": f"/upload-report/{token}"})

@app.route("/upload-report/<token>")
def upload_report(token):
    report = UPLOAD_REPORTS.get(token)
    if not report:
        return "Report not found or expired.", 404

    rows = report.get("rows", [])
    cols = report.get("columns", [])
    df = pd.DataFrame(rows, columns=cols)

    def esc(v):
        return (
            "" if v is None else str(v)
        ).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

    table_html = df.to_html(index=False, escape=True, classes="ro", border=0) if not df.empty else "<div class='tno-data'>No rows found</div>"
    return render_template_string(f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Uploaded File Details</title>
<style>
body{{font-family:Arial,sans-serif;background:#0b1220;color:#e5eefb;margin:0;padding:24px}}
.wrap{{max-width:1500px;margin:0 auto}}
.head{{background:linear-gradient(135deg,#111827,#0f172a);border:1px solid rgba(212,175,90,.25);border-radius:20px;padding:20px 22px;margin-bottom:16px}}
.head h1{{margin:0;color:#fff6df;font-size:26px;letter-spacing:1px}}
.sub{{margin-top:8px;color:#d4af5a;font-weight:700;letter-spacing:1px;text-transform:uppercase;font-size:11px}}
.kpis{{display:flex;gap:12px;flex-wrap:wrap;margin:16px 0}}
.kpi{{background:#fff;border-radius:14px;padding:14px 16px;border:1px solid #e5e7eb;min-width:160px}}
.kpi .l{{font-size:10px;letter-spacing:2px;text-transform:uppercase;color:#8c7a42;font-weight:800}}
.kpi .v{{margin-top:6px;font-size:20px;font-weight:900;color:#111827}}
.table-wrap{{overflow:auto;border-radius:18px;border:1px solid #dbe3ed;background:#fff}}
table.ro{{width:100%;border-collapse:collapse;font-size:12px}}
table.ro th, table.ro td{{padding:10px 12px;border-bottom:1px solid #eef2f7;white-space:nowrap;text-align:left;color:#1f2937}}
table.ro th{{position:sticky;top:0;background:#f8fafc;color:#8c7a42;text-transform:uppercase;letter-spacing:1px;font-size:10px;z-index:2}}
a{{color:#b8860b;text-decoration:none}}
a:hover{{text-decoration:underline}}

/* ===== Premium top app bar + navigation polish ===== */
.app-bar{
  position:sticky;
  top:0;
  z-index:70;
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:14px;
  padding:12px 18px;
  background:#ffffff;
  backdrop-filter:blur(16px);
  border-bottom:1px solid rgba(229,231,235,.95);
  box-shadow:0 10px 30px rgba(15,23,42,.05);
}
.app-bar-copy{
  display:flex;
  flex-direction:column;
  justify-content:center;
  min-width:0;
}
.app-bar-brand{
  font-size:12px;
  font-weight:1000;
  letter-spacing:4px;
  text-transform:uppercase;
  color:#b8860b;
  white-space:nowrap;
  overflow:hidden;
  text-overflow:ellipsis;
}
.app-bar-sub{
  margin-top:4px;
  font-size:10px;
  letter-spacing:3px;
  text-transform:uppercase;
  color:#64748b;
  font-weight:800;
}
.app-bar-actions{
  display:flex;
  align-items:center;
  gap:8px;
  flex-wrap:wrap;
  justify-content:flex-end;
}
.app-chip{
  border:1px solid #334155;
  background:#1e293b;
  color:#ffffff;
  border-radius:999px;
  padding:9px 14px;
  font-size:10px;
  font-weight:900;
  letter-spacing:2px;
  text-transform:uppercase;
  cursor:pointer;
  box-shadow:0 4px 12px rgba(15,23,42,.18);
}
.app-chip:hover{background:#0f172a;border-color:#475569;color:#ffffff}
.menu-btn{
  position:static;
  width:42px;
  height:42px;
  border-radius:14px;
  flex:0 0 auto;
}
.hero .menu-btn{
  position:static;
}
body:not([data-tab="home"]) #siteHero{
  display:none !important;
}
body[data-tab="home"] #siteHero{
  display:flex;
}
body[data-tab="home"] .tabs{
  top:10px;
}
body:not([data-tab="home"]) .tabs{
  top:70px;
}
body[data-tab="home"] .app-bar{
  background:#ffffff;
}
body:not([data-tab="home"]) .app-bar{
  background:#ffffff;
}
.hero{
  border-radius:0 0 26px 26px;
}
.hero-only{
  max-width:1100px;
}
.hero-title{
  font-size:clamp(24px,4.5vw,58px);
  letter-spacing:clamp(1px,.45vw,7px);
}
.hero-dev{
  letter-spacing:clamp(1.5px,.3vw,4px);
}

/* Global menu safety */
#navMenu{z-index:120;}
#navMenu .menu-item{display:block;}
.tabs{
  background:rgba(248,250,252,.9);
  backdrop-filter:blur(12px);
}
.tab{
  border-radius:999px;
}
.kpi,.filter-box,.card,.ro-table-wrap,.upload-area,.sd-head,#vInsights .insight-card,.home-card,.home-hero,.home-stage,.insight-summary-card{
  border-radius:22px;
}

</style>
</head>
<body>
<div class="wrap">
  <div class="head">
    <h1>Uploaded File Details</h1>
    <div class="sub">{esc(report.get("name",""))} • {esc(report.get("count",0))} rows • SKU column: {esc(report.get("sku_col",""))} • Created: {esc(report.get("created",""))}</div>
  </div>
  <div class="kpis">
    <div class="kpi"><div class="l">Rows</div><div class="v">{esc(report.get("count",0))}</div></div>
    <div class="kpi"><div class="l">Columns</div><div class="v">{esc(len(cols))}</div></div>
    <div class="kpi"><div class="l">Matched SKU Field</div><div class="v">{esc(report.get("sku_col",""))}</div></div>
  </div>
  <div class="table-wrap">
    {table_html}
  </div>
</div>
</body>
</html>
""")

# ── Cloudflare Tunnel ────────────────────────────────────────
def find_cloudflared():
    if CLOUDFLARED_PATH and os.path.isfile(CLOUDFLARED_PATH):
        return CLOUDFLARED_PATH
    try:
        here = os.path.dirname(os.path.abspath(__file__))
    except NameError:
        here = os.getcwd()
    candidates = []
    for folder in (here, os.getcwd()):
        candidates += glob.glob(os.path.join(folder, "cloudflared*.exe"))
        candidates += glob.glob(os.path.join(folder, "cloudflared*"))
    for c in candidates:
        if os.path.isfile(c):
            return c
    onpath = shutil.which("cloudflared") or shutil.which("cloudflared.exe")
    return onpath

def ensure_cloudflared():
    exe = find_cloudflared()
    if exe:
        return exe
    if not sys.platform.startswith("linux"):
        return None
    arch = "amd64" if (os.uname().machine in ("x86_64", "amd64")) else "arm64"
    url = f"https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-{arch}"
    dest = os.path.join(os.getcwd(), "cloudflared")
    try:
        print(f"Downloading cloudflared for Linux ({arch})…")
        r = requests.get(url, stream=True, timeout=60)
        r.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in r.iter_content(chunk_size=1 << 16):
                f.write(chunk)
        os.chmod(dest, 0o755)
        print("cloudflared downloaded to:", dest)
        return dest
    except Exception as e:
        print("Auto-download of cloudflared failed:", e)
        return None

def start_cloudflare_tunnel(port):
    exe = ensure_cloudflared()
    if not exe:
        print("cloudflared not found — running LOCAL ONLY.")
        return None, None

    print(f"Starting Cloudflare Tunnel via: {exe}")
    try:
        proc = subprocess.Popen(
            [exe, "tunnel", "--url", f"http://localhost:{port}", "--no-autoupdate"],
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, bufsize=1,
        )
    except Exception as e:
        print("Failed to launch cloudflared:", e)
        return None, None

    public_url = {"v": None}

    def _reader():
        url_re = re.compile(r"https://[-a-z0-9]+\.trycloudflare\.com")
        for line in proc.stdout:
            if public_url["v"] is None:
                m = url_re.search(line)
                if m:
                    public_url["v"] = m.group(0)
                    print("\n" + "="*60)
                    print("COSA NOSTRAA LIVE:", public_url["v"])
                    print("="*60 + "\n")
    threading.Thread(target=_reader, daemon=True).start()

    for _ in range(40):
        if public_url["v"]: break
        time.sleep(0.5)
    return public_url["v"], proc

# ── Background warmup + auto-refresh ─────────────────────────
REFRESH_INTERVAL = int(os.environ.get("REFRESH_INTERVAL", 600))   # seconds (10 min — 512MB par RAM-spikes kam)

KEEPALIVE_URL = (os.environ.get("KEEPALIVE_URL") or os.environ.get("RENDER_EXTERNAL_URL") or "").strip()

def _keepalive_loop():
    """Render free-tier ko sone se rokta hai — har 8 min khud ko ping.
    (Backup: cron-job.org se bhi external ping rakho)"""
    if not KEEPALIVE_URL:
        return
    url = KEEPALIVE_URL.rstrip("/") + "/api/warmup-status"
    print(f"KEEPALIVE active -> {url}")
    while True:
        time.sleep(480)
        try:
            requests.get(url, timeout=15)
        except Exception:
            pass

def _warmup_and_refresh_loop():
    """Server start hote hi data taiyaar; phir har REFRESH_INTERVAL par
    background mein fresh. MEMORY: sirf ek role ka response prebuild
    (dono ek saath 512MB par OOM -> Render restart loop kar deta tha).
    Baaki role pehli request par lazy ban jata hai."""
    try:
        get_data(True)
        try:
            _build_role_gz("admin")          # sirf admin prebuild (RAM bachat)
        except Exception as e:
            print("prebuild admin failed:", str(e)[:100])
        _wstage("ready", "Ready")
        print("WARMUP: data ready ✔")
        # vision init memory leta hai — Render 512MB par startup ke waqt skip.
        # SKU Finder pehli baar use hone par lazy load ho jayega (init_vision wahin call hota hai).
        if os.environ.get("EAGER_VISION") == "1":
            try:
                init_vision()
                _vision_self_test()
            except Exception as e:
                print("vision init skipped:", str(e)[:120])
    except Exception as e:
        print("WARMUP error:", str(e)[:160])
    while True:
        time.sleep(REFRESH_INTERVAL)
        try:
            get_data(True)
            _build_role_gz("admin")          # background me bhi sirf admin
            try:
                import resource
                _mb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
                print(f"BG refresh done | peak RAM {_mb:.0f}MB")
            except Exception:
                print("BG refresh done")
        except Exception as e:
            print("BG refresh error:", str(e)[:140])

# ── Launch ───────────────────────────────────────────────────
IS_DEPLOY = bool(os.environ.get("DEPLOY") or os.environ.get("RENDER")
                 or os.environ.get("RAILWAY_ENVIRONMENT") or os.environ.get("DYNO")
                 or os.environ.get("PORT"))

# Background warmup + keepalive start at IMPORT time too, so the app works under
# BOTH `python app.py` and `gunicorn app:app` (Render kisi bhi start command se).
# init_vision() inside the warmup loads SKU Finder (local torch if available,
# warna HF Space/API se) — isliye SKU Finder Render par bhi ON rehta hai.
_LAUNCHED = False
def _start_background_threads():
    global _LAUNCHED
    if _LAUNCHED:
        return
    _LAUNCHED = True
    threading.Thread(target=_warmup_and_refresh_loop, daemon=True).start()
    try:
        threading.Thread(target=_keepalive_loop, daemon=True).start()
    except Exception as e:
        print("keepalive thread skip:", str(e)[:80])

# Start now (covers gunicorn import). Safe + idempotent.
_start_background_threads()

if __name__ == "__main__":
    if IS_DEPLOY:
        print("Production mode — serving on port", PORT)
        app.run(host="0.0.0.0", port=PORT, threaded=True, use_reloader=False)
        raise SystemExit

    tunnel_proc = None
    if USE_TUNNEL:
        def _launch_tunnel():
            global tunnel_proc
            time.sleep(2)
            _, tunnel_proc = start_cloudflare_tunnel(PORT)
        threading.Thread(target=_launch_tunnel, daemon=True).start()
    else:
        print("USE_TUNNEL is False — running LOCAL ONLY at http://localhost:%d" % PORT)

    print("Server running on 0.0.0.0:", PORT, "(open http://localhost:%d locally)" % PORT)
    try:
        app.run(host="0.0.0.0", port=PORT, threaded=True, use_reloader=False)
    finally:
        if tunnel_proc:
            try: tunnel_proc.terminate()
            except: pass
