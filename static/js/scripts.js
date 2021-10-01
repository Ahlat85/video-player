const video = document.getElementById("video");

const btn_video_player_time = Array.from(document.getElementsByClassName("btn-video-player-time"));
btn_video_player_time.forEach(btn => {
  btn.addEventListener("click", function() {
    const a = this.getAttribute("time").split(":");
    video.currentTime = (+a[0]) * 60 * 60 + (+a[1]) * 60 + (+a[2]);
  });
});

const btn_video_player_time_left = Array.from(document.getElementsByClassName("btn-video-player-time-left"));
btn_video_player_time_left.forEach(btn => {
  btn.addEventListener("click", function() {
    video.currentTime -= parseInt(this.getAttribute("time"));
  });
});

const btn_video_player_time_right = Array.from(document.getElementsByClassName("btn-video-player-time-right"));
btn_video_player_time_right.forEach(btn => {
  btn.addEventListener("click", function() {
    video.currentTime += parseInt(this.getAttribute("time"));
  });
});