const texts = ["Create Explore Expand Conquer"]; // 循环的文字内容

const typewriterElement = document.getElementById("typewriter");
const introPage = document.getElementById("intro-page");
const mainContent = document.getElementById("main-content");

let textIndex = 0; // 当前播放的文字索引
let charIndex = 0; // 当前文字的字符索引

// 逐字显示效果
function typeEffect() {
    if (charIndex < texts[textIndex].length) {
        typewriterElement.textContent += texts[textIndex].charAt(charIndex);
        charIndex++;
        setTimeout(typeEffect, 100); // 控制显示速度
    } else {
        setTimeout(() => {
            resetTypeEffect(); // 完成后重置并播放下一句
        }, 500); // 停留 0.2 秒后重置
    }
}

// 重置文字效果并播放下一句
function resetTypeEffect() {
    typewriterElement.textContent = ""; // 清空文字
    charIndex = 0; // 重置字符索引
    textIndex = (textIndex + 1) % texts.length; // 循环切换到下一句
    typeEffect(); // 重新播放
}

// 点击特效页进入主页面
introPage.addEventListener("click", () => {
    introPage.style.opacity = "0"; // 淡出特效页
    setTimeout(() => {
        introPage.style.display = "none"; // 完全隐藏特效页
        mainContent.style.display = "block"; // 显示主页面内容
        setTimeout(() => {
            mainContent.style.opacity = "1"; // 淡入主页面
        }, 10); // 确保 display: block 生效后再进行淡入
    }, 500); // 保证淡出动画完成后再隐藏特效页
});

// 启动逐字显示特效
typeEffect();
