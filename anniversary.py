"""Anniversary gift app. Run: python -m streamlit run anniversary.py
Put couple1..couple5 images alongside this file (.jpg/.jpeg/.png/.webp).
"""
import base64
import json
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

BASE_DIR = Path(__file__).resolve().parent
PIN = "182022"  # Anniversary access code (decorative, not secure authentication)

# Edit each caption here.
MEMORY_CAPTIONS = [
    "ကိုကိုတို့နှစ်ယောက်ရဲ့ ပထမဆုံးအမှတ်တရလေး ❤️",
    "ရှက်ရှက်နဲ့ အတူတူ ပြုံးခဲ့ကြတဲ့ နေ့လေး 💕",
    "အလွမ်းတွေနဲ့ ပြန်ဆုံရတဲ့ နေ့လေး✨",
    "အမြဲသတိရနေမယ့် အခိုက်အတန့် 🌷",
    "နောင်နှစ်ပေါင်းများစွာလည်း အတူတူရှိကြမယ် 💖",
]
LETTER = """Happy 4 Years & 4 Months Anniversary ပါ ခလေးလေးရေ… ❤️

သဲသဲနဲ့စတွေ့ခဲ့တဲ့နေ့ကနေ ဒီနေ့အထိ အတူဖြတ်သန်းခဲ့တဲ့ အချိန်တိုင်းဟာ ကိုကိုတို့အတွက် အဖိုးတန်ဆုံး အမှတ်တရတွေပါ။

တစ်ခါတလေ အဆင်မပြေတဲ့အချိန်တွေ ရှိခဲ့ပေမယ့် ကိုကိုတို့နှစ်ယောက် အတူရှိနေသရွေ့ အရာအားလုံးကို ကျော်ဖြတ်နိုင်မယ်လို့ ယုံကြည်တယ်။

နောက်လာမယ့် နှစ်ပေါင်းများစွာကိုလည်း သဲသဲနဲ့ပဲ အတူလျှောက်လှမ်းချင်တယ်။ အမြဲတမ်းချစ်တယ်နော် ခလေးလေးရေ။ 💕"""

st.set_page_config(page_title="Happy Anniversary ❤️", page_icon="💞", layout="centered", initial_sidebar_state="collapsed")
st.markdown("""<style>
#MainMenu,header,footer {visibility:hidden}
.stApp{background:#f8f3ee}.block-container{padding:0;max-width:100%}
iframe{display:block}
</style>""",unsafe_allow_html=True)


def image_data(stem):
    for ext in (".jpg", ".jpeg", ".png", ".webp", ".gif"):
        for candidate in (BASE_DIR / (stem + ext), BASE_DIR / (stem + ext.upper())):
            if candidate.is_file():
                mime = "image/jpeg" if ext in (".jpg", ".jpeg") else f"image/{ext[1:]}"
                return f"data:{mime};base64,{base64.b64encode(candidate.read_bytes()).decode('ascii')}"
    return ""

images = {name: image_data(name) for name in ["Happy_birthday", "couple", *(f"couple{i}" for i in range(1, 6))]}
# If couple1..5 do not exist yet, show a placeholder instead of failing.
config = {
    "pin": PIN,
    "images": images,
    "captions": MEMORY_CAPTIONS,
    "letter": LETTER,
}

