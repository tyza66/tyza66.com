//获取控件
    //按钮
    github = document.querySelector("#github");
    info_close = document.querySelector("#info_close");
    //框
    info = document.querySelector("#info");
//添加监听器
github.addEventListener("click", () => {
    window.location.href = "https://github.com/tyza66/";
});
info_close.addEventListener("click", () => {
    info.hidden = true;
});