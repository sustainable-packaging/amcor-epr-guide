import streamlit as st

# ── PAGE CONFIG ──────────────────────────────────────────
st.set_page_config(
    page_title="Amcor EPR Customer Guide 2026",
    page_icon="https://www.amcor.com/favicon.ico",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── CUSTOM CSS ───────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;600;700;800&family=Barlow:wght@300;400;500;600&display=swap');

  :root {
    --navy:   #002F5F;
    --blue:   #0061A0;
    --sky:    #0093D0;
    --teal:   #00A878;
    --red:    #D94040;
    --amber:  #F5A623;
    --off:    #F4F6F9;
    --border: #D0D8E4;
    --grey:   #6B7A8D;
    --text:   #2D3E50;
    --white:  #FFFFFF;
  }

  html, body, [class*="css"] {
    font-family: 'Barlow', sans-serif;
    color: var(--text);
  }

  .main { background: #F0F2F6; padding: 0 !important; }
  .block-container { padding: 0 !important; max-width: 100% !important; }

  /* NAV */
  .nav-bar {
    background: var(--navy);
    padding: 14px 48px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: sticky;
    top: 0;
    z-index: 999;
  }
  .nav-brand {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 22px;
    font-weight: 800;
    letter-spacing: 4px;
    color: white;
    text-transform: uppercase;
  }
  .nav-links {
    display: flex;
    gap: 6px;
    align-items: center;
  }
  .nav-link {
    color: rgba(255,255,255,0.6);
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    text-decoration: none;
    padding: 6px 12px;
    border-radius: 3px;
    transition: all 0.2s;
  }
  .nav-link:hover { color: white; background: rgba(255,255,255,0.08); }
  .nav-cta {
    background: var(--sky);
    color: white !important;
    padding: 7px 16px !important;
    border-radius: 3px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    text-decoration: none;
  }

  /* HERO */
  .hero {
    background: linear-gradient(135deg, #001830 0%, #002F5F 50%, #0061A0 100%);
    padding: 80px 48px 60px;
    text-align: center;
  }
  .hero-eyebrow {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 4px;
    color: var(--sky);
    text-transform: uppercase;
    margin-bottom: 16px;
  }
  .hero-title {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 64px;
    font-weight: 800;
    color: white;
    text-transform: uppercase;
    line-height: 1.0;
    margin-bottom: 16px;
  }
  .hero-title span { color: var(--sky); }
  .hero-sub {
    font-size: 16px;
    font-weight: 300;
    color: rgba(255,255,255,0.65);
    max-width: 560px;
    margin: 0 auto 40px;
    line-height: 1.7;
  }

  /* STATS STRIP */
  .stats-strip {
    background: var(--navy);
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    border-top: 1px solid rgba(255,255,255,0.1);
  }
  .stat-item {
    padding: 20px 24px;
    text-align: center;
    border-right: 1px solid rgba(255,255,255,0.1);
  }
  .stat-item:last-child { border-right: none; }
  .stat-num {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 36px;
    font-weight: 700;
    color: var(--sky);
    line-height: 1;
    margin-bottom: 4px;
  }
  .stat-label {
    font-size: 10px;
    color: rgba(255,255,255,0.5);
    line-height: 1.4;
  }

  /* SECTIONS */
  .section { padding: 64px 48px; }
  .section-dark { background: #0D1F35; }
  .section-darker { background: #091829; }
  .section-light { background: white; }
  .section-mid { background: #F4F6F9; }

  .section-tag {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 3px;
    color: var(--sky);
    text-transform: uppercase;
    margin-bottom: 10px;
    display: block;
  }
  .section-title {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 40px;
    font-weight: 800;
    color: white;
    text-transform: uppercase;
    line-height: 1.05;
    margin-bottom: 12px;
  }
  .section-title-dark {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 40px;
    font-weight: 800;
    color: var(--navy);
    text-transform: uppercase;
    line-height: 1.05;
    margin-bottom: 12px;
  }
  .section-sub {
    font-size: 15px;
    color: rgba(255,255,255,0.55);
    max-width: 520px;
    line-height: 1.7;
    margin-bottom: 40px;
  }
  .section-sub-dark {
    font-size: 15px;
    color: var(--grey);
    max-width: 520px;
    line-height: 1.7;
    margin-bottom: 40px;
  }

  /* CARDS */
  .card-grid-3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin-bottom: 40px;
  }
  .card-grid-2 {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
  }
  .card-grid-4 {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 14px;
  }

  .fee-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 8px;
    padding: 28px 24px;
    text-align: center;
    transition: all 0.3s;
  }
  .fee-card:hover {
    background: rgba(0,147,208,0.08);
    border-color: rgba(0,147,208,0.3);
    transform: translateY(-3px);
  }
  .fee-card-num {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 44px;
    font-weight: 700;
    color: var(--sky);
    line-height: 1;
    margin-bottom: 8px;
  }
  .fee-card-label {
    font-size: 14px;
    font-weight: 700;
    color: white;
    margin-bottom: 6px;
  }
  .fee-card-desc {
    font-size: 12px;
    color: rgba(255,255,255,0.45);
    line-height: 1.5;
  }

  /* REGION CARDS */
  .region-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 8px;
    padding: 20px 24px;
    margin-bottom: 12px;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
  }
  .region-name {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 22px;
    font-weight: 700;
    color: white;
    margin-bottom: 4px;
  }
  .region-desc {
    font-size: 12px;
    color: rgba(255,255,255,0.55);
    line-height: 1.5;
    max-width: 280px;
  }
  .region-date {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 16px;
    font-weight: 700;
    color: var(--sky);
    text-align: right;
    white-space: nowrap;
    margin-left: 16px;
  }
  .region-date-amber { color: var(--amber) !important; }

  /* URGENCY BOX */
  .urgency-box {
    background: var(--navy);
    border-radius: 8px;
    padding: 24px;
    margin-bottom: 24px;
  }
  .urgency-tag {
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 2px;
    color: var(--amber);
    text-transform: uppercase;
    margin-bottom: 6px;
  }
  .urgency-date {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 32px;
    font-weight: 800;
    color: white;
    margin-bottom: 8px;
    line-height: 1;
  }
  .urgency-text {
    font-size: 12px;
    color: rgba(255,255,255,0.6);
    line-height: 1.6;
  }

  /* PPWR LIST */
  .ppwr-item {
    display: flex;
    gap: 10px;
    align-items: flex-start;
    margin-bottom: 12px;
    font-size: 13px;
    color: rgba(255,255,255,0.7);
    line-height: 1.5;
  }
  .ppwr-marker {
    font-weight: 700;
    color: white;
    flex-shrink: 0;
  }

  /* KEY TAKEAWAY */
  .key-box {
    background: rgba(244,246,249,0.07);
    border-left: 4px solid var(--amber);
    border-radius: 0 6px 6px 0;
    padding: 16px 18px;
    margin-top: 20px;
  }
  .key-box-tag {
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 2px;
    color: var(--amber);
    text-transform: uppercase;
    margin-bottom: 8px;
  }
  .key-box-text {
    font-size: 13px;
    color: rgba(255,255,255,0.7);
    line-height: 1.6;
  }

  /* TCO FORMULA */
  .tco-wrap {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 16px;
    margin: 32px 0;
    flex-wrap: wrap;
  }
  .tco-pill {
    background: var(--off);
    border: 2px solid var(--blue);
    border-radius: 12px;
    padding: 16px 24px;
    text-align: center;
    min-width: 160px;
  }
  .tco-pill-label {
    font-size: 10px;
    font-weight: 700;
    color: var(--sky);
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 4px;
  }
  .tco-pill-value {
    font-size: 13px;
    font-weight: 600;
    color: var(--navy);
  }
  .tco-result {
    background: var(--navy);
    border: 2px solid var(--sky);
    border-radius: 12px;
    padding: 16px 24px;
    text-align: center;
    min-width: 160px;
  }
  .tco-result-label {
    font-size: 10px;
    font-weight: 700;
    color: var(--amber);
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 4px;
  }
  .tco-result-value {
    font-size: 13px;
    font-weight: 600;
    color: white;
  }
  .tco-op {
    font-size: 28px;
    color: var(--grey);
    font-weight: 300;
  }

  /* EXAMPLE CARDS */
  .ex-card-standard {
    background: var(--off);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 20px;
  }
  .ex-card-better {
    background: #E8F8F2;
    border: 2px solid var(--teal);
    border-radius: 8px;
    padding: 20px;
  }
  .ex-tag-standard {
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 1px;
    color: var(--grey);
    text-transform: uppercase;
    margin-bottom: 8px;
  }
  .ex-tag-better {
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 1px;
    color: var(--teal);
    text-transform: uppercase;
    margin-bottom: 8px;
  }
  .ex-name {
    font-size: 15px;
    font-weight: 700;
    color: var(--navy);
    margin-bottom: 8px;
  }
  .ex-desc {
    font-size: 12px;
    color: var(--text);
    line-height: 1.6;
  }
  .ex-badge {
    display: inline-block;
    background: var(--teal);
    color: white;
    font-size: 9px;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 10px;
    margin-top: 8px;
    letter-spacing: 0.5px;
  }

  /* SOURCE REDUCTION */
  .sr-chain {
    background: var(--off);
    border-left: 4px solid var(--sky);
    border-radius: 0 8px 8px 0;
    padding: 16px 20px;
    margin: 20px 0;
  }
  .sr-chain-label {
    font-size: 9px;
    font-weight: 700;
    color: var(--navy);
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 8px;
  }
  .sr-chain-text {
    font-size: 13px;
    color: var(--text);
    font-weight: 500;
  }

  /* LOWER FEE STEPS */
  .step-card {
    background: white;
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 20px;
    display: flex;
    gap: 16px;
    transition: all 0.3s;
    margin-bottom: 10px;
  }
  .step-card:hover {
    border-color: var(--sky);
    box-shadow: 0 4px 12px rgba(0,147,208,0.1);
  }
  .step-num {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 40px;
    font-weight: 700;
    color: rgba(0,147,208,0.2);
    line-height: 1;
    flex-shrink: 0;
    width: 44px;
    transition: color 0.3s;
  }
  .step-card:hover .step-num { color: var(--sky); }
  .step-title {
    font-size: 14px;
    font-weight: 700;
    color: var(--navy);
    margin-bottom: 4px;
  }
  .step-desc {
    font-size: 12px;
    color: var(--grey);
    line-height: 1.6;
  }

  /* PCR ACHIEVEMENT */
  .pcr-box {
    background: #E8F8F2;
    border: 1px solid rgba(0,168,120,0.25);
    border-left: 4px solid var(--teal);
    border-radius: 0 8px 8px 0;
    padding: 20px;
    margin-bottom: 20px;
  }
  .pcr-tag {
    font-size: 9px;
    font-weight: 700;
    color: var(--teal);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 10px;
  }
  .pcr-stat-row {
    font-size: 13px;
    color: var(--text);
    margin-bottom: 6px;
    line-height: 1.5;
  }
  .pcr-stat-row b { color: var(--navy); }

  /* BENEFIT CARDS */
  .benefit-card {
    background: white;
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 10px;
    transition: all 0.3s;
  }
  .benefit-card:hover {
    border-color: var(--teal);
    box-shadow: 0 4px 12px rgba(0,168,120,0.1);
  }
  .benefit-title {
    font-size: 14px;
    font-weight: 700;
    color: var(--navy);
    margin-bottom: 6px;
  }
  .benefit-desc {
    font-size: 12px;
    color: var(--grey);
    line-height: 1.6;
  }

  /* DOS DONTS */
  .dd-header {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2px;
    margin-bottom: 2px;
  }
  .dd-do-head {
    background: #E2F7EE;
    color: var(--teal);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 10px 14px;
    border-radius: 6px 0 0 0;
  }
  .dd-dont-head {
    background: #FDEAEA;
    color: var(--red);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 10px 14px;
    border-radius: 0 6px 0 0;
  }
  .dd-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2px;
  }
  .dd-do {
    background: white;
    border-left: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
    padding: 10px 14px;
    font-size: 12px;
    color: var(--text);
    line-height: 1.5;
  }
  .dd-dont {
    background: white;
    border-right: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
    padding: 10px 14px;
    font-size: 12px;
    color: var(--text);
    line-height: 1.5;
  }

  /* REMEMBER */
  .remember-section {
    background: linear-gradient(135deg, var(--navy), var(--blue));
    padding: 64px 48px;
    text-align: center;
  }
  .remember-tag {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 3px;
    color: var(--amber);
    text-transform: uppercase;
    margin-bottom: 14px;
  }
  .remember-title {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 44px;
    font-weight: 800;
    color: white;
    text-transform: uppercase;
    line-height: 1.05;
    margin-bottom: 14px;
  }
  .remember-title span { color: var(--sky); }
  .remember-sub {
    font-size: 15px;
    color: rgba(255,255,255,0.6);
    max-width: 480px;
    margin: 0 auto 32px;
    line-height: 1.7;
  }
  .cta-btn {
    display: inline-block;
    background: var(--sky);
    color: white;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    text-decoration: none;
    padding: 13px 28px;
    border-radius: 4px;
    margin: 0 6px;
    transition: all 0.25s;
  }
  .cta-btn-outline {
    display: inline-block;
    background: transparent;
    color: rgba(255,255,255,0.8);
    border: 2px solid rgba(255,255,255,0.25);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    text-decoration: none;
    padding: 11px 28px;
    border-radius: 4px;
    margin: 0 6px;
  }

  /* FOOTER */
  .footer {
    background: #050F1E;
    padding: 24px 48px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid rgba(255,255,255,0.06);
  }
  .footer-brand {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 16px;
    font-weight: 800;
    letter-spacing: 4px;
    color: rgba(255,255,255,0.3);
    text-transform: uppercase;
  }
  .footer-note { font-size: 11px; color: rgba(255,255,255,0.2); }
  .footer-link { font-size: 11px; color: var(--sky); text-decoration: none; }

  /* DIVIDER */
  .divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.08), transparent);
  }
  .divider-light {
    height: 1px;
    background: var(--border);
    margin: 32px 0;
  }

  /* CENTER HEADER */
  .center-header { text-align: center; margin-bottom: 48px; }
