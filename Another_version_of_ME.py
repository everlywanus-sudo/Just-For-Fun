import streamlit as st
import streamlit.components.v1 as components
import base64


# =========================================================
# 页面配置
# 必须放在所有其他 Streamlit 命令之前
# =========================================================

st.set_page_config(
    page_title="電波圏外少女",
    page_icon="🩸",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# =========================================================
# 工具函数
# =========================================================

def to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


# =========================================================
# 读取资源
# =========================================================

gif_b64 = to_base64("background.GIF")

audio_b64 = to_base64("Dancin.mp3")

video_b64 = to_base64("MYLIFE.mp4")

bgm_b64 = to_base64("bgmusic.mp3")


# =========================================================
# 全局 CSS
# =========================================================

st.markdown(
    f"""
<style>


/* =========================================================
   GIF 背景
   ========================================================= */

.stApp {{

    background-image:
        linear-gradient(
            rgba(255,255,255,0.10),
            rgba(255,255,255,0.10)
        ),
        url("data:image/gif;base64,{gif_b64}");

    background-size:
        cover;

    background-position:
        center center;

    background-repeat:
        no-repeat;

    background-attachment:
        fixed;

    filter:
        brightness(.28);

    transition:
        filter 1.8s ease;
}}


body.vn-started .stApp {{

    filter:
        brightness(1);

}}


[data-testid="stAppViewContainer"],
[data-testid="stHeader"] {{

    background:
        transparent;

}}


/* =========================================================
   开场前压暗正式内容
   ========================================================= */

body:not(.vn-started)
[data-testid="stMainBlockContainer"] {{

    opacity:
        .08;

    filter:
        blur(5px);

    transition:
        opacity 1.2s ease,
        filter 1.2s ease;

}}


body.vn-started
[data-testid="stMainBlockContainer"] {{

    opacity:
        1;

    filter:
        blur(0);

}}


/* =========================================================
   开场文字
   ========================================================= */

#vn-boot-text {{

    position:
        fixed;

    left:
        50%;

    top:
        50%;

    transform:
        translate(-50%, -50%);

    z-index:
        2147483647;

    width:
        max-content;

    max-width:
        96vw;

    white-space:
        pre-line;

    pointer-events:
        none;

    text-align:
        center;

    line-height:
        1.55;

    font-family:
        "Arial Black",
        "PingFang SC",
        "Microsoft YaHei",
        sans-serif;

    font-size:
        clamp(
            25px,
            3vw,
            50px
        );

    font-weight:
        950;

    letter-spacing:
        1px;

    color:
        #fffaf4;

    -webkit-text-stroke:
        .7px rgba(20,10,20,.7);

    text-shadow:

        -5px 0 rgba(255,25,85,.65),

        5px 0 rgba(25,245,255,.62),

        0 0 5px rgba(255,255,255,1),

        0 0 14px rgba(255,165,225,.95),

        0 0 30px rgba(255,70,185,.78),

        0 0 60px rgba(100,130,255,.60);

    animation:

        vnBootFlash
        1.16s
        steps(1,end)
        infinite,

        vnBootGlitch
        .15s
        steps(2,end)
        infinite;

}}


/* =========================================================
   Glitch
   ========================================================= */

@keyframes vnBootGlitch {{

    0% {{
        transform:
            translate(-50%, -50%)
            translate(0,0);
    }}

    20% {{
        transform:
            translate(-50%, -50%)
            translate(4px,-1px);
    }}

    40% {{
        transform:
            translate(-50%, -50%)
            translate(-4px,1px);
    }}

    60% {{
        transform:
            translate(-50%, -50%)
            translate(2px,-1px);
    }}

    80% {{
        transform:
            translate(-50%, -50%)
            translate(-2px,1px);
    }}

    100% {{
        transform:
            translate(-50%, -50%);
    }}

}}


/* =========================================================
   屏闪
   ========================================================= */

@keyframes vnBootFlash {{

    0% {{
        opacity: .05;
        filter: brightness(.5) blur(.7px);
    }}

    4% {{
        opacity: 1;
        filter: brightness(2.7) blur(0);
    }}

    9% {{
        opacity: .12;
    }}

    13% {{
        opacity: 1;
    }}

    25% {{
        opacity: .92;
    }}

    29% {{
        opacity: 0;
    }}

    35% {{
        opacity: .65;
    }}

    39% {{
        opacity: 1;
        filter: brightness(3.5);
    }}

    42% {{
        opacity: .05;
    }}

    49% {{
        opacity: 1;
    }}

    63% {{
        opacity: .9;
    }}

    68% {{
        opacity: .08;
    }}

    74% {{
        opacity: 1;
        filter: brightness(2.3);
    }}

    80% {{
        opacity: .28;
    }}

    86% {{
        opacity: 1;
    }}

    93% {{
        opacity: .78;
    }}

    100% {{
        opacity: .04;
    }}

}}


/* =========================================================
   点击以后电影 CRT 关机
   ========================================================= */

#vn-boot-text.vn-exit {{

    animation:
        vnFilmCollapse
        .60s
        cubic-bezier(.72,0,.28,1)
        forwards !important;

}}


@keyframes vnFilmCollapse {{

    0% {{

        opacity: 1;

        transform:
            translate(-50%, -50%)
            scaleX(1)
            scaleY(1);

        filter:
            brightness(1)
            blur(0);
    }}


    14% {{

        opacity: 1;

        transform:
            translate(-50%, -50%)
            scaleX(1.025)
            scaleY(.98);

        filter:
            brightness(7)
            blur(.3px);

        text-shadow:
            0 0 10px white,
            0 0 30px white,
            0 0 65px rgba(255,110,225,1);
    }}


    52% {{

        opacity: 1;

        transform:
            translate(-50%, -50%)
            scaleX(.94)
            scaleY(.035);

        filter:
            brightness(11)
            blur(3px);
    }}


    68% {{

        opacity: .96;

        transform:
            translate(-50%, -50%)
            scaleX(.70)
            scaleY(.015);

        filter:
            brightness(14)
            blur(4px);
    }}


    84% {{

        opacity: .85;

        transform:
            translate(-50%, -50%)
            scaleX(.07)
            scaleY(.012);

        filter:
            brightness(18)
            blur(6px);
    }}


    94% {{

        opacity: .55;

        transform:
            translate(-50%, -50%)
            scale(.007);

        filter:
            brightness(22)
            blur(8px);
    }}


    100% {{

        opacity: 0;

        transform:
            translate(-50%, -50%)
            scale(0);

        visibility:
            hidden;
    }}

}}


/* =========================================================
   一级标题
   ========================================================= */

h1 {{

    font-size:
        70px !important;

    font-weight:
        900 !important;

    letter-spacing:
        -2px;

    white-space:
        nowrap !important;

    overflow:
        visible;

    color:
        #f5f0df !important;

    text-shadow:
        3px 3px 0 #111,
        6px 6px 0 #8b1e1e,
        9px 9px 0 rgba(0,0,0,.35);

}}


/* =========================================================
   二级标题
   ========================================================= */

h2 {{

    font-size:
        50px !important;

    font-weight:
        850 !important;

    letter-spacing:
        3px;

    color:
        #f7d7f0 !important;

    -webkit-text-stroke:
        1.5px #2b1838;

    text-shadow:
        2px 2px 0 #2b1838,
        4px 4px 0 #8b4f8f,
        0 0 8px rgba(255,180,240,.7),
        0 0 16px rgba(130,80,180,.45);

}}


/* =========================================================
   三级标题
   ========================================================= */

h3 {{

    font-size:
        36px !important;

    font-weight:
        900 !important;

    letter-spacing:
        2px;

    color:
        #d9fff7 !important;

    text-shadow:
        2px 2px 0 #142a2a,
        4px 4px 0 #315e59,
        0 0 6px rgba(150,255,235,.45);

}}


/* =========================================================
   正文
   ========================================================= */

p {{

    font-size:
        21px !important;

    font-weight:
        650 !important;

    color:
        #f3f3f3 !important;

    text-shadow:
        1px 1px 0 #111,
        2px 2px 0 rgba(0,0,0,.55);

}}


/* =========================================================
   表格
   ========================================================= */

[data-testid="stTable"] {{

    text-shadow:
        1px 1px 0 rgba(0,0,0,.5);

}}


/* =========================================================
   主标题浮现
   ========================================================= */

.main-title {{

    opacity: 0;

    transform:
        translateY(38px);

}}


body.vn-started
.main-title {{

    animation:
        mainTitleReveal
        1.55s
        ease
        .30s
        forwards;

}}


@keyframes mainTitleReveal {{

    from {{

        opacity: 0;

        transform:
            translateY(38px);

        filter:
            blur(6px);
    }}

    to {{

        opacity: 1;

        transform:
            translateY(0);

        filter:
            blur(0);
    }}

}}


/* =========================================================
   二三级标题浮现
   ========================================================= */

h2,
h3 {{

    opacity: 0;

    transform:
        translateY(28px);

}}


body.vn-started h2 {{

    animation:
        titleReveal
        1.5s
        ease
        .62s
        forwards;

}}


body.vn-started h3 {{

    animation:
        titleReveal
        1.5s
        ease
        .92s
        forwards;

}}


@keyframes titleReveal {{

    from {{

        opacity: 0;

        transform:
            translateY(28px);

        filter:
            blur(5px);
    }}

    to {{

        opacity: 1;

        transform:
            translateY(0);

        filter:
            blur(0);
    }}

}}


/* =========================================================
   正文逐行浮现
   ========================================================= */

.vn-line {{

    opacity: 0;

    transform:
        translateY(32px);

    filter:
        blur(6px);

}}


body.vn-started .line1 {{

    animation:
        vnLineUp
        1.3s
        ease
        1.25s
        forwards;

}}


body.vn-started .line2 {{

    animation:
        vnLineUp
        1.3s
        ease
        1.95s
        forwards;

}}


body.vn-started .line3 {{

    animation:
        vnLineUp
        1.3s
        ease
        2.65s
        forwards;

}}


@keyframes vnLineUp {{

    from {{

        opacity: 0;

        transform:
            translateY(32px);

        filter:
            blur(6px);
    }}

    to {{

        opacity: 1;

        transform:
            translateY(0);

        filter:
            blur(0);
    }}

}}


/* =========================================================
   Logo 呼吸
   ========================================================= */

body.vn-started
[data-testid="stLogo"] img {{

    animation:
        logoBreathing
        3s
        ease-in-out
        infinite;

}}


@keyframes logoBreathing {{

    0%,
    100% {{

        transform:
            scale(1);

        filter:
            brightness(1)
            drop-shadow(
                0 0 4px
                rgba(255,180,240,.35)
            );
    }}


    50% {{

        transform:
            scale(1.10);

        filter:
            brightness(1.18)
            drop-shadow(
                0 0 12px
                rgba(255,180,240,.85)
            );
    }}

}}


/* =========================================================
   图片启动后摇摆
   ========================================================= */

[data-testid="stImage"] img {{

    transform-origin:
        50% 85%;

}}


body.vn-started
[data-testid="stImage"] img {{

    animation:
        pendulum
        .9s
        ease-in-out
        infinite;

}}


@keyframes pendulum {{

    0% {{
        transform:
            rotate(-5deg);
    }}

    50% {{
        transform:
            rotate(5deg);
    }}

    100% {{
        transform:
            rotate(-5deg);
    }}

}}

</style>
""",
    unsafe_allow_html=True
)


# =========================================================
# 开场系统
# =========================================================

components.html(
    """
<script>

const parentDoc =
    window.parent.document;

const parentWin =
    window.parent;


/* 清除旧开场 */

const oldBoot =
    parentDoc.getElementById(
        "vn-boot-text"
    );

if (oldBoot) {
    oldBoot.remove();
}


/* 初始化状态 */

parentDoc.body
    .classList
    .remove(
        "vn-started"
    );

parentWin.__vnStarted =
    false;


/* 创建启动文字 */

const bootText =
    parentDoc.createElement(
        "div"
    );

bootText.id =
    "vn-boot-text";

bootText.textContent =
    "欢迎来到隐藏副本。\\n点击任意地方开启「深夜0系統」";

parentDoc.body.appendChild(
    bootText
);


let bootStarted =
    false;


/* =========================================================
   启动世界
   ========================================================= */

function launchWorld() {

    if (bootStarted) {
        return;
    }

    bootStarted =
        true;


    bootText.classList.add(
        "vn-exit"
    );


    setTimeout(
        () => {

            parentDoc.body
                .classList
                .add(
                    "vn-started"
                );

            parentWin.__vnStarted =
                true;


            parentWin.postMessage(
                {
                    type:
                        "START_EXPERIENCE"
                },
                "*"
            );

        },
        240
    );


    setTimeout(
        () => {

            if (
                bootText &&
                bootText.parentNode
            ) {

                bootText.remove();

            }

        },
        720
    );

}


/* 捕获整个页面第一次操作 */

parentDoc.addEventListener(
    "click",
    launchWorld,
    {
        once: true,
        capture: true
    }
);


parentDoc.addEventListener(
    "touchstart",
    launchWorld,
    {
        once: true,
        capture: true
    }
);


parentDoc.addEventListener(
    "keydown",
    launchWorld,
    {
        once: true,
        capture: true
    }
);

</script>
""",
    height=1
)


# =========================================================
# CUSTOM ABOUT // 404
# =========================================================

components.html(
    """
<script>

const parentDoc =
    window.parent.document;


/* =========================================================
   清理旧 About
   ========================================================= */

const oldAboutButton =
    parentDoc.getElementById(
        "about-404-button"
    );

if (oldAboutButton) {
    oldAboutButton.remove();
}


const oldAboutOverlay =
    parentDoc.getElementById(
        "about-404-overlay"
    );

if (oldAboutOverlay) {
    oldAboutOverlay.remove();
}


const oldAboutStyle =
    parentDoc.getElementById(
        "about-404-style"
    );

if (oldAboutStyle) {
    oldAboutStyle.remove();
}


/* =========================================================
   样式
   ========================================================= */

const style =
    parentDoc.createElement(
        "style"
    );

style.id =
    "about-404-style";


style.textContent = `

/* =====================================================
   ABOUT 按钮
   ===================================================== */

#about-404-button {

    position: fixed;

    top: 22px;
    right: 28px;

    z-index: 999999;

    padding: 10px 16px;

    border:
        2px solid #c8b99f;

    border-radius:
        3px;

    background:
        rgba(16,14,18,.80);

    backdrop-filter:
        blur(8px);

    color:
        #eee0ca;

    font-family:
        "Courier New",
        monospace;

    font-size:
        12px;

    font-weight:
        900;

    letter-spacing:
        2px;

    cursor:
        pointer;

    box-shadow:
        4px 4px 0 #090809,
        7px 7px 0 #741723,
        0 0 18px
        rgba(255,70,160,.35);

    transition:
        transform .2s ease,
        filter .2s ease,
        opacity .5s ease;

}


/* 启动画面阶段隐藏 */

body:not(.vn-started)
#about-404-button {

    opacity: 0;

    pointer-events:
        none;

}


body.vn-started
#about-404-button {

    opacity: 1;

    pointer-events:
        auto;

}


#about-404-button:hover {

    transform:
        translateY(-2px)
        rotate(-1deg);

    filter:
        brightness(1.25);

}


/* =====================================================
   Overlay
   ===================================================== */

#about-404-overlay {

    position:
        fixed;

    inset:
        0;

    z-index:
        2147483646;

    display:
        flex;

    align-items:
        center;

    justify-content:
        center;

    background:
        rgba(3,3,7,.84);

    backdrop-filter:
        blur(10px)
        saturate(.7);

    opacity:
        0;

    pointer-events:
        none;

    transition:
        opacity .35s ease;

}


#about-404-overlay.about-open {

    opacity:
        1;

    pointer-events:
        auto;

}


/* =====================================================
   主卡片
   ===================================================== */

#about-404-card {

    position:
        relative;

    width:
        min(720px, 84vw);

    padding:
        60px 58px 48px 58px;

    box-sizing:
        border-box;

    color:
        #eee4d3;

    background:
        linear-gradient(
            145deg,
            rgba(23,20,24,.98),
            rgba(43,34,40,.98) 58%,
            rgba(13,12,15,.99)
        );

    border:
        3px solid #bbae96;

    box-shadow:
        9px 10px 0 #080709,
        17px 18px 0 #6e1725,
        0 0 45px
        rgba(230,40,110,.30);

    transform:
        rotate(-.35deg)
        scale(.83)
        translateY(20px);

    opacity:
        0;

    overflow:
        hidden;

    transition:
        transform .45s
        cubic-bezier(.18,.9,.25,1),
        opacity .35s ease;

}


#about-404-overlay.about-open
#about-404-card {

    opacity:
        1;

    transform:
        rotate(-.35deg)
        scale(1)
        translateY(0);

}


/* 扫描纹 */

#about-404-card::before {

    content: "";

    position:
        absolute;

    inset:
        0;

    pointer-events:
        none;

    opacity:
        .18;

    background:
        repeating-linear-gradient(
            0deg,
            transparent 0px,
            transparent 4px,
            rgba(255,255,255,.025) 5px
        );

}


/* =====================================================
   关闭按钮
   ===================================================== */

#about-404-close {

    position:
        absolute;

    top:
        15px;

    right:
        17px;

    width:
        43px;

    height:
        43px;

    border:
        2px solid #c7b99f;

    background:
        #161318;

    color:
        #eee0cd;

    font-size:
        30px;

    font-weight:
        900;

    cursor:
        pointer;

    box-shadow:
        3px 3px 0 #080708,
        5px 5px 0 #741723;

}


/* =====================================================
   REJECTED 印章
   ===================================================== */

.about-stamp {

    position:
        absolute;

    top:
        20px;

    left:
        24px;

    padding:
        5px 10px;

    border:
        4px solid #872032;

    color:
        #a12a3b;

    font-family:
        "Courier New",
        monospace;

    font-size:
        13px;

    font-weight:
        900;

    letter-spacing:
        3px;

    transform:
        rotate(-9deg);

}


/* =====================================================
   系统编号
   ===================================================== */

.about-code {

    margin-bottom:
        10px;

    font-family:
        "Courier New",
        monospace;

    font-size:
        11px;

    font-weight:
        800;

    letter-spacing:
        4px;

    color:
        #8f8375;

}


/* =====================================================
   About 主标题
   ===================================================== */

.about-title {

    font-size:
        clamp(
            48px,
            7vw,
            82px
        );

    font-weight:
        950;

    letter-spacing:
        -4px;

    color:
        #f1e8d8;

    line-height:
        1;

    text-shadow:
        4px 4px 0 #111,
        8px 8px 0 #791c2b,
        -3px 0
        rgba(40,230,255,.32),
        3px 0
        rgba(255,40,100,.40);

    animation:
        aboutGlitch
        1.6s
        steps(2,end)
        infinite;

}


@keyframes aboutGlitch {

    0%,
    84%,
    100% {

        transform:
            translate(0);

    }

    86% {

        transform:
            translate(-3px,1px);

    }

    88% {

        transform:
            translate(4px,-1px);

    }

    90% {

        transform:
            translate(-1px,0);

    }

}


/* =====================================================
   Subtitle
   ===================================================== */

.about-subtitle {

    margin-top:
        11px;

    font-family:
        "Courier New",
        monospace;

    font-size:
        14px;

    font-weight:
        900;

    letter-spacing:
        5px;

    color:
        #b8a89a;

}


/* =====================================================
   分隔线
   ===================================================== */

.about-divider {

    height:
        3px;

    width:
        100%;

    margin:
        30px 0;

    background:
        repeating-linear-gradient(
            90deg,
            #7d1b29 0px,
            #7d1b29 13px,
            transparent 13px,
            transparent 20px
        );

}


/* =====================================================
   正文
   ===================================================== */

#about-404-card
.about-text {

    margin:
        0 0 22px 0;

    font-family:
        "PingFang SC",
        "Microsoft YaHei",
        sans-serif;

    font-size:
        18px;

    font-weight:
        650;

    line-height:
        1.9;

    color:
        #eee2d1;

    text-shadow:
        1px 1px 0 #000,
        2px 2px 0
        rgba(0,0,0,.45);

}


/* =====================================================
   Warning
   ===================================================== */

.about-warning {

    display:
        inline-block;

    margin-top:
        6px;

    padding:
        8px 11px;

    border:
        2px solid #842031;

    color:
        #d76a7c;

    font-family:
        "Courier New",
        monospace;

    font-size:
        12px;

    font-weight:
        900;

    letter-spacing:
        2px;

    transform:
        rotate(-1deg);

    animation:
        aboutWarning
        1.15s
        steps(2,end)
        infinite;

}


@keyframes aboutWarning {

    0%,
    68% {
        opacity: 1;
    }

    69%,
    100% {
        opacity: .38;
    }

}


/* =====================================================
   Footer
   ===================================================== */

.about-footer {

    margin-top:
        32px;

    font-family:
        "Courier New",
        monospace;

    font-size:
        10px;

    letter-spacing:
        3px;

    color:
        #746a61;

    text-decoration:
        line-through;

}

`;


parentDoc.head.appendChild(
    style
);


/* =========================================================
   创建按钮
   ========================================================= */

const aboutButton =
    parentDoc.createElement(
        "button"
    );

aboutButton.id =
    "about-404-button";

aboutButton.textContent =
    "ABOUT // 404";


parentDoc.body.appendChild(
    aboutButton
);


/* =========================================================
   创建 Overlay
   ========================================================= */

const overlay =
    parentDoc.createElement(
        "div"
    );


overlay.id =
    "about-404-overlay";


overlay.innerHTML = `

<div id="about-404-card">

    <button id="about-404-close">
        ×
    </button>


    <div class="about-stamp">
        REJECTED
    </div>


    <div class="about-code">
        SYSTEM // ABOUT_404
    </div>


    <div class="about-title">
        地下神経網
    </div>


    <div class="about-subtitle">
        UNDERGROUND NEURAL NETWORK
    </div>


    <div class="about-divider"></div>


    <div class="about-text">

        欢迎来到由一个神经病创建的地下神经网络系统 😈

        <br><br>

        此处不存在正常世界线。

        <br>

        只有损坏的记忆、过期的青春缓存、

        <br>

        以及仍然拒绝被格式化的人类残片。

    </div>


    <div class="about-warning">
        ⚠ REALITY CONNECTION UNSTABLE
    </div>


    <div class="about-footer">
        廃線記録 // MEMORY DUMP_404 // 未明通信
    </div>

</div>

`;


parentDoc.body.appendChild(
    overlay
);


/* =========================================================
   打开 / 关闭
   ========================================================= */

function openAbout() {

    overlay.classList.add(
        "about-open"
    );

}


function closeAbout() {

    overlay.classList.remove(
        "about-open"
    );

}


aboutButton.addEventListener(
    "click",
    event => {

        event.stopPropagation();

        openAbout();

    }
);


parentDoc
    .getElementById(
        "about-404-close"
    )
    .addEventListener(
        "click",
        event => {

            event.stopPropagation();

            closeAbout();

        }
    );


overlay.addEventListener(
    "click",
    event => {

        if (
            event.target ===
            overlay
        ) {

            closeAbout();

        }

    }
);


parentDoc.addEventListener(
    "keydown",
    event => {

        if (
            event.key ===
            "Escape"
        ) {

            closeAbout();

        }

    }
);

</script>
""",
    height=1
)


# =========================================================
# 标题
# =========================================================

st.markdown(
    """
<h1 class="main-title">
世界線アップロード失敗
</h1>
""",
    unsafe_allow_html=True
)


st.header(
    "青春キャッシュ未保存"
)


st.subheader(
    "電脳少女404"
)


st.write("")


# =========================================================
# 正文
# =========================================================

st.markdown(
    """
<p class="vn-line line1">
我现在还处于一种奥德赛时期，婚姻这种事情会让我失去主体性
</p>

<p class="vn-line line2">
而且我是一个低精力高敏感人群，我碰上的人不是npd就是ADHD或者回避型焦虑依恋人格，我想这应该和原生家庭有关
</p>

<p class="vn-line line3">
虽然时代是经济下行的，但人生是狂野的，所以我还需要一段沉淀的时间，专心经营自己的萨福生活
</p>
""",
    unsafe_allow_html=True
)


st.write("")
st.write("")
st.write("")


# =========================================================
# 图片
# =========================================================

st.image(
    "./第7章：AI应用/resources/FUCK.PNG"
)


st.write("")
st.write("")
st.write("")


# =========================================================
# 朋克音频播放器
# =========================================================

components.html(
    f"""
<div class="punk-player">

    <div class="rivet r1"></div>
    <div class="rivet r2"></div>
    <div class="rivet r3"></div>
    <div class="rivet r4"></div>

    <div class="ink-stamp">
        VOID
    </div>

    <div class="skull">
        ☠
    </div>

    <div class="player-title">
        LOST TRANSMISSION
    </div>


    <audio id="punk-audio">

        <source
            src="data:audio/mpeg;base64,{audio_b64}"
            type="audio/mpeg">

    </audio>


    <div class="controls">

        <button id="play-btn">
            ▶
        </button>

        <div
            class="time"
            id="current-time">
            0:00
        </div>

        <div class="track">

            <div
                class="progress"
                id="progress">
            </div>

        </div>

        <div
            class="time"
            id="duration">
            0:00
        </div>

        <button id="mute-btn">
            🔊
        </button>

    </div>


    <div class="warning">
        NO FUTURE // AUDIO ARCHIVE 404
    </div>

</div>


<style>

html,
body {{

    margin: 0;

    background:
        transparent;

}}


.punk-player {{

    position:
        relative;

    width:
        100%;

    box-sizing:
        border-box;

    padding:
        26px 30px
        22px 30px;

    background:
        linear-gradient(
            135deg,
            #19181a,
            #292529 55%,
            #141315
        );

    border:
        3px solid #b8aa91;

    border-radius:
        8px;

    box-shadow:
        7px 7px 0 #0b0a0b,
        12px 12px 0 #641722,
        0 0 25px
        rgba(120,15,35,.35);

    color:
        #ece3d3;

    font-family:
        "Courier New",
        monospace;

    transform:
        rotate(-.25deg);

    overflow:
        hidden;

}}


.punk-player::before {{

    content:
        "";

    position:
        absolute;

    inset:
        0;

    opacity:
        .20;

    pointer-events:
        none;

    background:
        repeating-linear-gradient(
            87deg,
            transparent 0px,
            transparent 13px,
            rgba(255,255,255,.035) 14px,
            transparent 15px
        );

}}


.rivet {{

    position:
        absolute;

    width:
        13px;

    height:
        13px;

    border-radius:
        50%;

    background:
        radial-gradient(
            circle at 35% 30%,
            #f0e6d5,
            #71685c 45%,
            #171416 75%
        );

    border:
        1px solid #0a090a;

}}


.r1 {{
    left: 9px;
    top: 9px;
}}


.r2 {{
    right: 9px;
    top: 9px;
}}


.r3 {{
    left: 9px;
    bottom: 9px;
}}


.r4 {{
    right: 9px;
    bottom: 9px;
}}


.skull {{

    position:
        absolute;

    top:
        8px;

    right:
        36px;

    font-size:
        34px;

    transform:
        rotate(8deg);

    text-shadow:
        2px 2px 0 #111,
        4px 4px 0 #741723;

}}


.ink-stamp {{

    position:
        absolute;

    left:
        18px;

    top:
        9px;

    padding:
        3px 8px;

    border:
        3px solid #831c29;

    color:
        #9c2633;

    font-weight:
        900;

    font-size:
        13px;

    letter-spacing:
        2px;

    transform:
        rotate(-9deg);

}}


.player-title {{

    margin-left:
        64px;

    margin-bottom:
        18px;

    font-size:
        18px;

    font-weight:
        900;

    letter-spacing:
        3px;

    color:
        #eadfc9;

    text-shadow:
        2px 2px 0 #111,
        4px 4px 0 #741723;

}}


.controls {{

    display:
        flex;

    align-items:
        center;

    gap:
        12px;

}}


#play-btn,
#mute-btn {{

    width:
        46px;

    height:
        46px;

    flex:
        0 0 auto;

    border-radius:
        50%;

    border:
        2px solid #b8aa91;

    background:
        radial-gradient(
            circle at 35% 30%,
            #454046,
            #181619 70%
        );

    color:
        #f0e4d1;

    font-size:
        18px;

    cursor:
        pointer;

    box-shadow:
        3px 3px 0 #080708,
        5px 5px 0 #751823;

}}


.time {{

    min-width:
        42px;

    font-size:
        13px;

    font-weight:
        800;

    color:
        #d4c6af;

}}


.track {{

    position:
        relative;

    height:
        12px;

    flex:
        1;

    background:
        #080708;

    border:
        2px solid #777066;

    cursor:
        pointer;

    overflow:
        hidden;

}}


.progress {{

    height:
        100%;

    width:
        0%;

    background:
        repeating-linear-gradient(
            90deg,
            #8b1c2c 0px,
            #8b1c2c 11px,
            #d8c2a5 12px,
            #d8c2a5 14px
        );

}}


.warning {{

    margin-top:
        17px;

    font-size:
        11px;

    letter-spacing:
        2px;

    color:
        #8f8170;

    text-decoration:
        line-through;

}}

</style>


<script>

const punkAudio =
    document.getElementById(
        "punk-audio"
    );


const playBtn =
    document.getElementById(
        "play-btn"
    );


const muteBtn =
    document.getElementById(
        "mute-btn"
    );


const progress =
    document.getElementById(
        "progress"
    );


const track =
    document.querySelector(
        ".track"
    );


const current =
    document.getElementById(
        "current-time"
    );


const duration =
    document.getElementById(
        "duration"
    );


function formatTime(seconds) {{

    if (
        !Number.isFinite(seconds)
    ) {{

        return "0:00";

    }}


    const min =
        Math.floor(
            seconds / 60
        );


    const sec =
        Math.floor(
            seconds % 60
        )
        .toString()
        .padStart(
            2,
            "0"
        );


    return `${{min}}:${{sec}}`;

}}


punkAudio.addEventListener(
    "loadedmetadata",
    () => {{

        duration.textContent =
            formatTime(
                punkAudio.duration
            );

    }}
);


playBtn.addEventListener(
    "click",
    async () => {{

        if (
            punkAudio.paused
        ) {{

            await
            punkAudio.play();

        }}

        else {{

            punkAudio.pause();

        }}

    }}
);


punkAudio.addEventListener(
    "play",
    () => {{

        playBtn.textContent =
            "❚❚";


        window.parent.postMessage(
            {{
                type:
                    "MEDIA_PLAY",

                source:
                    "custom-audio"
            }},
            "*"
        );

    }}
);


punkAudio.addEventListener(
    "pause",
    () => {{

        playBtn.textContent =
            "▶";


        if (
            !punkAudio.ended
        ) {{

            window.parent.postMessage(
                {{
                    type:
                        "MEDIA_STOP",

                    source:
                        "custom-audio"
                }},
                "*"
            );

        }}

    }}
);


punkAudio.addEventListener(
    "ended",
    () => {{

        playBtn.textContent =
            "▶";


        window.parent.postMessage(
            {{
                type:
                    "MEDIA_STOP",

                source:
                    "custom-audio"
            }},
            "*"
        );

    }}
);


/* 其他媒体开始时自动暂停 */

window.parent.addEventListener(
    "message",
    event => {{

        if (
            event.data?.type ===
                "MEDIA_PLAY"

            &&

            event.data?.source !==
                "custom-audio"
        ) {{

            if (
                !punkAudio.paused
            ) {{

                punkAudio.pause();

            }}

        }}

    }}
);


punkAudio.addEventListener(
    "timeupdate",
    () => {{

        if (
            !punkAudio.duration
        ) {{

            return;

        }}


        const pct =
            punkAudio.currentTime
            /
            punkAudio.duration
            *
            100;


        progress.style.width =
            pct + "%";


        current.textContent =
            formatTime(
                punkAudio.currentTime
            );

    }}
);


track.addEventListener(
    "click",
    event => {{

        const rect =
            track.getBoundingClientRect();


        const ratio =
            (
                event.clientX
                -
                rect.left
            )
            /
            rect.width;


        punkAudio.currentTime =
            ratio
            *
            punkAudio.duration;

    }}
);


muteBtn.addEventListener(
    "click",
    () => {{

        punkAudio.muted =
            !punkAudio.muted;


        muteBtn.textContent =
            punkAudio.muted
            ? "🔇"
            : "🔊";

    }}
);

</script>
""",
    height=160,
    scrolling=False
)


# =========================================================
# Logo
# =========================================================

st.logo(
    "./第7章：AI应用/resources/logo.png",
    size="large"
)


st.write("")
st.write("")


# =========================================================
# 信封 + 视频
# =========================================================

components.html(
    f"""
<div class="letter-zone">

    <div
        id="punk-envelope"
        class="envelope">


        <div class="envelope-back">
        </div>


        <div class="letter-card">

            <span>
                NO FUTURE
            </span>

            <small>
                未送達 / 404
            </small>

        </div>


        <div class="envelope-left">
        </div>


        <div class="envelope-right">
        </div>


        <div class="envelope-bottom">
        </div>


        <div class="envelope-flap">
        </div>


        <div class="stamp">
            ×
        </div>


        <div class="scribble">
            VOID MAIL
        </div>

    </div>


    <div
        id="video-shell"
        class="video-shell">


        <video
            id="letter-video"
            playsinline
            controls>

            <source
                src="data:video/mp4;base64,{video_b64}"
                type="video/mp4">

        </video>

    </div>

</div>


<style>

html,
body {{

    margin: 0;

    background:
        transparent;

    overflow:
        visible;

}}


.letter-zone {{

    position:
        relative;

    width:
        100%;

    height:
        700px;

    display:
        flex;

    justify-content:
        center;

    align-items:
        center;

    overflow:
        visible;

}}


.envelope {{

    position:
        relative;

    width:
        270px;

    height:
        175px;

    cursor:
        pointer;

    z-index:
        10;

    filter:
        drop-shadow(
            7px 9px 0
            rgba(0,0,0,.7)
        )
        drop-shadow(
            0 0 15px
            rgba(190,40,80,.30)
        );

    transition:
        transform .3s ease,
        opacity .4s ease;

}}


.envelope:hover {{

    transform:
        scale(1.05)
        rotate(-2deg);

}}


.envelope-back {{

    position:
        absolute;

    inset:
        0;

    background:
        #c7b99c;

    border:
        3px solid #241e22;

}}


.letter-card {{

    position:
        absolute;

    left:
        22px;

    right:
        22px;

    top:
        22px;

    height:
        120px;

    background:
        #171518;

    border:
        2px solid #d7d0bc;

    color:
        #efdfd1;

    display:
        flex;

    flex-direction:
        column;

    align-items:
        center;

    justify-content:
        center;

    z-index:
        2;

    transition:
        transform .7s
        cubic-bezier(.18,.9,.25,1);

    box-shadow:
        5px 5px 0 #8b1e1e;

}}


.letter-card span {{

    font-size:
        25px;

    font-weight:
        900;

    letter-spacing:
        3px;

}}


.letter-card small {{

    margin-top:
        8px;

    opacity:
        .7;

}}


.envelope-left,
.envelope-right,
.envelope-bottom,
.envelope-flap {{

    position:
        absolute;

    inset:
        0;

}}


.envelope-left {{

    background:
        #bfb396;

    clip-path:
        polygon(
            0 0,
            52% 52%,
            0 100%
        );

    z-index:
        4;

}}


.envelope-right {{

    background:
        #a99d82;

    clip-path:
        polygon(
            100% 0,
            48% 52%,
            100% 100%
        );

    z-index:
        4;

}}


.envelope-bottom {{

    background:
        #d1c5a7;

    clip-path:
        polygon(
            0 100%,
            50% 47%,
            100% 100%
        );

    z-index:
        5;

}}


.envelope-flap {{

    background:
        #c9bda1;

    clip-path:
        polygon(
            0 0,
            100% 0,
            50% 62%
        );

    transform-origin:
        50% 0%;

    transition:
        transform .7s ease;

    z-index:
        6;

}}


.stamp {{

    position:
        absolute;

    right:
        17px;

    bottom:
        14px;

    width:
        40px;

    height:
        40px;

    border:
        3px solid #571a25;

    color:
        #571a25;

    font-size:
        32px;

    font-weight:
        900;

    display:
        flex;

    align-items:
        center;

    justify-content:
        center;

    transform:
        rotate(12deg);

    z-index:
        9;

}}


.scribble {{

    position:
        absolute;

    left:
        17px;

    bottom:
        20px;

    color:
        #272126;

    font-size:
        13px;

    font-weight:
        900;

    transform:
        rotate(-5deg);

    z-index:
        9;

}}


.envelope.open
.envelope-flap {{

    transform:
        rotateX(180deg);

    z-index:
        1;

}}


.envelope.open
.letter-card {{

    transform:
        translateY(-85px);

}}


.envelope.hide {{

    opacity:
        0;

    pointer-events:
        none;

}}


/* =========================================================
   视频
   ========================================================= */

.video-shell {{

    position:
        absolute;

    left:
        50%;

    top:
        50%;

    width:
        900px;

    transform:
        translate(-50%,-50%)
        translateY(100px)
        scale(.12);

    opacity:
        0;

    pointer-events:
        none;

    z-index:
        30;

    transition:
        transform 1.1s
        cubic-bezier(.16,.85,.25,1),
        opacity .4s ease;

}}


.video-shell.show {{

    transform:
        translate(-50%,-50%)
        translateY(-20px)
        scale(1);

    opacity:
        1;

    pointer-events:
        auto;

}}


.video-shell video {{

    width:
        100%;

    display:
        block;

    border-radius:
        12px;

    background:
        black;

    box-shadow:
        8px 10px 0 #101014,
        14px 16px 0 #711d29,
        0 0 35px
        rgba(255,70,120,.35);

}}

</style>


<script>

const envelope =
    document.getElementById(
        "punk-envelope"
    );


const videoShell =
    document.getElementById(
        "video-shell"
    );


const letterVideo =
    document.getElementById(
        "letter-video"
    );


let busy =
    false;


/* =========================================================
   打开信封
   ========================================================= */

function openLetter() {{

    if (busy) {{
        return;
    }}


    busy =
        true;


    envelope
        .classList
        .add(
            "open"
        );


    setTimeout(
        () => {{

            videoShell
                .classList
                .add(
                    "show"
                );

        }},
        500
    );


    setTimeout(
        () => {{

            envelope
                .classList
                .add(
                    "hide"
                );

        }},
        850
    );


    setTimeout(
        async () => {{

            letterVideo.currentTime =
                0;


            try {{

                await
                letterVideo.play();

            }}

            catch(error) {{

                console.log(
                    "Video play failed:",
                    error
                );

            }}

        }},
        1100
    );

}}


/* =========================================================
   收回信封
   ========================================================= */

function closeLetter() {{

    videoShell
        .classList
        .remove(
            "show"
        );


    setTimeout(
        () => {{

            envelope
                .classList
                .remove(
                    "hide"
                );


            envelope
                .classList
                .remove(
                    "open"
                );


            busy =
                false;

        }},
        1050
    );

}}


envelope.addEventListener(
    "click",
    openLetter
);


/* 视频开始 */

letterVideo.addEventListener(
    "play",
    () => {{

        window.parent.postMessage(
            {{
                type:
                    "MEDIA_PLAY",

                source:
                    "letter-video"
            }},
            "*"
        );

    }}
);


/* 视频暂停 */

letterVideo.addEventListener(
    "pause",
    () => {{

        if (
            !letterVideo.ended
        ) {{

            window.parent.postMessage(
                {{
                    type:
                        "MEDIA_STOP",

                    source:
                        "letter-video"
                }},
                "*"
            );

        }}

    }}
);


/* 视频结束 */

letterVideo.addEventListener(
    "ended",
    () => {{

        window.parent.postMessage(
            {{
                type:
                    "MEDIA_STOP",

                source:
                    "letter-video"
            }},
            "*"
        );


        closeLetter();

    }}
);


/* 其他媒体播放，当前视频暂停 */

window.parent.addEventListener(
    "message",
    event => {{

        if (
            event.data?.type ===
                "MEDIA_PLAY"

            &&

            event.data?.source !==
                "letter-video"
        ) {{

            if (
                !letterVideo.paused
            ) {{

                letterVideo.pause();

            }}

        }}

    }}
);

</script>
""",
    height=720,
    scrolling=False
)


# =========================================================
# 表格
# =========================================================

character_data = {

    "代号": [
        "電脳少女404",
        "Cloud_17",
        "Offline少年",
        "404人格",
        "夢境.exe"
    ],

    "状态": [
        "ONLINE",
        "SLEEP",
        "OFFLINE",
        "ERROR",
        "LOADING"
    ],

    "精神值": [
        96,
        83,
        41,
        12,
        67
    ],

    "社交电量": [
        18,
        56,
        7,
        0,
        34
    ],

    "现实同步率": [
        "99%",
        "82%",
        "31%",
        "0%",
        "65%"
    ],

    "世界线": [
        "α",
        "β",
        "γ",
        "δ",
        "Unknown"
    ]

}


st.table(
    character_data
)


# =========================================================
# BGM 总控制中心
# =========================================================

components.html(
    f"""
<audio
    id="bgm"
    loop
    preload="auto">

    <source
        src="data:audio/mpeg;base64,{bgm_b64}"
        type="audio/mpeg">

</audio>


<script>

const bgm =
    document.getElementById(
        "bgm"
    );


const parentWin =
    window.parent;


const parentDoc =
    window.parent.document;


let started =
    false;


let targetVolume =
    .30;


let bgmUserEnabled =
    true;


/* =========================================================
   当前前景媒体
   ========================================================= */

if (
    parentWin
    .__activeForegroundMedia
    ===
    undefined
) {{

    parentWin
    .__activeForegroundMedia =
        null;

}}


/* =========================================================
   获取喇叭
   ========================================================= */

function getSpeaker() {{

    return parentDoc
        .getElementById(
            "vn-speaker"
        );

}}


/* =========================================================
   暂停 BGM
   ========================================================= */

function pauseBgmForMedia() {{

    if (
        !bgm.paused
    ) {{

        bgm.pause();

    }}


    const btn =
        getSpeaker();


    if (btn) {{

        btn.innerHTML =
            "🔇";

    }}

}}


/* =========================================================
   恢复 BGM
   ========================================================= */

function resumeBgmIfAllowed() {{

    if (
        !started
        ||
        !bgmUserEnabled
        ||
        parentWin
            .__activeForegroundMedia
            !== null
    ) {{

        return;

    }}


    bgm.play()

    .then(
        () => {{

            bgm.volume =
                targetVolume;


            const btn =
                getSpeaker();


            if (btn) {{

                btn.innerHTML =
                    "🔊";

            }}

        }}
    )

    .catch(
        error => {{

            console.log(
                "BGM resume failed:",
                error
            );

        }}
    );

}}


/* =========================================================
   Fade In
   ========================================================= */

function fadeInMusic() {{

    if (
        parentWin
            .__activeForegroundMedia
            !== null
    ) {{

        return;

    }}


    bgm.volume =
        0;


    bgm.play()

    .then(
        () => {{

            let volume =
                0;


            const fade =
                setInterval(
                    () => {{

                        if (
                            parentWin
                                .__activeForegroundMedia
                                !== null
                        ) {{

                            clearInterval(
                                fade
                            );


                            pauseBgmForMedia();


                            return;

                        }}


                        volume +=
                            .01;


                        if (
                            volume >=
                            targetVolume
                        ) {{

                            volume =
                                targetVolume;


                            clearInterval(
                                fade
                            );

                        }}


                        bgm.volume =
                            volume;

                    }},
                    65
                );

        }}
    )

    .catch(
        error => {{

            console.log(
                "BGM autoplay blocked:",
                error
            );

        }}
    );

}}


/* =========================================================
   创建左上角喇叭
   ========================================================= */

function createSpeaker() {{

    if (
        parentDoc
            .getElementById(
                "vn-speaker"
            )
    ) {{

        return;

    }}


    const button =
        parentDoc.createElement(
            "button"
        );


    button.id =
        "vn-speaker";


    button.innerHTML =
        "🔊";


    Object.assign(
        button.style,
        {{

            position:
                "fixed",

            top:
                "18px",

            left:
                "70px",

            width:
                "48px",

            height:
                "48px",

            border:
                "2px solid #f5f0df",

            borderRadius:
                "50%",

            background:
                "rgba(15,15,20,.62)",

            backdropFilter:
                "blur(8px)",

            color:
                "white",

            fontSize:
                "21px",

            cursor:
                "pointer",

            zIndex:
                "999999",

            transition:
                "transform .2s ease",

            boxShadow:
                "3px 3px 0 #111," +
                "6px 6px 0 #8b1e1e," +
                "0 0 15px rgba(255,120,220,.5)"

        }}
    );


    button.addEventListener(
        "mouseenter",
        () => {{

            button.style.transform =
                "scale(1.10)";

        }}
    );


    button.addEventListener(
        "mouseleave",
        () => {{

            button.style.transform =
                "scale(1)";

        }}
    );


    button.addEventListener(
        "click",
        event => {{

            event.stopPropagation();


            if (
                !bgm.paused
            ) {{

                bgmUserEnabled =
                    false;


                bgm.pause();


                button.innerHTML =
                    "🔇";


                return;

            }}


            bgmUserEnabled =
                true;


            if (
                parentWin
                    .__activeForegroundMedia
                    !== null
            ) {{

                button.innerHTML =
                    "🔇";


                return;

            }}


            bgm.play()

            .then(
                () => {{

                    bgm.volume =
                        targetVolume;


                    button.innerHTML =
                        "🔊";

                }}
            );

        }}
    );


    parentDoc.body
        .appendChild(
            button
        );

}}


/* =========================================================
   启动 BGM
   ========================================================= */

function startExperience() {{

    if (started) {{
        return;
    }}


    started =
        true;


    createSpeaker();


    fadeInMusic();

}}


/* =========================================================
   MEDIA BUS
   ========================================================= */

parentWin.addEventListener(
    "message",
    event => {{

        const type =
            event.data?.type;


        const source =
            event.data?.source;


        if (
            type ===
            "START_EXPERIENCE"
        ) {{

            startExperience();


            return;

        }}


        if (
            type ===
            "MEDIA_PLAY"
        ) {{

            parentWin
                .__activeForegroundMedia =
                source;


            pauseBgmForMedia();

        }}


        if (
            type ===
            "MEDIA_STOP"
        ) {{

            if (
                parentWin
                    .__activeForegroundMedia
                    === source
            ) {{

                parentWin
                    .__activeForegroundMedia =
                    null;

            }}


            setTimeout(
                resumeBgmIfAllowed,
                120
            );

        }}

    }}
);


/* =========================================================
   重要：
   如果开场早于 BGM 控制器加载，
   自动补上启动状态
   ========================================================= */

if (
    parentWin.__vnStarted === true
) {{

    startExperience();

}}

</script>
""",
    height=1
)


# =========================================================
# 身份 / 世界线输入
# =========================================================

st.write("")
st.write("")


codename = st.text_input(
    "IDENTITY // 输入你的代号"
)


access_key = st.text_input(
    "ACCESS KEY // 世界线认证",
    type="password"
)


route = st.radio(
    "SELECT ROUTE // 选择你的世界线",
    [
        "α // 現実未接続",
        "β // 青春缓存损坏",
        "γ // 夜間漂流",
        "δ // ERROR 404"
    ]
)


st.write(
    f"USER // {codename}"
)


st.write(
    f"ROUTE // {route}"
) 
