const btn_video_player_time = Array.from(document.getElementsByClassName("btn-video-player-time"));

btn_video_player_time.forEach(btn => {
  btn.addEventListener("click", function() {
    const a = this.getAttribute("time").split(":");

    const video = document.getElementById("video");
    video.currentTime = (+a[0]) * 60 * 60 + (+a[1]) * 60 + (+a[2]); 
  });
});