</style>
""", unsafe_allow_html=True)

# ── NAV ─────────────────────────────────────────────────
st.markdown("""
<div class="nav-bar">
  <div class="nav-brand">Amcor</div>
  <div class="nav-links">
    <a href="#epr" class="nav-link">What is EPR</a>
    <a href="#tco" class="nav-link">True Cost</a>
    <a href="#source-reduction" class="nav-link">Source Reduction</a>
    <a href="#lower-fee" class="nav-link">Lower Your Fee</a>
    <a href="#amcor-helps" class="nav-link">How Amcor Helps</a>
    <a href="#dos-donts" class="nav-link">Dos & Don'ts</a>
    <a href="https://www.amcor.com/sustainability" target="_blank" class="nav-link nav-cta">Get Help</a>
  </div>
</div>
""", unsafe_allow_html=True)

# ── HERO ─────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-eyebrow">Extended Producer Responsibility · Customer Guide 2026</div>
  <div class="hero-title">Your Packaging Choices<br>Now Have a <span>Cost</span></div>
  <div class="hero-sub">New laws require brands to pay fees based on the packaging they use. Choosing the right packaging lowers that fee — here is everything you need to know.</div>
</div>
<div class="stats-strip">
  <div class="stat-item">
    <div class="stat-num">28%</div>
    <div class="stat-label">of U.S. PET bottles recycled — why EPR exists</div>
  </div>
  <div class="stat-item">
    <div class="stat-num">99.9%</div>
    <div class="stat-label">of Canadians covered by packaging laws</div>
  </div>
  <div class="stat-item">
    <div class="stat-num">Aug '26</div>
    <div class="stat-label">PPWR active in Europe right now</div>
  </div>
  <div class="stat-item">
    <div class="stat-num">2030</div>
    <div class="stat-label">all EU packaging must be recyclable</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── EPR SECTION ──────────────────────────────────────────
st.markdown('<div class="section section-dark" id="epr">', unsafe_allow_html=True)
st.markdown("""
<div class="center-header">
  <span class="section-tag">What Is EPR</span>
  <div class="section-title">You Now Pay for Your Packaging Waste</div>
  <div class="section-sub" style="margin:0 auto;">Governments in the U.S., Canada, and Europe now require brands to take financial responsibility for the packaging they put on the market.</div>
