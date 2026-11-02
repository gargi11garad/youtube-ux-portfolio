import streamlit as st

st.set_page_config(page_title="YouTube UX · Portfolio", page_icon="✳", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');
:root{--bg:#111214;--panel:#1a1c20;--line:#303238;--muted:#a3a5ad;--ink:#f5f4f1;--lime:#d5f17a;--red:#ff6576;--blue:#8db9ff;--lav:#bb9cff}
html,body,[class*="css"]{font-family:'DM Sans',sans-serif;color:var(--ink)}
.stApp{background:radial-gradient(ellipse at 75% 0%,#2b2730 0%,#111214 45%);color:var(--ink)}
#MainMenu,footer,header{visibility:hidden}.block-container{max-width:1450px;padding:1.35rem 2.3rem 3.2rem}
h1,h2,h3{font-family:'Space Grotesk',sans-serif;letter-spacing:-.05em}h1{font-size:3.3rem!important;line-height:1.03!important;margin:.35rem 0 .8rem!important}h2{font-size:1.65rem!important}h3{font-size:1.12rem!important}
.brand{font-family:'Space Grotesk';font-weight:700;font-size:1.16rem;letter-spacing:-.04em}.brand b{color:var(--lime)}
.top{display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid var(--line);padding-bottom:1rem;margin-bottom:1.6rem}
.eyebrow{color:var(--lime);font-size:.72rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase}.muted{color:var(--muted);line-height:1.6}
.hero{border:1px solid #45414b;border-radius:24px;padding:40px 42px;min-height:310px;display:flex;align-items:end;position:relative;overflow:hidden;background:radial-gradient(ellipse at 82% 27%,#b992f466,transparent 28%),radial-gradient(ellipse at 73% 30%,#83934e44,transparent 55%),linear-gradient(130deg,#252329,#27242d 62%,#31302a)}
.hero:after{content:'✳';position:absolute;right:6%;top:-44px;font-size:19rem;color:#ffffff09;transform:rotate(-18deg)}.hero-inner{position:relative;z-index:1;max-width:760px}
.hero p{font-size:1.08rem;color:#d6d3d0;line-height:1.65;max-width:700px}.badge{display:inline-block;border:1px solid #ffffff30;background:#ffffff12;border-radius:100px;padding:6px 11px;font-size:.76rem;margin-right:6px;color:#e8e5e1}
.case-card{border:1px solid #34363c;border-radius:19px;overflow:hidden;background:linear-gradient(145deg,#1d1f23,#17181b);height:100%}.cover{height:155px;padding:17px 19px;position:relative;display:flex;align-items:end;overflow:hidden}.cover:before{content:'';position:absolute;inset:0;background:linear-gradient(180deg,transparent,#0c0d10ba)}.cover-title{z-index:1;position:relative;font-family:'Space Grotesk';font-size:1.15rem;font-weight:700;line-height:1.1}.c1{background:radial-gradient(ellipse at 70% 15%,#d9788c,#61405f 48%,#211d2d)}.c2{background:radial-gradient(ellipse at 70% 15%,#e28a5c,#61404a 50%,#211c29)}.c3{background:radial-gradient(ellipse at 70% 15%,#7496cf,#384a74 48%,#1a1d2b)}
.card-body{padding:18px 19px}.card-label{color:var(--lime);font-size:.7rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase}.tag{display:inline-block;border:1px solid #3c3e44;border-radius:100px;padding:4px 9px;color:#c7c8ce;font-size:.72rem;margin:5px 4px 0 0}
.panel{background:linear-gradient(145deg,#1b1d21,#17181b);border:1px solid #303238;border-radius:17px;padding:20px 22px}.quote{border-left:3px solid var(--lime);padding:4px 0 4px 16px;font-size:1.12rem;color:#e6e3df;line-height:1.5}
.flow{display:flex;align-items:center;gap:8px;flex-wrap:wrap}.step{border:1px solid #45464b;border-radius:11px;padding:10px 13px;background:#202227;color:#efeeec;font-size:.85rem}.arrow{color:var(--lime);font-size:1.2rem}
.decision{padding:15px 0;border-top:1px solid #303238}.decision:first-child{border-top:0}.decision b{color:#f5f4f1}.decision .muted{font-size:.9rem;margin-top:5px}
div[data-testid="stButton"]>button,div[data-testid="stLinkButton"]>a{border-radius:100px;border:1px solid #46484e;background:#202227;color:#f5f4f1;font-weight:600;min-height:2.8rem}
div[data-testid="stButton"]>button:hover,div[data-testid="stLinkButton"]>a:hover{border-color:var(--lime);color:var(--lime)}button[kind="primary"]{background:var(--lime)!important;color:#141610!important;border-color:var(--lime)!important}
div[role="radiogroup"]{gap:.5rem}div[role="radiogroup"] label{background:#191a1e;border:1px solid #36383f;border-radius:100px;padding:.42rem .9rem!important}
.foot{border-top:1px solid var(--line);padding-top:15px;margin-top:30px;color:var(--muted);font-size:.83rem}
@media(max-width:800px){.block-container{padding-left:1rem;padding-right:1rem}h1{font-size:2.35rem!important}.hero{padding:25px;min-height:290px}}
</style>
""", unsafe_allow_html=True)

CASES={
 "Shorts · Accessibility":{
  "num":"01","title":"Shorts, on your terms.","subtitle":"A short-form video experience with more control and less friction.","class":"c1","project":"YouTube Shorts — User experience & accessibility","problem":"Short-form feeds make discovery effortless, but important controls can be hard to find. Captions, playback, recommendations, and saved videos often feel separate from the watching experience.","opportunity":"How might we help viewers shape what they see, access the controls they need, and keep the Shorts they want to revisit?","audience":"Viewers who rely on captions, people who want more control over recommendations, and anyone saving useful or entertaining Shorts for later.","flow":["Tune interests","Browse feed","Adjust playback / captions","Save to a collection"],"decisions":[("Keep key controls beside the video","Captions, playback, and next-video actions are visible at the point of use."),("Make recommendations adjustable","A small preference control gives viewers a legible way to ask for more, less, or a balanced mix."),("Turn saves into a library","Saved Shorts have a destination and a collection context, so saving has a clear payoff.")],"principles":["Captions are one tap away","Playback actions are grouped","Preference changes are reversible","No essential state is conveyed by color alone"],"tradeoff":"The prototype demonstrates the interaction model with sample content. It does not connect to YouTube accounts, real recommendation signals, or persistent collections.","demo":"https://youtube-shorts-accessibility-redesign-bfgycrdcb26ntn4artf4ph.streamlit.app/","repo":"https://github.com/gargi11garad/youtube-shorts-accessibility-redesign","tags":["Accessibility","Mobile","Interaction design"]},
 "Creator Studio · Analytics":{
  "num":"02","title":"Creator Studio, made clearer.","subtitle":"Turn a wall of channel metrics into a quick read and a useful next step.","class":"c2","project":"Creator Studio — Analytics dashboard UX redesign","problem":"Creators encounter views, impressions, watch time, subscriber change, and traffic sources together. A new creator can struggle to tell which numbers matter or what to do next.","opportunity":"How might we help creators understand performance at a glance, compare content, and connect metrics to clear actions?","audience":"Independent and emerging creators who need a quick performance check without advanced analytics expertise.","flow":["Choose a time period","Scan channel health","Compare top videos","Read a practical takeaway"],"decisions":[("Lead with a small KPI set","Views, watch time, subscribers, and impressions establish a quick overview before deeper analysis."),("Pair charts with plain-language meaning","Each visualization answers a focused question, with an accompanying insight in everyday language."),("Keep comparisons close to action","Top-video performance and next-step guidance sit in the same reading path.")],"principles":["Label units and comparison periods","Use readable number abbreviations","Show trend direction with text and color","Keep synthetic data clearly identified"],"tradeoff":"Metrics are synthetic demo data. The concept does not connect to YouTube Analytics or validate correlations against a real channel.","demo":"https://creator-studio-analytics-dashboard-dtnsbj3eabczjktvugnakp.streamlit.app/","repo":"https://github.com/gargi11garad/creator-studio-analytics-dashboard","tags":["Dashboard design","Data visualization","Responsive"]},
 "YouTube TV · Discovery":{
  "num":"03","title":"YouTube TV, from the couch.","subtitle":"Make discovery comfortable with a remote, a larger screen, and more than one viewer.","class":"c3","project":"YouTube TV — Smart content discovery & navigation","problem":"Browsing on television is slower than on mobile when the interface assumes precise pointer input, dense menus, or long text entry. Household preferences and watch-later picks can also get lost.","opportunity":"How might we make it easier to find something good, move through the interface from across the room, and save choices for later?","audience":"People browsing on a Smart TV with a directional remote, including households making a shared viewing choice.","flow":["Scan recommendation rows","Open a title","Play or save","Return to My List"],"decisions":[("Design for focus, not hover","Large targets and clear focus states support directional remote navigation."),("Make browsing the default","Home rows, genre search, and clear title details reduce reliance on text entry."),("Give saving a dependable home","My List keeps picks together and supports a cross-device mental model.")],"principles":["Large, high-contrast controls","Short labels and scannable rows","Remote keyboard navigation","Preferences for text size and reduced motion"],"tradeoff":"This is a web-based interaction concept. Real TV remote behavior, device safe areas, and account synchronization need validation on target hardware.","demo":"https://youtube-tv-smart-discovery-jriu6jebkzlbaategfvzrl.streamlit.app/","repo":"https://github.com/gargi11garad/youtube-tv-smart-discovery","tags":["Smart TV","Cross-platform","Remote UX"]},
}

top1,top2=st.columns([1,2.4])
with top1: st.markdown('<div class="brand">✳ YouTube <b>UX portfolio</b></div>',unsafe_allow_html=True)
with top2: page=st.radio("Portfolio navigation",["Overview"]+list(CASES.keys())+["Design system"],horizontal=True,label_visibility="collapsed",key="nav")

if page=="Overview":
 st.markdown('<div class="hero"><div class="hero-inner"><span class="badge">PRODUCT DESIGN · 3 CONCEPT CASE STUDIES</span><span class="badge">INTERACTION · ACCESSIBILITY · DATA</span><h1>Designing YouTube<br>for the moments around the video.</h1><p>Three connected product concepts explore how viewers discover, watch, save, and understand content—on mobile, on TV, and in the creator studio.</p></div></div>',unsafe_allow_html=True)
 st.write("")
 st.markdown('<div class="eyebrow">ONE PRODUCT ECOSYSTEM · THREE ENTRY POINTS</div><h2 style="margin-top:8px">Make the next step feel obvious.</h2><p class="muted">The work follows the same design question across different contexts: what does this person need to understand or do next?</p>',unsafe_allow_html=True)
 cols=st.columns(3,gap="medium")
 for col,(name,item) in zip(cols,CASES.items()):
  with col:
   st.markdown(f'<div class="case-card"><div class="cover {item["class"]}"><div class="cover-title">{item["num"]}　{item["title"]}</div></div><div class="card-body"><div class="card-label">{item["project"]}</div><p class="muted">{item["subtitle"]}</p>{"".join(f"<span class='tag'>{tag}</span>" for tag in item["tags"])}</div></div>',unsafe_allow_html=True)
   if st.button("Read case study →",key=f"open_{item['num']}",use_container_width=True): st.session_state.nav=name; st.rerun()
 st.write("")
 left,right=st.columns([1.3,1],gap="large")
 with left:
  st.markdown('<div class="panel"><div class="eyebrow">PORTFOLIO THROUGH-LINE</div><h2>Reduce the work between intent and action.</h2><div class="quote">Help people understand where they are, what they can do, and what happens next.</div><div style="margin-top:15px" class="muted">On Shorts, that means accessible playback and adjustable discovery. In Creator Studio, it means turning metrics into meaning. On TV, it means moving confidently with a remote.</div></div>',unsafe_allow_html=True)
 with right:
  st.markdown('<div class="panel"><div class="eyebrow">HOW TO READ THESE CONCEPTS</div><h2>Clear scope, honest evidence.</h2><div class="muted">These are design concepts with working front-end prototypes and synthetic example content. No claims of completed interviews, usability tests, or production analytics are made. Each case study documents the design rationale and the validation that should happen next.</div></div>',unsafe_allow_html=True)
 st.markdown('<div class="section-head"><div><h2>Interactive prototypes</h2><div class="muted">Open each deployed concept in a new tab.</div></div></div>',unsafe_allow_html=True)
 demos=st.columns(3)
 for col,(name,item) in zip(demos,CASES.items()):
  with col: st.link_button(f"Open {item['num']} · {item['project']}",item["demo"],use_container_width=True)

elif page in CASES:
 c=CASES[page]
 st.markdown(f'<div class="eyebrow">CASE STUDY {c["num"]} / 03 · {c["project"].upper()}</div><h1>{c["title"]}</h1><p class="muted" style="font-size:1.1rem">{c["subtitle"]}</p>',unsafe_allow_html=True)
 a,b=st.columns([1.25,1],gap="large")
 with a:
  st.markdown('<div class="panel"><div class="eyebrow">THE PROBLEM</div><h2>What needs to get easier?</h2><div class="muted">'+c["problem"]+'</div><div class="eyebrow" style="margin-top:18px">DESIGN QUESTION</div><div class="quote" style="margin-top:8px">'+c["opportunity"]+'</div></div>',unsafe_allow_html=True)
 with b:
  st.markdown('<div class="panel"><div class="eyebrow">PRIMARY AUDIENCE</div><div class="muted" style="margin-top:10px">'+c["audience"]+'</div><div class="eyebrow" style="margin-top:22px">SUCCESS LOOKS LIKE</div><div class="muted" style="margin-top:10px">A person can complete the main task without hunting for a control, decoding a dense dashboard, or entering unnecessary text.</div></div>',unsafe_allow_html=True)
 st.markdown('<div class="section-head"><div><div class="eyebrow">CORE USER FLOW</div><h2>From intent to outcome</h2></div></div>',unsafe_allow_html=True)
 flow="<div class='flow'>"+" <span class='arrow'>→</span> ".join(f"<span class='step'>{x}</span>" for x in c["flow"])+"</div>"
 st.markdown(flow,unsafe_allow_html=True)
 st.markdown('<div class="section-head"><div><div class="eyebrow">DESIGN DECISIONS</div><h2>Why the interface works this way</h2></div></div>',unsafe_allow_html=True)
 left,right=st.columns([1.1,1],gap="large")
 with left:
  st.markdown('<div class="panel">'+"".join(f"<div class='decision'><b>{title}</b><div class='muted'>{copy}</div></div>" for title,copy in c["decisions"])+"</div>",unsafe_allow_html=True)
 with right:
  st.markdown('<div class="panel"><div class="eyebrow">ACCESSIBILITY & INTERACTION PRINCIPLES</div>'+"".join(f"<div class='decision'><b>✓　{principle}</b></div>" for principle in c["principles"])+"</div>",unsafe_allow_html=True)
 st.markdown('<div class="section-head"><div><div class="eyebrow">SCOPE & NEXT VALIDATION</div><h2>What this prototype proves—and what it does not</h2></div></div>',unsafe_allow_html=True)
 l,r=st.columns(2,gap="large")
 with l: st.markdown(f'<div class="panel"><div class="eyebrow">CURRENT LIMITATION</div><div class="muted" style="margin-top:10px">{c["tradeoff"]}</div></div>',unsafe_allow_html=True)
 with r: st.markdown('<div class="panel"><div class="eyebrow">NEXT RESEARCH STEP</div><div class="muted" style="margin-top:10px">Test the primary task with 5–7 people from the intended audience. Observe success rate, time to first action, mis-taps or navigation errors, and confidence after the task. Follow with accessibility review using keyboard, screen reader, captions, and target device checks.</div></div>',unsafe_allow_html=True)
 b1,b2=st.columns([1,1])
 with b1: st.link_button("Open interactive prototype ↗",c["demo"],type="primary",use_container_width=True)
 with b2: st.link_button("View source on GitHub ↗",c["repo"],use_container_width=True)

else:
 st.markdown('<div class="eyebrow">SHARED PRODUCT PRINCIPLES</div><h1>A small system for clear decisions.</h1><p class="muted">The three concepts use one consistent set of principles, adapted to each screen and input method.</p>',unsafe_allow_html=True)
 left,right=st.columns(2,gap="large")
 with left:
  st.markdown('<div class="panel"><h2>Interaction model</h2>'+"".join(f"<div class='decision'><b>{a}</b><div class='muted'>{b}</div></div>" for a,b in [("Make the next step visible","Group primary actions near the content or metric they affect."),("Keep navigation predictable","Use stable destinations: For you, Explore, Saved; Overview, Content, Audience; Home, Search, My List."),("Give feedback after actions","Confirm when a video is saved, a setting changes, or a choice is selected."),("Preserve control","Preferences and filters are reversible and user-directed.")])+"</div>",unsafe_allow_html=True)
 with right:
  st.markdown('<div class="panel"><h2>Accessibility and technical scope</h2>'+"".join(f"<div class='decision'><b>{a}</b><div class='muted'>{b}</div></div>" for a,b in [("Readable hierarchy","Use clear page titles, labels, units, and short supporting text."),("Input-aware controls","Touch-sized buttons on mobile, large focusable targets on TV, direct toggles on dashboard settings."),("Accessible chart context","Pair color with text, describe the chart question, and retain tabular values where possible."),("Honest prototype data","Mark sample titles and metrics as synthetic; avoid implying real account access.")])+"</div>",unsafe_allow_html=True)
 st.markdown('<div class="section-head"><div><div class="eyebrow">FUTURE VALIDATION PLAN</div><h2>How I would evaluate the design</h2></div></div>',unsafe_allow_html=True)
 st.dataframe([{"Study":"Shorts controls","Tasks":"Turn on captions, adjust playback, tune a recommendation, save a Short","Signals":"Task success, time, errors, perceived control"},{"Study":"Creator analytics","Tasks":"Identify the strongest video and one next action","Signals":"Metric comprehension, time to insight, confidence"},{"Study":"TV discovery","Tasks":"Find a genre, open a title, save it, return to My List","Signals":"Remote steps, focus loss, search reliance, task completion"}],hide_index=True,use_container_width=True)

st.markdown('<div class="foot">YouTube UX portfolio · Independent concept work · All prototype content and analytics are illustrative; not affiliated with YouTube.</div>',unsafe_allow_html=True)