page = r'''<!doctype html><html lang="my"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=no"/>
<style>
:root{--ink:#402329;--gold:#b18b3b;--wine:#602e3a;--paper:#fffefa;--muted:#83716d}
*{box-sizing:border-box}html,body{margin:0;min-height:100%;font-family:'Segoe UI','Myanmar Text','Noto Sans Myanmar',sans-serif;color:var(--ink)}
body{background:radial-gradient(circle at 50% 15%,#fffdf8 0%,#f7eee9 60%,#eadbd8 100%);overflow:hidden}
#app{height:100dvh;min-height:560px;max-width:580px;margin:0 auto;position:relative;overflow:hidden;padding:18px 16px 32px}
.scene{height:100%;display:none;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:14px;animation:appear .6s both}
.scene.active{display:flex}.serif{font-family:Georgia,'Times New Roman',serif}.hero{font-size:clamp(31px,7vw,45px);line-height:1.15;margin:4px 0 8px}.sub{font-size:14px;line-height:1.9;margin:0;max-width:95%}
.starline{color:var(--gold);letter-spacing:12px;margin:4px auto}.heart{font-size:78px;color:#fff;filter:drop-shadow(0 12px 18px #b8a8a4);animation:pulse 2.3s ease-in-out infinite}
.gold{color:var(--gold)}.primary{border:1px solid #bba198;background:linear-gradient(#f5e1d9,#d9b8ae);color:#fff;border-radius:100px;padding:13px 32px;min-width:190px;font-weight:700;cursor:pointer;box-shadow:0 5px 12px #d9c4b7}.primary:active,.iconbtn:active{transform:scale(.97)}
.card{width:min(100%,380px);border:1px solid #b3a16e;border-radius:36px;background:#fffefaad;padding:30px 23px;box-shadow:0 16px 55px #bba4a31c}
.pin-dots{display:flex;justify-content:center;gap:10px;margin:19px 0}.pin-dot{width:48px;height:55px;border:1px solid #948c80;border-radius:15px;display:grid;place-items:center;background:linear-gradient(#fff,#f5f4ec);font-size:22px;color:var(--gold)}
.keypad{display:grid;grid-template-columns:repeat(3,1fr);gap:9px}.key{border:1px solid #a99c83;border-bottom:4px solid #af8f4a;border-radius:15px;background:linear-gradient(170deg,#fff,#eeeae1);font-family:Georgia,serif;font-size:22px;font-weight:bold;height:56px;color:#292222;cursor:pointer}.key.small{font:700 12px 'Segoe UI',sans-serif;color:#82612c}.error{color:#bf4c5e;min-height:20px;font-size:12px}
.cake{position:relative;display:flex;align-items:end;justify-content:center;width:275px;height:260px;cursor:pointer;touch-action:manipulation;user-select:none;filter:drop-shadow(0 15px 8px #a68c7430)}
.tier{position:absolute;border:1.5px solid #a6a27e;border-radius:12px 12px 9px 9px;background:linear-gradient(170deg,#f8f8e8,#eceac1);box-shadow:inset 0 -10px 12px #d8d6ab}.tier:after{content:'• • • • •';position:absolute;inset:35% 0 auto;text-align:center;color:#ab9144;font-size:19px;letter-spacing:6px}.tier.bottom{bottom:16px;width:230px;height:68px}.tier.middle{bottom:76px;width:180px;height:58px}.tier.top{bottom:127px;width:130px;height:50px}
.candle{position:absolute;bottom:173px;width:11px;height:62px;border-radius:3px;background:repeating-linear-gradient(45deg,#e9e5c4 0 7px,#cab784 7px 10px)}
.flame{position:absolute;left:-6px;top:-28px;width:23px;height:32px;border-radius:70% 10% 65% 65%;transform:rotate(-45deg);background:radial-gradient(circle at 60% 68%,#fff 8%,#ffdf75 28%,#ffa52c 70%,#ed722a);box-shadow:0 0 18px #fca92c;animation:flicker .25s infinite alternate}
.smoke{position:absolute;top:-26px;left:-4px;width:18px;height:30px;border-radius:50%;filter:blur(6px);opacity:0;background:#a4a2a1}.out .flame{display:none}.out .smoke{animation:smoke 2.4s both}.helper{color:#796864;font-size:13px;line-height:1.8}
.ring{width:202px;height:202px;border:4px solid #e6e2dc;border-top-color:var(--gold);border-radius:50%;display:grid;place-items:center;animation:spin 5s linear forwards}.ring .heart{animation:counterspin 5s linear forwards;font-size:65px}
.giftrow{display:flex;justify-content:center;gap:24px;margin-top:32px}.gift{background:#fffef5;border:1.5px solid #aa966a;border-radius:50%;width:115px;height:115px;display:grid;place-items:center;font-size:51px;color:var(--gold);cursor:pointer}.gift-label{font-weight:600;margin-top:9px}.dialog{position:absolute;inset:10px;display:none;flex-direction:column;justify-content:center;background:#f1e7e0a8;backdrop-filter:blur(12px);padding:12px;z-index:10}.dialog.show{display:flex}.paper{position:relative;background:var(--paper);border:1px solid #d9d1bd;border-radius:28px;padding:27px 18px 16px;width:100%;max-height:86%;display:flex;flex-direction:column;text-align:left;box-shadow:0 12px 35px #73605b33}.paper h2{margin:0 34px 15px 4px;font-size:24px}.close{position:absolute;right:12px;top:12px;width:36px;height:36px;border-radius:50%;border:1px solid #ddd5c9;background:#fff;font-size:24px;color:#81716b;cursor:pointer}.scroll{overflow:auto;flex:1;padding:7px 7px 12px;line-height:2;white-space:pre-wrap;font-size:14px}.fullbtn{width:100%;background:var(--wine);border:0;color:#fff;border-radius:40px;padding:14px;margin-top:12px;cursor:pointer;font-weight:700}
.memory{border-radius:17px;background:white;border:1px solid #eee7db;padding:9px;margin-bottom:17px;box-shadow:0 5px 18px #b3aba222;white-space:normal}.memory img{display:block;width:100%;max-height:350px;object-fit:contain;border-radius:11px;background:#f4eee8}.memory figcaption{padding:11px 4px 5px;text-align:center;font-size:13px;color:#60454a;line-height:1.8}.placeholder{height:140px;display:grid;place-items:center;color:#aaa19a;background:#f8f6f1;border-radius:12px;font-size:13px}
.confetti{position:absolute;pointer-events:none;color:var(--gold);opacity:.28;animation:drift 7s linear infinite}.hidden{display:none!important}
@keyframes appear{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:translateY(0)}}@keyframes flicker{from{transform:rotate(-52deg) scale(.96)}to{transform:rotate(-38deg) scale(1.1)}}@keyframes pulse{50%{transform:scale(1.12)}}@keyframes smoke{0%{opacity:.8;transform:translateY(0)}100%{opacity:0;transform:translateY(-65px) translateX(16px) scale(2)}}@keyframes spin{to{transform:rotate(360deg)}}@keyframes counterspin{to{transform:rotate(-360deg)}}@keyframes drift{to{transform:translateY(-120vh) rotate(160deg)}}
 .love-heart{height:245px;width:245px;display:flex;align-items:center;justify-content:center;position:relative;cursor:pointer;user-select:none;touch-action:manipulation;border-radius:50%;background:radial-gradient(circle,#fff 5%,#ffe6ef 65%,#f2d4df 100%);box-shadow:0 0 0 2px #f0d3dd,0 12px 50px #e5b4c7aa;animation:loveBeat 2s infinite}
.love-heart span{font-size:100px;filter:drop-shadow(0 8px 14px #d8a2b6)}.love-heart.loved{background:radial-gradient(circle,#fff,#ffd5e2);box-shadow:0 0 35px #f6a9c6}.love-sparkles{position:absolute;bottom:35px;font-size:16px;color:#c89f50;letter-spacing:7px;animation:pulse 2s infinite}@keyframes loveBeat{50%{transform:scale(1.045)}}
@media(max-height:690px){#app{padding-top:8px}.scene{gap:7px}.love-heart{width:185px;height:185px}.love-heart span{font-size:73px}.card{padding:15px}.key{height:46px}.pin-dot{height:45px}.giftrow{margin-top:15px}}
</style></head><body><div id="app">
<section class="scene active" id="login"><div class="card"><h1 class="serif hero">Enter Code</h1><p class="helper">Hint: ကိုကိုတို့နှစ်ယောက်ရဲ့ လျှို့ဝှက်နံပါတ် (123456)</p><div class="pin-dots" id="dots"></div><div class="keypad" id="keypad"></div><div class="error" id="pinError"></div></div></section>
<section class="scene" id="welcome"><h1 class="hero serif">Happy Anniversary</h1><div class="starline">— ✦ —</div><p class="sub">ကိုကို့ရဲ့ ချစ်သူလေးအတွက် အထူးလက်ဆောင် 💕</p><div class="heart">♥</div><button class="primary" id="startBtn">ဆက်ကြည့်မယ် ♡</button></section>
<section class="scene" id="wish"><h1 class="hero serif">Our Love Story</h1><p class="sub">တစ်နေ့ထက်တစ်နေ့ ပိုချစ်လာတဲ့ ကိုကိုတို့နှစ်ယောက်ရဲ့ အမှတ်တရလေး ❤️<br/>HAPPY 4 YEARS & 4 MONTHS ANNIVERSARY ပါ ခလေးလေးရေ</p><div class="love-heart" id="cake" role="button" tabindex="0" aria-label="Double tap the heart"><span id="loveIcon">💗</span><div class="love-sparkles">✦　♡　✦</div></div><p class="helper" id="cakeHint">နှလုံးပုံလေးကို နှစ်ချက်နှိပ်ပါ ♡</p></section>
<section class="scene" id="heartScene"><h1 class="hero">ချစ်ခြင်းမေတ္တာတွေ ပြည့်နေပြီ ❤️</h1><p class="sub">လက်ဆောင်လေး ဖွင့်ဖို့ ၅ စက္ကန့်ပဲ ကျန်တော့တယ်။</p><div class="ring"><span class="heart">♥</span></div><p class="helper">လက်ဆောင်လေး ပွင့်လာတော့မယ်…</p></section>
<section class="scene" id="gifts"><h1 class="hero serif">For My Love</h1><p class="sub">လက်ဆောင် နှစ်ခု စီစဉ်ထားတယ်</p><div class="giftrow"><div><button class="gift" id="letterBtn" aria-label="Letter">♧</button><div class="gift-label">Letter</div></div><div><button class="gift" id="memBtn" aria-label="Memories">🎁</button><div class="gift-label">Memories</div></div></div></section>
<div class="dialog" id="letterDialog"><div class="paper"><button class="close" data-close="1">×</button><h2>To My Favorite Person</h2><div class="scroll" id="letterText"></div><button class="fullbtn" data-close="1">ဆက်ကြည့်မယ်</button></div></div>
<div class="dialog" id="memDialog"><div class="paper"><button class="close" data-close="1">×</button><h2>Our Precious Memories 💕</h2><div class="scroll" id="memoryList"></div><button class="fullbtn" data-close="1">ဆက်ကြည့်မယ်</button></div></div>
</div><script>
const CFG=__CONFIG__;
const $=id=>document.getElementById(id);
const screens=['login','welcome','wish','heartScene','gifts'];
function show(id){for(const s of screens)$(s).classList.toggle('active',s===id)}
let input='';
function renderDots(){ $('dots').innerHTML=''; for(let i=0;i<6;i++){const el=document.createElement('div');el.className='pin-dot';el.textContent=i<input.length?'♥':'♡';$('dots').appendChild(el)} }
function key(k){$('pinError').textContent='';if(k==='CLR')input='';else if(k==='DEL')input=input.slice(0,-1);else if(input.length<6)input+=k;renderDots();if(input.length===6){if(input===CFG.pin){setTimeout(()=>show('welcome'),230)}else{$('pinError').textContent='Code မှားနေပါတယ်။ ပြန်ထည့်ပါ';setTimeout(()=>{input='';renderDots()},650)}}}
for(const k of ['1','2','3','4','5','6','7','8','9','CLR','0','DEL']){const b=document.createElement('button');b.textContent=k;b.className='key'+(isNaN(Number(k))?' small':'');b.addEventListener('click',()=>key(k));$('keypad').appendChild(b)}renderDots();
$('startBtn').onclick=()=>show('wish');
let taps=0,finished=false;
function tapCake(){if(finished)return;taps++;if(taps===1){$('cakeHint').textContent='နောက်တစ်ချက် ထပ်နှိပ်ပါ ♡';return}finished=true;$('cake').classList.add('loved');$('loveIcon').textContent='💞';$('cakeHint').textContent='အချစ်တွေ အပြည့်ပဲ! 💖';setTimeout(()=>{show('heartScene');setTimeout(()=>show('gifts'),5000)},1700)}
$('cake').addEventListener('click',tapCake);$('cake').addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();tapCake()}});
$('letterBtn').onclick=()=>{$('letterDialog').classList.add('show')};$('memBtn').onclick=()=>{$('memDialog').classList.add('show')};
for(const b of document.querySelectorAll('[data-close]'))b.onclick=()=>{ $('letterDialog').classList.remove('show');$('memDialog').classList.remove('show')};
$('letterText').textContent=CFG.letter;
const list=$('memoryList');
for(let i=1;i<=5;i++){
 const fig=document.createElement('figure');fig.className='memory';fig.style.margin='0 0 17px';
 const src=CFG.images['couple'+i];
 if(src){const img=document.createElement('img');img.src=src;img.alt='Memory '+i;img.loading='lazy';fig.appendChild(img)}
 else {const ph=document.createElement('div');ph.className='placeholder';ph.textContent='couple'+i+' ပုံ မတွေ့သေးပါ';fig.appendChild(ph)}
 const caption=document.createElement('figcaption');caption.textContent=CFG.captions[i-1]||'';fig.appendChild(caption);list.appendChild(fig);
}
for(let i=0;i<15;i++){let e=document.createElement('span');e.className='confetti';e.textContent=i%2?'✦':'•';e.style.left=((i*41+8)%98)+'%';e.style.top=(30+(i*17)%65)+'%';e.style.animationDelay=(-i*.43)+'s';$('app').prepend(e)}
</script></body></html>'''
page = page.replace('__CONFIG__', json.dumps(config, ensure_ascii=False).replace('</', '<\\/'))
components.html(page, height=860, scrolling=False)