</div>
<div class="card-grid-3">
  <div class="fee-card">
    <div class="fee-card-num">01</div>
    <div class="fee-card-label">Units Sold</div>
    <div class="fee-card-desc">The more products you put on the market, the higher your base EPR fee</div>
  </div>
  <div class="fee-card">
    <div class="fee-card-num">02</div>
    <div class="fee-card-label">Package Weight</div>
    <div class="fee-card-desc">Heavier packaging means a higher fee — weight is the key variable in the calculation</div>
  </div>
  <div class="fee-card">
    <div class="fee-card-num">03</div>
    <div class="fee-card-label">Recyclability Score</div>
    <div class="fee-card-desc">Better recyclability means a lower fee — this is where packaging choices directly save money</div>
  </div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <span class="section-tag">Where These Laws Apply</span>
    <div class="region-card">
      <div>
        <div class="region-name">United States</div>
        <div class="region-desc">State by state, growing fast. Colorado, California, Maine, and Oregon already have active programs.</div>
      </div>
      <div class="region-date">Now → 2027</div>
    </div>
    <div class="region-card">
      <div>
        <div class="region-name">Canada</div>
        <div class="region-desc">99.9% of Canadians covered. Most provinces transitioning to fully producer-funded programs.</div>
      </div>
      <div class="region-date">2025 – 2027</div>
    </div>
    <div class="region-card" style="border-color:rgba(245,166,35,0.3);">
      <div>
        <div class="region-name">Europe</div>
        <div class="region-desc">Strictest globally — PPWR. Non-compliant packaging cannot be sold in Europe at all.</div>
      </div>
      <div class="region-date region-date-amber">Aug 2026</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <span class="section-tag">Europe — PPWR</span>
    <div style="font-family:'Barlow Condensed',sans-serif;font-size:28px;font-weight:800;color:white;text-transform:uppercase;margin-bottom:10px;">The Strictest Standard Globally</div>
    <div style="font-size:13px;color:rgba(255,255,255,0.6);line-height:1.7;margin-bottom:16px;">If you sell in Europe, the Packaging and Packaging Waste Regulation (PPWR) is already in force. Non-compliant packaging cannot be sold in Europe — this goes beyond fees.</div>
    <div class="urgency-box">
      <div class="urgency-tag">Active Right Now</div>
      <div class="urgency-date">12 August 2026</div>
      <div class="urgency-text">PPWR provisions are in force. Packaging decisions for European markets need to be made now — not later.</div>
    </div>
    <div class="ppwr-item"><span class="ppwr-marker">By 2030 —</span>&nbsp;all packaging sold in Europe must be recyclable</div>
    <div class="ppwr-item"><span class="ppwr-marker">Banned —</span>&nbsp;single-use plastic sachets and individual condiment portions</div>
    <div class="ppwr-item"><span class="ppwr-marker">Required —</span>&nbsp;brands must increase recycled content and reduce new plastic use</div>
    <div class="ppwr-item"><span class="ppwr-marker">Restricted —</span>&nbsp;certain chemicals in food-contact packaging above set limits</div>
    <div class="key-box">
      <div class="key-box-tag">Key Takeaway</div>
      <div class="key-box-text">What Europe requires today is where U.S. and Canadian regulations are heading. Planning ahead protects your brand and your bottom line.</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── TCO SECTION ──────────────────────────────────────────
