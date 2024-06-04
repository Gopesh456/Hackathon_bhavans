const result = document.querySelectorAll(".res");
const pts = document.querySelectorAll(".pts");
const questionlink = document.querySelectorAll(".links");
let points = 400;
let totalPoints = document.querySelector("#totalPoints");
function adding() {
  let total_pts = 0;
  for (let i = 0; i < 10; i++) {
    total_pts += parseInt(pts[i].textContent);
    // console.log(total_pts);
    totalPoints.textContent = total_pts;
  }
}
setInterval(adding, 1000);