st.markdown('<div class="section section-light" id="tco">', unsafe_allow_html=True)
st.markdown("""
<div class="center-header">
  <span class="section-tag" style="color:var(--blue);">Total Cost of Ownership</span>
  <div class="section-title-dark">The Real Price of Your Packaging</div>
  <div class="section-sub-dark" style="margin:0 auto;">Most brands only look at upfront material cost. Under EPR, the true cost of packaging includes the EPR fee on top. Cheaper packaging today can mean a higher fee tomorrow.</div>
</div>
<div class="tco-wrap">
  <div class="tco-pill">
    <div class="tco-pill-label">Customer's Price</div>
    <div class="tco-pill-value">What you pay for the material</div>
  </div>
  <div class="tco-op">+</div>
  <div class="tco-pill">
    <div class="tco-pill-label">EPR Fee (based on weight)</div>
    <div class="tco-pill-value">Fee charged by the government</div>
  </div>
  <div class="tco-op">=</div>
  <div class="tco-result">
    <div class="tco-result-label">True Total Cost</div>
    <div class="tco-result-value">What you actually pay</div>
  </div>
</div>
<div class="card-grid-2" style="max-width:700px;margin:0 auto;">
  <div class="ex-card-standard">
    <div class="ex-tag-standard">Standard Option</div>
    <div class="ex-name">Hard-to-Recycle Mixed Pouch</div>
    <div class="ex-desc">Lower material cost upfront. But mixed materials score poorly under EPR — resulting in a higher government fee and a higher true total cost.</div>
  </div>
  <div class="ex-card-better">
    <div class="ex-tag-better">Better True Cost</div>
    <div class="ex-name">Recyclable Single-Material Pouch</div>
    <div class="ex-desc">Recyclable single material scores better under EPR. Lower fee means lower true total cost — the smarter choice over time.</div>
    <div class="ex-badge">Lower Total Cost</div>
  </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="divider-light"></div>', unsafe_allow_html=True)

# ── SOURCE REDUCTION ─────────────────────────────────────
st.markdown('<div class="section section-mid" id="source-reduction">', unsafe_allow_html=True)
st.markdown("""
<div class="center-header">
  <span class="section-tag" style="color:var(--blue);">Source Reduction</span>
  <div class="section-title-dark">Less Packaging. Lower Fee.</div>
  <div class="section-sub-dark" style="margin:0 auto;">Source reduction means using less packaging material overall. Less material means less weight — and since your EPR fee is based on weight, reducing your packaging directly reduces your fee.</div>
</div>
<div class="sr-chain" style="max-width:700px;margin:0 auto;">
  <div class="sr-chain-label">The Source Reduction Chain</div>
  <div class="sr-chain-text">Reduce packaging material &nbsp;<b>→</b>&nbsp; Lower weight &nbsp;<b>→</b>&nbsp; Lower EPR fee &nbsp;<b>→</b>&nbsp; Lower true total cost</div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── LOWER YOUR FEE ───────────────────────────────────────
st.markdown('<div class="section section-light" id="lower-fee">', unsafe_allow_html=True)
st.markdown("""
<div class="center-header">
  <span class="section-tag" style="color:var(--blue);">Action Guide</span>
  <div class="section-title-dark">4 Ways to Lower Your Fee</div>
  <div class="section-sub-dark" style="margin:0 auto;">These are the four levers your brand can pull to actively reduce your EPR fees starting today.</div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
steps = [
    ("01", "Switch to Recyclable Packaging", "The more recyclable your packaging is, the better it scores under EPR fee calculations — directly lowering your fee."),
    ("02", "Use Packaging With Recycled Content", "Packaging containing post-consumer recycled material qualifies for fee reductions in most U.S. states, Canadian provinces, and under PPWR in Europe."),
    ("03", "Reduce Packaging Weight", "EPR fees are based on weight. Less material means lower weight means a lower fee baseline across every single unit you sell."),
    ("04", "Choose Single-Material Packaging", "Mixed materials are harder to recycle and score poorly. Single-material packaging scores better and earns a lower fee."),
]
for i, (num, title, desc) in enumerate(steps):
    with col1 if i % 2 == 0 else col2:
        st.markdown(f"""
        <div class="step-card">
          <div class="step-num">{num}</div>
          <div>
            <div class="step-title">{title}</div>
            <div class="step-desc">{desc}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ── AMCOR HELPS ──────────────────────────────────────────
st.markdown('<div class="section section-mid" id="amcor-helps">', unsafe_allow_html=True)
st.markdown("""
<div class="center-header">
  <span class="section-tag" style="color:var(--blue);">How Amcor Helps</span>
  <div class="section-title-dark">Packaging That Lowers Your Fee</div>
  <div class="section-sub-dark" style="margin:0 auto;">Amcor sources recycled plastic directly from recycling companies and incorporates post-consumer recycled (PCR) material into packaging — primarily bottles — to help brands lower their EPR fees.</div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="pcr-box">
      <div class="pcr-tag">Amcor's PCR Achievement</div>
      <div class="pcr-stat-row"><b>10% PCR</b> global target achieved — 218,000 metric tons of recycled plastic used</div>
      <div class="pcr-stat-row"><b>100%</b> recycled plastic possible depending on your packaging needs</div>
      <div class="pcr-stat-row"><b>96%</b> of rigid packaging portfolio designed for recyclability</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    for title, desc in [
        ("Lowers Your EPR Fee", "Packaging with recycled content scores better under EPR fee calculations — directly reducing how much you pay per unit."),
        ("Meets Requirements Globally", "PCR content satisfies recycled content requirements in the U.S., Canada, and under PPWR in Europe — one solution across all markets."),
        ("Less New Plastic Used", "Every unit of PCR replaces new plastic — reducing your environmental footprint and supporting a circular economy."),
    ]:
        st.markdown(f"""
        <div class="benefit-card">
          <div class="benefit-title">{title}</div>
          <div class="benefit-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""<div style="text-align:center;margin-top:32px;">
  <a href="https://www.amcor.com/sustainability" target="_blank" class="cta-btn">Explore Amcor's Sustainability Solutions</a>
</div>""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── DOS AND DONTS ────────────────────────────────────────
st.markdown('<div class="section section-light" id="dos-donts">', unsafe_allow_html=True)
st.markdown("""
<div class="center-header">
  <span class="section-tag" style="color:var(--blue);">Quick Reference</span>
  <div class="section-title-dark">Dos & Don'ts</div>
  <div class="section-sub-dark" style="margin:0 auto;">The most important actions and mistakes when navigating EPR regulations and packaging decisions.</div>
</div>
<div style="max-width:800px;margin:0 auto;">
  <div class="dd-header">
    <div class="dd-do-head">DO</div>
    <div class="dd-dont-head">DON'T</div>
  </div>
  <div class="dd-grid">
    <div class="dd-do">Start thinking about EPR fees early in your packaging decisions</div>
    <div class="dd-dont">Wait until a deadline — fees and penalties add up fast</div>
    <div class="dd-do">Choose recyclable or recycled-content packaging to lower your fee</div>
    <div class="dd-dont">Assume the same rules apply in every state, province, or country</div>
    <div class="dd-do">Reduce packaging weight wherever possible — it lowers the fee directly</div>
    <div class="dd-dont">Focus only on upfront material cost — always calculate the true total</div>
    <div class="dd-do">Ask Amcor which PCR options help lower your specific EPR fees</div>
    <div class="dd-dont">Ignore PPWR if you sell globally — it affects your full product range</div>
  </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── REMEMBER ─────────────────────────────────────────────
st.markdown("""
<div class="remember-section">
  <div class="remember-tag">Remember</div>
  <div class="remember-title">Reduce your EPR fees, meet compliance,<br>and build a more <span>sustainable brand</span> — with Amcor</div>
  <div class="remember-sub">Amcor's team is ready to help you find the right packaging solution for your products, your markets, and your budget.</div>
  <a href="https://www.amcor.com/sustainability" target="_blank" class="cta-btn">Talk to Amcor Today</a>
  <a href="https://www.amcor.com/products" target="_blank" class="cta-btn-outline">Explore Our Products</a>
</div>
""", unsafe_allow_html=True)

# ── FOOTER ───────────────────────────────────────────────
st.markdown("""
<div class="footer">
  <div class="footer-brand">Amcor</div>
  <div class="footer-note">Customer Guide · Extended Producer Responsibility · 2026</div>
  <a href="https://www.amcor.com/sustainability" target="_blank" class="footer-link">amcor.com/sustainability</a>
</div>
""", unsafe_allow_html=True)
